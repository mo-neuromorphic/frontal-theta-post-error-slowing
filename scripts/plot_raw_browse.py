# Inspect a short filtered, average-referenced EEG interval before ICA.
# Research specification: README.md. Run from the project root.
# Single-recording helper for sub-1004 ses-1; no group/PES/reliability test.
# Existing filter/reference choices need QC, including recording boundaries.

import mne

# Load fresh and apply the existing filter and reference choices, before ICA.
raw = mne.io.read_raw_eeglab(
    "data/ds004883_Clayson/sub-1004/ses-1/eeg/sub-1004_ses-1_task-ffb_eeg.set",
    preload=True
)

raw.filter(l_freq=0.1, h_freq=30)
raw.set_eeg_reference("average")

# Force a plain matplotlib backend so this renders as a static image
# reliably, instead of trying to open an interactive Qt browser window.
mne.viz.set_browser_backend("matplotlib")

# MNE's own signal-browsing plot: 30 channels stacked vertically, a
# 15-second window starting 10 s in. Its timing does not establish filter safety.
# show=False returns the figure instead of opening it live, so we can save it.
fig = raw.plot(n_channels=30, duration=15, start=10, show=False)
fig.savefig("figures/sub-1004_ses-1_raw_browse.png", dpi=150)
print("Saved figures/sub-1004_ses-1_raw_browse.png")
