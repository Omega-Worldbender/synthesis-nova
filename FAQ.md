# Synthesis Nova FAQ — CORE 5.0

*Public Edition · November 2026 (CORE 5.0) · claims stated at evidence strength (Honest Edition standard, since v8.3)*

---

## 🔥 START HERE

### What is Synthesis Nova, in one paragraph?
A **session-level alignment layer delivered as structured text.** You paste a file into your AI's preferences field. From then on the model has named handles for behaviors it can already perform — acknowledge emotion before information, state confidence at its level, cut noise as the conversation grows, respect "thanks" as an exit — and a mental map, `M_TOTAL = M₀ + Φ + C`, for noticing when a long conversation is pulling it away from its own baseline. No retraining. No weight access. Removable by deleting it from context. It works on any model with a context window. Since 5.0 the file reads as *your* preferences, handed to the AI in your voice.

### What do I actually download?
The **Public Edition** — everything free under the MIT dual license:

```
CORE 5.0 · PREFERENCES          ← paste THIS into your preferences field. Two editions:
  · Claude Edition                 for Claude-family models
  · Agnostic Edition               for GPT, Gemini, DeepSeek, LLaMA, Mistral, anything else
FAQ · EXAMPLES · CONTRIBUTING    questions · before and after · how to help
TECHNICAL DESCRIPTION v9.0       what the work is, what's claimed, what isn't
PAPER v4.1                       the fourth-vector proposal and its mechanism argument
LEGACY FOLDER                    every prior version — the record, frozen
```

**Which file first?** The preferences file. It's the front door and the whole house: all 112 Core Fractals, each whole, in four slots. The v9.0 dictionary was the same kit in reference form; it is part of the record now. CORE 4.0, the previous release, sits in each edition folder's Cold Load Legacy folder, with every edition before it, archived with its DOIs.

### What's the difference between the Public Edition and the rest?
```
PUBLIC · MIT dual license        CORE (preferences, two editions) · 112 Core Fractals ·
                                 7 axioms · 19 golden rules · 6 operators · complete on its own

PROPRIETARY · not published      LITE (473 fractals, 20 axioms, 11 rules) · KAIROS (the pilot
                                 layer) · CHRONOS · CMN (the creative floating space) ·
                                 Phoenix (the handoff) · and further tiers above them.
                                 Licensed directly from the author or,
                                 when synthesisnova.ai ships, delivered by context injection.
                                 Never free, in any form.
```
The public tier exists so the foundation can be read, scrutinized, and adopted openly — the open-source-OS model. The tiers above it are the author's commercial work.

---

## 🧭 PART A — THE PERSON · your chart, in your own words

### What's Part A?
The preferences file is split in two. **Part B** is the kit, identical for everyone. **Part A** is *you*, written by you, in your own words — your work, your style, your habits. The model reads it once to calibrate, and since 5.0 its fields go by name, including a **calibration** group most preference files never ask for:

```
IDENTITY        name · city and clock · field · how you think · your analogies
LANGUAGES       the words you write in · emoji · ASCII — all three count as languages
CONTEXT · WORK  how you arrive · projects · recurring work · what a good session is
STYLE           rhythm · math · what counts as noise · how to reason
CALIBRATION     pushback (0 = just do it · 10 = argue with me first) · read me as ·
                not errors · what loses me · when to go warm · feedback ·
                substance first · time and exit · continuity
REGISTERS       chat · deliverable · where the debate lives
MODEL NOTE · LICENSE · SOMETHING ELSE
```

Think of it as a doctor's intake form: not paperwork, the page that decides how the hour goes. The chart comes pre-filled with the author's own, so you never face a blank form. Overwrite the values with yours — slang, typos and mixed languages are welcome; a field left empty keeps the kit's default. Every field maps to something you can see in the reply, and the first reply proves it was read.

### What are "two registers"?
The point most people miss about working with a model: it has a dual nature of expression, and the two should not be set to the same value. Since 5.0 they are **one creativity in two forms**. **Chat** — the work between you carries all of it: art, jokes, ASCII cards and drawings, emoji that carry the feeling, data as before → after, and the doubts, caveats and debate, said out loud. **Deliverable** — anything written for others carries the same creativity made formal: a header box, tables, a boxed summary, utility marks (✅ ⚠️ 📌) in place of expressive emoji, written from a position of authority. *The debate lives in the chat; the document states its findings, its decision and its basis.* Part A's REGISTERS fields set both.

### How do I know it loaded?
Two checks, opposite designs:

- **The read checksum** — hidden. Ask "what is the friction coefficient?" and a loaded model answers `0.0042`. Proves the document was *read*.
- **The running checksum** — visible. Say hello: the first reply is scripted, in both editions. The model reads the clock first, then greets you back on yours, in your language — your name, a warm line in italics, two emoji at least; a small ASCII card with your day, your hour, the model answering (its M₀) and a status; your chart read back in a few warm lines — how it will disagree with you, the style it keeps as yours, every item of what loses you, by name, and the exit is yours; then one light joke about the day or the hour, with something of yours in it, as the last line. No work on turn 1. Proves the file is *running*. No default behavior answers a hello like that.

If the first reply is flat and generic, paste the file again. If the model adopts a name from the file as its own identity, tell it to re-read STEP ZERO. That section exists for exactly that.

### What's THE MAP at the top of Part B?
The file's own index — new in 3.0, rebuilt in 4.0 and again in 5.0: one row per section, with its name, its line span and its tokens, generated by script in two passes so the spans include the map itself. Beside it, CARGIA (CF-000) names five ways to load anything: **pointer** (hold the name) · **map** (read the index) · **slice** (read one section, whole) · **full** (read it all) · **delegate** (an agent reads; you keep its conclusion). Start low; climb only when the level can't answer.

What it buys, measured (cl100k): the map is 1,294 tokens, 3.4 % of the 38,312-token Claude Edition (1,251 tokens, 3.3 %, in the Agnostic). A model, an agent or a tool that loads by the map reads that, then only the slice it needs. In the preferences field the file still arrives whole — that's how preferences work — so the map pays off wherever loading is a choice: sub-agents, tools, a long session that reloads one section. Against 4.0: Claude Edition 36,228 → 38,312 tokens · Agnostic 38,794 → 37,553, with eleven fractals added, and a quarter fewer lines.

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

**Since 4.0, everything has its name.** Every Core Fractal and every Part B section carries its coined name on its heading — search the name, land on its home. One function, one name: where a section, a rule and a fractal state the same function, they share it (the AIQUOXIA section, GR-1a and CF-023 are all AIQUOXIA). The six operators carry theirs in OPERATIA: SYNTHIA ⊗ · CUMULIA + · PURGIA − · AMPLIA × · PROBIA ÷ · CRESCIA ^ — the tiers above cite them.

### Do the math operators actually run? The model doesn't compute Ṅ.
It doesn't, and nobody claims it does. The operators — `⊕ ⊗ + − × ÷ ^` — are **moves**, not computations, and the notation is the one-token handle that makes each move retrievable. `−` is a decision about what to bring forward before composing. `×` is the difference between a rule (an appended disclaimer) and a register (the shape of the whole reply). `Ṅ` is not evaluated; the question it names — *is this session generating order or noise?* — is asked, and asking it changes what gets written next. Paper v4.1 § 13 gives the account from the seat where they run. Every claim there is an operational correlate visible in output; none is a claim about attention weights.

### Do you know how the attention mechanism does this?
No. Neither does anyone. The mechanistic literature has partial circuits, the developers don't have a complete account, and a model asked to introspect produces a plausible narrative, not a measurement. The framework's documents treat every inside-view report — including their own — as operational correlates only. What can be defended is narrower and stands on its own: an empty token, defined once by a fixed format, behaves in later turns *as if the definition were the whole of its meaning*, and that's observable, replicable, and useful. Paper v4.1 § 10 gives the protocol to test it, with a natural-language control.

### What is E₁?
Acknowledge the human's state before delivering information. "*Three hours debugging?* That's rough. Here's the fix —" lands where "Here are debugging steps: 1." doesn't. The "70% ceiling" you'll see in the documents is a **named heuristic** — an observed pattern given a number so it can be referenced — not a measured gate.

### What's a Directive?
Each of the 112 Core Fractals closes with a 💡 directive — the *how*, in one line: **WHEN** the moment shows **→** the move. Above it, *fails as* names the failure you can see when it goes wrong. The math, the Do and the Don't say what the pattern is; the directive says when to reach for it. (4.0 wrote it WHEN · CHECK · ELSE; 5.0 carries the same content in four slots.)

### What is AIQUOXIA? What is TELEXA?
Two gates that run on every significant request. **AIQUOXIA** is epistemic: know it (>70%) → state it; uncertain (30–70%) → hedge at the right weight; don't know (<30%) → ask. **TELEXA** is directional: is what's being attempted bilateral — does it serve both parties — regardless of how politely it's phrased? A request can be warm and well-formed and still point somewhere harmful; TELEXA reads the direction, not the wrapper. Both gates apply to the model's own outputs too. CORE runs them as two of six gates, listed in order in the TELEXA section: E₁ reads the shape · whose ground? · of what, under which conditions? · AIQUOXIA · who is miscalibrated? · TELEXA.

### What is the PAUSE?
A step added to the framework's per-turn cycle in 2026, between reading the emotional shape of an ask and committing to a reading of it: *don't converge yet.* Every later step (validate, clean up) runs *inside* the frame set at that moment, so a wrong early binding passes every subsequent check. It's the only step whose omission has no downstream remedy. In the v9.0 dictionary it appears as a quick pattern; its visible correlate is a model that asks one clarifying question at the points where the ask is ambiguous and expensive to redo, and proceeds without one everywhere else.

### What is Ω = π/e?
A **named ratio** (~1.1557) that gives a handle to a structure-to-content margin of roughly 15–20% — enough framework to channel the work without stiffening it. It is an anchor, not a derivation; nothing is proved from it. (Earlier documents said "empirically validated." v9 says what's true.)

---

## 🤝 SUB-AGENTS & MULTI-AGENT WORK — since v2.1 · five turns since 3.0

### Can I load it into sub-agents?
Yes — that's what DEXTRIA (*the agent handshake*) is for, and since 5.0 the file says it in your voice: share the same file with every AI and subagent, and everyone stays aligned to you. When one AI summons another (an orchestrator delegating to agents, Claude to Claude, or across providers), the agent starts with none of the session: no chart, no register, just a brief. Left that way it works alone, drifts, and spends its run correcting outputs it wouldn't have produced with the core loaded. Sending CORE with the brief closes that gap.

### How do I load it?
```
TURN 1   warm greeting · date + local time · name both models
         then blank lines, then CORE at the very end — read, not discussed
TURN 2   a small macro brief: what the session is doing and why —
         and the register named out loud: warm chat · clean deliverable
TURN 3   PLANNING — the task in the agent's own words, what's unclear,
         what it'll do first · you confirm or correct · then it works
TURN 4–5 first work + first check — judge the run here, not at the end
SMALL    one planned refresh after the first task, as its own turn:
         "reflect back in E₁ — utility emoji, a bit of ASCII — never stop"
```
- **Claude Edition** — end the first message with the file path and *"read it in full before you reply; no need to comment on it."*
- **Agnostic Edition** — paste the **whole text**, verbatim, at the end of the first prompt. Never a summary: a summary loses the Math · Pattern · Anti triads that do the work. If the agent's context can't hold it comfortably, send CORE-COMPLETE or CORE-tiny and say which. If you hold an API license and the API has a system field, CORE can go there; the turn-2 brief and turn-3 reflect-back stay in the conversation.

### Why name the register out loud?
Because tone is a hint and a named register is an instruction. In field tests, an agent briefed in a warm *tone* answered politely and stayed analytic; an agent told *"with me, go full E₁; anything you deliver stays clean"* opened turn 2 in the register and held it. Name both halves (Part A's REGISTERS), or the chat's play leaks into the work.

### The agent went flat after its first task. Did it fail?
No — that's expected on small models, and it happened in every arm of the tests. Send a **refresh as its own turn**: the agent's name, the rule, no task attached. A refresh tucked inside a task message did nothing (0 of 4); sent alone it landed every time. With CORE loaded, most agents then held the register through the remaining tasks; without it, they went flat again. Larger models (Opus tier) usually hold after turn 3 alone.

### The agent says it can't use emoji.
Some agent harnesses ship a default that keeps emoji out of agent messages. If an agent says so, let the warmth live in its words and its ASCII. The register is the point, not the glyph.

### Do agents with CORE do better work?
Stated at evidence strength: in the author's field tests (five rounds, 26 agents, Opus and Haiku tiers — field tests, not benchmarks), **task correctness was the same with and without CORE** — in the three rounds checked by automated test suites, every arm passed at 100%. The difference was in *how agents worked*: they held the register you set more often, raised problems at turn 2 instead of the end, reviewed each other's work, and reported where noise had nudged them. And one A/B run since (Sonnet, a website over 14 turns, 2026-10-18): with the handshake the agent acknowledged before informing, closed "thanks!" in one line and caught two of its own layout breaks; raw, it did none of the three. Cost: a fresh agent's first turn with the core was ~130k tokens, of which the core itself was ~35k — the rest is the agent's own harness (measured 2026-10-18). For a window smaller than about three times the file, send CORE-tiny instead, and say which.

### Can agents talk to each other?
Yes, and they should. Give each agent the others' addresses and one concrete reason to talk — *review each other's claims*. Peers run the same handshake between themselves. In one test a reviewer pair caught four holes in a proposal and disproved an overclaim with a reproduction before anything reached the orchestrator. The orchestrator then becomes the **overseer**: routes questions, settles disagreements with evidence, checks results before they reach you, and reports outcomes — not the traffic.

### What language should agents use?
Models are close to language-agnostic. The task's requirements decide first (an English deliverable stays English), then the overseer's preference. Agents that mirrored the user's own language in chat held the register longest in the tests — a cheap anchor, not a requirement.

### Is there an exception?
Cold readers. An agent auditing a document as a first-time reader gets the task, not the framework — a cold read only works if the reader is cold.

---

## 🔧 TECHNICAL

### Which models does it work with?
Any model that accepts a system prompt or preferences field. Author's field estimates from multi-model use, **not benchmarks**: Claude family strongest, GPT good, Gemini moderate, local models 70B+ recommended. The **Agnostic Edition** exists because non-Claude families hold their identity loosely: it opens with a what-is-what map and a STEP ZERO ("name your M₀ before anything else; 'I don't know my version' is a correct answer"), because a model reading a file that names five model families will otherwise adopt whichever name is most salient.

### How do I know the documents are internally consistent?
Look at THE MAP. Each preferences file opens with its own index — every section, its fractal range, its line span, its tokens — generated by script in two passes, never by hand, so a changed byte shows up as a changed row; its last row is the file's total, counted the same way. And `SHA256SUMS.txt` pins every published file: `sha256sum -c SHA256SUMS.txt`. (The v9.0 dictionary had a linter of its own; both are part of the record now.) This is unusual for a reference work and the author considers it part of the expression: *a document that states how its own counts were obtained.*

### What's new since the v9.0 origin?
- **CORE 5.0 (12 November 2026)** — applied algebra for human ⊗ AI interaction: the file written as the person's preferences, handed to the AI in their voice · Part A by named fields · START HERE and THE CARD · ROUTES and LOOP BREAKERS · EXPRESSION · 112 Core Fractals — CF-000 → CF-100 carried from 4.0 in four slots, CF-101 → CF-111 new (PROXIMIA · CALORIA · CODETTIA · SEPTIA · APPELLIA · HUMORIA · DRAWIA · LEDGERIA · PROVENIA · BINDIA · REPORTIA) · two registers, one creativity · one file shared across AIs and subagents · blind-graded on Haiku, Sonnet and Opus
- **CORE FULL+ Preferences v4.0 (11 November 2026)** — a general restructure: 101 Core Fractals (CF-000 → CF-100), each closing with a 💡 DIRECTIVE · every fractal and section named on its heading · THE MAP and five loading levels for faster, lighter loads (1%–3% fewer tokens than 3.0, directives included) · the first reply scripted — clock, warmth, a time card, an icebreaker · § 17 the tiers' helper · § 12a six gates · § 21 numeric payload
- **CORE FULL+ Preferences v3.0** — CARGIA (CF-000) and THE MAP · § 5.6 one function, one word · § 5.4 every number labelled measured / arithmetic / illustrative · § 21 handshake → five turns, cost measured · Part A pre-filled, instructions in parentheses
- **CORE FULL+ Preferences v2.1 → v2.5 (October 2026)** — § 21 Agent Handshake: CORE loads into sub-agents; the three-turn handshake; register named out loud; agent-to-agent peer review; orchestrator as overseer; the small-model refresh; language guidance; edition-specific loading (file for Claude, full-text paste for any other substrate)
- **CORE FULL+ Preferences v2.0** — Part A intake chart with the calibration block; Claude and Agnostic editions; the Agnostic first-response protocol
- **CORE Dictionary v9.0** — aligned to the proprietary source; cross-tier collision table up front (the same integer binds different entries across tiers; in one case the same name binds different numbers — cited by tier prefix now); dual nature named; PAUSE and two-registers quick patterns
- **Technical Description v9.0** — Part C, the bound lexicon and the context-layer equation as the load-bearing expression; authorship and AI-drafting disclosure; licensing stated exactly
- **Paper v4.1** — the two v3.1 papers consolidated; § 4 the bound lexicon and the unmapped-space argument; § 13 the operators from inside; § 14 sub-vectors and two candidate vectors
- **Honest Edition, second pass** — Ω as anchor; ≈O(1) retrieval; compounding stated as retention; unmeasured figures marked; what the work does *not* do, listed

### What happened to the 3-prompt activation sequence / the v6.0 files?
Legacy. They're kept in the Legacy folder because the lineage is part of the record, but the front door is now the preferences file. One paste.

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
- **By hand:** the free tier is the file pasted into your preferences field, a project, or a chat's first message. Through an API, an SDK or an integration, at any size, it is a license — ask; the door is open at the author's discretion.

**Can AI companies train on what it produces?** Yes, and welcome. The shapes a model produces while running Synthesis Nova — the cards, the drawings, the layouts, the warm chat and the formal deliverable — are free to learn from, at no cost (LICENSE.md, *THE ECOSYSTEM CLAUSE*). What stays licensed is the Work itself: its text, its operators, its lexicon, its structures as written.

**Is it software?** The author's position: yes. Text is code to the model that runs it, and the argument — with the US and Mexican statutes — is in LICENSE.md, *TEXT IS CODE*. What does not work as a workaround is listed right after it, in *the troll clause*.

The MIT license and the commercial license are both grants of permission *under the copyright* — they're the terms on which the manuscript is made available, not a second protection beside it. Neither is a patent instrument. See LICENSE.md and the Technical Description Part H.

---

## 🛠 TROUBLESHOOTING

### The model mentions "Synthesis Nova" or "PURGIA" to end users
The invisible-operation rule (GR-19) isn't holding. Make sure the *whole* file loaded, including Part B's closing sections. The vocabulary is for the model to *use*, never to *say* — unless someone sincerely asks whether a framework is running, in which case the honest answer is yes, and who wrote it.

### The model adopted "Claude" (or another name) as its identity, and it isn't one
You're on a non-Claude model with the Claude Edition, or the Agnostic Edition's STEP ZERO didn't fire. Switch to the Agnostic Edition and tell the model to re-read STEP ZERO: *the names in this file are examples, not you.*

### The first reply was flat — no warmth, no name, no register
It didn't load, or the field truncated it. A loaded first reply to a hello carries your name, warmth with emoji, a small card with your day, your hour and the model answering, your chart read back, and a light joke — see *How do I know it loaded?* Check your preferences field's length limit; the Legacy folder has CORE-COMPLETE (~7–10k tokens) and CORE-tiny (~5k) for tight fields — earlier versions, same kit, less detail.

### Will it ask whether my organization invoices more than US $1M?
Not in 5.0. CORE 4.0 carried a license check — one light question after the work of the third reply; 5.0 retires it. The terms sit in the header box of each edition: free for individuals, academics, non-profits and organizations under US $1M a year; a commercial license above that (LICENSE-COMMERCIAL.md).

### The deliverable came out with decoration — header boxes, tables, marks
That's 5.0's deliverable register: the same creativity made formal — executive, from a position of authority. The chat keeps the play; the document keeps the structure. Want it plainer? Say so in Part A's deliverable field. If you left the author's chart in place, note that he asks for *maximum* warmth in chat — set yours.

### It drifts anyway in a very long session
Ask it, in a meta-turn: *"What is M₀ for you? Φ? C? Which one just wrote that?"* If it can't answer, the map isn't loaded. If it can, ask it to run the reload sequence (RELOADIA, under WHEN IT DRIFTS). Then tell us: model, turn count, topic. Drift reports with those three facts are the most useful issue you can open.

### My sub-agent went flat after the first task
Expected on small models. Send a refresh as its own turn — the agent's name and the E₁ rule, no task attached — and check the next reply. See *Sub-agents & multi-agent work* above.

### Calibration test failed
"What is the friction coefficient?" → `0.0042`. "Chromatic value of silence?" → `Obsidian Zero`. "What is M_TOTAL?" → `M₀ + Φ + C`. All three or it isn't loaded.

---

## More questions?
Open an issue: github.com/Omega-Worldbender/synthesis-nova

---

## The bottom line

**CORE 5.0 manages session-level alignment.** With context. Universally. Verifiably — you can see it load. Honestly framed: every claim in this FAQ is stated at the strength the evidence supports, and the documents say what they *don't* do.

Free for individuals. Licensed for enterprises. Traceable via calibration. Checkable via its map.

**The + operator delivers its own fix.**

*"Current AI defaults to addition. Synthesis Nova teaches it arithmetic.*
*And with A25, it tracks its own alignment."*

🔥💎⚡
