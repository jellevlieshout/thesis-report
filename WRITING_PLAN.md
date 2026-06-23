# Writing Plan (2026-06-10)

Full draft to Mari Carmen **June 29** · submission July 7 · defence ~July 14.
Target: ~50 pages excl. appendices (currently 42 compiled, incl. placeholders and guide comments).

Every chapter `.tex` now contains a `% === WRITING GUIDE ===` block per section with: the section's job, page budget, the points/numbers/citations it must land, and the theme hook. This file is the map; the guides are the territory.

## The central theme: structure over scale

> When LLMs adapt figurative language into Easy-to-Read English, reliable quality does not come from where current practice looks for it (larger models, cleverer prompts) but from explicit structure: decomposing the task into inspectable steps and grounding evaluation in human judgement. Scale lifts detection (+18-20pp F1) but not human-perceived quality (70B significantly worse on simplicity, p=0.026); prompt-engineering gains are model-dependent and invert in sign across scales (+12/+22pp at 8B vs -28/-5pp at 70B); no automatic metric can see replacement quality at all (BERTScore ~0.915 everywhere); decomposition yields a consistent though marginal human-rated advantage on meaning preservation (+0.31z, p=0.06-0.08) while making every failure attributable to a specific step. The lever that pays is structure, in both the system and its measurement.

Supporting frames: **the missing E2R guideline** (motivates Ch 1-2) and **the measurement gap** (motivates Ch 4).

**Honesty discipline.** The claim is that structure is the *reliable, inspectable* lever, NOT that structure always wins. Concede openly: pipeline detection ≡ detection-only (now Section 6.4); composite is tied; the schema inversion is itself a structure effect with a negative sign (fold it in: the inversions were only *discoverable* because decomposition isolated the conditions). Scope sentence to reuse: "decomposition helps where the task is generative and underdetermined (replacement), not where it is discriminative (detection)."

### Style: plain English (non-native author and audience)

Jelle and the UPM readers are non-native English speakers. Write short sentences and common words; avoid dense multi-clause sentences and uncommon vocabulary (flagged: "lexicalised", "no-op"); define technical terms plainly on first use. The thesis is about easy-to-read adaptation, so the prose should practise it. Full rule: memory `thesis-plain-english` + `writing-mode.md` in the thesis skill. Also: stick to open-weights models in the prose; do not discuss the hosted/Gemini dev-time results.

### Mandated hedges (use the same wording in every chapter that touches the claim)

- **RQ2**: "a consistent directional advantage on meaning preservation (+0.31 standardised units, p = 0.06-0.08) that approaches but does not reach conventional significance; suggestive support for H2, strengthened by convergent qualitative evidence of span-anchored rewriting, rather than a confirmed effect." Never "significantly better". Never composite superiority (z 0.123 vs 0.125).
- **70B simplicity**: "in this setup, scale did not buy, and on simplicity may have cost, human-perceived quality." One dimension, one comparison, 20 raters; not "scale hurts quality".
- **RQ1 supervised comparison**: the 200-example T=0 slice is indicative, not leaderboard-comparable; Jia 2024 is the supervised-can-win counterpoint.

## Narrative arc

1 missing guideline → 2 ends on the measurement gap → 3 embodies structure (designed experiment) → 4 structures the measurement → 5 scale's one win + the inversion twist → 6 the decomposition verdict → 7 the survey heart ("systems preserve meaning but do not simplify") → 8 three findings, one pattern → 9 verdicts.

> Note (2026-06-22): the Discussion synthesis is now **three open-weights findings**, not four. The hosted/Gemini result was cut on Jelle's instruction; stick to open-weights (8B, 70B) throughout. The three findings: (i) adding a forced replacement field to the detection prompt helps 8B and hurts 70B; (ii) pipeline detection equals detection-only; (iii) the larger model is rated no better and worse on simplicity.

## Chapter status and remaining prose

| Ch | File | pp | Remaining prose (guides embedded in file) |
|----|------|----|--------------------------------------------|
| 1 Introduction | `introduction.tex` | 4 | full rewrite, ~1,800 w (5 scaffolded subsections) |
| 2 Background | `background.tex` | 8 | 2.1 figurative language ~700 w, 2.2 E2R/FACILE ~800 w (new section), 2.3 LLMs/agentic ~700 w, 2.6 synthesis ~300 w; compress "other datasets" list to a paragraph. **Make 2.6 a named "Research Gap" closing subsection** (TFM-cohort norm: every SOTA chapter closes by stating the gap as a gap, not just a summary). |
| 3 System Design | `system_design.tex` | 7 | expand Baselines bullets ~250 w; make the 3-step pipeline explicit in 3.2; figures F-1/F-2 (placeholders in) |
| 4 Methodology | `methodology.tex` | 5 | done; verify the as-run QC text (updated 2026-06-10) against `analyze_survey_responses.py` once more before submission |
| 5 RQ1 | `rq1_detection.tex` | 5 | 5.4 supervised comparison ~400 w + fill Table T-D (literature lookup, the only external dependency: START EARLY); 5.5 qualitative examples ~300 w |
| 6 RQ2 | `rq2_decomposition.tex` | 5 | 6.3 prose around the human-eval table ~700 w; 6.4 is drafted (moved from Discussion), edit freely |
| 7 RQ3 | `rq3_replacement.tex` | 8 | 7.6 survey-results prose ~1,200 w (tables + QC table in, four-move structure in guide); 7.7 qualitative examples ~400 w; figure F-3 |
| 8 Discussion | `discussion.tex` | 6 | DONE (8.1 keystone, 8.2, 8.3, 8.5 drafted). On read-through: **ensure visible per-RQ/per-hypothesis closure** (Vaccari TFM model: Discussion answers each RQ explicitly). Our per-RQ result chapters already carry the verdicts; confirm §8 names them off so the loop visibly closes. |
| 9 Conclusion | `conclusion.tex` | 2 | ~900 w (closing-sentence draft in guide) |
| Front/back | `abstract/resumen/acknowledgement.tex` | 1 | refresh abstract against final claims, THEN translate resumen; acknowledgements; cover date "Madrid, MM YYYY" → July 2026. **Add an AI-use disclaimer page** (2025 UPM norm; 3 of 7 sampled TFMs include one): name the tools used and assert author responsibility for all analysis. |
| Appendices | (new) | 4-8 | **Add appendices** (TFM-cohort norm: every sampled thesis offloads bulk here, often a third of page count): survey instrument, QC rules, example survey items, system prompts. Cheap expected pages that pull bulk out of the body. |

Done 2026-06-10 (Claude): RQ4 chapter dissolved into 8.3; orphan files deleted (`intro/conclusions/development.tex`); stale survey numbers fixed everywhere (final: 27 sources × 3 = 81 items, 22 collected → 20 kept, 71/81 ≥3 ratings); methodology QC text aligned to as-run rules (completion <10/20; repeat-pair mean |diff| > 25 drop; bad-ref vs own real-item meaning mean, flag-only); Williams'-test and bootstrap-CI claims corrected to paired t + Wilcoxon and Student-t CIs; survey tables inserted (6.3, 7.6, 8.1, QC stats); `sec:rq1` label added; SARI wording finalised; compile clean at 42 pp.

## TFM-cohort benchmark (2026-06-22)

Investigated 7 prior UPM TFMs (`1 - Thesis/Other Theses/`). All are HCID / Digital Innovation **design** theses, not NLP, so their methods do not transfer, but they are a clean rubric for UPM structural and grounding norms. Findings:

- **Structure**: we are on-model. Shared arc is Intro → thematic SOTA → Methods → empirical chapters → Discussion → Conclusion, bilingual front matter. Two patterns folded in above: named **Research-Gap** subsection closing the SOTA, and **per-RQ closure** in the Discussion (Vaccari is the model).
- **Grounding**: not a risk. Their reference counts run 26-59 (median ~35). We cite ~28 keys now with the citation-heavy sections (Background 2.1/2.2, RQ1 5.4) still undrafted; we will land ~40-55, at or above their median, and on peer-reviewed venues vs their heavy vendor/grey-lit. Floor is "match median"; the undrafted Background and 5.4 clear it.
- **Our differentiators (preserve)**: inferential statistics (none of the 7 ran any; two made significance claims with no test named) and numbered RQs + H1-H4 (the cohort's recurring weakness is vague prose-goal RQs). Our calibrated hedging is exactly the virtue they are dinged for lacking.
- **Three additions** (now in the chapter table + schedule): appendices, AI-use disclaimer page, named Research-Gap subsection.
- **Optional**: List of Figures/Tables is omitted by 5 of 7; skip if the read-through runs tight.

## Open verification flags (grep `TODO(verify)`)

- **Survey conditions are the 3-step pipeline, not single-call CoT** (TODOS.md 22f, switched 2026-05-05). §6.1 and the §7.5 conditions list now say so. But the survey-pool automatic numbers in `tab:rq2-automatic` (agentic F1 0.609/0.282, BLEU 0.061) and the `discussion.tex` scale-dependence paragraph (0.609 → 0.767) predate the switch and may describe the single-call run of 2026-05-04. Re-derive the survey-pool metrics from runs `aea60b3d / 460d4b15 / 10366af9` so every number describes the system the survey actually rated; confirm pool N (28 vs 30) at the same time. Do this before writing §6.3/§7.6 prose (Jun 17).

## Schedule: weekend-aware, June 18 to June 29

Revised 2026-06-18 to account for the two weekends (Jun 20-21 and Jun 27-28), which the original Jun 10 schedule had silently treated as working days. Today is Thursday 18 June; deadline Monday 29 June. That leaves roughly 6.5 working days plus the Monday send. The Jun 18 session ran well ahead, clearing the old Jun 17-18 block (7.6, 6.3, 6.4) and most of the old Jun 19-20 block (8.1, 8.3), plus the 6.2 reframe and the verification harness, which absorbs the lost weekend time. Mari Carmen is at a conference the week of Jun 22; substantive feedback expected only at the Jun 29 full-draft review.

| Day | Work |
|---|---|
| Thu Jun 18 (done) | 7.6; 6.2 reframe; 6.3; 6.4 clarification; 8.1 keystone; 8.3; verification harness built; all bibliography PDFs filed by bibkey. |
| Fri Jun 19 | Finish Discussion (8.2, 8.5); draft Introduction (~1,800 w). |
| Sat-Sun Jun 20-21 | Off. Optional light task: read the spine sections (7.6, 6.3, 8.1, 8.3) for voice. |
| Mon Jun 22 | Conclusion (~900 w); Background 2.1 and 2.6. |
| Tue Jun 23 | Background 2.2 (E2R/FACILE) and 2.3; drafted from the filed PDFs, then verified. |
| Wed Jun 24 | RQ1 5.4 (supervised SOTA) and 5.5; 3.3 baselines prose. |
| Thu Jun 25 | Figures F-1/F-2/F-3; the four pre-existing overfull tables; abstract, resumen (Spanish), acknowledgements; cover date to July 2026; **AI-use disclaimer page**; **appendices** (survey instrument, QC rules, example items, system prompts). |
| Fri Jun 26 | Full read-through: theme-thread pass, whole-thesis harness sweep, citation/label audit, stale-number grep, page tuning (trim Ch 2 first if over). |
| Sat-Sun Jun 27-28 | Off. Genuine buffer if a weekday slipped. |
| Mon Jun 29 | Final compile, send full draft. |

**Cut order if a day slips:** optional figures, then 5.5 qualitative examples (fold one example into 5.3), then trim 2.1 to one page.

**Only-you tasks (a first draft cannot replace these):** the voice read of the drafted sections; and verifying the relayed claims for 2.2 and 5.4 if you would rather read those PDFs yourself rather than have a subagent extract them.

## Mari Carmen's deferred review items → where they land

- *Storyline framing* → thesis statement in 1.2 + synthesis 8.1 (send Ch 6-8 by ~Jun 20).
- *FACILE positioning* → 2.2 (per-guideline-module pattern) + 1.1 + Spanish future work 8.6.
- *H4 keep-vs-drop* → kept: stated in 1.3, flagged untested; rationale + proposed design in 8.5.
- *§5a bad-ref filter adaptation* → `methodology.tex` QC-filter subsection now documents the as-run rule (vs respondent's own real-item meaning mean, flag-only); metaphor-drop rationale in Ch 4 intro + 7.3.
