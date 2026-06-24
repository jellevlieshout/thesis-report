# Read-through feedback — 2026-06-24

Format: one line per note. Verbatim snippet is what I use to locate the spot, so keep a few exact words.

```
[section/file] "short verbatim snippet…" → what's wrong / how it feels
```

Status tags (optional, for me to fill in): `[ ]` open · `[x]` done · `[?]` needs discussion

---

## Register / tone
<!-- too dense, too clipped, doesn't sound like me -->
[abstract] "Decomposition yields a consistent directional advantage on meaning preservation that approaches but does not reach conventional significance," -> what does conventional significance mean here? 
[1.1] "develops this gap in full" -> I'd rather have something like 'describes this gap in more detail'
[2.6] -> "The two bodies of work reviewed above do not meet" -> be more concrete 
about which bodies of work we're talking about here
[4] "rubric triad" -> confusing wording, what does this mean (used multiple times in paragraph)
[4] "Direct Assessment (DA), the WMT-standard" -> what is WMT standard
[4] "MT setting" -> what does MT mean
[5.3] "IoU" -> what does this mean
[5.4] " other way. [22] show that" -> should authors be named explicitely here? Same here: "ng. [18] reach state-of-the-art"
[6.4] "Decomposition Does Not Sharpen Detection" -> I want a more generic title for this paragraph. Such as earlier ones, "Human-Evaluation Results". 
[6.5] Same here: "Further Comparisons Deferred to Future Work" more generic title (e.g. "further comparisions")
[8.2] Why the Replacements Preserve Meaning but Do Not Simplify title too long, make more generic
Overall, I really like the writing style of the intro, background and methodology, but as soon as we start discussing RQ's and results, it gets complicated to follow. What can we do about this?
## Hedges (RQ2 significance, 70B result)
<!-- over-qualified? not yours? -->



## Numbers / tables
<!-- body vs table vs appendix mismatches -->
[table 4]: why are the 'highest' values not in bold here such as in the other tables?
same for table 5. 
[fgure 5] in figure 5, some of the whiskers go all the way to 0, and 100, is that correct


## Vocabulary
<!-- surviving ablation/adjudicate/salient/lexicalized, or awkward replacements -->



## Appendix references
<!-- reference points somewhere sensible? -->



## Other
[abstract] -> I'd like the abstract to contain a short sentence of contributions made by this thesis.
[1.4] -> describes "two hundred persisted and reproducible runs" -> isn't that number much higher now, since we ran the whole dataset? 
[2.5.1] -> "RoBERTa in this work" -> what is meant by 'in this work'? We don't use 
Roberta here. It can be referred to, but this might sound confusing. 
[ figure 1]: : it's actually a H100 node, not A100
[3.1] "• A set of detected figurative spans {(ei, starti, endi)}, where each ei is a verbatim copy of

an expression from s with character-offset boundaries;

• A per-token binary label sequence l ∈{0,1}|T (s)| over the whitespace-tokenised form of s,

derived from the detected spans;

• A brief linguistic explanation of the figurative usage;

• Optionally, a literal paraphrase ˆ

s of the full senten"" -> can we verify this againts the codebase to see if still accurate or not please
[3.3] 'on port 3030' -> don't mention on which port this runs.
[3.3] once again h100 not a100
[4] 4.1.3 starts talking about the Student-t distribution, but then in 4.2.2 we start elaborating on the paired t-test and wilcoxon signed-rank test. Is this correct? 
[4.3] -> I think this whole section can be dropped. I don't see the relevance. I also don't think we should mention mine or Mari Carmens network, you can remove the reference in 4.2.2 (" supervisor’s and the author’s network") as well. 
[5.1] A100 -> H100 (check this throughout the whole paper!)
[5.3] "including the conventional and grammatical metaphors that saturate ordinary English." -> can we add a brief example of what this looks like in the dataset
[8.5] "end of what Graham 2013 found stab" -> improper citation












---

## Scratch (anything, unsorted)


