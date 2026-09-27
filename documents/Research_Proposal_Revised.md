# Frontal Theta Phase Synchrony and Post-Error Slowing: A Psychobiological and Psychometric Investigation of Error Monitoring in a Large Open EEG Dataset

Moyosore Olasupo
University of Essex Online
Module: Psychobiology & Neuroscience
Working revision: 27 September 2026
Original submission: 13 September 2026

## Revision status

This working revision updates [the submitted proposal](<Research Proposal Report_submission.pdf>) in response to supervisor feedback. The submitted PDF remains unchanged. The original research questions and H1–H4b structure are retained.

This is a revised analysis protocol for review, prepared at the researcher’s request. The supervisor requested explicit decisions but did not prescribe particular tests, wavelet cycles or trial thresholds. The choices below are therefore project recommendations, not quotations of the supervisor’s instructions or evidence of their approval. No analysis code has been changed or executed. Data-governance facts still require the researcher’s confirmation; this document is not labelled submission-ready while those facts are missing. The original word count does not apply to this expanded protocol.

The original signed/declaration page is retained in the submitted PDF. Any declaration for a later submission must describe the assistance actually used in that version and follow the required university wording.

## Response to supervisor feedback

| Feedback | Change in this working revision | Status |
| --- | --- | --- |
| Specify H1 and H2 inferential tests | Two-sided paired-samples t-tests on participant-level condition scores, with effect sizes and confidence intervals. | Specified in this revision |
| Specify connectivity implementation | Debiased squared wPLI, explicit pair averaging, frequency grid, Morlet cycles and signal support. | Specified; implementation validation remains |
| Specify multiplicity | One Holm family for H1–H3 and a Bonferroni-adjusted interval family for secondary H4a comparisons. | Specified; family scope stated |
| Explain unsupported H2 | Retain the planned H3 test, but restrict claims about error-specific synchrony. | Revised interpretation |
| Complete data governance | Add a lifecycle plan for source data, derived files, access, backups, retention and disposal. | Personal/institutional details still require confirmation |
| Document data-informed decisions | Add a dated decision log and distinguish existing exploratory work from prospective decisions. | Required throughout subsequent work |
| Add targeted methodological support | Include paired-test documentation, Cohen’s wavelet-methods paper, Morlet implementation documentation and Holm’s methodological paper. | Added; exact settings remain project choices |

## Background Literature Review

Successful goal-directed behaviour requires individuals to monitor their actions and adjust their responses when a mistake occurs. However, detecting an error does not necessarily improve subsequent performance (Danielmeier & Ullsperger, 2011). The study of how neural error signals are related to behavioural adjustment is important for understanding cognitive control. My literature review search was conducted by using APA PsycINFO, covering error monitoring, frontal theta activity, post-error slowing (PES), and reliability measurement. Error-related negativity (ERN) is an event-related potential that occurs shortly after an incorrect response and is measured at frontocentral scalp electrodes, including during flanker tasks (Holroyd & Coles, 2002). It provides an established measure of error processing. Theta power describes the strength of activity within a frequency band and is related to squared amplitude. Inter-site phase synchrony describes the consistency of phase relationships between signals recorded at different electrodes. These measures capture different aspects of the neural response to errors.

### Prior Findings

 Cavanagh et al. (2009) found increased theta synchrony between midfrontal and lateral-frontal EEG sites during error trials in a flanker task. Greater synchrony was associated with subsequent post-error slowing (PES), suggesting a relationship between synchronised frontal activity and behavioural adjustment. Valadez and Simons (2018) additionally found that error-related frontal theta power and PES predicted performance recovery. However, findings concerning theta power do not directly establish the behavioural relevance of connectivity, and these associations alone do not demonstrate causation. Danielmeier and Ullsperger (2011) reviewed evidence that PES and improved post-error accuracy are not consistently associated. This means that a slower response does not automatically indicate successful adaptation. Murphy et al. (2016) found that larger error-evoked pupil responses predicted greater slowing and a higher probability of a correct subsequent response in a task with long inter-stimulus intervals. This suggests that the timing of subsequent task demands influences whether an error response supports beneficial adjustment. Volume conduction poses a challenge for interpreting scalp connectivity. Vinck et al. (2011) introduced the weighted phase-lag index (wPLI) to estimate phase synchrony with reduced sensitivity to volume conduction effects and noise. They also developed a debiased estimator of its squared value to reduce sample-size bias. This provides a basis for estimating lagged connectivity. Reliability must be assessed when interpreting individual differences. Clayson et al. (2021) distinguished measurement precision from internal consistency, explaining why good data quality does not automatically establish reliable measurement of differences between individuals. Consequently, the reliability of error-related theta synchrony should be assessed alongside its relation with behaviour.

### Theory

The reinforcement-learning account proposes that the ERN reflects a negative learning signal carried through the dopamine system to the anterior cingulate cortex, contributing to subsequent performance adjustment (Holroyd & Coles, 2002). This provides a connection between error monitoring and behavioural adaptation. A complementary network interpretation proposes that theta synchrony supports coordination between frontal regions involved in performance monitoring and implementing adjustments. The findings of Cavanagh et al. (2009) are consistent with this interpretation, but do not establish direct communication between particular anatomical regions. A positive association between theta connectivity and PES would support a neural–behavioural relationship. Examining this relationship separately from measurement reliability allows the study to address both the behavioural relevance and psychometric properties of frontal theta connectivity.

## Rationale and Hypotheses

Previous findings provide a basis for examining whether error-related frontal theta synchrony is associated with PES (Cavanagh et al., 2009). This study will investigate the relationship between participants using the ds004883 flanker dataset. A secondary comparison will test whether connectivity is more reliable than ΔERN; this advantage has not yet been established. This study will use the publicly available EEG dataset ds004883. Its retained behavioural information supports trial reconstruction, although final eligibility for the planned analyses will depend on the specified screening criteria. The research questions are: Is error-related frontal theta phase synchrony associated with post-error slowing (PES) between participants? Does error-trial theta synchrony demonstrate higher internal consistency than ΔERN at matched numbers of usable error trials?

H1: Error responses will produce a more negative mean response-locked ERP amplitude at FCz than correct responses during 0–100 ms after the response. Prediction: ΔERN = ERN − CRN < 0.

H2: Frontal theta synchrony, measured using dWPLI between FCz and lateral-frontal electrodes, will be greater on error trials than correct trials.

H3: Individuals with stronger error-related theta synchrony will show greater PES. PES = RT(E+1) − RT(E−1), using valid correct responses immediately surrounding an error.

H4a: Error-trial theta dWPLI will show higher Spearman–Brown-corrected split-half reliability than ΔERN at matched numbers of usable error trials.

H4b: Examine the stability of the H4a reliability comparison across repeated random splits of the same trials. This is a robustness analysis, not a separate formal hypothesis.

## Aims and Objectives

The primary aim is to examine the between-participant relationship between error-related frontal theta synchrony and PES. The secondary aim is to compare the internal consistency of connectivity and ΔERN. The objectives are to evaluate error-related EEG effects, test the synchrony–PES association, and compare reliability using matched usable error-trial counts. H4b describes robustness to trial partitioning rather than an additional formal hypothesis.

## Research Design

### Design

The study uses secondary EEG and behavioural data from ds004883. H1 and H2 compare response conditions within participants; H3 examines differences between participants. No additional participants will be recruited. Reliability remains a secondary methodological question.

### Materials

The study will use EEG recordings and associated behavioural metadata from the ds004883 flanker dataset (Clayson et al., 2024). The original study presented three arrow-flanker task variants using E-Prime 3.0. EEG was recorded using an Electrical Geodesics, Inc. HydroCel Geodesic Sensor Net with 128 scalp sites and a vertex reference, sampled at 500 Hz. The dataset contains EEGLAB SET/FDT files, electrode information and event metadata. Behavioural fields retained in the SET files include response times, response accuracy and original trial identifiers. These fields will provide information for reconstructing behavioural sequences. EEG processing and analysis will use MNE-Python 1.12.1, supported by NumPy, SciPy, and Matplotlib. Picard will be used for independent component analysis. The standard montage provides approximate correspondences between E6 and FCz, E27 and F5, and E123 and F6. These represent standard electrode locations rather than individual anatomical localisation.

The software versions above reproduce the submitted specification. Installed versions and any additional connectivity dependency must be checked and recorded before implementation; the environment file alone does not guarantee those versions.

### Participants

The source dataset contains records for 172 participants recruited from undergraduate courses at Brigham Young University and the University of South Florida. According to Clayson et al. (2024), participants received course credit, and the eligibility criterion specified an age over 18 years. Eligibility excluded individuals reporting psychiatric or neurological diagnoses, psychoactive medication use, uncorrected visual impairment or limited English fluency. All participants whose data meet the prespecified, analysis-specific eligibility criteria will be considered for the secondary analysis. Inclusion will depend on EEG quality and sufficient usable error and correct trials. The synchrony PES analysis will additionally require sufficient valid behavioural sequences. Consequently, eligible sample sizes may differ across the ERP, connectivity, behavioural-association and reliability analyses. Participants will be included according to predefined data-quality and trial-count criteria. The final sample size and reasons for exclusion will be reported for each analysis. Statistical sensitivity will be evaluated using the number of eligible participants.

### Data Analysis Plan

#### Participant-level observations and task variants

Measures will first be estimated separately for each task variant. For this revised protocol, eligible participants will contribute all three variants for the relevant analysis, and variant-level scores will be averaged with equal weights to produce one score per participant per condition. For H3, both synchrony and PES will use the same three eligible variants. For H4a, the same variant set and eligible participants will be used for both neural measures within each trial-count comparison. Trials will not be concatenated across variants before connectivity estimation.

Equal weighting of all three variants is a project choice, not a requirement from the supervisor. It avoids varying task composition between participants but may reduce the eligible sample. Feasibility must be reviewed using counts and data quality, without selecting the approach according to hypothesis results. A change to this approach must be recorded before testing. Variant-specific analyses, if undertaken, will be labelled exploratory.

#### Preprocessing and behavioural eligibility

EEG preprocessing will include filtering that respects discontinuities, referencing, recording-specific ocular-artefact assessment and response-locked epoching. Original trial identifiers, exclusions and retained trial counts will be preserved. The same preprocessing rules will apply across response conditions. ICA component numbers selected in one recording will not be transferred automatically to another.

PES will be calculated as RT(E+1) − RT(E−1), using valid correct responses immediately surrounding an error (Dutilh et al., 2012). Neighbours will be identified from the original trial sequence before exclusions. Triplets crossing blocks or recording discontinuities, involving omissions or incorrect flanking responses, or failing the agreed RT criteria will be excluded. The primary RT screen will exclude missing, non-finite or non-positive stored RTs at any of the three triplet positions and records with ambiguous response or sequence coding. RTs will be interpreted relative to the recorded stimulus marker: no undocumented physical-onset correction or presumed task deadline will be imposed. The primary analysis will not trim positive RTs using a sample-dependent standard-deviation rule, because that can selectively remove slow post-error responses. This conservative scoring choice retains possible anticipatory or unusually slow responses; it is a limitation, not evidence that all retained RTs are behaviourally valid.

Only trials explicitly coded as practice will be removed as practice. The saved practice audit found no cell-99 trials among the inspected trial events; the first 24 trials will not be removed automatically. Original sequence positions and uncertain boundaries will be preserved, and triplets with uncertain membership will be excluded.

The revised working eligibility rule requires at least 10 usable error and 10 usable correct epochs per variant for H1/H2. H3 additionally requires at least 10 valid triplets per variant with the central error retained for connectivity; the synchrony score will use all eligible error trials, not only PES-valid errors. Each analysis requires all three variants for its participant-level composite. These minimums are pragmatic proposed floors for this protocol, not literature-established guarantees of reliable measurement. H4 has its own higher per-comparison requirements below. Attrition and actual counts will be reported; if feasibility is inadequate, the protocol will be amended transparently before testing rather than relaxing thresholds to obtain a favourable result.

#### H1: response-locked ERP contrast

ERN and CRN will be measured as mean FCz/E6 amplitude during 0–100 ms after error and correct responses. ΔERN = ERN − CRN. A two-sided paired-samples t-test will compare participant-level error and correct scores; equivalently, a one-sample t-test will compare participant-level ΔERN with zero. The predicted direction is negative. A significant effect in the opposite direction will not support H1.

Report the mean difference in microvolts, its 95% confidence interval, t statistic, degrees of freedom, raw and adjusted p-values, and paired effect size d_z (mean difference divided by the standard deviation of differences). The paired test is appropriate to the matched response conditions; it assumes independent participants and, for exact small-sample inference, normally distributed participant-level differences. Pairing does not require equal condition variances. The implementation is documented in SciPy's paired-test reference (SciPy community, n.d.).

Difference distributions and influential values will be inspected as diagnostics. They will not be used to choose whichever test produces significance. Serious violations will be reported and any additional robust analysis labelled as a sensitivity analysis. A change to the confirmatory test requires a documented protocol amendment.

#### H2: theta connectivity and condition contrast

Connectivity will use the debiased estimator of squared weighted phase-lag index described by Vinck et al. (2011), referred to here as dWPLI. The square root will not be taken and negative finite-sample estimates will not be silently truncated to zero. The implementation must reproduce the chosen estimator rather than substituting ordinary wPLI or a phase-locking value.

Complex Morlet coefficients will be calculated at 4, 5, 6, 7 and 8 Hz using three cycles at each frequency, with zero-mean wavelets. At each frequency and time point, the estimator will be calculated across trials separately for E6–E27 and E6–E123. Connectivity values will then be averaged with equal weights across the five frequencies and samples from 0–150 ms, followed by the arithmetic mean of the two pair scores. Cross-spectra from different pairs will not be pooled before estimation. No pair will be selected according to the observed effect.

Three cycles are a proposed project choice balancing temporal and frequency resolution, not a value mandated by Vinck et al. The time–frequency trade-off and reporting of Gaussian-envelope width follow Cohen (2019). At 4 Hz, the Gaussian standard deviation is approximately 0.119 s; MNE's ±5-standard-deviation wavelet support therefore extends approximately 0.597 s either side of each centre (MNE-Python contributors, n.d.). The amplitude-envelope temporal full width at half maximum is approximately 281 ms at 4 Hz and 141 ms at 8 Hz; frequency-envelope full width at half maximum is approximately 3.14 and 6.28 Hz respectively. The broad spectral sensitivity is a cost of using three cycles, so 4–8 Hz describes wavelet centre frequencies rather than an ideal sharply bounded passband. Connectivity epochs will be −1.0 to +1.15 s, with coefficients computed over the full epoch before selecting the scoring interval. Epochs intersecting discontinuities will be excluded. Use complex single-trial coefficients without ERP subtraction, power normalisation or baseline correction of connectivity. ERP baseline correction remains specific to H1. Compute the transform before cropping to 0–150 ms; do not crop the raw epoch to that window before convolution. Signal support and implementation will be checked before hypothesis testing. This smoothing means the score cannot be interpreted as activity confined strictly to the first 150 ms after a response.

Within each participant and variant, let m be the smaller usable trial count across error and correct conditions. Draw m trials without replacement from each condition, estimate both scores, and repeat this matching 1,000 times using seed 42. Average these estimates to obtain one score per condition per variant. Repeated draws are computational averaging, not independent observations. Report the actual trial counts; matching within a participant does not match precision across participants. H3 will use the resulting error-condition measure to maintain consistency of measurement.

A two-sided paired-samples t-test will compare the resulting participant-level error and correct scores. The predicted error-minus-correct difference is positive. Report the paired mean difference, its 95% confidence interval, d_z, t statistic, degrees of freedom and raw/adjusted p-values. The assumptions and diagnostic policy specified for H1 also apply to H2.

#### H3: synchrony–PES association and the role of H2

Spearman's correlation will assess the association between participant-level error-trial synchrony and mean valid PES. The prediction is positive; the primary test will be two-sided. A participant-label permutation test with 10,000 permutations and seed 42 is proposed, using the proportion of absolute permuted correlations at least as large as the observed value, with a plus-one correction. Participants, rather than trials or recordings, are the units permuted. This permutation test assumes exchangeability of participant labels under the null; it is an unadjusted association and does not establish independence from study site or other participant characteristics. Report rho, the p-value and a paired participant-bootstrap percentile 95% interval using 10,000 resamples, resampling each participant’s synchrony and PES together. These resampling settings are proposed project choices.

H3 will be tested irrespective of whether H2 reaches statistical significance. If H2 is unsupported, an H3 association would indicate a relationship between connectivity measured on error trials and PES, but would not establish that the relevant connectivity is elevated specifically by errors. A null H2 result will not be interpreted as proof of equality. Effect sizes and intervals will inform whether the H2 evidence is imprecise or inconsistent with the predicted contrast. H3 will not be used retrospectively to claim that H2 was supported.

#### H4a: reliability comparison and uncertainty

Use only error and correct trials eligible under the same EEG support and artefact criteria for both measures, so differences in epoch support do not give one measure a different error-trial pool. PES-valid triplets are not required for H4a. For each participant and variant, draw N error trials without replacement and split them randomly into two halves of N/2. Use the identical error identities and halves for connectivity and ERN. Independently draw N usable correct trials and divide these into two non-overlapping N/2 halves for CRN. Each half's ΔERN is its ERN minus CRN. Thus N always denotes total errors per variant, not errors per half; there are also N correct trials per variant. This equal correct-trial allocation is a controlled methodological comparison, not necessarily the most precise ΔERN obtainable from all correct trials.

For each half, calculate connectivity and ERP scores separately within each variant, then average the three variant scores with equal weights. Across the same eligible participants, calculate Pearson's correlation between half scores for each measure and apply r_SB = 2r/(1+r). Report both raw and corrected coefficients; retain negative estimates rather than replacing them with zero. The Spearman–Brown correction is the supervisor-requested convention, but its equal-half assumptions are not guaranteed for nonlinear connectivity estimators. The comparison therefore concerns empirical split-half consistency under this scoring procedure.

The candidate grid is N = 20, 40, 60, … total error trials per variant, giving 10, 20, 30, … errors per half. Retain a grid point only if at least 30 participants have N eligible errors and N eligible correct trials in each of the three variants. Freeze this feasible grid from quality-control counts before computing reliability coefficients. These grid and participant floors are explicit project recommendations, not thresholds from the submitted proposal or proof of adequate statistical power. If no point qualifies, report H4a as infeasible under the protocol; do not claim a reliability advantage. Changing participant composition across grid points will be reported and prevents attributing the entire curve to trial count alone.

The primary estimate at each feasible count uses one reproducible random draw/partition from seed 42. Preserve trial identifiers and deterministic participant/variant ordering. Define D = r_SB(connectivity) − r_SB(ΔERN). Obtain its sampling interval from 20,000 paired participant bootstrap resamples (seed 43), retaining each sampled participant's four half scores together and recomputing both correlations and corrections. Hold the original trial partition fixed during this bootstrap: these intervals quantify participant sampling uncertainty conditional on that partition. Dependence between the measures must be retained, as in bootstrap comparisons of dependent correlations (Rousselet, 2017).

If K trial counts are feasible, construct percentile intervals using the α/(2K) and 1−α/(2K) quantiles with α = .05. An interval wholly above zero supports higher reliability at that particular count; one wholly below zero indicates the opposite direction. An interval including zero does not establish a difference. This is an interval-based, approximate bootstrap comparison with a Bonferroni adjustment across the K counts; no additional p-value is manufactured from repeated trial splits. A favourable count does not establish superiority at every count.

Zero-variance half scores, undefined correlations or a singular Spearman–Brown correction make a comparison non-estimable. Report their frequency. If any bootstrap estimates are undefined, do not silently drop them and claim a valid interval; flag the interval as not estimable under this procedure. Near-singular corrections and strongly skewed bootstrap distributions will be reported as instability. The adjusted intervals have only approximate coverage and require particular caution in small or low-reliability samples.

#### H4b: stability across partitions

Repeat trial selection and the matched split-half procedure using 1,000 random draws/partitions with seed 44, keeping the sampling rules and participant set fixed within each trial-count comparison. Summarise the median and 2.5th and 97.5th percentiles of the reliability estimates and paired reliability differences. These describe sensitivity to partitioning, not population confidence intervals. Splits are not independent cases and will not be entered as observations into a t-test or other inferential comparison.

#### Multiple testing and decision rules

H1, H2 and H3 will form one confirmatory family, with their three two-sided p-values adjusted by Holm's method at familywise α = .05 (Holm, 1979). H3 remains the primary scientific question; including all three tests in this family does not change that priority. Report raw and adjusted p-values. A supported directional hypothesis requires both an adjusted p-value below .05 and an effect in its predicted direction. If a planned test cannot be estimated, retain its family slot with p = 1 for the adjustment and explicitly report the analysis as unavailable rather than as a measured null result.

H4a is a separate secondary family, controlled approximately by the Bonferroni-adjusted bootstrap intervals described above. This family separation controls each family at .05, not the probability of any false positive across the entire project at .05. H4b is descriptive. Unadjusted 95% intervals accompanying H1–H3 are estimates of uncertainty, not simultaneous familywise intervals. No additional electrode-pair, time-window or variant-specific confirmatory tests will be added after inspecting effects.

#### Decision timing and reproducibility

Maintain the dated decision log in Appendix A, stating the decision, rationale, information already inspected, review status and affected analyses. Existing behavioural feasibility audits and single-recording EEG checks precede this revision; later choices cannot be described as having been made before any data inspection. Decisions informed by trial counts or artefacts will be identified as data-informed feasibility decisions. Changes prompted by hypothesis results will be reported as exploratory departures. Record software versions, seeds, exclusions and analysis-specific sample sizes.

### Procedure

Review this revised methodological specification and confirm institutional review requirements and the factual governance arrangements. Apply the agreed behavioural screening and recording-specific EEG checks to eligible recordings. Derive the participant-level ERP, synchrony and PES measures, then conduct the specified hypothesis tests and reliability analyses. Preserve original trial identities and maintain reproducible processing and exclusion records throughout.

### Ethics and Data Governance

The study uses existing de-identified ds004883 EEG and behavioural data. The submitted proposal cites Clayson et al. (2024) for written consent covering public sharing and associated risks. No participants will be contacted, no new data will be collected, and no attempt will be made to identify individuals or link records to identifying information. University review arrangements must be confirmed with the module tutor; this revision does not claim approval has been obtained.

The following lifecycle plan replaces the general promise to document storage later. Its proposed controls must be confirmed and implemented; their presence in this document is not evidence that they currently exist.

| Lifecycle element | Planned arrangement | Confirmation required |
| --- | --- | --- |
| Source storage | Preserve the dataset under `/home/moyo/neuro_projects/essex_project/data/ds004883_Clayson/` as the unmodified source copy. | Identify the host/device, ownership and whether this location meets university requirements. |
| Derived storage | Keep processed participant-level outputs and audit tables under `results/`; figures under `figures/`; code under `scripts/` and `notebooks/`. Use dataset codes, not identifying information. | Confirm suitable protection for saved epochs and any future derived-file locations. |
| Access | Proposed access is limited to the researcher; additional access is granted only to named authorised people through approved arrangements. | State who currently has host/account/administrative access and the intended supervisor access route. |
| Security | Use authenticated accounts and encrypted storage and transfers for working and backup copies. | Confirm actual authentication, encryption and device-security arrangements; do not assert implementation without checking. |
| Backup and recovery | Proposed automated daily backup of code, decision logs and irreplaceable derived outputs to an approved separate location, with periodic restore checks. Record the dataset version/retrieval source. | Name the backup service/location, access holders, encryption and restore-check schedule. |
| Retention | Retain project records and necessary derived data for the period required by the programme and applicable institutional policy. Record its start event and end date. | Obtain the exact retention period and authoritative policy; no arbitrary number of years is assumed. |
| Sharing | Report aggregate results and reproducible code. Review participant-level tables and notebook outputs before any sharing; use approved channels and the dataset's terms. | Confirm permissible repositories, recipient access and any required institutional review. |
| Disposal | At the approved retention endpoint, remove unnecessary local and backup copies through the storage provider's approved deletion process. Record what was disposed of and when. | Confirm the practical deletion procedure, including backup expiry and any exceptions requiring continued retention. |

Until the outstanding facts are supplied, the data-governance correction is incomplete. Source files and the final submitted PDF will remain unchanged. Exclusion reporting and methodological amendments are documented in Methods rather than treated as data-security safeguards.

### Limitations

This study uses an existing dataset, so the available task design, recordings and behavioural information cannot be modified. Differences between the three flanker variants may influence EEG responses and post-error behaviour, requiring explicit consideration in the analysis. Participant eligibility will depend on EEG quality, usable error trials and valid behavioural sequences. Exclusions may reduce the analysable sample and limit generalisability. Small error-trial counts may also produce imprecise synchrony and reliability estimates, particularly when trials are divided into halves. Post-error slowing is a behavioural index rather than a direct measure of adaptive cognitive control. Comparing responses immediately before and after errors addresses some local fluctuations in response speed but does not eliminate all influences, including trial difficulty and congruency. Uncertainty about the correspondence between recorded event markers and physical stimulus timing also limits interpretation of absolute reaction times. Scalp EEG provides limited anatomical specificity. Although dWPLI reduces sensitivity to some zero-lag effects and sample size bias, it does not eliminate artefact contamination or establish direct communication between brain regions. Standard electrode correspondences do not represent individual anatomical localisation, and time frequency smoothing limits the temporal specificity of connectivity estimates. Finally, associations between synchrony and PES cannot establish causation. Higher split-half reliability would indicate greater internal consistency under the chosen conditions, but would not by itself establish greater validity or stability across separate recording sessions.

The complete-variant participant summary may further reduce the eligible sample. Equal averaging across tasks and electrode pairs provides a single interpretable score but can conceal heterogeneity. The wavelet settings trade frequency specificity against temporal resolution and require validation. These choices do not eliminate residual confounding from trial counts, congruency, recording quality or stable participant differences.

## Timeline

The submitted timeline remains indicative and is not a claim of completed work or guaranteed review duration.

| Work package | Main activities | Indicative timing |
| --- | --- | --- |
| Finalise protocol | Agree revisions, eligibility, connectivity and reliability settings; complete governance details. | Week 1 |
| Ethics review | Confirm the required process, submit documents and address revisions. | Weeks 2–3 |
| Behavioural screening | Apply agreed exclusions to existing trial records. | Weeks 4–5 |
| EEG preprocessing | Extend reviewed processing and record usable trials. | Weeks 5–7 |
| Calculate measures | Derive PES, ΔERN and theta synchrony. | Weeks 7–9 |
| Statistical analysis | Test H1–H3; conduct H4a and H4b. | Weeks 10–12 |
| Write-up | Complete results, discussion and limitations. | Weeks 13–14 |
| Revision and submission | Proofread and check reporting, references and formatting. | Week 15 |

## References

Cavanagh, J. F., Cohen, M. X., & Allen, J. J. B. (2009). Prelude to and resolution of an error: EEG phase synchrony reveals cognitive control dynamics during action monitoring. *Journal of Neuroscience, 29*(1), 98–105. https://doi.org/10.1523/JNEUROSCI.4137-08.2009

Clayson, P. E., Brush, C. J., & Hajcak, G. (2021). Data quality and reliability metrics for event-related potentials (ERPs): The utility of subject-level reliability. *International Journal of Psychophysiology, 165*, 121–136. https://doi.org/10.1016/j.ijpsycho.2021.04.004

Clayson, P. E., Rocha, H. A., McDonald, J. B., Baldwin, S. A., & Larson, M. J. (2024). A registered report of a two-site study of variations of the flanker task: ERN experimental effects and data quality. *Psychophysiology, 61*(9), Article e14607. https://doi.org/10.1111/psyp.14607

Cohen, M. X. (2019). A better way to define and describe Morlet wavelets for time-frequency analysis. *NeuroImage, 199*, 81–86. https://doi.org/10.1016/j.neuroimage.2019.05.048

Danielmeier, C., & Ullsperger, M. (2011). Post-error adjustments. *Frontiers in Psychology, 2*, Article 233. https://doi.org/10.3389/fpsyg.2011.00233

Dutilh, G., van Ravenzwaaij, D., Nieuwenhuis, S., van der Maas, H. L. J., Forstmann, B. U., & Wagenmakers, E.-J. (2012). How to measure post-error slowing: A confound and a simple solution. *Journal of Mathematical Psychology, 56*(3), 208–216. https://doi.org/10.1016/j.jmp.2012.04.001

Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70. https://www.ime.usp.br/~abe/lista/pdf4R8xPVzCnX.pdf

Holroyd, C. B., & Coles, M. G. H. (2002). The neural basis of human error processing: Reinforcement learning, dopamine, and the error-related negativity. *Psychological Review, 109*(4), 679–709. https://doi.org/10.1037/0033-295X.109.4.679

MNE-Python contributors. (n.d.). *mne.time_frequency.tfr.morlet*. Retrieved September 27, 2026, from https://mne.tools/stable/generated/mne.time_frequency.tfr.morlet.html

Murphy, P. R., van Moort, M. L., & Nieuwenhuis, S. (2016). The pupillary orienting response predicts adaptive behavioral adjustment after errors. *PLOS ONE, 11*(3), Article e0151763. https://doi.org/10.1371/journal.pone.0151763

Rousselet, G. (2017, March 1). *How to compare dependent correlations*. Basic Statistics. https://garstats.wordpress.com/2017/03/01/comp2dcorr/

SciPy community. (n.d.). *ttest_rel*. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html

University of Essex Online. (2025). *Research: Ethical approval policy.* https://online.essex.ac.uk/uploads/sites/7/2025/09/Research-Ethical-Approval-Policy.pdf

Valadez, E. A., & Simons, R. F. (2018). The power of frontal midline theta and post-error slowing to predict performance recovery: Evidence for compensatory mechanisms. *Psychophysiology, 55*(4), Article e13010. https://doi.org/10.1111/psyp.13010

Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., & Pennartz, C. M. A. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. *NeuroImage, 55*(4), 1548–1565. https://doi.org/10.1016/j.neuroimage.2011.01.055

The online MNE documentation is a moving reference; implementation must be checked against the project’s installed version. The wavelet and software sources support the mathematical descriptions; they do not establish that the selected cycles, aggregation or eligibility thresholds are optimal for this dataset. The dependent-correlation source supports preserving participant-level dependence, not a validated coverage guarantee for this particular transformed reliability statistic.

## Appendix A: Decision record and remaining factual requirements

| Date | Decision or evidence | Basis and status |
| --- | --- | --- |
| Before 27 September 2026 | Behavioural structure/counts and one recording's ERP had already been inspected. | Existing notebook and saved Task 2/4/5 audits; the revision is not prior to all data inspection. |
| 27 September 2026 | Specify paired H1/H2 tests, one H1–H3 Holm family and explicit H2–H3 interpretation. | Response to supervisor feedback; revised protocol choices, no hypothesis tests executed. |
| 27 September 2026 | Specify three-cycle complex Morlet estimation and equal pair/task averaging. | Proposed balance of resolution and a fixed participant-level score; technical assumptions and attrition costs disclosed. |
| 27 September 2026 | Specify marker-relative RT screening, 10-trial eligibility floors, H4 count grid and bootstrap/partition procedures. | Project recommendations to make the protocol concrete; thresholds are not claimed as published adequacy guarantees. |
| 27 September 2026 | Inspect existing practice/timing audits rather than reconstruct trials again. | No automatic first-24-trial exclusion or assumed physical-onset correction. |
| Before implementation | Review feasibility and verify the scoring implementation using synthetic or diagnostic checks. | Do not tune settings to maximise hypothesis effects; record any amendments and their timing. |

The outstanding factual requirements are the host/device and ownership, actual access holders, implemented encryption, backup destination and restore procedure, the applicable retention period and disposal arrangements, and institutional review status. These require the researcher or programme to provide facts; they cannot be completed by inventing arrangements. The data-governance table records the intended controls until those facts are supplied.

No confirmatory analyses were run as part of preparing this document. The next review should confirm that the researcher understands the proposed implementation and resolve the factual governance details before calling this a complete final protocol.
