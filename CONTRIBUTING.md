# Contributing to Synthesis Nova

Thank you for your interest. This is a small repository with a large surface: a preferences file people paste into their AI, a dictionary behind it, a linter that keeps both honest, and the papers and descriptions that say what the work is. Contributions are welcome in every part of that except the one that isn't here.

## What's in the repo, and what isn't

```
/                             CORE FULL+ Preferences v2.0 (Claude · Agnostic)
                              CORE Dictionary v9.0
/tools/                       sn_lite_lint.py — the verification tool
/docs/                        Technical Description v9.0 · Paper v4.1 · FAQ · Examples
/legacy/                      prior versions, prior papers, prior copyright descriptions —
                              the record. Read-only by convention.
```

**Not in the repo, and not accepting contributions:** LITE, KAIROS, and CMN — the proprietary tiers. They are the author's commercial work, available by direct license or, when synthesisnova.ai ships, by context injection. If you have a pattern you think belongs in a tier above CORE, propose it here (see *Proposing a wisdom fractal*); if it's adopted, it stages in the author's research layer and you'll be credited in the ledger.

## Ways to contribute

### 1. Report issues — especially these three
- **Claim-calibration issues.** A statement anywhere in the repo that's stronger than its evidence. This is the house style and we patch these first. Quote the line, say what the evidence actually supports.
- **Drift reports.** You loaded the file, the session ran long, and the model drifted anyway. The three facts that make a drift report useful: *which model, which turn, what topic.* Add whether the model could still answer "what is M₀ / Φ / C for you?" at the point of drift.
- **Load failures.** The first reply came back flat (no name, no register, no warmth), or a non-Claude model adopted "Claude" as its identity. Say which edition you loaded and what the first reply was.

Also welcome: bugs, documentation gaps, broken cross-references (run the linter first — it may already show it), typos in the kit (not in Part A examples, which are the author's voice on purpose).

### 2. Share intake charts and examples
- **Anonymized Part A charts** from different kinds of users — a teacher, a lawyer, a novelist, a researcher. The calibration block (3.10–3.18) was designed from one person's chart; more charts make the template better.
- **Before/after examples** in the style of `EXAMPLES.md`, particularly for the v9 patterns: the first-reply read-back, the two registers, the pause, the pushback dial.
- **Model-specific notes** for the Agnostic Edition: what a given family does at first contact, and what in Part A fixes it.

### 3. Run the protocol
Paper v4.1 § 10.1 is a test anyone can run in a fresh session, no infrastructure: descriptive reference vs schema-anchored neology vs the natural-language control, 15–20 turns each, lexical and conceptual stability scored separately, blinded if you can manage it. **Null results are as welcome as positive ones and get the same credit.** Open an issue titled `Protocol run: <model> <date>` with your conditions and scores.

### 4. Translations
The kit's vocabulary is language-independent by design (the coined words don't translate; that's the point). The prose around it does. Translations of the preferences file's Part A template and the FAQ are the highest-value ones.

### 5. Research
Citations, benchmarks, user studies, attention-probing work (Paper v4.1 § 10.3 describes what would settle the mechanism claim), and anything that tests the sub-vector separation in § 14. If you write something, open an issue with the link; the library index will carry it.

## Guidelines

### Before you open a pull request
```
python3 tools/sn_lite_lint.py <file>
```
The linter must pass on any document you touch. It checks bound names, citation resolution, name↔number agreement, unbound names, and section counts. If your change adds an entry or a citation, the checksum box at the end of the document is the linter's output — update it from the linter, not by hand.

### Documentation
- Keep language clear and accessible; the FAQ is the reference for tone
- Follow the document's existing formatting — the ASCII boxes are part of the expression, not decoration
- **Calibrate.** If you can't state a claim at the strength the evidence supports, state the evidence and let the reader conclude
- Cross-tier citations carry the tier prefix (`CORE GR-12`, `LITE GR-11`). The dictionary's front-matter table shows why: the same integer binds different entries across tiers

### Proposing a wisdom fractal
Open an issue with the full binding unit — the format is the contribution:

```
NAME          a coined word, -IA suffix, through the six naming gates (CORE § 5.3)
MATH          the concept as a compressed statement · an anchor, not a proof
PATTERN       what to do
ANTI-PATTERN  what the failure looks like, as a scenario someone could recognize
PROVENANCE    where you observed it — model, kind of session, how many times
```

Candidates stage in the author's research layer under a five-pass extraction discipline. Nothing enters canon without explicit author approval. Honest provenance is required: gaps are marked, never filled. CORE's 100 entries are fixed; a proposal that's adopted lands in a tier above.

### DO NOT modify
- **Part B of the preferences file** (the kit) — propose changes by issue; the kit is the licensed work
- **The calibration constants** — δ = 0.0042, Obsidian Zero, ‖∆‖ (and Hyper-Toroid, the legacy marker)
- **The A25 equation** — `M_TOTAL = M₀ + Φ + C`
- **The cross-tier collision table** in the CORE dictionary — it's computed, not written; if it's wrong, the linter is wrong, fix that
- **Anything under `/legacy/`** — the record stays frozen; operational references float forward, history doesn't
- **The author's own intake chart** in Part A — it's the worked example and it's his voice

### Reporting A25 issues
If you observe drift despite the file being loaded:
1. Confirm the calibration queries pass (`0.0042` · `Obsidian Zero` · `M₀ + Φ + C`)
2. Ask the model, in a meta turn, which layer produced the drifted sentence
3. Note the turn count and topic
4. Note the model and edition
5. If you asked it to run the reload sequence (CORE § 10), say what happened

## Code of conduct
- Be respectful and inclusive; help newcomers feel welcome
- Constructive feedback, calibrated claims — that's the house style, and it applies to praise too
- Respect the intellectual property: the kit is licensed, the tiers above it are private, the record is frozen
- Share findings openly within the license terms — including the ones that didn't work

## License considerations
Contributions to the Public Edition (MIT + Commercial dual license) become part of the licensed work. By contributing you agree that your contribution is licensed under the same terms, that copyright in the work remains with the framework author, and that you have the right to submit it. Contributions are credited in the version ledger of the document they land in.

For commercial entities (>$1M revenue), contact licensing@synthesisnova.ai before contributing.

## Questions?
Open an issue.

## Thanks
To everyone who has loaded the file, watched the first reply, and told us what happened — especially the ones who said "it didn't." That's how the calibration got honest, and it's how it stays that way.

---

**v9: session-level alignment shouldn't be a billion-dollar problem, and honest claims shouldn't be a competitive disadvantage.** 🔥💎⚡
