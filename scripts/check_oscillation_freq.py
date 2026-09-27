# Exploratory spectrum of the correct-response evoked waveform; not connectivity.
# Research specification: README.md. Run from the project root.
# Single-recording helper for sub-1004 ses-1; no group/PES/reliability test.
# Existing filter/reference choices need QC, including recording boundaries.
# ICA, baseline and rejection settings are walkthrough choices, not universal rules.

import numpy as np
from scipy.signal import detrend, windows
import mne
import matplotlib.pyplot as plt

# Compute the correct-response evoked waveform after the existing preprocessing.
# The saved notebook run retained 299 correct trials; this run recomputes the count.
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

evoked_cor = epochs['cor'].average()

# Inspect the pre-response interval (-500 to -100 ms) of the evoked average.
# Its position before the response does not establish that it is background-only.
# This is not the average of individual-trial spectra or a test of signal origin.
baseline = evoked_cor.copy().pick('E6').crop(tmin=-0.5, tmax=-0.1)
signal = detrend(baseline.data[0])  # remove linear trend, not just the mean
sfreq = evoked_cor.info['sfreq']

n = len(signal)
window = windows.hann(n)
signal_windowed = signal * window

freqs = np.fft.rfftfreq(n, d=1/sfreq)
# Squared FFT magnitude, without PSD normalisation; short-window bins are coarse.
# Search is restricted to bins >=3 Hz, after the existing 30 Hz low-pass filter.
power = np.abs(np.fft.rfft(signal_windowed)) ** 2

mask = freqs >= 3
peak_freq = freqs[mask][np.argmax(power[mask])]
print(f"Largest inspected FFT bin in pre-response evoked spectrum (E6): {peak_freq:.1f} Hz")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(freqs[mask], power[mask])
ax.axvline(peak_freq, color='red', linestyle='--', label=f'peak: {peak_freq:.1f} Hz')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Squared FFT magnitude (unnormalised)')
ax.set_title('Exploratory pre-response evoked spectrum at E6')
ax.legend()
fig.savefig("figures/sub-1004_ses-1_baseline_oscillation_spectrum.png", dpi=150)
plt.close(fig)
print("Saved figures/sub-1004_ses-1_baseline_oscillation_spectrum.png")
