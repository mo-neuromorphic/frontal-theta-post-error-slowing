# Visualise EGI E-number coordinates to inspect the working E6/FCz mapping.
# Numbered channel labels require positional identification rather than an FCz name lookup.
# The plot displays supplied geometry; it does not prove exact anatomical equivalence.
# Research specification: README.md. Run from the project root.
# Single-recording helper for sub-1004 ses-1; no group/PES/reliability test.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset's electrode coordinates; individual digitisation is not verified.
# Coordinate system is CTF: +x = anterior, +y = left, +z = superior.
electrodes = pd.read_csv(
    "data/ds004883_Clayson/sub-1004/ses-1/eeg/sub-1004_ses-1_electrodes.tsv",
    sep="\t",
)

# Bird's-eye-view scatter: x-axis = right (flip -y since native +y is left),
# y-axis = anterior. This lays out the head as if viewed from above.
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(-electrodes["y"], electrodes["x"], s=15)

# Label every point with its E-number so individual channels can be identified.
for _, row in electrodes.iterrows():
    ax.annotate(
        row["name"],
        (-row["y"], row["x"]),
        fontsize=6,
        ha="center",
        va="bottom",
    )

ax.set_aspect("equal")  # keep head shape proportional, not stretched
ax.set_xlabel("right (mm)")
ax.set_ylabel("anterior (mm)")
ax.set_title("sub-1004 ses-1: electrode layout (bird's-eye view)")

fig.savefig("figures/sub-1004_ses-1_electrode_positions.png", dpi=150)
print("Saved figures/sub-1004_ses-1_electrode_positions.png")
