# Inspect spectra around the existing filter settings; this is partial preprocessing QC.
# Research specification: README.md. Run from the project root.
# Single-recording helper for sub-1004 ses-1; no group/PES/reliability test.
# Existing filter/reference choices need QC, including recording boundaries.

import mne
import matplotlib.pyplot as plt

# Load the raw EEG fresh (unfiltered) for sub-1004, ses-1.
raw = mne.io.read_raw_eeglab("data/ds004883_Clayson/sub-1004/ses-1/eeg/sub-1004_ses-1_task-ffb_eeg.set",
    preload=True
    )


# sharey=True is required: without it each panel auto-scales its own y-axis,
# which makes the before/after curves look deceptively similar even when the
# underlying power values differ.
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True, sharey=True)

# Top panel: power spectral density BEFORE filtering.
# fmax=60 caps the x-axis so both the low end and just past our 30 Hz
# cutoff are visible.
# E129 was documented as flat in the earlier recording inspection.
# Exclude it from this spectral display to avoid near-zero power dominating
# the dB scale. This display choice does not resolve reference-channel handling.
raw.compute_psd(fmax=60, exclude=["E129"]).plot(axes=axes[0], show=False)
axes[0].set_title("Before filtering (raw)")
axes[0].axvline(30, color="red", linestyle="--", linewidth=1)  # marks the 30 Hz cutoff


# Apply the same 0.1-30 Hz band-pass filter used in Step 3 of the pipeline.
raw.filter(l_freq=0.1, h_freq=30)

# Bottom panel: power spectral density AFTER filtering, for comparison.
# Inspect attenuation around the transition band; 30 Hz is not a brick-wall cutoff.
# This plot does not validate discontinuity handling or all ERP filter effects.
raw.compute_psd(fmax=60, exclude=["E129"]).plot(axes=axes[1], show=False)
axes[1].set_title("After filtering (0.1-30 Hz band-pass)")
axes[1].axvline(30, color="red", linestyle="--", linewidth=1)


plt.tight_layout()
plt.savefig("figures/sub-1004_ses_1_filter_check.png", dpi=150)
print("Saved figures/sub-1004_ses_1_filter_check.png")
