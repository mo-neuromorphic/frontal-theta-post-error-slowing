# Visualise the single-recording H1 ERP comparison at the working FCz channel E6.
# Research specification: README.md. Run from the project root.
# Single-recording helper for sub-1004 ses-1; no group/PES/reliability test.
# Existing filter/reference choices need QC, including recording boundaries.
# ICA, baseline and rejection settings are walkthrough choices, not universal rules.

import mne
import matplotlib.pyplot as plt

# Repeat the existing recording-specific filtering, reference and ICA choices.
# Unlike the notebook, this script retains the montage loaded from the SET file.
raw = mne.io.read_raw_eeglab(
    "data/ds004883_Clayson/sub-1004/ses-1/eeg/sub-1004_ses-1_task-ffb_eeg.set",
    preload=True
)
raw.filter(l_freq=0.1, h_freq=30)
raw.set_eeg_reference("average")

raw_for_ica = raw.copy().filter(l_freq=1.0, h_freq=None)
ica = mne.preprocessing.ICA(n_components=25, method="picard", random_state=42)
ica.fit(raw_for_ica)
# Recorded exclusions for this fit only; review components after any changed fit.
ica.exclude = [2, 3]
ica.apply(raw)

# Steps 7-8: epoch and reject.
events, event_id = mne.events_from_annotations(raw)
epoch_event_id = {"cor": event_id["cor"], "err": event_id["err"]}
epochs = mne.Epochs(raw, events, event_id=epoch_event_id, tmin=-0.5, tmax=0.8, baseline=(None, 0), preload=True)
epochs.drop_bad(reject=dict(eeg=100e-6))

# Step 9: ERN/CRN waveforms at FCz.
evoked_err = epochs['err'].average()
evoked_cor = epochs['cor'].average()

times = evoked_err.times * 1000  # seconds -> ms
err_uv = evoked_err.copy().pick('E6').data[0] * 1e6  # volts -> microvolts
cor_uv = evoked_cor.copy().pick('E6').data[0] * 1e6

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(times, err_uv, label='ERN (error)', color='crimson')
ax.plot(times, cor_uv, label='CRN (correct)', color='steelblue')

# Shade the waveform separation in the H1 measurement window.
# ΔERN is the mean error-minus-correct amplitude, not the area itself.
mask = (times >= 0) & (times <= 100)
ax.fill_between(times, err_uv, cor_uv, where=mask, color='gray', alpha=0.4, label='ERP separation (0-100 ms)')

ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.axhline(0, color='black', linewidth=0.8)
ax.set_xlabel('Time relative to response (ms)')
ax.set_ylabel('Amplitude (µV)')
ax.set_title('sub-1004 ses-1: ERN vs CRN at E6 (working FCz)')
ax.legend()

fig.savefig("figures/sub-1004_ses-1_ern_crn.png", dpi=150)
plt.close(fig)
print("Saved figures/sub-1004_ses-1_ern_crn.png")
