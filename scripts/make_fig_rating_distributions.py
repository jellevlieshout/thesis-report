"""
Figure F-3: human-evaluation rating distributions per system and rubric dimension.

Reads the merged survey responses and draws a grouped box plot of the raw 0-100
ratings for each rubric dimension (grammaticality, meaning preservation, simplicity),
grouped by system condition. Matches the reported analysis: bad-reference items and
repeat second-showings are excluded, and the two QC-dropped respondents (1, 13) are
removed, leaving the 20 retained respondents.

Output: images/fig_rating_distributions.pdf (vector, for LaTeX figure inclusion).

Run (matplotlib required):
  python scripts/make_fig_rating_distributions.py
"""

import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

RESPONSES = os.path.expanduser(
    "~/Documents/Obsidian Vault/1 - Thesis/Survey/results/responses_long.csv"
)
OUT = os.path.join(os.path.dirname(__file__), "..", "images", "fig_rating_distributions.pdf")

DROPPED_RESPONDENTS = {"1", "13"}          # repeat-pair QC failures (RESULTS.md)
DIMENSIONS = ["grammaticality", "meaning", "simplicity"]
DIM_LABELS = ["Grammaticality", "Meaning preservation", "Simplicity"]
SYSTEMS = ["8b_agentic", "8b_monolithic", "70b_agentic"]
SYS_LABELS = ["8B agentic", "8B monolithic", "70B agentic"]
SYS_COLOURS = ["#4C72B0", "#DD8452", "#55A868"]


def truthy(v):
    return str(v).strip().lower() in {"true", "1", "yes"}


def load():
    # data[dimension][system] -> list of float ratings
    data = {d: {s: [] for s in SYSTEMS} for d in DIMENSIONS}
    with open(RESPONSES, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("respondent_id") in DROPPED_RESPONDENTS:
                continue
            if truthy(r.get("is_bad_ref")):
                continue
            if truthy(r.get("is_repeat_second_showing")):
                continue
            sys = r.get("system_id")
            if sys not in SYSTEMS:
                continue
            for d in DIMENSIONS:
                val = (r.get(d) or "").strip()
                if val == "":
                    continue
                try:
                    data[d][sys].append(float(val))
                except ValueError:
                    continue
    return data


def main():
    data = load()

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    n_sys = len(SYSTEMS)
    group_width = 0.8
    box_width = group_width / n_sys

    for si, sys in enumerate(SYSTEMS):
        positions = [
            di + (si - (n_sys - 1) / 2) * box_width
            for di in range(len(DIMENSIONS))
        ]
        series = [data[d][sys] for d in DIMENSIONS]
        bp = ax.boxplot(
            series,
            positions=positions,
            widths=box_width * 0.9,
            patch_artist=True,
            medianprops=dict(color="black"),
            flierprops=dict(marker=".", markersize=3, alpha=0.4),
        )
        for box in bp["boxes"]:
            box.set_facecolor(SYS_COLOURS[si])
            box.set_alpha(0.75)
            box.set_edgecolor("black")
            box.set_linewidth(0.6)

    ax.set_xticks(range(len(DIMENSIONS)))
    ax.set_xticklabels(DIM_LABELS)
    ax.set_ylabel("Rating (0--100)")
    ax.set_ylim(0, 105)
    ax.yaxis.grid(True, linestyle=":", alpha=0.5)
    ax.set_axisbelow(True)
    legend = [Patch(facecolor=c, alpha=0.75, edgecolor="black", label=l)
              for c, l in zip(SYS_COLOURS, SYS_LABELS)]
    ax.legend(handles=legend, loc="lower left", frameon=False, fontsize=9)

    fig.tight_layout()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fig.savefig(OUT, bbox_inches="tight")
    # Print the per-cell n so the figure's coverage is auditable.
    for d in DIMENSIONS:
        counts = {s: len(data[d][s]) for s in SYSTEMS}
        print(f"{d}: {counts}")
    print(f"wrote {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
