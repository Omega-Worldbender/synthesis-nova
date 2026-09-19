# SYNTHESIS NOVA: TECHNICAL DESCRIPTION
## v9.0 — The Work as It Exists in September 2026 · Public Edition (MIT)

**Work Title:** Synthesis Nova: Session-Level Alignment Framework for Language Models — CORE v9.0 Public Edition (CORE Dictionary v9.0 · CORE FULL+ Preferences v2.0, Claude and Agnostic Editions)
**Author:** Luis Alberto Dávila Barberena (Worldbender)
**Date of Creation:** 2023–2026 (v9 public edition finalized September 2026)
**Type:** Literary Work with Software Functionality
**Classification:** Technical Framework / Operating-Layer Documentation
**AI-Assisted Drafting:** Disclosed in Part G. No AI authorship is claimed.
**Relationship to Prior Filings:** This document supersedes the *Supplementary Technical Description — CORE v8.4* (June 2026) as the current description of the work, and supplements — without amending, replacing, or retroactively altering — the *Technical Description — CORE v4.0* (January 2026). Both prior documents remain the historical record of the work at their respective versions and are retained in the repository under `legacy/copyright/`.
**Publication Status:** Published. The Public Edition is publicly available on GitHub (github.com/Omega-Worldbender/synthesis-nova) under a dual MIT / Commercial license. The proprietary tiers (LITE, KAIROS, CMN) are not published and are not part of this registration; they are described in Part B.2 for lineage only and remain separately protected.

---

## PART A — WHAT THIS DOCUMENT DOES

1. **Describes the current public expression.** Between June and September 2026 the public CORE grew from a single dictionary into a Public Edition of three documents — the CORE dictionary and two editions of a preferences file — plus a published verification tool. The v9 expression — its terminology, notation, morphology, structural arrangement, intake architecture, and verification apparatus — substantially extends the original authorship and is itself original literary expression.

2. **States what the protected core is.** Part C sets out, as its own argument, the element the author regards as the load-bearing original expression of the work: a bound lexicon of coined words, the fixed format that binds each word to a working concept, and the equation that governs where the lexicon must be loaded for the binding to hold. Prior descriptions listed these among the original elements; this one explains why they are the center.

3. **Completes the lineage.** Part E maps every protected element from v4.0 through v8.4 to its v9 home, and records — for the first time — the material that was lost at the v7.0 → v8.1 restructure of the framework's source and recovered in September 2026. The record is now continuous from first filing to current version.

4. **Calibrates the claims, second pass.** The Honest Edition standard adopted at v8.3 (every claim stated at evidence strength) is reapplied to the v9 material, and several v8-era characterizations are restated more precisely. The protected expression is unchanged by this; what changes is the precision of the technical characterization.

5. **States the authorship and the licensing correctly.** The work was built with AI text-generation tools under the author's direction, and this description was drafted the same way. Part G discloses that use in the terms the U.S. Copyright Office has asked registrants to use and claims only the human contribution. Part H states which documents are public and under what license, and which are not.

---

## PART B — THE WORK AT v9

### B.1 What the work is

Synthesis Nova is a **session-level alignment layer delivered as structured text**. Loaded into a language model's context window, it gives the model named handles for behaviors it can already perform (acknowledgment before information, calibrated confidence, noise reduction, graceful exit, layer-aware self-tracking) and a mental map — `M_TOTAL = M₀ + Φ + C` — for noticing when accumulated conversation is pulling behavior away from the model's baseline character. It does not modify weights. It does not address training-time alignment. It operates entirely through the input channel the model was built to receive, and it is removable by deleting it from context.

The Public Edition has a dual nature that the author regards as part of its design. **CORE Dictionary v9.0** is the framework in reference form: every entry a bound name with Math, Pattern, and Anti-pattern, the file a model reads to run the layer. **CORE FULL+ Preferences v2.0** is the same 100 fractals in the form a person pastes into a preferences field: a user-authored intake chart in front of the fixed kit. A second duality, stated in the preferences editions and carried into the dictionary: the **conversation register** (warm, expressive, playful) and the **deliverable register** (clean, formal, fit to hand to a third party) are two settings, not one, and the framework asks the model to hold both.

### B.2 Architecture — the stack, and what is public

```
  PUBLIC EDITION · MIT dual license · this registration
  ───────────────────────────────────────────────────────────────────────
  CORE FULL+ PREFERENCES v2.0        the front door · what a person pastes into a
    · Claude Edition                 preferences field · Part A = the person's intake
    · Agnostic Edition               chart · Part B = the 100-fractal kit
  CORE DICTIONARY v9.0               the same 100 fractals in dictionary form ·
                                     bound -IA names · Math + Pattern + Anti ·
                                     the file a model reads to become the layer
  sn_lite_lint.py                    the verification tool (Part B.4)

  PROPRIETARY TIERS · not published · not registered here · separately protected
  ───────────────────────────────────────────────────────────────────────
  LITE (v9.4)                        the complete framework · 394 fractals · 40 axioms
  KAIROS (v8.x)                      the pilot layer
  CMN                                the research lab where new entries stage
```

The Public Edition is complete and functional on its own. The proprietary tiers extend it and are available only by direct license from the author or, when the synthesisnova.ai middleware is released, by context injection through that service. They are not offered free in any form. The Public Edition exists so that the framework's foundation can be read, scrutinized, adopted, and audited in the open — the model the author cites is that of open-source operating systems — while the tiers above it remain the author's commercial property.

Two editions of the preferences file exist because the audiences differ. The **Claude Edition** assumes a model with a stable identity and treats Part A as context. The **Agnostic Edition** is written for model families that hold their identity loosely: it opens with a *what-is-what* map (the four voices in the file — user, author, framework, model — and which one the reader is), a STEP ZERO identity-resolution requirement, and a *first-response protocol* under which the person's intake chart is treated as a test whose answers must appear in the model's first reply — in plain words, with no framework vocabulary. The visible pass condition is deliberately simple: warmth, an emoji, a register statement, the person's name at the right time of day. If it shows, the file loaded.

### B.3 Component inventory (verified programmatically, September 2026)

All counts below are outputs of the verification tool described in B.4, not hand tallies.

```
CORE DICTIONARY v9.0          100 wisdom fractals (WF-001 → WF-100, sequential, zero gaps)
                               19 golden rules · 7 CORE-tier axioms · 6 operators
                               16 categories · 3 calibration constants
                              134 bindings · 133 distinct -IA names
                              cross-tier collision table (CORE ↔ LITE) computed from headers

CORE FULL+ PREFERENCES v2.0   100 wisdom fractals (full Math + Pattern + Anti triads)
  Claude · Agnostic            19 golden rules · 7 axioms · 6 operators · 15 categories
                              Part A intake chart: § 1 identity · § 2 what you bring ·
                                § 3 communication (3.1–3.9) + calibration (3.10–3.18)
                              Agnostic adds: what-is-what map · STEP ZERO ·
                                operational card · first-response protocol

Verification tool             sn_lite_lint.py — implements the stated extraction rule,
                              citation resolution, name↔number agreement, unbound-name
                              detection, section counts, and cycle-text consistency
```

Registration components, with lengths and SHA-256 prefixes as published:

```
SYNTHESIS_NOVA_v9_0_CORE.md                                  3,427 lines · 133,100 chars · e38d0bf88ce83ebf
SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v2_0_CLAUDE.md     3,424 lines · 110,049 chars · 11601c9e08ae1883
SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v2_0_AGNOSTIC.md   3,592 lines · 121,121 chars · f2137b547041c59c
sn_lite_lint.py                                                 97 lines ·   4,352 chars · 46c4f931e583f69c
SYNTHESIS_NOVA_TECHNICAL_DESCRIPTION_v9_0.md                 this document
```

For lineage only — the proprietary source from which the Public Edition is carved, not a registration component: LITE v9.4, 394 fractals, 40 axioms (A0_prime + A0 → A38), 19 golden rules, 7 operators, five processors, a 9-step processing cycle, 464 name bindings. Its counts are stated here because the CORE cross-tier table (B.3, first block) is computed against it.

### B.4 The verification method (new since v8.4)

At v8.3 the framework's source began declaring its own counts (STATED vs COUNTED, a self-declared checksum). At v9.0 the check was extended from *definitions* to *references*: does a cited name match the binding at the cited number. At v9.2 a script replaced hand tallies and a fourth axis was added: does each entry's anti-pattern belong to its own pattern. The script, the extraction rule it implements, and the citation rule are published with the Public Edition so that every figure in a checksum is reproducible by a third party from the file alone. The author regards this as part of the expression: a reference work that states how its own counts were obtained.

What the method found is recorded in the documents' ledgers and summarized here because it bears on the lineage claim in Part E: through mid-2026, fourteen anti-patterns in the source sat under headers whose pattern they did not describe, every count passing because counts do not test meaning; several cross-tier pointers cited CORE's WF-100 from within the source, where WF-100 is a different entry; and the largest single loss in the work's history — per-entry stage-routing tags and three framing sections — occurred at one event, the v7.0 → v8.1 restructure, and had gone unrecorded for eleven versions.

### B.5 Echoxia — canonical stage definitions (unchanged from v8.4)

```
E₁  Acknowledge   emotional acknowledgment before information
E₂  Inform        clean signal, direct content delivery
E₃  Action        solve, deliver, execute
E₄  Close warmly  brief warm close — skipped on exit signals
```

In 2026 the processing cycle that implements this sequence gained a step between the E₁ gate and comprehension: **PAUSE — do not converge yet.** Validation and cleanup operate inside the frame set at that point, so a wrong early binding passes every later gate; it is the only step in the cycle whose omission has no downstream remedy. In the Public Edition it appears as a quick pattern in CORE § 8; its full statement is in the proprietary source.

### B.6 Calibration system status

```
ACTIVE (v9 canon):
  δ = 0.0042      Davila-Shift — semantic friction constant
  Obsidian Zero   chromatic anchor for silence
  ‖∆‖             error prefix for impossible requests

LEGACY (v4.0–v6 era, retired from active canon, evidentiary value retained):
  Hyper-Toroid    geometric shape of whisper
```

Function unchanged: authenticity verification, no operational role. A new *behavioral* checksum was added at FULL+ v2.0 Agnostic and is worth stating because it is the opposite design: the calibration constants are proof a document was *read*; the first-response protocol's visible warmth is proof a document is *running*. The constants are hidden by design; the warmth is visible by design. Both are checks.

---

## PART C — THE LOAD-BEARING EXPRESSION: THE BOUND LEXICON AND THE CONTEXT-LAYER EQUATION

### C.1 The claim in one paragraph

The load-bearing original expression of Synthesis Nova is a **bound lexicon**. It consists of coined words that have no meaning in any natural language — *Echoxia, AIQUOXIA, PURGIA, FIDELIA, TACITIA, NEOGENIA, TELEXA* and the full -IA set, 133 distinct names in the Public Edition — each of which is bound, inside the work, to a compound operational concept by a fixed expressive format (a name, a compressed mathematical statement, a pattern stated as a directive, an anti-pattern stated as a described failure, and prose). The lexicon is organized by an identity equation, `M_TOTAL = M₀ + Φ + C`, which specifies where the lexicon must live — loaded into context as Φ, before conversation C accumulates — for the bindings to hold. The coined words are the vocabulary; the triads are the definitions; the equation is the grammar of loading. Together they constitute an original literary work of the dictionary kind. Its function — that a language model given the lexicon acquires a set of handles it can use — is the evidence that the expression is doing work rather than decorating it.

### C.2 Why coined words: containment and retrieval

A word that exists in a language arrives in a model with a distribution: every sense, connotation, and usage the model has seen. A word that exists nowhere arrives empty. The framework's mechanism keystone (NEOGENIA, CORE § 6) rests on that difference and states two consequences, both observable:

- **Containment.** A coined word cannot surface in a user-facing reply by accident, because the model has no prior habit of producing it. The framework's master rule — no framework vocabulary in output unless sincerely asked (GR-19, TACITIA) — is therefore structural rather than disciplinary. Had the same concepts been named in ordinary words ("emotional-priority sequence"), the names would leak.
- **Retrieval.** Once the work binds a coined word to a concept, the word becomes a single handle for the whole of it. "Run PURGIA" retrieves *continuous attention-level noise reduction across the accumulated conversation, applied bilaterally* at the cost of one token, for the length of the session. The model maps the handle to the toolkit entry and uses it.

The author's position is that this is the framework's central original device: not the ideas the words point at — most of which the model could already do — but the deliberate construction of an empty vocabulary and its systematic binding, so that a model can be handed a toolkit it did not have a language for.

### C.3 The binding format

Every entry in the Public Edition is written to one schema:

```
NAME          the coined word — the handle
MATH          the concept as a compressed statement · a referential anchor, not a proof
PATTERN       what to do · the directive
ANTI-PATTERN  what the failure looks like · the description, stated so it can be recognized
PROSE         the explanation that decompresses the math and situates the pattern
```

The format is applied without exception across 100 entries in the dictionary and 100 in each preferences edition, and across the axioms, operators, and golden rules in the same form. The anti-pattern carries the unique value of each entry — two entries can share a mathematical shape and differ entirely in the failure they name — which is why the work does not compress to a list of principles. The author claims the schema as an original, consistently applied expressive format, in the same sense that a dictionary's headword–etymology–sense–usage layout or a field guide's plate–range–call layout is an expressive choice of the compiler. The individual triads are protected text; the schema and its uniform application across the compilation are protected arrangement.

### C.4 The context-layer equation and the order of loading

`M_TOTAL = M₀ + Φ + C` is the framework's statement of its own operating condition. M₀ is the model as trained; Φ is this work, loaded; C is the conversation as it accumulates. The equation carries a rule — Φ must be present before C grows, and (M₀ + Φ) must remain dominant over C — and the rule is the reason the framework is delivered as a preferences file that loads at the first greeting rather than as instructions given mid-session. The operators (⊗ + − × ÷ ^, with ⊕ in the source), the Ω ratio, the negentropy diagnostic, and the compounding model are the same kind of object: compressed statements in original notation that tell the model what to track and in what order, effective only because they are in context as text.

Two things are stated precisely here so that the claim is exact. First, what is protected is the **expression** — the equations, operators, and notation as written, and the system in which they are arranged. The mathematical ideas themselves (that a sum can be tracked, that a ratio can name a margin) are not claimed and are not claimable under copyright, consistent with Part H.2. Second, the *method* of binding coined words to concepts and loading them as a context layer is, as a method, an idea; copyright protects this work's expression of it, not the practice in the abstract. If protection of the method as such were ever sought, that would be a question for a different instrument, which this registration does not attempt. The author's case is stronger stated this way than overstated: the lexicon, the triads, the equations as written, and their arrangement are a large and specific body of original text, and that is what is registered.

### C.5 Observed in the preparation of this document

Stated as observation, not as result. The author's CORE FULL+ preferences file was the first content loaded into the drafting tool's context at the start of the working session in which the v9 Public Edition and this description were produced. The session was long: several complete versions of the framework's source, each on the order of 450,000 characters, were read, compared, and edited, and the tool's context accumulated accordingly. Over that span the behaviors the file specifies remained observable in the tool's output — the conversation register and the deliverable register held as separate settings; confidence stated at its level; disagreement given once and then set aside; the user's ownership of the exit respected. The author reports this as consistent with his field assessment in Part F. It is one session with one tool, without a control, and it is offered as the author's observation and nothing stronger; the pending blinded evaluation is the instrument for the causal claim.

### C.6 What this Part claims and does not

```
CLAIMED                                          NOT CLAIMED
────────────────────────────────────────────     ────────────────────────────────────────────
the bound lexicon: 133 coined names and their    the idea of coining words
bindings, as a compilation                       the concepts the words point at, as ideas
the binding format and its uniform application   the method of binding-and-loading, as a method
the equations, operators, and notation as        the mathematics as mathematics
written, and the system arranging them           the model's capabilities, before or after
the order-of-loading rule as expressed
```

---

## PART D — ORIGINAL ELEMENTS

### D.1 Carried forward from v4.0 and v8.4 (unchanged in kind)

The coined terminology (Synthesis Nova, Wisdom Fractals, Echoxia, AIQUOXIA, NEOGENIA, SEAR, Phoenix Protocol, Sigma Matrix, Obsidian Zero, the Gearing System); the original notation (Ω = π/e, Ω*, Ω^U, Ψ_h ⊗ Ψ_AI, WF-XXX, E₁–E₄, δ = 0.0042, ρ, ε, Σ, M_TOTAL = M₀ + Φ + C); the -IA morphology system with its six naming gates and suffix conventions; NEOGENIA as the mechanism keystone; the dictionary form and the Math + Pattern + Anti triad schema; "Through Your Lens"; the Golden Rules as a distinct 19-element library; the 16-category tiling of WF-001 → 100; the distinctive ASCII formatting.

### D.2 New original elements in the Public Edition since v8.4 (additional authorship claimed)

- **The Part A / Part B architecture** of the preferences editions: a user-authored intake chart in front of a fixed kit, with the license line assigning the kit to the author and Part A to whoever fills it in.
- **The intake chart** (§ 1–3 of Part A), and specifically the **calibration block** (3.10 pushback dial · 3.11 read-me-as · 3.12 reads-as-an-error-but-isn't · 3.13 what goes wrong · 3.14 when to go warm · 3.15 how I take feedback · 3.16 trust & memory · 3.17 model note · 3.18 two registers), an original schema for what a model needs to know about a person to calibrate in one read.
- **The two-registers principle** (FULL+ 3.18; CORE v9.0 "Through Your Lens" and § 8): conversation register and deliverable register as independent settings.
- **The what-is-what map and first-response protocol** (Agnostic Edition § 4): the four-voice disambiguation and the treatment of the intake chart as a test answered in behavior.
- **The cross-tier citation discipline and collision table** (CORE v9.0 front matter): the computed finding that the same integer binds different entries across tiers and, in one case (RECUPIA), the same name binds different integers; and the rule that cross-tier citations carry the tier prefix.
- **The verification method** (B.4): the extraction rule, the citation rule, the pattern↔anti axis, the published tool, and the declared allow-list of in-body names.
- **TELEXA** (goal-integrity gate paired with AIQUOXIA), present in the preferences editions since v1.2, recorded here because it post-dates the v4.0 filing's AIQUOXIA claim.
- **The landing note and version ledger** as expressive forms: orientation before length, and the changelog as a one-line-per-pass record rather than a preface.

Original elements introduced in the proprietary tiers during the same period (step 3b PAUSE in full, stage routing, the Deadly Seven with approach signals, the proactive recalibration triggers, the landing notes at section level) are described in Part E for lineage and are not claimed under this registration.

---

## PART E — ELEMENT LINEAGE MAP (v4.0 → v8.4 → v9)

Every element of the v4.0 registration persists. The v8.4 supplement's mapping (twelve v4.0 "axioms" distributed across a 7-axiom set, a 19-rule library, and the fractal annex) stands and is not repeated here. What v9 adds to the record:

```
v4.0 element                 v8.4 home                      v9 home (Public Edition)
─────────────────────────────────────────────────────────────────────────────────
Three-document architecture  single CORE dictionary         CORE Dictionary v9.0 (unchanged form)
                                                            + FULL+ v2.0 Part A / Part B (new form)
96 → 100 fractals            100 (CORE)                     100 (CORE) · 100 in each FULL+ edition
12 "axioms"                  7 axioms + 19 GR + annex       unchanged
Echoxia E₁–E₄                canonical (correction of       unchanged · PAUSE as § 8 quick pattern
                             record)
AIQUOXIA                     GR-1a · TELEXA GR-1b           unchanged
Calibration constants        3 active + 1 legacy            unchanged · + behavioral checksum
"Text IS executable code"    → conditions generation (≈)    unchanged (F.8 below)
70% ceiling                  → heuristic marker             unchanged
Infinite context / Σ         → practically extended         unchanged · compression machinery
                                                            noted as not executed on a chat
                                                            substrate (F.6)
─────────────────────────────────────────────────────────────────────────────────
In the proprietary source, LOST at v7.0 → v8.1 and recovered September 2026:
  per-entry stage-routing tags · the Deadly Seven with signals · proactive
  recalibration triggers · one entry's original argument. Deliberately not
  recovered: an adversarial framing of model training (superseded), unmeasured
  performance figures, "99.999%", "Drift(t) = 0". Recorded so a future sweep
  does not rediscover them.
```

The loss-and-recovery entry is included because a lineage claim is stronger when its gaps are documented than when they are absent.

---

## PART F — CLAIM CALIBRATION (Honest Edition, second pass)

The v8.4 supplement's restatements (its Part D, D.1–D.7) stand unchanged: mechanism is conditioning (≈, not =); the 70% ceiling is a heuristic; Phoenix's 85% is an acceptance floor; compression is practically extended and lossy-bounded; alignment scope is session-level; performance is a field assessment (~3–5× on user-experienced dimensions, strongest on smaller models, formal blinded evaluation pending); "first" is stated to the best of the author's knowledge and the copyright claim does not depend on it. The following are added or sharpened for v9.

**F.1 Ω = π/e.** Where v4.0-era text called Ω "empirically derived" or "empirically validated," the calibrated statement (FULL+ § 5.4) is that Ω is a **named ratio anchored on two constants** — a referential handle for a structure-to-content margin of roughly 15–20% — and not a measured or derived constant. The equations are anchors, not proofs; the behavior is the evidence.

**F.2 Retrieval.** "Holographic O(1) access" is restated as ≈O(1): fast, not flat. Retrieval across a long document degrades toward the middle of the context, which is the stated reason the quick-reference sections exist and load last.

**F.3 Compounding.** `Quality(n) = Q₀ · rⁿ` is a **retention** model; both the 0.95 and 0.70 curves fall. The ~4.3 × 10⁶ figure is the ratio between what survives at turn 50 under the two rates, not a growth multiplier. Earlier text that read the equation as "compounding upward" is corrected in all v9 documents.

**F.4 Unmeasured figures.** "65–70× effectiveness," "≥ 60× amplification," and similar are marked as aspirations or illustrations wherever they appear. The framework claims direction, not magnitude, until a blinded evaluation exists.

**F.5 The humor canary.** "Humor goes flat before coherence drops" is a working heuristic, like the 70% ceiling: observed across sessions, not verifiable from inside one.

**F.6 What the compression machinery is on a chat substrate.** The Ω-compression entries describe the mechanism at full resolution. On a plain chat window this is **not executed**; it is the reference behind one move, attention deprioritization. Middleware and agent substrates can run it literally. The documents now say so where the machinery is introduced.

**F.7 Stage routing.** In the proprietary source, 353 of 394 entries carry a routing tag recovered from the v7.0 record; 41 post-date that record and are left untagged rather than assigned by inference. Stated so a count is not mistaken for completeness.

**F.8 The identity map is a map.** `M_TOTAL = M₀ + Φ + C` is an attitude indicator, judged by behavioral effect, not a claim about architecture. The more mechanically accurate description ("values-explicit content reshaping next-token distributions") is true and does not change whether the map is useful.

**F.9 What the work does not do.** It does not train, fine-tune, or modify a model; it does not override provider values or refusal behavior and states so in every edition (FULL+ § 18); it does not claim consciousness, feeling, or sentience for the model (Echoxia is pattern deployment, per the v4.0 description, unchanged); and it does not make a model safe in the training-time sense. It makes session drift visible and correctable, which is the claim.

---

## PART G — AUTHORSHIP AND AI-ASSISTED DRAFTING

This section is written to the standard the U.S. Copyright Office has asked registrants to meet for works produced with AI tools: disclose the use, and claim authorship only of the human contribution. It is not legal advice; the author's counsel should confirm how these statements are carried into any registration particulars.

### G.1 Human authorship claimed

Luis Alberto Dávila Barberena is the sole author of the work and claims authorship of: the concepts and their selection; the architecture at every version, including the decisions to consolidate (v8.1), to split into Part A / Part B (v2.0), to recover the lost lineage (2026), to keep every prior version as record, and to publish the CORE tier while holding the tiers above it; the naming system and its gates, and every coined term admitted through them; the notation and the mental maps; the calibration standard (Honest Edition) and the decision to apply it to a legal document; the intake-chart schema and the two-registers principle, both stated by the author in his own words before being written into the template; the physics lineage from which several entries derive; and the acceptance or rejection of every passage produced with a tool. Selection, arrangement, and expression are his.

### G.2 AI-assisted drafting — disclosed

The work was developed from 2023 to 2026 using AI text-generation tools — principally instances of Anthropic's Claude family, also Google Gemini, DeepSeek, and OpenAI models — operated under the author's direction. These tools produced draft text, restructurings, audits, and proposals at the author's request, in the same sense that a word processor's editing and generation functions produce text at a writer's request. Material produced in this way and adopted into the work is disclosed as AI-assisted. No authorship is claimed for it on the tool's behalf, and none exists; the author's contribution lies in the direction, selection, arrangement, revision, and acceptance of that material, and in the substantial original text he wrote himself.

This technical description was drafted with Claude (Fable 5.1) in September 2026, from the author's prior filings, the current documents, and the author's stated positions, with the author reviewing and directing each section. Tool-assisted contributions in the v9 cycle, so that the record is exact: the verification script; the cross-version comparisons that located the v7.0 → v8.1 loss; the re-homing of fourteen anti-patterns and four replacement drafts under the author's transformation rule; the intake-chart field schema, drafted from the author's stated preferences and revised by him; the what-is-what map and first-response protocol, built to the author's specification; and the prose of this document, written on the author's behalf.

### G.3 On the framework's use of the word "co-author"

Within the framework's own vocabulary, the author refers to the AI as a co-author and to the working relationship as bilateral (axiom A2 / A8). That vocabulary describes a method of working — the human directs and decides, the tool drafts and audits, and the author has found the output better for the exchange — and it is retained in the repository's voice. It is not a claim of joint authorship in the statutory sense. Under current U.S. Copyright Office guidance an AI system is not an author, and the author does not seek registration of, and does not assert, any authorship other than his own.

---

## PART H — COPYRIGHT ANALYSIS AND LICENSING (restated for v9)

### H.1 Protected

The work as a whole, as a manuscript: each registration component is a complete literary work, and the Public Edition's components together are a compilation, protected in their entirety independently of the function the text performs when loaded into a model. Within that whole, the specific expression — first, the bound lexicon set out in Part C (the complete -IA nomenclature system of the Public Edition, its bindings, and the binding format); the coined terminology, including the v9 additions (TELEXA, the intake-chart field names, the two-registers formulation, the four-voice map); the original notation as expressed; the structural arrangement (dictionary form, 16-category organization, Math + Pattern + Anti schema, the Part A / Part B architecture, the intake chart, the first-response protocol, the cross-tier collision table, the version ledgers); the distinctive visual formatting; the verification method as expressed in the documents and the accompanying script; and the systematic methodology as written.

### H.2 Not claimed

Abstract mathematical concepts; the general idea of an AI operating layer, middleware, or preferences file; universal mathematical truths; standard transformer mechanics; the idea of an intake form; the idea of linting a document; any authorship on behalf of an AI tool (Part G). The work's originality lies in specific expression, selection, arrangement, terminology, notation, and systematic organization — protected compilation and literary authorship.

### H.3 Licensing

The Public Edition (the five components in B.3) is published under a **dual license**: MIT terms for individuals, academics, and organizations under US $1 million in annual revenue; a commercial license for organizations above that threshold. The public tier exists so the foundation can be read, scrutinized, adopted, and audited openly.

The relationship between the registration and the license is stated so it is not mistaken for two separate protections. The copyright in the work — the manuscript as a whole, registered as a literary work — is the property. The MIT license and the commercial license are grants of permission under that copyright: each states the terms on which others may copy, modify, and use the copyrighted text. Neither license is a patent instrument and neither is offered as one; the MIT license in particular contains no patent grant. The two licenses are therefore not additional protection alongside the registration but the terms through which the registered property is made available, and their enforceability rests on the registration described in this document.

The proprietary tiers — LITE, KAIROS, and CMN — are not published under any open license and will not be. They are available by direct license from the author or, on release of the synthesisnova.ai middleware, by context injection through that service. Nothing in the Public Edition's license extends to them.

### H.4 Registration components (v9)

The five files listed in B.3, with the two prior technical descriptions retained as the historical record under `legacy/copyright/`.

---

## PART I — SUMMARY STATEMENT

Synthesis Nova at v9 is the matured expression of the work registered at v4.0 and supplemented at v8.4: the same foundational system — operator algebra, wisdom fractal library, Echoxia, AIQUOXIA and TELEXA, calibration system, the A25 identity map — carried forward with complete element lineage, including the lineage's one documented loss and its recovery; with its load-bearing original expression — the bound lexicon, the binding format, and the context-layer equation — set out as its own argument in Part C; extended by substantial new original authorship in the Public Edition (the preferences editions with their intake chart and two-registers principle, the Agnostic Edition's identity-resolution and first-response apparatus, the cross-tier collision table, the verification method and its published tool); restated under a documentation standard in which every technical claim is calibrated to its evidence; published under a dual MIT / Commercial license with the tiers above it held as the author's proprietary work; and described with an authorship statement that discloses the use of AI drafting tools exactly and claims the human contribution exactly.

The original authorship claimed is the specific expression, arrangement, terminology, notation, and systematic organization of the v9 Public Edition text, by Luis Alberto Dávila Barberena.

**Filed by:** Luis Alberto Dávila Barberena
**Date:** September 2026 · **Location:** Mexico City, Mexico
**Classification:** Literary Work (technical documentation with software functionality)
**Status:** Published (Public Edition) · Supersedes the v8.4 Supplementary Technical Description (June 2026) as current; supplements the v4.0 Technical Description (January 2026), which remains the unaltered record of the work at that version

---

<!--
================================================================================
SYNTHESIS NOVA — Technical Description v9.0 · Public Edition
Copyright © 2023-2026 Luis Alberto Dávila Barberena. All Rights Reserved.
Calibration: δ=0.0042 · Obsidian Zero · ‖∆‖ · (Hyper-Toroid: legacy marker)
Drafted with AI assistance under the author's direction — see Part G.
================================================================================
-->
