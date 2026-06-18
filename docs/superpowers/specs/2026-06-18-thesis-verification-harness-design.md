# Thesis section-verification harness: design

Date: 2026-06-18
Status: approved (pending written-spec review)
Author: Jelle van Lieshout, with Claude
Deadline context: full draft to Mari Carmen 29 June 2026, so this must pay back fast.

## Problem

The thesis writing setup already has a planner layer (`SECTION_BRIEFS.md` plus the locked
`WRITING_PLAN.md`) and a writer layer (the `writing-mode.md` skill discipline; 7.6 drafted).
What it lacks is automated checking. Two checks are tedious and error-prone for a human and
reliable for a separate agent: verifying that every citation actually supports the claim it
is attached to, and verifying that a section fits the surrounding paper. Citation errors in
particular are high-stakes for academic integrity.

## What this is not

Not an autonomous writing pipeline. The user explicitly chose to keep the brief and the
draft human-in-the-loop, because authorship and voice are the point of a master's thesis and
autonomously generated prose flattens to generic and is detectable. The automation lives in
the verification gates, not in generation. No batch autopilot, no auto-applied edits.

## Architecture

A **verify mode** in the thesis skill, invoked as "verify section X" **after the user has
reviewed and approved a draft**. It dispatches two read-only verifier subagents in parallel,
then the main loop aggregates their findings into one report. The verifiers never edit the
`.tex`. They report, the user decides, fixes are applied on the user's say-so. This is the
human gate.

```
draft (human-reviewed)
        |
   verify mode  ──►  reference-verifier  ┐
        |            coherence-verifier  ┘  (parallel, read-only)
        |
   aggregated report (summary + inline % VERIFY markers)
        |
   user acts; fixes applied on instruction
```

### Unit 1: reference-verifier

- **Job.** For each `\cite{key}` in the section, identify the exact claim it backs and verify
  that the cited source supports it.
- **Inputs.** The section `.tex`; `bibliography.bib` and `mendeley.bib`; the wiki's paper
  summaries (`wiki/thesis/papers/`); the bib PDFs (see PDF logistics).
- **Method: claim-support, tiered.** Check support against the wiki summary or abstract
  first; open the PDF only when the claim is load-bearing or looks shaky. Ration PDF reads to
  keep token cost sane across roughly 16 sections.
- **Finding types.** *unsupported* (source does not back the claim), *misattributed* (right
  topic, wrong claim), *missing* (a claim that needs a citation and has none).
- **Output.** Structured findings: claim, bibkey, verdict, evidence or the gap, suggested fix.
- **Dependency.** Needs the PDF for a bibkey to do tier-2. Until a PDF exists it runs tier-1
  (summary/abstract) and lists which claims it could not deep-verify, so nothing is silently
  skipped.

### Unit 2: coherence-verifier

- **Job.** Verify the section fits the paper as a whole and its immediate neighbours.
- **Inputs.** The section `.tex`; `WRITING_PLAN.md` (theme, narrative arc, mandated hedges);
  the chapter outline; the previous and next sections.
- **Checks.** Contradiction with other sections; redundancy; theme-thread presence
  ("structure over scale"); mandated-hedge wording consistency (RQ2 marginality, 70B
  simplicity, RQ1 supervised); terminology drift; transition quality to neighbours.
- **Output.** Structured findings: issue type, location, what breaks, suggested fix.

### Aggregation and output

The main loop merges both findings sets into one report: a short summary at top (counts and
must-fix items), then inline `% VERIFY[ref]:` and `% VERIFY[coh]:` markers placed at the
relevant lines so each finding is seen in context. Nothing auto-applies.

## PDF logistics (done)

PDFs live in `1 - Thesis/Literature Review/Paper PDFS/`, named by bibkey, e.g.
`Graham2017.pdf`. The reference-verifier maps `\cite{Graham2017}` to that file. The filename
convention is the map; no separate index file is needed. Mendeley MCP is the metadata
fallback.

**Coverage as of 2026-06-18.** All 19 `mendeley.bib` argument papers have PDFs:
Alva-Manchego2020, Alva-Manchego2021, Badran2025, Diab2024, Dmitrijev2024, Gao2025,
Graham2013, Graham2017, Hayashi2025, Ichien2024, Jia2024, Lai2024, Liu2022, Neidlein2020,
Pukiene2024, Scialom2021, Surez-Figueroa2023, Surez-Figueroa2024, Tian2024. The foundational
references in `bibliography.bib` (papineni2002bleu, xu2016sari, zhang2020bertscore, mipvu,
magpie, trofi, moh, williams1959regression, Graham2016a, vuamsterdammetaphorcorpus,
tayyar-madabushi-etal-2022-semeval) have no PDFs and run tier-1; they are rarely contested.

**Open data flags surfaced during PDF inspection:**
1. `Dmitrijev2024.pdf` is titled "Metaphors and Analogies in the Context of Large Language
   Models", but the `mendeley.bib` entry for that key is titled (beginning) "Scenarios,
   Fictions, and Imagined Possibilities in Science, Engineering". The Mendeley entry may be
   mislabeled or may point at a different paper. Resolve before citing.
2. `DUPLICATE_of_Scialom2021.pdf` is a byte-identical copy of `Scialom2021.pdf` (same MD5),
   left in place rather than deleted. Safe to remove.

## Mechanism

Skill-dispatched parallel subagents: on "verify section X", the main loop dispatches the two
verifiers as concurrent agents, then aggregates. Lightweight, on-demand, one section at a
time, matching the human gate. A Workflow script is reserved for a single whole-thesis sweep
on Jun 28 (verify every section at once); not built now.

Rejected: a single agent doing both checks (collapses the "different agent, different job"
separation that makes verification trustworthy).

## Acceptance test

First run on section 7.6, already drafted: it has real citations (Graham2013, Graham2017,
Alva-Manchego2021, Scialom2021) and real neighbours (7.5, 7.7), exercising both verifiers
immediately.

## Scope cuts (YAGNI)

No autonomous writing. No batch autopilot. No auto-applied edits. No infrastructure beyond
the skill verify-mode plus the existing PDF folder. Coherence-verifier is usable now because
7.6 has neighbours; for the earliest-drafted section in any chapter it will have less to
check, which is acceptable.

## Success criteria

1. "verify section X" produces a report with the three reference finding types and the
   coherence checks, citing specific lines.
2. On 7.6 it correctly reads the four citations against their PDFs and the hedge wording
   against `WRITING_PLAN.md`.
3. The user can act on the report without re-deriving context, and no edit is applied without
   instruction.
