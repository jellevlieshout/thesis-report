# Section Briefs

Per-section writing briefs for the 17-29 June drafting phase. Companion to
`WRITING_PLAN.md` (the locked plan) and the `% === WRITING GUIDE ===` blocks in each
chapter `.tex`. Format and workflow are defined in the thesis skill's `writing-mode.md`.

Each brief layers two dimensions on top of the existing guide blocks: a **grounding
assessment** (does this section need new literature, and if so what to research) and a
**relay checklist** (what to hand Claude before drafting). Briefs are generated
just-in-time, one section ahead, not all at once.

## Master triage table

Grounding status across all remaining sections, so the literature load is visible at a
glance. `solid` = writes from data or citations already held; `EXPAND` = needs new
literature research before drafting. **Front-load the two EXPAND sections** (2.2 and 5.4):
they are the only hard external dependencies, everything else writes from owned data plus
the wiki's existing paper summaries.

| Section | Budget | Schedule | Grounding | Research needed |
|---|---|---|---|---|
| 7.6 Survey Results | ~1,200 w | Jun 17-18 | solid | none (own survey data) |
| 6.3 RQ2 prose + table reframe | ~700 w | Jun 17-18 | solid | none (own data + recompute) |
| 8.1 Discussion keystone | ~800 w | Jun 19-20 | solid | none (synthesis of findings) |
| 8.2 Metaphors | ~500 w | Jun 19-20 | light | optional: 1-2 metaphor-processing cites (wiki likely covers) |
| 8.3 Observability | ~500 w | Jun 19-20 | solid | none (own system) |
| 8.5 H4 future work | ~250 w | Jun 19-20 | solid | none (proposed design) |
| 1 Introduction | ~1,800 w | Jun 21-22 | light | E2R-guideline + FACILE framing cites (shared with 2.2) |
| 9 Conclusion | ~900 w | Jun 21-22 | solid | none |
| 2.1 Figurative language | ~700 w | Jun 23-25 | mostly solid | wiki summaries cover; confirm 1-2 anchor cites |
| **2.2 E2R / FACILE** | ~800 w | Jun 23-25 | **EXPAND** | E2R guidelines, Inclusion Europe, FACILE method, per-guideline-module framing |
| 2.3 LLMs / agentic | ~700 w | Jun 23-25 | mostly solid | wiki summaries cover; confirm agentic-decomposition cites |
| 2.6 Synthesis | ~300 w | Jun 23-25 | solid | none (ties the chapter to the gap) |
| **5.4 Supervised comparison** | ~400 w | Jun 26 | **EXPAND** | supervised SOTA for VUA + SemEval Task 2A: Neidlein 2020, Jia 2024, task-overview paper, fill `tab:rq1-supervised` |
| 5.5 Qualitative examples | ~300 w | Jun 26 | solid | none (own outputs) |
| 3.3 Baselines + figures | ~250 w | Jun 26 | solid | none |
| Abstract / resumen / ack | ~1 p | Jun 27 | solid | none (refresh against final claims) |

---

## §7.6 Survey Results [budget: ~1,200 w · Jun 17-18 · FIRST]

**JOB.** The evidentiary heart of the thesis. Report the human-evaluation results in four
moves (guide block in `rq3_replacement.tex` lines 119-139). Land the headline: the systems
preserve meaning but do not simplify.

**THEME HOOK.** Structure over scale plus the measurement gap. The survey is the
load-bearing human-grounded instrument; the simplicity shortfall is the remaining E2R
challenge that no automatic metric in 7.2 could see (BERTScore ~0.915 for everything).
Apply the mandated 70B-simplicity hedge verbatim. Defer the agentic-vs-monolithic meaning
claim and its hedge to 6.3, report only the per-system means here.

**DATA** (from `Survey/results/RESULTS.md`; tables `tab:rq3-survey-results` and
`tab:rq3-survey-qc` already inserted):

- *Move 1, response + QC.* 22 collected (19 native, 3 long-term residents); 2 excluded on
  the repeat-pair filter (mean |diff| > 25); 0 completion exclusions; 0 bad-reference
  flags; 20 retained. Coverage: all 81 (source, system) pairs rated >= 2 times, 71/81
  rated >= 3 times.
- *Move 2, per-system scores.* Raw means gram / meaning / simplicity: 8B agentic
  83.1 / 81.6 / 60.6; 8B monolithic 85.4 / 72.6 / 64.1; 70B agentic 78.4 / 76.4 / 51.9.
  Grammar and meaning high (78-85) across all systems; simplicity uniformly weakest
  (52-64). Headline sentence: systems preserve meaning but do not simplify.
- *Move 3, scale cut (RQ1).* 70B agentic directionally lower on every dimension,
  significantly lower on simplicity (paired by source, n=27: delta-z = -0.347 vs 8B
  agentic, Wilcoxon p = 0.026, t p = 0.075); composite p = 0.066. Mandated hedge.
- *Move 4, free text.* 108 alternative replacements collected. Qualitative signal: humans
  shorten and restructure, not just substitute. Feature 1-2 examples; fuller treatment
  optional in Discussion 8.x.

**CITES ON HAND.** Graham2013, Graham2017 (Direct Assessment, already used in
methodology); Alva-Manchego2021, Scialom2021 (automatic-metric spuriousness, used in 7.2 /
rq2). No new literature required.

**GROUNDING.** Solid. No external research. Optional once 2.2 exists: one sentence linking
the simplicity gap to E2R readability literature, not blocking.

**RELAY** (what to hand back before drafting):
1. Pick the 1-2 free-text alternative replacements to feature (from
   `Survey/results/responses_long.csv`), or say "you choose".
2. Confirm: fold the RQ2 meaning result into 6.3 only (recommended), or also preview it here?
3. No literature relay needed for this section.

## §1 Introduction [budget: ~1,800 w · next · write AFTER reading 8.1]

**JOB.** Establish the "missing E2R guideline" motivation; state the central thesis; present RQ1-RQ3 with H1-H4 (H4 flagged untested up front); list contributions. Carries Mari Carmen's deferred items: storyline framing and FACILE positioning, first. Guide block is in `introduction.tex` (detailed, self-sufficient).

**THEME HOOK.** Structure over scale, in the plain wording the fixed 8.1 keystone now uses: explicit task structure is the reliable lever; human evaluation is how its effect is made visible (NOT "evaluation is a lever"). Anchor to 8.1 in `discussion.tex` so the framing does not overstate the evidence.

**DATA / anchors.** Three open-weights findings (not four; hosted/Gemini cut). Do not discuss hosted models. **H4 dependency (from 8.5):** the intro must state H4 verbatim ("explicit intermediate explanations generated by the agent correlate positively with the semantic correctness of the final literal replacement"), flag it untested up front, and forward-ref `\ref{sec:discussion-h4}`.

**CITES ON HAND.** FACILE per-guideline-module pattern: `Surez-Figueroa2023` (morphological), Diab2024 (dialogues), `Surez-Figueroa2024` (FACILE). All PDFs filed in Paper PDFS/. Position this thesis as the figurative-language module of that pattern.

**GROUNDING.** Solid. The guide block + wiki cover the motivation; FACILE cites in hand. No new reading required.

**RELAY.** None needed. Write in plain English (non-native audience). Say "parallel" treatment of idioms/metaphors, not "unified".

## §9 Conclusion [budget: ~900 w · Jun 22 · write AFTER §1 so the bookends match]

**JOB.** One verdict paragraph per RQ with the headline number; contributions recap; theme restated in one sentence; short forward pointer (do not rehash 8.6). Guide block in `conclusion.tex`. Bookend to §1: same framing, same hedge wordings as Ch 6/8.

**THEME HOOK.** Structure over scale, stated once in the closing sentence (past tense, with the evidence counts behind it). Echo the §1 / 8.1 wording; do not overstate.

**DATA / verdicts (mandated hedges verbatim):**
- *RQ1 (partial).* Zero-shot detection lags supervised SOTA (indicative, not leaderboard-comparable; Jia2024 is the supervised-can-win counterpoint). Within-family scale lifts sentence F1 +18-20pp (VU 0.430->0.635, SemEval 0.255->0.435), but the schema-commitment prompt effect inverts at scale (+12/+22pp at 8B vs -28/-5pp at 70B). Scale's gains end at detection. Forward-ref \ref{sec:rq1}.
- *RQ2 (suggestive support).* Automatic metrics blind (BLEU and BERTScore disagree). Human eval: "a consistent directional advantage on meaning preservation (+0.31 standardised units, p = 0.06-0.08) that approaches but does not reach conventional significance". Composite tied (z 0.123 vs 0.125). Failure traceability is the structural dividend (\ref{sec:discussion-observability}). Forward-ref \ref{sec:rq2}.
- *RQ3 (meaning yes, simplicity no).* Grammar and meaning high (raw 73-85), simplicity weakest everywhere (52-64). Idioms > metaphors (H3); metaphors have no gold paraphrases, itself the finding. 70B hedge: "in this setup, scale did not buy, and on simplicity may have cost, human-perceived quality" (Wilcoxon p=0.026). Forward-ref \ref{sec:rq3}.
- *H4.* Stated, untested, design proposed (\ref{sec:discussion-h4}).

**CITES ON HAND.** None new. Closing recap cites nothing; the verdicts point to the RQ chapters by \ref.

**GROUNDING.** Solid. No external research.

**RELAY.** None. Plain English (smooth, not choppy, per Jelle's §1 note). Closing sentence: avoid the contestable "four prompt designs" count from the guide draft; use defensible scope (two phenomena, two scales, agentic-vs-monolithic, 20-rater eval).

## §2.1 Figurative Language + §2.6 Research Gap [budget: ~700 w + ~300 w · Jun 22]

**JOB.** 2.1: idioms vs metaphors as phenomena; detection SOTA + its critique; the contested state of LLM figurative competence; the thin generation/adaptation side. 2.6: close Ch 2 by naming the gap as a gap (TFM norm), set up Ch 3 (build) + Ch 4 (measure). Guide blocks in `background.tex`.

**THEME HOOK.** "two literatures, one missing guideline." 2.6 closes: the literature offers structure as a promising lever (Tian, Badran, Gao) and warns no metric can adjudicate it (Lai, Alva-Manchego, Scialom); the next two chapters take both seriously.

**CITES ON HAND (all claims confirmed against wiki summaries 2026-06-22):**
- mipvu / vuamsterdammetaphorcorpus: MIP/MIPVU token-level metaphor procedure; corpus.
- Neidlein2020: high metaphor-detection F-scores largely reflect conventionalised word-sense disambiguation, not metaphor competence (frames Ch 5).
- Ichien2024: GPT-4 shows emergent ability to interpret novel literary metaphors, rated above college students (optimistic).
- Dmitrijev2024: pessimistic on detection (best detector finds 6/20 metaphorical words); detection needs phrase-level + world knowledge.
- Liu2022 (Fig-QA): LMs above chance but below human, gap largest zero-/few-shot.
- Lai2024 (Lai & Nissim): evaluation is the dominant bottleneck of figurative-language generation; auto metrics correlate weakly.
- Tian2024: theory-guided multi-step scaffolding (TSI) beats vanilla prompting and fine-tuned SOTA on metaphor.
- Badran2025: three-stage pipeline > monolithic on SemEval-2025 Task 1A (idioms).
- Gao2025 (PASS): paraphrase + self-check decomposition improves idiom understanding, esp. low-transparency idioms.
- Alva-Manchego2021, Scialom2021: auto metrics correlate only spuriously with human judgement on simplification (already in 2.5).

**GROUNDING.** Solid. No external research needed.

**RELAY.** None. Plain English (smooth). For 2.6 method-bet: do NOT assert all precedents used "hosted closed-source" backbones (unverified per-paper); phrase as "report wins on large models; whether decomposition holds on a mid-size open-weights deliverable is what RQ2 tests." Rename 2.6 to name the gap (TFM norm); add \label{sec:research-gap}.

## §2.3 Large Language Models & Agentic Systems [budget: ~700 w · Jun 23]

**JOB.** (1) prompting foundations (zero/one/few-shot, structured output, chain-of-thought); (2) decomposition precedents that make H2 motivated; (3) the supervised counterpoint (H1 not assumable); (4) observability as a design property (one paragraph, examined qualitatively in 8.3). Guide block in `background.tex`.

**THEME HOOK.** Structure as a promising-but-unsettled lever; sets up RQ2. Observability ties to the structure dividend.

**CITES ON HAND (verified 2026-06-22):**
- Tian2024: theory-guided multi-step scaffolding beats plain prompting on metaphor.
- Gao2025: paraphrase-then-self-check raises idiom understanding, no training.
- Badran2025: multi-stage idiom pipeline, competitive results (NOT pipeline-vs-monolithic).
- Hayashi2025: LLM-generated auxiliary context improves transformer metaphor detection (context-augmentation scaffolding).
- Jia2024: curriculum fine-tuning reaches SOTA metaphor detection (H1 counterpoint).
- **GAP**: foundational few-shot (Brown 2020) and chain-of-thought (Wei 2022) are NOT in bib/Mendeley; catalog did not surface clean metadata. Drafted with `% NEEDS SOURCE` markers; Jelle to add to Mendeley or drop.

**GROUNDING.** Mostly solid. Only gap = the two canonical prompting anchors (NEEDS SOURCE).

**RELAY.** Add Brown 2020 (few-shot) + Wei 2022 (CoT) to Mendeley if those anchors are wanted; otherwise the sentences can drop the citation. Plain English.

## §2.2 Easy-to-Read and Cognitive Accessibility [budget: ~800 w · Jun 23 · EXPAND - now grounded]

**JOB.** (1) E2R guidelines + target populations; figurative language explicitly discouraged, yet no guideline says HOW to replace it (the missing module); (2) UPM per-guideline-module pattern (FACILE trio); (3) position this thesis as the figurative-language module (English; Spanish port = future work 8.6); (4) E2R vs generic simplification (rubric implications, pays off in Ch 7). Guide block in `background.tex` lines 40-55. Carries Mari Carmen's FACILE-positioning deferred item.

**THEME HOOK.** "two literatures, one missing guideline." This section IS the missing-guideline motivation.

**CITES ON HAND (all verified 2026-06-23):**
- **InclusionEurope2009** (NEW, PDF filed by bibkey): "Information for All: European Standards for Making Information Easy to Read and Understand", Inclusion Europe, 2009, ISBN 2-87460-110-1. Target population stated: people with intellectual disabilities. **KEYSTONE QUOTE (p.10, General standards, rule 10):** "Do not use difficult ideas such as metaphors. A metaphor is a sentence that does not actually mean what it says. An example of a metaphor is 'it is raining cats and dogs'." Also rule 6-8 (use easy/known words, explain difficult words, use everyday examples), rule 14 (short sentences). This is the primary source for "E2R discourages figurative language but does not say how to replace it".
- **UNE2018** (NEW, no PDF - paywalled): Spanish standard UNE 153101:2018 EX, "Lectura Fácil: Pautas y Recomendaciones para la Elaboración de Documentos", UNE, 2018. Use for the Spanish-context / future-work tie (8.6) and to show E2R is formally standardised.
- Surez-Figueroa2023 (morphological module), Diab2024 (dialogue module), Surez-Figueroa2024 (FACILE: assess + transform architecture). Already held + verified.
- Alva-Manchego2020 (simplification rubric/survey) for the E2R-vs-simplification distinction; already cited in 2.5.

**GROUNDING.** Now SOLID (was EXPAND). Both primary E2R standards in hand + added to Mendeley.

**RELAY.** Complete. Plain English. Lead the section on the InclusionEurope2009 metaphor rule (the keystone). Frame FACILE as the per-guideline-module programme this thesis extends. Say E2R adaptation, not simplification; note they are distinct goals.
