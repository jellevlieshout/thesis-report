# Easy-to-Read (E2R) Adaptation of Figurative Language

## Overview
This repository contains the LaTeX source code and documentation for the Master Thesis "Easy-to-Read (E2R) Adaptation of Figurative Language".

The project investigates the effectiveness of agentic Large Language Model (LLM) pipelines for the detection, interpretation, and Easy-to-Read (E2R) adaptation of figurative language (specifically idioms and metaphors). It aims to demonstrate that structured, observable agentic reasoning enables reliable figurative language interpretation and transformation without the need for extensive task-specific training.

## Repository Structure
- **`main.tex`**: The entry point for the LaTeX document. It handles the document configuration, packages, and inclusion of chapters.
- **`includes/`**: Contains individual `.tex` files for each chapter and section (Abstract, Introduction, Background, etc.).
- **`bibliography.bib` / `mendeley.bib`**: Bibliography data files.
- **`notes.md`**: Personal notes, daily logs, and detailed thesis planning.

## Current Status
### Report
- **Abstract**: Drafted.
- **Introduction**: Outlined.
- **Background & Related Work**: Outlined with key literature references.
- **System Design**: High-level outline of the agentic pipeline and problem formulation.
- **Methodology (RQ1-RQ4)**: Initial outlines created for separate research questions.

### Implementation
- **Environment**: Basic environment set up (Client-facing frontend, API, LangGraph workflows, LangSmith observability).
- **Prototype**: Initial prototype capable of accepting text input and processing it via a placeholder agent/prompt.

## Getting Started
### Prerequisites
- TeX Live Distribution (or MikTeX/MacTeX).
- LaTeX Workshop extension for VS Code (recommended).

### Building the PDF
The project uses `latexmk` for building the PDF. 
1. Open the repository in VS Code.
2. Open `main.tex`.
3. Build the LaTeX project using the LaTeX Workshop extension commands or run:
   ```bash
   latexmk -pdf -synctex=1 -interaction=nonstopmode -file-line-error -outdir=. main.tex
   ```

## Next Steps
- **Writing**: Expand the outlines in `introduction.tex`, `background.tex`, and `system_design.tex` into full prose.
- **Research**: Refine the Research Questions and Hypotheses (see `notes.md`).
- **Development**:
    - Implement the "Agentic Pipeline" described in the System Design.
    - Integrate the SemEval-2022 Task 2 and VU Amsterdam Metaphor Corpus datasets.
    - Develop evaluation metrics for detection and replacement quality.

## Author
**Jelle van Lieshout**
Supervised by Dr. Mari Carmen Suárez-Figueroa
Universidad Politécnica de Madrid
