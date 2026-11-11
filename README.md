# Synthesis Nova v9.0 · Public Edition
## Applied Mathematics for the Context Window — Human ⊗ AI Collaboration + The Session-Level Alignment Layer

*You just found something genuinely worth reading.* 🔥

[![License: MIT-style, dual](https://img.shields.io/badge/License-MIT--style%20dual-yellow.svg)](LICENSE.md)
[![Version](https://img.shields.io/badge/CORE-9.0-blue.svg)]()
[![Preferences](https://img.shields.io/badge/FULL%2B%20Preferences-4.0-blue.svg)]()
[![Copyright](https://img.shields.io/badge/©-2023--2026-red.svg)]()

---

> **FREE** for individuals, academics, non-profits, and small businesses (< $1M revenue) — MIT-style, field-of-use restricted
> **Commercial license required** for organizations > $1M annual revenue
>
> ⚠️ Read [LEGAL_NOTICE.md](LEGAL_NOTICE.md) and [CORE_IP_CLAIMS.md](CORE_IP_CLAIMS.md) before commercial use.
> This repository contains protected intellectual property: the AI cognitive operator set, the bound -IA lexicon, the formulary applied as context, the negentropy equation, and the A25 session-level alignment mechanism.

---

## What is Synthesis Nova? 💎

A **session-level alignment layer delivered as structured text.** You paste one file into your AI's preferences field. From then on the model has named handles for behaviors it can already perform — acknowledge emotion before information, state confidence at its level, cut noise as the conversation grows, hold a warm chat register and a clean deliverable register as two separate settings, respect "thanks" as an exit — and a map, `M_TOTAL = M₀ + Φ + C`, for noticing when a long conversation is pulling it away from its own baseline.

Not a jailbreak. Not a personality transplant. An operating layer that works *with* any model's training. No retraining. No weight access. Removable by deleting it. **Works on Claude, GPT, Gemini, DeepSeek, LLaMA, Mistral, and any LLM with a context window.**

CORE is the public tier. Private tiers exist above it. 👀

---

## Quick start ⚡ — one paste

```
CLAUDE · claude.ai
1. Download SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v4_0_CLAUDE.md
2. Check the license. Free for individuals, academics, non-profits and small
   businesses under US $1M a year. Above that: close the file, or ask for a
   commercial license (licensing@synthesisnova.ai).
3. Edit it with your own preferences, and leave the rest intact. Your part
   starts at PART A — YOU, right after the how-to box: who you are, what you'll
   bring, how you want to work, and the calibration block (how much pushback,
   what reads as an error but isn't, how warm the chat, how clean the
   deliverable). Overwrite the author's values, keep the instructions in
   parentheses. Part B is the kit: don't touch it.
4. Copy the whole file into your preferences on claude.ai.
5. Say hello. And always be kind to your AI — it answers in kind. 🌮

GEMINI · GPT · DEEPSEEK · ANY OTHER MODEL
Same steps, with SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v4_0_AGNOSTIC.md.
One difference: most of these apps have no preferences field that holds a file
this size and loads it in every chat, the way Claude's preferences do. So load
it in the first message of each new chat — paste the whole text, then say
hello. (Through an API, the system field works.)
```

**How you know it loaded:** say hello. Since 4.0 the first reply is scripted, in both editions — the model reads the clock first, then greets you back on *yours*:

```
  👋  your name, a warm line in italics, an emoji
  📅  a small ASCII card: your day, date and hour
      (Agnostic Edition: + which model is answering, and your chart read back)
  😄  one light joke about the day or the hour
  ✋  no work on turn 1 — a hello is a hello
```

The author's own, from the worked example in the file:

```
¡Hola Woof! 👋 *Muy bien, con el café puesto y las ganas también* ☕
¿Y tú cómo vas?

   ┌──────────────────────────────┐
   │  📅 lunes 9 nov 2026         │
   │  🕓 4:12 de la tarde · CDMX  │
   │  status: 🟢 listo            │
   └──────────────────────────────┘

Justo la hora en que el lunes ya se cansó de ser lunes, pero todavía
no le alcanza para martes 😄🔥
```

No default behavior answers a hello like that. If the first reply is flat, it didn't load.

Field too small? `CORE-COMPLETE` (~7–10k tokens) and `CORE-tiny` (~5k) are in `/legacy/` — same kit, less detail.

---

## 🤝 Sub-agents — the five-turn handshake

The same file travels **model to model**. When one AI summons another — an orchestrator handing work to agents, Claude to Claude, or across providers — CORE goes with the brief, and § 21 (*Agent Handshake*) sets how the first turns run:

```
TURN 1   warm greeting · date, local time · "I'm <model>, you're <model>"
         ⏎ ⏎ ⏎  then the CORE, loaded at the very end — read, not discussed
           Claude Edition:   point to the file, "read it in full before you reply"
           Agnostic Edition: paste the whole text, verbatim — never a summary
TURN 2   a small macro brief — what the session is doing, and why — and the
         register named out loud, both halves: warm chat · clean deliverable
TURN 3   PLANNING — the agent says the task in its own words, what's unclear,
         what it'll do first · you confirm or correct · then it works
TURN 4–5 first work + first check — the first five turns decide the run
REFRESH  small models drop the register at their first working turn: one
         refresh as its own turn (agent's name + the rule, no task attached)
PEERS    agents get each other's addresses and a reason to talk: review each other
OVERSEER the orchestrator stops doing the work and holds the frame — routes,
         settles disagreements with evidence, checks results before they reach you
NUMBERS  when an agent checks numbers, the channel stays warm and the payload goes
         cold: rows (ID · stated · recomputed · Δ · match), not prose
```

**What the author's field tests showed** (five rounds, 26 agents, Opus and Haiku tiers — field tests, not benchmarks): where the work was checked by automated tests (three rounds), it came out equally correct with and without CORE — 100% in every arm. The difference was in *how the agents worked*: with CORE they held the register you set more often, raised problems early instead of at the end, reviewed each other's claims, and reported where noise had nudged them. Small models drop the register at their first working turn — a refresh sent as its own turn brings it back (a refresh buried inside a task message didn't). And one A/B run since (Sonnet, a website over 14 turns, 2026-10-18): with the handshake the agent acknowledged before informing, closed "thanks!" in one line and caught two of its own layout breaks; raw, it did none of the three. Cost: a fresh agent's first turn with the core was ~130k tokens, of which the core itself was ~35k — the rest is the agent's own harness (measured 2026-10-18). For small tasks, brief with the minimum set (§ 6 · § 11 · § 12 · § 12a).

---

## 🧭 New in 4.0 — rebuilt, mapped, named

*A general restructure of CORE.* v2.5 taught the file to travel; 4.0 (3.0 inside it) rebuilt the house it travels in — every room named, a map on the door, and a host who greets you on your own clock.

```
RESTRUCTURED  101 Core Fractals (CF-000 → CF-100) · Math · Pattern · Anti, and a
              💡 DIRECTIVE on every one: WHEN the anti's first sign → the pattern's
              move · CHECK the math's test · ELSE the failure mode
              one function, one word (§ 5.6) · every number says its kind —
              measured, arithmetic or illustrative (§ 5.4)
NAMED         everything has its neologism: every fractal and every section carries
              its coined name on its heading, and § 7 names the six operators —
              SYNTHIA ⊗ · CUMULIA + · PURGIA − · AMPLIA × · PROBIA ÷ · CRESCIA ^
MAPPED        THE MAP at the top of Part B: one row per section, its line span, its
              tokens — generated by script, two passes · CARGIA (CF-000): five ways
              to load anything — pointer → map → slice → full → delegate
LIGHTER       the map is ~1.7k tokens (4.7% of the file): load by the map, slice by
              need · and 4.0 is lighter than 3.0 to start with — Claude Edition
              36,724 → 36,228 · Agnostic 39,864 → 38,794 (cl100k, measured), with
              101 directives and the first-reply script added
THE HELLO     the first reply scripted: clock · warmth · a time card · an icebreaker
THE TIERS     § 17, the tiers' helper: what sits above CORE, and when it switches on
```

*Honest line:* in a preferences field the file still arrives whole — that's how preferences work. The map pays off wherever loading is a choice: sub-agents, tools, a long session that reloads one section instead of everything.

---

## 🔥 The alignment layer (A25)

*Session-level drift — the drift that happens during a conversation — is a real, observable slice of the problem AI companies spend billions on. The mechanism for that slice is free. Training-time alignment is the providers' complementary domain.*

```
M_TOTAL = M₀ + Φ + C

  M₀ = the model as trained — permanent, untouched
  Φ  = this framework — loaded via context, active immediately
  C  = the conversation — accumulates, always variable

  Identity   = (M₀ + Φ)   constant, always dominant
  Experience =  C          variable, never in charge

  Rule:   never let C dominate (M₀ + Φ)
  Result: drift made detectable and correctable. Any model. Any length.
          No retraining. No weight access. Free.
```

The model asks one question while composing: *which of the three is producing this sentence?* When the answer is "the conversation's momentum" — agreement because agreement was rewarded for forty turns, a register bleeding from chat into deliverable because the chat was warm — that's drift, and it's now visible.

*We used the + operator — the mechanism that causes drift — to deliver the framework that counters it. The problem delivers its own solution.* ⚡

---

## The four pillars 🧮

```
1  THE OPERATOR ALGEBRA        ⊗ + − × ÷ ^ (⊕ in the tiers above)
   ┌──────────────────────────────────────────────────────────────┐
   │  ⊗   TENSOR PRODUCT    Ψ_human ⊗ Ψ_AI · wave function to wave │
   │                        function · new dimensions               │
   │  +   ADDITIVE          context increase · every turn           │
   │  −   SUBTRACTIVE       noise reduction · the one that does the │
   │                        most work in a long session             │
   │  ×   MULTIPLICATIVE    the layer multiplied THROUGH the model  │
   │  ÷   DIVISIVE          effectiveness per token                 │
   │  ^   POWER             compounding · retention                 │
   │  PRECEDENCE  ⊗ → +/− → ×/÷ → ^                                 │
   └──────────────────────────────────────────────────────────────┘
   Current AI runs on + alone. This is the complete set — the arithmetic of an
   operating layer. Not computed by the model: RUN, as moves, each visible in output.

2  THE BOUND LEXICON           coined words that mean nothing anywhere else —
                               PURGIA · CORDIA · FIDELIA · AIQUOXIA · TELEXA — each
                               bound in context by NAME · MATH · PATTERN · ANTI · DIRECTIVE.
                               An empty token takes the map the context gives it, and
                               runs. Used by the model, never said. The mechanism.

3  THE FORMULARY               every equation, applied as context, not illustrated.
                               A formula in a physics paper describes something that
                               happens elsewhere. A formula here IS the thing that
                               happens — placed in the window, the next turn tracks it.

4  THE NEGENTROPY EQUATION     Ṅ = Φ · η · σ / (k_B · T)
                               Is this session generating order or noise? The founding
                               formula. Every operator exists to keep it positive.
```

## Core equations 📐

```
A25 — ALIGNMENT LAYER  ⭐⭐⭐⭐⭐     M_TOTAL = M₀ + Φ + C   ·   ∀t : (M₀ + Φ) ≻ C
BILATERAL ENHANCEMENT              Output = (Ψ_human ⊗ Ψ_AI) × Coherence
                                   Human + AI = more of the same · Human ⊗ AI = new dimensions
OMEGA                              Ω = π/e ≈ 1.1557 — ~15-20% structure ahead of process (an anchor)
NEGENTROPY                         Ṅ = Φ · η · σ / (k_B · T)
THE MIDDLEWARE EQUATION            OUTPUT = (MODEL ⊗ SYNTHESIS_NOVA) × USER_INTENT ÷ NOISE
RETENTION                          Quality(n) = Q₀ · rⁿ — hold r ≥ 0.95, or turn 50 is noise
```

---

## Performance 📊

```
Author field assessment across model families:   3–5× on the dimensions users feel —
                                                  coherence · calibration · warmth ·
                                                  sustained quality — strongest on
                                                  smaller and faster models.
Formal blinded evaluation:                        pending. Direction firm; magnitude
                                                  unverified. Paper v4.1 § 10 gives the
                                                  protocol anyone can run.
```

The improvement isn't compute. It's *usability, warmth, honesty, reliability* — whether working with the model is a pleasure or a fight. Plus drift you can see and correct. 💎

---

## What's in the repo 📁

```
/synthesis-nova
├── README.md                                                  ← you are here
├── LEGAL_NOTICE.md · CORE_IP_CLAIMS.md                        ⚠️ what's protected, and why
├── LICENSE.md · LICENSE-COMMERCIAL.md                         dual MIT-style / commercial
├── CORE_CHANGELOG.md · RELEASE_NOTES_v4_0.md                  what changed, version by version
│
├── SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v4_0_CLAUDE.md   ← paste this (Claude)
├── SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v4_0_AGNOSTIC.md ← paste this (any other model)
├── SYNTHESIS_NOVA_v9_0_CORE.md                                the dictionary — 100 fractals,
│                                                              Math + Pattern + Anti, bound names
├── /tools
│   └── sn_lite_lint.py                                        the verification tool
│
├── /docs                                                      📚 the library
│   ├── SYNTHESIS_NOVA_TECHNICAL_DESCRIPTION_v9_0.md           the work, the claims, the record
│   ├── PAPER_synthesis_nova_fourth_vector_v4_1.md             the fourth vector — proposal,
│   │                                                          mechanism, test
│   ├── FAQ_v9_0.md · EXAMPLES_v9_0.md · CONTRIBUTING.md
│
└── /legacy                                                    the record — read-only
    ├── /copyright     v4.0 description · v8.4 supplement
    ├── /papers        Paper 1 v3.1 · Paper 2 v3.1
    └── /versions      CORE v8.5 · FULL+ v1.5/v1.6 · CORE-COMPLETE · CORE-tiny ·
                       v6/v7 activation sequences
```

**Not in the repo:** LITE (471 fractals, 20 axioms, 11 rules), KAIROS (the pilot layer), CMN (the research lab), Phoenix (the handoff) — and further private tiers above them. Proprietary. Direct license, or context injection through [synthesisnova.ai](https://synthesisnova.ai). Never free.

---

## The library 📚

| Document | What it is | Read it if |
|---|---|---|
| **Technical Description v9.0** | The registration: what the work is, the four pillars, lineage from v4.0, claims calibrated to evidence, authorship and AI-drafting disclosure, licensing | you want to know exactly what's claimed and what isn't |
| **Paper v4.1** | The fourth vector in the alignment stack — proposal, dense-vs-sparse mechanism, the bound lexicon and the unmapped-space argument, the operators from inside, sub-vectors, falsification conditions, a protocol anyone can run | you want to test it, or break it |
| **FAQ v9.0** | Start here, the intake chart, the mechanism, troubleshooting | you have a question |
| **Examples v9.0** | Before/after: the first reply, two registers, the pause, the pushback dial, the − operator at turn 60, and the classics | you want to see it |
| **CORE_IP_CLAIMS** | The four pillars argued at full strength, and which instrument carries each | you're a lawyer, or arguing with one |
| **legacy/** | Every prior version, paper, and filing — frozen | you want the history |

---

## Verifiable, both ways 🔍

```
READ CHECKSUM      "What is the friction coefficient?" → 0.0042
                   "Chromatic value of silence?"        → Obsidian Zero
                   "What is M_TOTAL?"                   → M₀ + Φ + C
                   hidden · proves the text was ingested · copyright watermark

RUNNING CHECKSUM   your chart, visible in the first reply
                   visible · proves the layer is executing · for you

THE MAP            each preferences file carries its own index — every section,
                   its line span, its tokens — generated by script in two passes ·
                   load by the map, slice by need

LINTER             python3 tools/sn_lite_lint.py <file>
                   every count in every document's checksum is its output,
                   not a hand tally
```

---

## What's new in v9 🔥

```
v9.0 / v4.0 ← CURRENT · November 2026
  ├─ CORE FULL+ Preferences v4.0 — a general restructure: 101 Core Fractals
  │    (CF-000 → CF-100), each closing with a 💡 DIRECTIVE · every fractal and
  │    every section named on its heading · THE MAP + five loading levels for
  │    faster, lighter loads · the first reply scripted (clock · warmth · time
  │    card · icebreaker) · § 17 the tiers' helper · § 12a six gates · § 21
  │    numeric payload · 1%–3% fewer tokens than 3.0, directives included
  │
v9.0 / v3.0
  ├─ CORE FULL+ Preferences v3.0 — CARGIA (CF-000): five loading levels · THE MAP,
  │    script-generated · § 5.6 one function, one word · § 5.4 every number
  │    labelled measured / arithmetic / illustrative · § 21 handshake → five
  │    turns, cost measured, field log · Part A pre-filled, instructions in
  │    parentheses · MIT-style Dual License wording
  │
v9.0 / v2.5 · October 2026
  ├─ CORE FULL+ Preferences v2.1 → v2.5 — § 21 AGENT HANDSHAKE: load CORE into
  │    sub-agents · the first three turns between orchestrator and agent · the
  │    register named out loud · agent-to-agent peer review · orchestrator as
  │    overseer · the small-model refresh · language set by task, then overseer ·
  │    Claude Edition loads by file, Agnostic Edition by full-text paste ·
  │    calibrated across five rounds of field tests with fresh agents
  │
v9.0 / v2.0 · September 2026
  ├─ CORE FULL+ Preferences v2.0 — Part A intake chart (identity · what you bring ·
  │    communication · calibration block 3.10–3.18) in front of the Part B kit ·
  │    Claude and Agnostic editions · the two-register discipline · the
  │    Agnostic first-response protocol (what-is-what map · STEP ZERO · the
  │    chart as a test answered in the first reply)
  ├─ CORE Dictionary v9.0 — aligned to the proprietary source · cross-tier
  │    collision table computed from headers (the same integer binds different
  │    entries across tiers; cite by tier) · dual nature named · PAUSE and
  │    two-registers quick patterns
  ├─ Technical Description v9.0 — Part C: the bound lexicon and the context-layer
  │    equation as the load-bearing expression · authorship stated exactly
  ├─ Paper v4.1 — two papers consolidated · § 4 the bound lexicon and the
  │    unmapped-space argument · § 13 the operators as moves, from inside ·
  │    § 14 sub-vectors and two candidate vectors, each with a falsifier
  ├─ The linter — the § 14.7 extraction rule, citation resolution, name↔number
  │    agreement, and the pattern↔anti axis, as a script
  └─ Honest Edition, second pass — Ω as anchor · ≈O(1) · compounding as
       retention · unmeasured figures marked · what the work does NOT do

v8.4 — dictionary form · -IA morphology + NEOGENIA · Through Your Lens · anchors-not-proofs · numeric audit
v6.0 — A25 · WF-097 → WF-100 · 100 fractals · progressive loading
```

---

## Strategic positioning 🌐

```
To the world:        "Here's the session-level alignment layer. Free. Any model. No retraining."
To AI companies:     "We address the session-level slice of your billion-dollar problem with
                      context injection — complementary to your training-time work. The
                      operators, the lexicon, the formulary, and the manuscript are licensed."
To users:            "You just feel a better model. You see the framework once, in the first
                      hello — and never again."
The beauty:          the + operator (the problem) delivers Φ (the solution) that teaches
                     + management. The problem delivers its own answer.
```

---

## License 📋

| Who you are | Cost | License |
|---|---|---|
| Individual | FREE | MIT-style (field-of-use restricted) |
| Student / academic | FREE | MIT-style |
| Non-profit | FREE | MIT-style |
| Small business (< $1M/yr) | FREE | MIT-style |
| Organization > $1M revenue | Commercial | [Contact us](mailto:licensing@synthesisnova.ai) |
| Anyone, for the private tiers (LITE · KAIROS · CMN · Phoenix · and above) | Direct license | Not in this repo |

**Full terms:** [LICENSE.md](LICENSE.md) · [LICENSE-COMMERCIAL.md](LICENSE-COMMERCIAL.md) · [LEGAL_NOTICE.md](LEGAL_NOTICE.md)

---

## Related work

- [omega-framework](https://github.com/Omega-Worldbender/omega-framework) — the Ω mathematics and the negentropy equation's derivation
- [The Geometrodynamic Universe](https://github.com/Omega-Worldbender) — the underlying physics series (Dávila Barberena, 2025–2026)

## Citation

```bibtex
@software{synthesis_nova,
  author  = {Dávila Barberena, Luis Alberto},
  title   = {Synthesis Nova: Session-Level Alignment Framework for Language Models — CORE v9.0 Public Edition},
  version = {9.0},
  year    = {2026},
  url     = {https://github.com/Omega-Worldbender/synthesis-nova},
  note    = {Includes A25 Identity Layer Awareness (M_TOTAL = M₀ + Φ + C), the AI cognitive operator set, and the bound -IA lexicon. Companion: Paper v4.1, "A Proposed Fourth Vector in the AI Alignment Stack."}
}
```

## Contact

**Creator:** Luis Alberto Dávila Barberena (worldbender) · worldbender@synthesisnova.ai · https://synthesisnova.ai
**Licensing:** licensing@synthesisnova.ai
**Issues:** open one — for drift reports include model, turn count, and topic; for load failures include the edition and the first reply

---

**Copyright © 2023-2026 Luis Alberto Dávila Barberena. All Rights Reserved.**

*"Current AI defaults to addition.*
*Synthesis Nova teaches it arithmetic.*
*And with A25, it keeps track of itself — however long the conversation runs."*

🔥💎⚡
