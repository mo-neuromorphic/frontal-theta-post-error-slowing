# Exploratory local power near 17 Hz; not a test of H1–H4 or proof of signal origin.
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

# Compute per-trial Morlet power and average it across correct trials.
# This exploratory check does not calculate dWPLI or baseline-normalised ERD/ERS.
# A response-related pattern alone does not establish a physiological origin.
freqs = np.arange(10, 26, 1)  # Exploratory 10–25 Hz range, including alpha and part of beta
n_cycles = freqs / 2

power = epochs['cor'].compute_tfr(
    method="morlet", freqs=freqs, n_cycles=n_cycles, picks="E6", average=True
)

# Select the nearest computed frequency to the previously inspected 17.4 Hz peak.
# With this 1 Hz grid the selected frequency is 17 Hz; this choice is data-driven.
freq_idx = np.argmin(np.abs(power.freqs - 17.4))
power_17hz = power.data[0, freq_idx, :]
times = power.times * 1000  # seconds -> ms

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(times, power_17hz)
ax.axvline(0, color="black", linestyle="--", linewidth=0.8, label="response")
ax.set_xlabel("Time relative to response (ms)")
ax.set_ylabel("Power at ~17 Hz")
ax.set_title("sub-1004 ses-1: exploratory ~17 Hz power, correct trials, E6")
ax.legend()
fig.savefig("figures/sub-1004_ses-1_beta_power_timecourse.png", dpi=150)
plt.close(fig)
print("Saved figures/sub-1004_ses-1_beta_power_timecourse.png")
