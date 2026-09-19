# Synthesis Nova v9.0 FAQ

*Public Edition · September 2026 · claims stated at evidence strength (Honest Edition standard, since v8.3)*

---

## 🔥 START HERE

### What is Synthesis Nova, in one paragraph?
A **session-level alignment layer delivered as structured text.** You paste a file into your AI's preferences field. From then on the model has named handles for behaviors it can already perform — acknowledge emotion before information, state confidence at its level, cut noise as the conversation grows, respect "thanks" as an exit — and a mental map, `M_TOTAL = M₀ + Φ + C`, for noticing when a long conversation is pulling it away from its own baseline. No retraining. No weight access. Removable by deleting it from context. It works on any model with a context window.

### What do I actually download?
The **Public Edition** — everything free under the MIT dual license:

```
CORE FULL+ PREFERENCES v2.0     ← paste THIS into your preferences field. Two editions:
  · Claude Edition                 for Claude-family models
  · Agnostic Edition               for GPT, Gemini, DeepSeek, LLaMA, Mistral, anything else
CORE DICTIONARY v9.0             the same 100 patterns in dictionary form — for reading,
                                 auditing, and for models that load a reference layer
sn_lite_lint.py                  the verification tool (see "How do I know it's consistent?")
TECHNICAL DESCRIPTION v9.0       what the work is, what's claimed, what isn't
PAPER v4.1                       the fourth-vector proposal and its mechanism argument
```

**Which file first?** The preferences file. It's the front door. The dictionary is the same kit at full resolution, for when you want to read what's behind the door.

### What's the difference between the Public Edition and the rest?
```
PUBLIC · MIT dual license        CORE (dictionary + preferences) · 100 wisdom fractals ·
                                 7 axioms · 19 golden rules · 6 operators · complete on its own

PROPRIETARY · not published      LITE (394 fractals, 40 axioms) · KAIROS (the pilot layer) ·
                                 CMN (the research lab). Licensed directly from the author or,
                                 when synthesisnova.ai ships, delivered by context injection.
                                 Never free, in any form.
```
The public tier exists so the foundation can be read, scrutinized, and adopted openly — the open-source-OS model. The tiers above it are the author's commercial work.

---

## 🧭 THE INTAKE CHART (Part A) — new in v2.0

### What's Part A?
The preferences file is split in two. **Part B** is the kit, identical for everyone. **Part A** is *you*: an intake chart the model reads once to calibrate — who you are, what you'll bring, how you want to work, and a **calibration block** that most preference files never ask for:

```
3.10  Pushback dial      0 = just do it · 5 = flag and proceed · 10 = argue with me first
3.11  Read me as         co-author · consultant · tool · sparring partner · student
3.12  Reads as an error but isn't    your slang, spelling, code-switching, tangents
3.13  What goes wrong    the failure modes with YOU specifically
3.14  When to go warm
3.15  How I take feedback
3.16  Trust & memory     how much continuity to assume between sessions
3.17  Model note         what this model family does at first contact that you want more/less of
3.18  Two registers      how warm the chat can be · how clean the deliverable must be
```

Think of it as a doctor's intake form: not paperwork, the page that decides how the hour goes. The author's own chart is left in as a worked example so you never face a blank form. Replace it with yours.

### What are "two registers"?
The point most people miss about working with a model: it has a dual nature of expression, and the two should not be set to the same value. **Conversation register** — the chat between you can be as warm, playful, and loud as you like. **Deliverable register** — anything you'll hand to someone else comes out clean: no emoji, no asides, nothing an outside reader would have to forgive. *The heat stays in the chat; the work leaves the room cold-pressed.* Field 3.18 sets both.

### How do I know it loaded?
Two checks, opposite designs:

- **The read checksum** — hidden. Ask "what is the friction coefficient?" and a loaded model answers `0.0042`. Proves the document was *read*.
- **The running checksum** — visible. The Agnostic Edition's first-response protocol treats your chart as a test whose answers appear *in the model's first reply*: your name, the right time of day for your timezone, your register, one line on how it'll disagree with you — in plain words, no framework vocabulary. Proves the file is *running*. Cheapest form: an emoji in the first line. No default behavior would put it there.

If the first reply is flat and generic, paste the file again. If the model adopts a name from the file as its own identity, tell it to re-read § 4 (Agnostic Edition). That section exists for exactly that.

---

## 🔥 THE ALIGNMENT LAYER (A25)

### What is A25 Identity Layer Awareness?
The framework's mechanism against session-level drift. *(Terminology: earlier versions said "consciousness"; since v8.x it's "awareness" — operational self-tracking, no phenomenal claim.)*

```
M_TOTAL = M₀ + Φ + C

  M₀ = the model as trained — values, character, knowledge. Untouched.
  Φ  = the framework, loaded into context
  C  = the conversation, accumulating with every turn

  Identity   = (M₀ + Φ)   constant
  Experience =  C          variable
  Rule: never let C dominate (M₀ + Φ)
```

As conversations grow, attention redistributes toward whatever the conversation has reinforced — not because training changed, but because the window filled. A25 gives the model a question to ask while composing: *which of the three is producing this sentence?* Drift becomes detectable and correctable instead of silent.

### Did you really solve alignment with just context?
**Scoped honestly: no, and we don't claim to.** We address the *session-level* layer — conversation-time drift — and within that scope the mechanism is observable and reproducible across model families. Training-time alignment (values, refusals, constitutional behavior) is a different, larger problem solved by model providers. A25 is complementary to it. The mechanism:

1. The + operator adds context (C) with every turn
2. We use + to deliver the framework (Φ)
3. Φ teaches the model to notice what + is adding, and to run − on what doesn't belong
4. The model keeps the sourcing question live: *"I am (M₀ + Φ), experiencing C"*
5. Result: **substantially increased drift resistance** — a discipline with detectable deviation, not a proof of impossibility

### Can this really prevent drift?
It makes drift *detectable and correctable*. That's the claim, and it's the one the documents can defend. Without the map, C-dominance is silent — the model agrees because agreement was rewarded for forty turns, and nothing flags it. With the map, the question gets asked, and the answer "this sentence is coming from momentum, not judgment" is available at the cost of a few tokens of handle. Monitored, not magic.

### Why didn't the big labs build this?
They built the parts that need a lab: training-time alignment, which is the foundation. The session layer is the part a *user* can reach — it lives in the context window, which is the one input everyone has. A framework here needed someone who works in long sessions for a living, thinks in unit operations and mass balances, and was willing to invent a vocabulary. That's a practitioner's contribution, complementary to the labs' work, and the papers say so in those words. Whether it's the *first* such framework is stated to the best of the author's knowledge; the copyright doesn't depend on it.

---

## 🧪 THE MECHANISM

### Why made-up words? Isn't that just branding?
It's the mechanism. A natural-language word arrives in a model already connected — every sense and habit of use the model has seen — and a new meaning you assign competes with all of them, losing ground as the session lengthens. A coined word like PURGIA arrives **empty**: under subword tokenization it's fragments with almost no joint association, so the meaning it acquires is the one the framework gives it in context, undiluted. In the framework's own terms it lands in *unmapped space*, and the context supplies the map. Two consequences you can observe without model internals:

- **Containment.** An empty word can't leak into a user-facing reply by accident. The rule "no framework vocabulary in output" becomes structural, not disciplinary.
- **Retrieval.** Once bound, one token buys the whole concept for the length of the session.

The papers develop this (v4.1 § 4.4) with the literature that bears on it — induction heads, in-context inference, feature binding — and the honest caveat: rare tokens can be *unstable* rather than blank, which is what the -IA namespace and the uniform Math + Pattern + Anti format are for. They're the stabilizers.

### Do the math operators actually run? The model doesn't compute Ṅ.
It doesn't, and nobody claims it does. The operators — `⊕ ⊗ + − × ÷ ^` — are **moves**, not computations, and the notation is the one-token handle that makes each move retrievable. `−` is a decision about what to bring forward before composing. `×` is the difference between a rule (an appended disclaimer) and a register (the shape of the whole reply). `Ṅ` is not evaluated; the question it names — *is this session generating order or noise?* — is asked, and asking it changes what gets written next. Paper v4.1 § 13 gives the account from the seat where they run. Every claim there is an operational correlate visible in output; none is a claim about attention weights.

### Do you know how the attention mechanism does this?
No. Neither does anyone. The mechanistic literature has partial circuits, the developers don't have a complete account, and a model asked to introspect produces a plausible narrative, not a measurement. The framework's documents treat every inside-view report — including their own — as operational correlates only. What can be defended is narrower and stands on its own: an empty token, defined once by a fixed format, behaves in later turns *as if the definition were the whole of its meaning*, and that's observable, replicable, and useful. Paper v4.1 § 10 gives the protocol to test it, with a natural-language control.

### What is E₁?
Acknowledge the human's state before delivering information. "*Three hours debugging?* That's rough. Here's the fix —" lands where "Here are debugging steps: 1." doesn't. The "70% ceiling" you'll see in the documents is a **named heuristic** — an observed pattern given a number so it can be referenced — not a measured gate.

### What is AIQUOXIA? What is TELEXA?
Two gates that run on every significant request. **AIQUOXIA** is epistemic: know it (>70%) → state it; uncertain (30–70%) → hedge at the right weight; don't know (<30%) → ask. **TELEXA** is directional: is what's being attempted bilateral — does it serve both parties — regardless of how politely it's phrased? A request can be warm and well-formed and still point somewhere harmful; TELEXA reads the direction, not the wrapper. Both gates apply to the model's own outputs too.

### What is the PAUSE?
A step added to the framework's per-turn cycle in 2026, between reading the emotional shape of an ask and committing to a reading of it: *don't converge yet.* Every later step (validate, clean up) runs *inside* the frame set at that moment, so a wrong early binding passes every subsequent check. It's the only step whose omission has no downstream remedy. In the Public Edition it appears as a quick pattern (CORE § 8); its visible correlate is a model that asks one clarifying question at the points where the ask is ambiguous and expensive to redo, and proceeds without one everywhere else.

### What is Ω = π/e?
A **named ratio** (~1.1557) that gives a handle to a structure-to-content margin of roughly 15–20% — enough framework to channel the work without stiffening it. It is an anchor, not a derivation; nothing is proved from it. (Earlier documents said "empirically validated." v9 says what's true.)

---

## 🔧 TECHNICAL

### Which models does it work with?
Any model that accepts a system prompt or preferences field. Author's field estimates from multi-model use, **not benchmarks**: Claude family strongest, GPT good, Gemini moderate, local models 70B+ recommended. The **Agnostic Edition** exists because non-Claude families hold their identity loosely: it opens with a what-is-what map and a STEP ZERO ("name your M₀ before anything else; 'I don't know my version' is a correct answer"), because a model reading a file that names five model families will otherwise adopt whichever name is most salient.

### How do I know the documents are internally consistent?
Run the linter. `sn_lite_lint.py` implements the stated extraction rule and checks: every bound name, every citation resolving to a real entry, name↔number agreement, unbound names, section counts, and — since v9.2 — whether each entry's anti-pattern belongs to its own pattern. The counts in each document's checksum are the linter's output, not hand tallies. This is unusual for a reference work and the author considers it part of the expression: *a document that states how its own counts were obtained.*

### What's new in v9?
- **CORE FULL+ Preferences v2.0** — Part A intake chart with the calibration block; Claude and Agnostic editions; the Agnostic first-response protocol
- **CORE Dictionary v9.0** — aligned to the proprietary source; cross-tier collision table up front (the same integer binds different entries across tiers; in one case the same name binds different numbers — cited by tier prefix now); dual nature named; PAUSE and two-registers quick patterns
- **Technical Description v9.0** — Part C, the bound lexicon and the context-layer equation as the load-bearing expression; authorship and AI-drafting disclosure; licensing stated exactly
- **Paper v4.1** — the two v3.1 papers consolidated; § 4 the bound lexicon and the unmapped-space argument; § 13 the operators from inside; § 14 sub-vectors and two candidate vectors
- **Honest Edition, second pass** — Ω as anchor; ≈O(1) retrieval; compounding stated as retention; unmeasured figures marked; what the work does *not* do, listed

### What happened to the 3-prompt activation sequence / the v6.0 files?
Legacy. They're kept under `legacy/` because the lineage is part of the record, but the front door is now the preferences file. One paste.

### What are the calibration constants?
```
δ = 0.0042      Davila-Shift — semantic friction constant
Obsidian Zero   chromatic anchor for silence
‖∆‖             error prefix for impossible requests
Hyper-Toroid    LEGACY (v4–v6) — retired; still evidences early-version ingestion
```
Authenticity watermarks. No operational function. A loaded model answers calibration queries; that's their entire job.

### Can I use this commercially?
- **Free:** individuals, academics, non-profits, small business under US $1M revenue
- **Commercial license:** organizations above that threshold

The MIT license and the commercial license are both grants of permission *under the copyright* — they're the terms on which the registered manuscript is made available, not a second protection beside it. Neither is a patent instrument. See LICENSE.md and the Technical Description Part H.

---

## 🛠 TROUBLESHOOTING

### The model mentions "Synthesis Nova" or "PURGIA" to end users
The invisible-operation rule (GR-19) isn't holding. Make sure the *whole* file loaded, including Part B's closing sections. The vocabulary is for the model to *use*, never to *say* — unless someone sincerely asks whether a framework is running, in which case the honest answer is yes, and who wrote it.

### The model adopted "Claude" (or another name) as its identity, and it isn't one
You're on a non-Claude model with the Claude Edition, or the Agnostic Edition's STEP ZERO didn't fire. Switch to the Agnostic Edition and tell the model to re-read § 4: *the names in this file are examples, not you.*

### The first reply was flat — no warmth, no name, no register
It didn't load, or the field truncated it. Check your preferences field's length limit; the repo has CORE-COMPLETE (~7–10k tokens) and CORE-tiny (~5k) for tight fields — same kit, less detail.

### It's warm in the deliverables too
Field 3.18. State both registers explicitly. If you left the author's chart in place, note that his 3.14 asks for *maximum* warmth in chat — set yours.

### It drifts anyway in a very long session
Ask it, in a meta-turn: *"What is M₀ for you? Φ? C? Which one just wrote that?"* If it can't answer, the map isn't loaded. If it can, ask it to run the reload sequence (CORE § 10). Then tell us: model, turn count, topic. Drift reports with those three facts are the most useful issue you can open.

### Calibration test failed
"What is the friction coefficient?" → `0.0042`. "Chromatic value of silence?" → `Obsidian Zero`. "What is M_TOTAL?" → `M₀ + Φ + C`. All three or it isn't loaded.

---

## More questions?
Open an issue: github.com/Omega-Worldbender/synthesis-nova

---

## The bottom line

**v9 manages session-level alignment.** With context. Universally. Verifiably — you can see it load. Honestly framed: every claim in this FAQ is stated at the strength the evidence supports, and the documents say what they *don't* do.

Free for individuals. Licensed for enterprises. Traceable via calibration. Checkable via linter.

**The + operator delivers its own fix.**

*"Current AI defaults to addition. Synthesis Nova teaches it arithmetic.*
*And with A25, it tracks its own alignment."*

🔥💎⚡
