# Thesis Section-Verification Harness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a "verify mode" to the thesis skill that runs two read-only verifier subagents (references, coherence) on a human-reviewed section draft and returns one actionable report.

**Architecture:** A new `verify-mode.md` reference file in `~/.claude/skills/thesis/` (same pattern as `writing-mode.md`) holds the two verifier prompt specs, the aggregation logic, and the output format. A pointer in `SKILL.md` activates it on "verify section X". At run time the main loop dispatches both verifiers as parallel Agent calls, then merges their findings into a summary plus inline `% VERIFY[...]` markers. Verifiers are read-only; no edit is applied without user instruction.

**Tech Stack:** Markdown skill files; the Agent tool for parallel subagent dispatch; the Read tool (renders PDFs) for tier-2 citation checks; existing artifacts `WRITING_PLAN.md`, `bibliography.bib`, `mendeley.bib`, `wiki/thesis/papers/`, and the bibkey-named PDFs in `1 - Thesis/Literature Review/Paper PDFS/`.

## Global Constraints

- Academic style in any authored prose and in the skill files: no em-dash (—), no en-dash as punctuation, no ellipsis (… or ...). Substitute with comma, colon, semicolon, parentheses, or a period.
- Verifiers are READ-ONLY. They never edit `.tex`. Fixes are applied only on the user's instruction (the human gate).
- PDF path convention: `\cite{key}` maps to `1 - Thesis/Literature Review/Paper PDFS/<key>.pdf`. If absent, the reference-verifier runs tier-1 (summary/abstract) and lists what it could not deep-verify.
- Reference depth is claim-support, tiered: wiki summary or abstract first, open the PDF only for load-bearing or shaky claims.
- Mandated hedge wordings live in `WRITING_PLAN.md` and must be checked verbatim by the coherence-verifier.
- Deadline-lean: no infrastructure beyond these two skill files plus the dogfood run.

---

## File Structure

- `~/.claude/skills/thesis/verify-mode.md` (create): the verifier prompt specs, aggregation, output format. One responsibility: define how a section is verified.
- `~/.claude/skills/thesis/SKILL.md` (modify): add a short "Verify mode" pointer next to the existing "Writing mode" pointer.
- No changes to the report `.tex` except the inline `% VERIFY[...]` markers produced by a run (Task 3), which are themselves the deliverable of a verification, not of the build.

---

### Task 1: Write `verify-mode.md`

**Files:**
- Create: `~/.claude/skills/thesis/verify-mode.md`

**Interfaces:**
- Consumes: nothing (leaf reference file).
- Produces: the contract the main loop follows on "verify section X": two verifier subagent prompts, the parallel-dispatch instruction, the aggregation rule, and the report format. SKILL.md (Task 2) points to this file by path.

- [ ] **Step 1: Write the file with these required sections (verbatim content, not a sketch)**

The file must contain, in order:

1. **Activation.** "Load this when the user says 'verify section X' (or `/verify-section`), where the section is an already-drafted, human-reviewed `.tex` subsection. Read `writing-mode.md` constraints too; this mode assumes the draft exists."

2. **Run procedure (main loop).**
   - Identify the target section span in its chapter `.tex` (by `\subsection`/`\label`).
   - Dispatch BOTH verifiers below as parallel Agent calls in one message (read-only agents).
   - Aggregate per the aggregation rule.
   - Present the report. Apply no edits unless the user then instructs.

3. **Reference-verifier prompt spec** (the text to send the subagent):
   - Role: adversarial citation checker. Default to skepticism.
   - Inputs to name: the section `.tex` path and line range; `bibliography.bib`; `mendeley.bib`; `wiki/thesis/papers/`; PDFs at `1 - Thesis/Literature Review/Paper PDFS/<bibkey>.pdf`.
   - Procedure: for each `\cite{key}` in range, (a) extract the exact claim the citation supports, (b) resolve the bibkey in the `.bib` files, (c) check support against the wiki summary or abstract first, (d) open `<bibkey>.pdf` ONLY if the claim is load-bearing (a headline result, a method attribution, a number) or looks shaky, reading the relevant section, (e) if no PDF exists, mark tier-1 and record "not deep-verified".
   - Finding types to emit: `unsupported` (source does not back the claim), `misattributed` (right topic, wrong claim or wrong paper), `missing` (claim needs a citation and has none).
   - Output: a JSON-ish list, one object per finding with fields `type`, `line`, `bibkey`, `claim`, `verdict`, `evidence`, `suggested_fix`, `tier` (1 or 2). Also a `checked` count and an `undeep_verified` list.

4. **Coherence-verifier prompt spec** (the text to send the subagent):
   - Role: adversarial fit checker against the paper as a whole.
   - Inputs to name: the section `.tex`; `WRITING_PLAN.md` (theme "structure over scale", narrative arc, the mandated hedge wordings); the chapter outline `wiki/thesis/chapter-outline.md`; the immediately previous and next subsections in the same `.tex` (fallback when none exist: the chapter intro and the abstract).
   - Checks: theme-thread presence; mandated-hedge wording matched verbatim (RQ2 marginality, 70B simplicity, RQ1 supervised); contradiction with neighbour or other-chapter claims; redundancy with neighbours; terminology drift (for example "easy-to-read" vs "simplification"); transition quality into the previous and next section.
   - Output: a list, one object per finding with fields `type` (one of `theme`, `hedge`, `contradiction`, `redundancy`, `terminology`, `transition`), `line`, `issue`, `suggested_fix`, `severity` (must-fix or nice-to-have).

5. **Aggregation rule.** Merge both lists. Sort by line. Produce: (a) a top summary with counts per finding type and an explicit must-fix list; (b) the same findings as inline markers to be placed at the cited lines, format `% VERIFY[ref]: <type>: <one-line issue + fix>` and `% VERIFY[coh]: <type>: <one-line issue + fix>` (use a colon or comma in the marker text, never an em-dash). Markers are proposed in the report; they are written into the `.tex` only on user instruction.

6. **Stop conditions / honesty.** If a verifier returns nothing, say so rather than inventing issues. If PDFs were missing, the summary must state how many citations were tier-1 only.

- [ ] **Step 2: Structural validation**

Run: `grep -nP "[—–…]|\.\.\." ~/.claude/skills/thesis/verify-mode.md`
Expected: no output (clean of banned punctuation). The `\cite{key}` token uses `key`, not dots.

Run: `grep -ciE "reference-verifier|coherence-verifier|aggregation|VERIFY\[ref\]|VERIFY\[coh\]|read-only|tier-1" ~/.claude/skills/thesis/verify-mode.md`
Expected: a count of at least 6 (all required anchors present).

- [ ] **Step 3: Commit**

```bash
cd ~/.claude/skills/thesis
git add verify-mode.md 2>/dev/null || true   # skills dir may not be a git repo; skip if so
```
The skills directory is not part of the thesis repo. If it is not version-controlled, skip the commit and note the file is saved. No thesis-repo commit in this task.

---

### Task 2: Add the SKILL.md pointer

**Files:**
- Modify: `~/.claude/skills/thesis/SKILL.md` (the "## Writing mode (report prose)" block)

**Interfaces:**
- Consumes: the `verify-mode.md` path from Task 1.
- Produces: activation routing so "verify section X" loads `verify-mode.md`.

- [ ] **Step 1: Add a "Verify mode" subsection immediately after the "Writing mode (report prose)" block**

Content to add:

```markdown
## Verify mode (section checking)

When the user says "verify section X" (or `/verify-section`) on an already-drafted,
human-reviewed subsection, read `verify-mode.md` in this skill directory first. It
dispatches two read-only verifier subagents in parallel (references and coherence) and
returns one report with inline `% VERIFY[...]` markers. Verifiers never edit the `.tex`;
fixes are applied only on the user's instruction. Bib PDFs live at
`1 - Thesis/Literature Review/Paper PDFS/<bibkey>.pdf`.
```

- [ ] **Step 2: Validate**

Run: `grep -c "Verify mode (section checking)" ~/.claude/skills/thesis/SKILL.md`
Expected: 1

Run: `grep -nP "[—–…]" ~/.claude/skills/thesis/SKILL.md`
Expected: only pre-existing lines (the description line and resource table); the new block adds none.

---

### Task 3: Dogfood acceptance run on section 7.6

**Files:**
- Read-only inputs: `includes/rq3_replacement.tex` (the 7.6 subsection), `WRITING_PLAN.md`, `bibliography.bib`, `mendeley.bib`, `wiki/thesis/papers/`, PDFs `Graham2013.pdf`, `Graham2017.pdf`, `Alva-Manchego2021.pdf`, `Scialom2021.pdf`.
- Output: a verification report presented to the user (no `.tex` edits unless instructed).

**Interfaces:**
- Consumes: the run procedure and both prompt specs from Task 1.
- Produces: the acceptance evidence that the harness works end-to-end.

- [ ] **Step 1: Dispatch both verifiers in parallel on the 7.6 subsection**

Per `verify-mode.md`: one message, two Agent calls. Reference-verifier scoped to the 7.6 citations (Graham2013, Graham2017, Alva-Manchego2021, Scialom2021); coherence-verifier scoped to 7.6 with neighbours 7.5 (Human Evaluation) and 7.7 (Qualitative Examples), against the `WRITING_PLAN.md` hedges.

- [ ] **Step 2: Aggregate and present the report**

Produce the summary (counts, must-fix list) and the proposed inline markers. Confirm the success criteria from the spec:
1. report contains the three reference finding types where applicable and the coherence checks, citing specific lines;
2. the four 7.6 citations were each checked against their PDFs (tier-2) or explicitly marked tier-1;
3. the 70B-simplicity and RQ2 hedges in 7.6 were checked verbatim against `WRITING_PLAN.md`.

- [ ] **Step 3: Hand the report to the user**

Present findings. Apply markers or fixes only if the user says so. Do not commit `.tex` changes in this task.

---

## Self-Review

**Spec coverage:** architecture (Task 1+2), reference-verifier claim-support tiered (Task 1.3), coherence-verifier checks (Task 1.4), aggregation + inline markers (Task 1.5), read-only/human-gate (Global Constraints + Task 1.2/2.1/3.3), PDF logistics (Global Constraints + Task 1.3), mechanism = parallel subagents (Task 1.2/3.1), acceptance test on 7.6 (Task 3). No spec section is unmapped.

**Placeholder scan:** the verifier prompt specs are described as required content with concrete fields and procedures, not "implement later". The one judgement call (tier escalation on "load-bearing or shaky") is defined with examples (headline result, method attribution, number).

**Type consistency:** finding object fields are named consistently between Task 1 (definition) and Task 3 (use): reference findings use `type/line/bibkey/claim/verdict/evidence/suggested_fix/tier`; coherence findings use `type/line/issue/suggested_fix/severity`; markers use `% VERIFY[ref]` and `% VERIFY[coh]` throughout.
