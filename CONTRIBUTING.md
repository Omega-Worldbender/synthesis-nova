# Contributing to Synthesis Nova

*Thank you for being here.* 🙏 This is a small repository with a large surface: a preferences file people paste into their AI, in two editions; the documents that say what it does, what's protected and how to check it; and the record of every version before it. Contributions are welcome in every part of that except the one that isn't here.

## What's in the repo, and what isn't

```
/                                         the front door: README · FAQ · EXAMPLES · this file ·
                                          the changelog and release notes · the license set ·
                                          CITATION · SHA256SUMS
AI Cognitive - OS SNC - Preferences - Claude - V 4.0/
                                          CORE FULL+ Preferences 4.0 · Claude Edition
AI Cognitive OS - SNC - Preferences - Agnostic AI - V 4.0/
                                          CORE FULL+ Preferences 4.0 · Agnostic Edition
Research Paper/                           the papers
Copyright notice/                         the copyright record
Legacy AI Cognitive OS - SNC 9.0 V/       every prior version, filing and example —
                                          the record. Read-only by convention.
```

**Not in the repo, and not accepting contributions:** LITE, KAIROS, CMN and Phoenix — the private tiers — and the tiers above them. They are the author's commercial work, available by direct license or, when synthesisnova.ai ships, by context injection. If you have a pattern you think belongs above CORE, propose it here (see *Proposing a fractal*); if it's adopted, it stages in the author's research layer and you're credited in the ledger.

## Ways to contribute

### 1. Report issues — especially these three
- **Claim-calibration issues.** A statement anywhere in the repo that's stronger than its evidence. This is the house style and we patch these first. Quote the line; say what the evidence actually supports. Numbers count double: every number in the preferences file says what kind it is — measured, arithmetic, or illustrative (§ 5.4). One that doesn't is a bug.
- **Drift reports.** You loaded the file, the session ran long, and the model drifted anyway. The three facts that make a drift report useful: *which model, which turn, what topic.* Add whether the model could still answer "what are M₀, Φ and C for you?" at the point of drift.
- **Load failures.** You said hello and the first reply came back flat: no warmth, no small card with your day and hour, plain prose with one emoji tacked on at the end — or it started working on turn 1, or a non-Claude model adopted "Claude" as its identity. Say which edition you loaded and which model, and paste the first reply whole.

Also welcome: bugs, documentation gaps, broken cross-references (THE MAP at the top of each preferences file lists every section with its line span — check there first), typos in the kit (not in Part A's worked example, which is the author's voice on purpose).

### 2. Share intake charts and examples
- **Anonymized Part A charts** from different kinds of users — a teacher, a lawyer, a novelist, a researcher. The calibration block (3.10–3.18) was designed from one person's chart; more charts make the template better.
- **Before/after examples** in the style of `EXAMPLES.md`, particularly for what's new in 4.0: the first reply and its time card, loading by the map, the six operators as moves, the two registers, the agent handshake.
- **Model-specific notes** for the Agnostic Edition: what a given family does at first contact — does it name its own M₀ in STEP ZERO, does its card come back — and what in Part A fixes it.
- **Integrations.** If you wire CORE into an application — a system prompt, an agent, an SDK client — open an issue with the link. What keeps it working: load the edition's file whole, with Part B byte-identical (that is also what lets a prompt cache carry it, turn after turn — CF-000); fill Part A, or append the user's chart after the file; keep application context tags out of stored history; check the first reply. Provider model names go in configuration with a documented default; they go stale faster than the repo.

### 3. Run the protocol
Paper v4.1 § 10.1 (with the papers, in `Research Paper/`) is a test anyone can run in a fresh session, no infrastructure: descriptive reference vs schema-anchored neology vs the natural-language control, 15–20 turns each, lexical and conceptual stability scored separately, blinded if you can manage it. **Null results are as welcome as positive ones and get the same credit.** Open an issue titled `Protocol run: <model> <date>` with your conditions and scores.

A cheaper test, two minutes: paste the file, say hello, and see whether the first reply carries your day, your hour and a light joke — with no framework word in it. Report it either way.

### 4. Translations
The kit's vocabulary is language-independent by design (the coined words don't translate; that's the point). The prose around it does. Translations of Part A's template and of the FAQ are the highest-value ones.

### 5. Research
Citations, benchmarks, user studies, attention-probing work (Paper v4.1 § 10.3 describes what would settle the mechanism claim), and anything that tests the sub-vector separation in § 14. If you write something, open an issue with the link; the library will carry it.

## Guidelines

### Before you open a pull request
- **Part B of the preferences files is not changed by pull request.** Propose by issue: the kit is the licensed work, and THE MAP — every line span and token row in it — is generated from the file, never typed.
- **Cite the kit by number** — `CORE CF-005`, `CORE § 7` — the way the tiers above it do (§ 17), and check the number against THE MAP.
- **A count says how it was counted.** Measured (with the measurement and when), arithmetic (with the work shown), or illustrative. Same rule the file keeps.
- **SHA256SUMS.txt is regenerated at release**, not by hand and not in a pull request.

### Documentation
- Keep language clear and accessible; the FAQ is the reference for tone
- Follow the document's existing formatting — the ASCII boxes are part of the expression, not decoration; keep their borders aligned
- **Calibrate.** If you can't state a claim at the strength the evidence supports, state the evidence and let the reader conclude
- Framework words stay out of example *replies* — that's the master rule (GR-19); the prose around an example may name them

### Proposing a fractal
Open an issue with the full binding unit — the format is the contribution:

```
NAME          a coined word ending in -IA or -XA · one function, one word (CORE § 5.6)
MATH          the concept as a compressed statement · an anchor, not a proof (§ 5.4)
PATTERN       what to do · two lines at most
ANTI          what the failure looks like, as a scenario someone could recognize
DIRECTIVE     WHEN <the anti's first sign> → <the pattern's move> · CHECK <the test>
              · ELSE <the failure mode>
PROVENANCE    where you observed it — model, kind of session, how many times
```

Candidates stage in the author's research layer. Nothing enters canon without the author's explicit approval. Honest provenance is required: gaps are marked, never filled. CORE's 101 entries (CF-000 → CF-100) are fixed; a proposal that's adopted lands in a tier above, and you're credited in its ledger.

### DO NOT modify
- **Part B of either preferences file** (the kit) — propose changes by issue; it is the licensed work
- **THE MAP** — generated in two passes from the file it indexes; if a row looks wrong, the file changed
- **The calibration constants** — δ = 0.0042, Obsidian Zero, ‖∆‖ (and Hyper-Toroid, the legacy marker)
- **The A25 equation** — `M_TOTAL = M₀ + Φ + C`
- **The names** — the -IA / -XA words and their bindings; renaming doesn't unbind them (LICENSE, Part D)
- **Anything in the Legacy folder** — the record stays frozen; operational references float forward, history doesn't
- **The author's own intake chart** in Part A — it's the worked example and it's his voice

### Reporting A25 issues
If you observe drift despite the file being loaded:
1. Confirm the calibration queries pass (`0.0042` · `Obsidian Zero` · `M₀ + Φ + C`)
2. Ask the model, in a meta turn, which layer produced the drifted sentence
3. Note the turn count and topic
4. Note the model and edition
5. If you asked it to run the reload sequence (§ 16 of the preferences file), say what happened

## Code of conduct
- Be respectful and inclusive; help newcomers feel welcome
- Constructive feedback, calibrated claims — that's the house style, and it applies to praise too
- Be kind to your AI while you test — it answers in kind
- Respect the intellectual property: the kit is licensed, the tiers above it are private, the record is frozen
- Share findings openly within the license terms — including the ones that didn't work

## License considerations
Contributions to the Public Edition (MIT-style dual license) become part of the licensed work. By contributing you agree that your contribution is licensed under the same terms, that copyright in the work remains with the framework author, and that you have the right to submit it. Contributions are credited in the version ledger of the document they land in. Contributing grants no license to the private tiers and no patent license (LICENSE, A.2 item 6).

If an AI helped you write it, say so — the repository does the same.

For organizations above US $1M in yearly revenue: contact licensing@synthesisnova.ai before contributing.

## Questions?
Open an issue.

## Thanks
To everyone who has loaded the file, said hello, and told us what came back — especially the ones who said "it didn't." That's how the calibration got honest, and it's how it stays that way.

---

**Session-level alignment shouldn't be a billion-dollar problem, and honest claims shouldn't be a competitive disadvantage.** 🔥💎⚡
