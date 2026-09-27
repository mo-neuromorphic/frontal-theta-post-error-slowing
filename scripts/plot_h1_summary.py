# Visualise the H1 ERP comparison alongside exploratory local theta power, not H2 dWPLI.
# Research specification: README.md. Run from the project root.
# Single-recording helper for sub-1004 ses-1; no group/PES/reliability test.
# Existing filter/reference choices need QC, including recording boundaries.
# ICA, baseline and rejection settings are walkthrough choices, not universal rules.

import numpy as np
import mne
import matplotlib.pyplot as plt

# Repeat the existing recording-specific preprocessing and epoch rejection.
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

events, event_id = mne.events_from_annotations(raw)
epoch_event_id = {"cor": event_id["cor"], "err": event_id["err"]}
epochs = mne.Epochs(raw, events, event_id=epoch_event_id, tmin=-0.5, tmax=0.8, baseline=(None, 0), preload=True)
epochs.drop_bad(reject=dict(eeg=100e-6))

# Step 9: ERN/CRN waveforms at FCz.
evoked_err = epochs['err'].average()
evoked_cor = epochs['cor'].average()

times = evoked_err.times * 1000  # seconds -> ms
err_uv = evoked_err.copy().pick('E6').data[0] * 1e6
cor_uv = evoked_cor.copy().pick('E6').data[0] * 1e6

# Exploratory local theta power at E6, using the existing wavelet settings.
# This does not test H2: proposed H2 dWPLI uses electrode pairs and 0–150 ms.
# No power baseline normalisation or trial-count matching is applied here.
freqs = np.arange(4, 9, 1)
n_cycles = freqs / 2

power_err = epochs['err'].compute_tfr(method="morlet", freqs=freqs, n_cycles=n_cycles, picks="E6", average=True)
power_cor = epochs['cor'].compute_tfr(method="morlet", freqs=freqs, n_cycles=n_cycles, picks="E6", average=True)

theta_times = power_err.times * 1000
theta_err_tc = power_err.data[0].mean(axis=0)  # average across theta band, keep time
theta_cor_tc = power_cor.data[0].mean(axis=0)

# H1 ERP panel plus supporting exploratory power panel; descriptive only.
fig, axes = plt.subplots(2, 1, figsize=(9, 9), sharex=True)

# Top: ERP separation in 0–100 ms; ΔERN is its signed mean, not its area.
axes[0].plot(times, err_uv, label='ERN (error)', color='crimson')
axes[0].plot(times, cor_uv, label='CRN (correct)', color='steelblue')
mask = (times >= 0) & (times <= 100)
axes[0].fill_between(times, err_uv, cor_uv, where=mask, color='gray', alpha=0.4, label='ERP separation (0-100 ms)')
axes[0].axvline(0, color='black', linewidth=0.8, linestyle='--')
axes[0].axhline(0, color='black', linewidth=0.8)
axes[0].set_ylabel('Amplitude (µV)')
axes[0].set_title('H1 ERP comparison at E6 (working FCz)')
axes[0].legend()

# Bottom: exploratory local power with its existing 0–400 ms window.
# This window does not replace the proposed H2 0–150 ms connectivity window.
axes[1].plot(theta_times, theta_err_tc, label='Error trials', color='crimson')
axes[1].plot(theta_times, theta_cor_tc, label='Correct trials', color='steelblue')
axes[1].axvspan(0, 400, color='gray', alpha=0.15, label='0-400ms window')
axes[1].axvline(0, color='black', linewidth=0.8, linestyle='--')
axes[1].set_xlabel('Time relative to response (ms)')
axes[1].set_ylabel('Theta power (4-8 Hz)')
axes[1].set_title('Exploratory theta power at E6 (working FCz)')
axes[1].legend()

fig.suptitle('sub-1004 ses-1: H1 ERP comparison and exploratory theta power')
fig.tight_layout()
fig.savefig("figures/sub-1004_ses-1_h1_summary.png", dpi=150)
plt.close(fig)
print("Saved figures/sub-1004_ses-1_h1_summary.png")
