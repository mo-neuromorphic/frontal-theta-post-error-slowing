# Frontal theta phase synchrony and post-error slowing

A psychobiological and psychometric investigation of error monitoring in a large open EEG dataset.

Moyosore Olasupo · University of Essex Online · Psychobiology & Neuroscience

## Abstract

This project investigates the relationship between error-related frontal theta synchrony and post-error slowing (PES) using existing EEG and behavioural data from the OpenNeuro ds004883 flanker dataset. The primary analysis will examine whether participants with stronger error-trial theta synchrony show greater PES, calculated from reaction times on valid correct trials immediately before and after an error.

Supporting analyses will compare error- and correct-response ERP amplitudes at FCz and frontal theta synchrony measured using the debiased estimator of squared weighted phase-lag index (dWPLI). A secondary analysis will compare the Spearman–Brown-corrected split-half reliability of dWPLI and ΔERN using matched usable error-trial counts. Repeated random partitions will assess the stability of this comparison.

Behavioural reconstruction and preliminary single-recording EEG processing have been undertaken. The main hypotheses remain untested. The study aims to assess both the behavioural relevance and internal consistency of frontal theta synchrony.

## Setup

### 1. Clone the project

```bash
git clone https://github.com/mo-neuromorphic/frontal-theta-post-error-slowing.git
cd frontal-theta-post-error-slowing
```

### 2. Create the Python environment

Install Conda before proceeding.

The supplied `environment.yml` contains a machine-specific `prefix:` line. Remove that line when setting up on another computer, then run:

```bash
conda env create -f environment.yml
conda activate essex_project
```

If the environment already exists, activate it without recreating it:

```bash
conda activate essex_project
```

The environment specification includes Python, MNE, NumPy, SciPy, Matplotlib, mne-bids and pymatreader. It is not a fully pinned reproduction of the analysis environment.

The notebook also requires a Jupyter kernel and Picard for ICA. Check whether these are available:

```bash
python -c "import ipykernel, picard; print('Notebook and ICA dependencies available')"
```

If either import fails, install the missing dependencies:

```bash
python -m pip install ipykernel python-picard
```

### 3. Obtain the source data

Download the ds004883 dataset from [OpenNeuro](https://openneuro.org/datasets/ds004883) and place it at:

```text
data/ds004883_Clayson/
```

The raw dataset is excluded from this repository. Preserve its directory structure and original files.

EEGLAB recordings require both their `.set` files and associated `.fdt` files. If using a git-annex dataset clone, ensure the required file contents have been retrieved; a symlink alone does not mean the data are available.

## Run the Project

1. Open the project folder in VS Code.
2. Install the Python and Jupyter extensions if needed.
3. Open `notebooks/h1_pipeline.ipynb`.
4. Select the Python kernel from the `essex_project` environment.
5. Check the notebook's project and dataset paths against your local folders.
6. Read the Markdown instructions and execute the relevant cells sequentially.

The notebook is a staged research workflow, not a completed end-to-end pipeline. Some cells perform dataset retrieval or batch processing, so review them before using **Run All**. Saved outputs do not restore variables in a newly started kernel.

Supporting scripts are located in `scripts/`. Inspect each script's paths and required inputs before running it.

Generated figures are stored in `figures/`, and derived results and audit tables are stored in `results/`. Keep derived outputs separate from the source dataset.
