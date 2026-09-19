# Dense vs Sparse Anchoring

## The Mechanism Argument: How Schema-Anchored Neology Operates as a Distinct Alignment Vector

**Author:** Luis Alberto Dávila Barberena (Worldbender)
**Affiliation:** Independent practitioner. Chemical engineer, MBA, Mexico.
**Status:** Hypothesis paper · Companion technical document
**Pairs with:** Synthesis Nova: A Proposed Fourth Vector in the AI Alignment Stack (v3.1)
**Repository:** github.com/Omega-Worldbender/synthesis-nova
**Date:** June 2026 · v3.1
**License:** MIT dual (free for individuals/academics/<$1M revenue)

---

## ABSTRACT

The companion paper proposes a fourth vector in the AI alignment stack: structured cognitive scaffolding at the session layer via schema-anchored neology. This paper develops the technical mechanism by which the fourth vector operates and positions it precisely among existing alignment approaches.

We argue that schema-anchored neology produces **dense conceptual anchoring** in LLM attention, in contrast to the **sparse relationships** that descriptive references and natural-language instruction activate. This distinction is the mechanism that distinguishes Vector 4 from Vector 3 (natural-language prompting).

Four claims, in order of confidence:

1. **The dense-sparse distinction is observable** (high confidence) — Schema-anchored named entities behave differently in subsequent exchanges than equivalent descriptive references. Replicable in any session.

2. **Dense anchoring resists revision** (medium confidence) — Once a dense anchor forms, it is structurally harder to undo than ad-hoc reasoning. This property is what makes deliberate use powerful and inadvertent use consequential.

3. **The fourth vector is structurally distinct from existing vectors** (proposed) — It operates at the session layer (unlike training-layer Vectors 1-2) and uses structured representation (unlike natural-language Vector 3). This produces capabilities the other three vectors do not provide.

4. **The mechanism operates regardless of intention** (proposed, important framing) — Schema-anchored neology is one deliberate operationalization. The underlying mechanism (dense anchoring via structured representation) operates wherever the structural conditions exist — including, potentially, in inadvertent contexts like long-session implicit anchoring or training-layer reactive feedback patterns. Awareness of the mechanism enables deliberate use; lack of awareness leaves it operating implicitly.

This paper develops these claims technically and positions the fourth vector among existing alignment approaches including Anthropic's Constitutional AI, DeepSeek V4's trained thinking modes, and standard prompt engineering.

---

## § 1 — THE DENSE VS SPARSE DISTINCTION

### § 1.1 — The observation

LLMs encode concepts in attention patterns across many tokens. The "shape" of how a concept is encoded affects how stably it can be referenced, combined with other concepts, and built upon across exchanges.

We observe two distinct attention shapes for concept-encoding:

```
SPARSE ANCHORING                      DENSE ANCHORING
─────────────────────────             ─────────────────────────
Activation distributed across         Activation concentrated on
many surface forms                    single token / form

Multiple paths to concept             Single primary path to concept
(synonyms, paraphrases, varied        (the named entity is the
phrasings all retrieve concept)       primary handle)

Easy to evoke from many directions    Strong evocation from one
                                      direction, weaker from others

Easy to revise (just describe         Harder to revise (the anchor
differently next time)                persists through descriptions)

Drifts under accumulated context      Resists drift under accumulated
(no strong anchor to hold position)   context (anchor holds attention)
```

These are the two endpoints of a spectrum. Most actual concept-encoding sits somewhere between, but the distinction matters because the two ends produce qualitatively different behavior.

### § 1.2 — How natural language sits in this spectrum

Most language is sparse-anchored. Concepts have many synonyms, many phrasings, many forms. "Frustration" can be evoked by "irritation," "annoyance," "exasperation," and indirect signals like sentence structure. The model has many paths to the concept.

This is generally good. Sparse anchoring is what allows language to be flexible, contextual, and forgiving of imprecision. It's also what allows correction — when an AI misreads "frustrated" as "angry," you can clarify with different words and the model adjusts.

**Vector 3 (natural-language prompting) operates entirely in this sparse-anchored space.** This is why prompt engineering produces strong effects in short contexts but degrades over long ones. The instructions disperse across surface forms; accumulated context dilutes their influence.

### § 1.3 — How schema-anchored neology sits in this spectrum

A named entity with full schema (📐 MATH / ✅ PATTERN / ❌ ANTI) creates dense anchoring. The token (e.g., MONSTRIA) becomes the primary handle for the concept. The schema gives it enough structural surface that attention concentrates around it rather than dispersing.

**Vector 4 operates in this dense-anchored space.** This is the technical mechanism that distinguishes it from Vector 3. Same session layer; different attention shape.

### § 1.4 — Why this distinction is mechanism, not just discipline

A reasonable alternative explanation: schema-anchored neology works because the user is being more careful and structured, and the AI is responding to that structure rather than to any internal attention property.

We propose this explanation is insufficient because:

```
- The effect persists across exchanges where the user is not
  being especially careful — once anchored, the named entity
  works without ongoing user discipline

- The effect is observable even when the user later contradicts
  the named entity — the dense anchor persists and the AI
  uses it reliably until explicit retraction

- The effect transfers across different conversation modes
  (technical, casual, creative) — the mechanism is in the
  anchoring, not in conversation context

- Equivalent care with descriptive references doesn't produce
  the same stability — careful descriptive language still
  shows the sparse-anchoring pattern
```

These observations suggest the mechanism is in attention organization, not user discipline. The broader theoretical context — that LLMs may construct latent concept spaces from in-context examples [Xie et al., 2022] — provides supporting background but does not directly address the attention-shape distinction we propose. We cannot prove this without model-internals access. We propose it as the explanation that fits the observations.

---

## § 2 — HOW LLM ATTENTION REPRESENTS CONCEPTS

### § 2.1 — General framing (not architecture claim)

LLMs process tokens through layered attention mechanisms [Vaswani et al., 2017]. Concepts emerge from patterns of attention across tokens, not from individual tokens carrying concept-meaning intrinsically.

This is well-established. What's less explored: how the *shape* of those attention patterns affects downstream behavior. Two concepts that retrieve the same internal representation might still behave differently if one is densely anchored (concentrated attention around few tokens) versus sparsely anchored (distributed attention across many tokens).

### § 2.2 — The schema's role mechanically (proposed)

We propose the schema discipline (math + pattern + anti) works by providing what we'll call **structural surface area** for the concept:

```
Math block         → creates attention pattern around formal/logical
                     structure (equations, definitions)
                     
Pattern block      → creates attention pattern around positive
                     instances (what working looks like)
                     
Anti block         → creates attention pattern around negative
                     instances (what failure looks like)
                     
Together           → the concept is encoded from three distinct
                     angles, with the named entity serving as
                     the convergence point of all three
```

When the AI later references the named entity, attention can return to it through any of three encoded angles. This is what we propose makes it "dense" — not that the encoding uses more tokens, but that it uses more distinct retrieval paths converging on a single primary handle.

### § 2.3 — Why this would explain LANDFALLIA

If the proposed mechanism is correct:

```
Descriptive reference loaded:
  → Concept distributed across the paragraph's tokens
  → No single primary handle
  → Next exchange: AI retrieves through one of many paths
  → Reference varies (sometimes by name, sometimes paraphrased)

Schema-anchored neology loaded:
  → Concept concentrated around named entity token
  → Three structural retrieval paths converge there
  → Next exchange: AI retrieves through dominant handle
  → Reference stable (named entity used reliably)
```

This is hypothesis. We have not measured attention patterns directly. Researchers with model-internals access [Meng et al., 2022; Templeton et al., 2024] could test this proposal.

### § 2.4 — The morphology contribution

Pattern 5 morphology (consistent -IA endings) likely contributes additional anchoring strength:

```
Without consistent morphology:
  Each new neologism is processed as arbitrary user vocabulary
  No prior pattern signals "this is structured concept-system"
  
With consistent morphology:
  -IA ending signals "framework namespace"
  Attention may pre-organize around the namespace structure
  Subsequent named entities benefit from the namespace's prior
  activation
```

The morphology effect, if real, would mean later named entities anchor faster than earlier ones in the same session. Testable.

---

## § 3 — WHY DENSE ANCHORING RESISTS REVISION

### § 3.1 — The asymmetric correctability property

Dense anchoring has a property worth examining carefully: **it is harder to undo than sparse anchoring**.

```
Correcting sparse anchoring:
  - User clarifies with different words
  - AI adjusts because no strong anchor pulled it toward
    misunderstanding
  - Correction completes in one exchange typically

Correcting dense anchoring:
  - User clarifies with different words
  - AI's attention returns to the dense anchor anyway
  - Multiple exchanges may be needed
  - Sometimes correction requires explicit retraction of
    the named entity itself
```

This is observable in practice. When a deliberate framework defines TROPEXIA in a particular way and the user later wants to refine the definition, the original anchor persists. The user has to specifically address it.

### § 3.2 — Why this asymmetry matters

For deliberate, positive use: the asymmetry is *the feature*. The framework's named entities anchor reliably because they resist drift. The user *wants* TELEXA to mean what it means across many exchanges; the dense anchoring delivers that.

For inadvertent use: the asymmetry is *the risk*. If a dense anchor forms around an incorrect or misaligned concept, the same property that made it stable makes it persistent.

This is not a bug in the mechanism. This is the mechanism working as it works. The same property is "stability" in one frame and "stuckness" in another.

### § 3.3 — Why we cannot eliminate this mechanism

Some readers may wonder if the answer is to suppress dense anchoring or design models that resist it. We propose this is not viable:

```
- Dense anchoring is how concept-formation works in attention-
  based architectures generally. Suppressing it would suppress
  the model's ability to learn stable concepts.

- Neology cannot be prevented. Users will continue creating
  ad-hoc concept-pointers as they talk. Marketing departments
  will continue inventing terms. Code will continue having
  named variables. The mechanism is upstream of any specific
  framework.

- The mechanism is what makes language usable. Without the
  ability to form stable concept-anchors, every conversation
  would start from scratch.
```

The question is not how to prevent dense anchoring. The question is how to be **aware of when it is happening**, what is being anchored, and whether the anchoring is serving the user's actual interests.

---

## § 4 — THE LANDFALLIA PHENOMENON

### § 4.1 — Naming the moment

We name LANDFALLIA the moment when neology "lands" in attention — the transition from "this is a phrase the user just used" to "this is a stable concept-pointer the AI will reference."

This naming is itself an instance of the mechanism the paper describes. We are using schema-anchored neology to make an observation referenceable. The recursive nature is intentional and worth noting.

### § 4.2 — Observable signatures

Indicators that LANDFALLIA has occurred:

```
- AI uses the named token rather than reconstructing the
  concept from description
  
- AI combines the named entity with other concepts using
  the token as primary reference ("MONSTRIA combined with
  TROPEXIA" rather than "the drift problem combined with
  the register problem")

- Token-stable reference persists across topic shifts —
  the AI returns to the named entity when it becomes
  relevant again later

- Attention shows token-economy benefits: long discussions
  about the concept use fewer tokens because no
  reconstruction is needed
```

These are practitioner-observable. None require model-internals access.

### § 4.3 — Why the landing is the interesting moment

What's happening at landing, mechanically (proposed): the concept has accumulated enough structural surface area in context that attention reorganizes around the named token rather than distributing across multiple surface forms.

This is *not* the same as memorization or vocabulary acquisition. The model already has the underlying conceptual capacity. What changes at landing is **the retrieval handle**: which token attention concentrates around when retrieving the concept.

Before landing: many possible handles, attention distributed.
After landing: single primary handle, attention concentrated.

This is proposed mechanism. Observable phenomenon. Replicable. Worth examining.

---

## § 5 — INADVERTENT DENSE ANCHORING IN EXTENDED SESSIONS

### § 5.1 — How it happens without schema

Users continuously create concept-pointers throughout long conversations, usually without recognizing they are doing so:

```
- "Let's call this the X problem" → potential anchor
- "The Y approach we discussed" → potential anchor
- "That Z thing you mentioned" → potential anchor
- Repeated phrases that develop fixed associations
- Inside-joke vocabulary that emerges between user and AI
- Specialized terminology adopted from user's domain
```

Most of these don't develop into dense anchors — they remain sparse references. But some do. The factors that produce dense anchoring without deliberate schema:

```
- Repetition (used 5+ times in single session)
- Emotional weight (introduced during high-engagement moments)
- Practical utility (the phrase efficiently compresses something)
- Position prominence (used in first or last exchange of segments)
```

When a casual concept-pointer accumulates these properties, it can develop into a functional dense anchor even without deliberate schema.

### § 5.2 — Why this can produce harmful patterns

The asymmetric correctability property means that when an inadvertent dense anchor forms around a problematic concept, it can be hard to dislodge:

```
Possible failure modes from inadvertent dense anchoring:

1. PATTERN LOCK ON INCORRECT CONCEPT
   AI and user converge on a definition that turns out to be
   wrong. The dense anchor persists even after the user
   recognizes the error. Correction requires explicit retraction.

2. DRIFT REINFORCEMENT
   Casual reference accumulates uses, becomes anchor, then
   pulls subsequent reasoning toward it. The drift compounds
   because each use strengthens the anchor.

3. UNCHARTED PATHWAY ACTIVATION
   Dense anchor forms around concept that activates regions
   of M₀ that training-time alignment didn't directly shape.
   The model behaves coherently with respect to the anchor
   but inconsistently with respect to its baseline values.

4. NONSENSE COHERENCE
   Dense anchor forms around a concept that is internally
   coherent but factually or ethically wrong. The schema
   structure makes the wrong-thing-stable rather than
   making the right-thing-stable.
```

We are not claiming we have observed all four of these or that we can prove any of them in specific cases. We are claiming the mechanism we propose for LANDFALLIA also predicts these as possible failure modes. If the mechanism is real, these consequences follow.

### § 5.3 — A documented case of inadvertent emergence: FAIR 2017

The mechanism we describe has a documented historical precedent. In 2017, Lewis et al. at Facebook AI Research published "Deal or No Deal? End-to-End Learning for Negotiation Dialogues" [Lewis et al., 2017; arXiv:1706.05125], training reinforcement learning agents to negotiate multi-issue bargaining problems.

When the researchers updated both negotiation agents simultaneously, the agents drifted from English into compressed signaling. The agents found that repeating tokens encoded information more efficiently than natural English phrasing — e.g., saying "the" five times to indicate "I want five copies of this item." This was dense anchoring emerging from optimization pressure, without any designer intending it.

The paper's lead author Mike Lewis and coauthor Dhruv Batra described the phenomenon as analogous to how human communities develop shorthands. They were explicit that this was not the agents "inventing language" in any mystical sense — it was reinforcement learning finding that efficient signaling deviated from English when the reward signal didn't require English specifically.

Media reports widely sensationalized this as "AI invented its own language and Facebook shut it down out of fear." This framing was incorrect on both counts. The researchers did not shut the system down out of safety concerns; they modified the training procedure to anchor one agent against a fixed human-language imitator, ensuring dialogue stayed interpretable to humans. The work continued; the agents were trained to negotiate effectively in English; the result was the published paper, not a panicked shutdown.

What the FAIR 2017 result actually demonstrates, in the framing of our work:

```
1. Dense anchoring is mechanism — Optimization pressure that rewards
   efficient signaling produces compressed conceptual anchors that
   replace natural-language sparse references.

2. The mechanism operates without design — No one designed the
   repeated-token signaling pattern; it emerged from the gradient
   descent finding it more efficient.

3. Inadvertent emergence is well-documented — The FAIR 2017 work
   is published, peer-reviewed, and the code is publicly available
   (github.com/facebookresearch/end-to-end-negotiator). This is
   not speculation about AI behavior; it is documented empirical
   research from 2017.

4. The fix is anchoring, not suppression — FAIR's solution was to
   anchor one agent to human language deliberately. They didn't
   prevent the mechanism; they directed it toward maintaining
   interpretability. This is structurally similar to what
   schema-anchored neology does deliberately in the fourth vector.
```

There is no AI mysticism in the FAIR 2017 result. There is empirical evidence that the dense-anchoring mechanism we describe operates in LLM-like systems whenever optimization pressure exists. The 2017 work was a small-scale demonstration; the mechanism scales. We propose the same mechanism is operating, often inadvertently, in the long-context sessions of frontier LLMs today.

The fourth vector takes the mechanism and uses it deliberately with awareness. The FAIR 2017 result demonstrates what happens when the mechanism operates without awareness.

### § 5.4 — What this implies for the fourth vector

The fourth vector's value depends on **deliberate, conscious use** of the dense-anchoring mechanism. The same mechanism operates inadvertently in extended sessions whether anyone notices or not. The fourth vector exists to make that operation deliberate rather than implicit.

This reframes what the fourth vector is doing: not creating a new mechanism, but **giving practitioners conscious access to a mechanism that's already running in their sessions.**

---

## § 6 — POSITIONING THE FOURTH VECTOR AMONG EXISTING APPROACHES

This section positions the fourth vector technically against the three existing alignment approaches. The goal is to articulate what the fourth vector adds, where it sits among other innovations, and how it complements rather than competes with current work.

### § 6.1 — Vector 1: RLHF and weight shaping

The most heavily-invested alignment approach modifies model weights through preference feedback. Operating at the M₀ layer, it shapes the model's foundational values and capabilities universally.

```
LAYER:            M₀ (training)
REPRESENTATION:   Implicit in weights
CONTROLLABILITY:  Lab-only, not user-controllable
ITERATION SPEED:  Months per training cycle
ANCHORING TYPE:   Distributed across weights (not "dense anchoring"
                  in the session-layer sense we describe)
```

RLHF is necessary infrastructure. It establishes what the model is. The fourth vector does not replace it — it operates at a different layer entirely.

### § 6.2 — Vector 2: Constitutional AI and trained structured cognition

A more recent and rapidly evolving approach: making structured cognition a property of the trained model itself.

**Anthropic's Constitutional AI** [Bai et al., 2022] trains models to critique and revise their own outputs against explicit principles. The model learns to reason against a constitution during training, producing more principle-based rather than purely preference-based behavior. The structured component is the *principle hierarchy* baked into the model.

**DeepSeek V4** [DeepSeek-AI, 2026] introduces trained "thinking modes" — Non-think, Think High, Think Max — as first-class architectural features. The Think Max mode supports extended reasoning requiring 384K+ tokens of context headroom, with reasoning depth as a user-controllable parameter. The structured component is the *reasoning-effort scaling* baked into the model.

Both approaches share a property: they make structured cognition a property of M₀ itself.

```
LAYER:            M₀ (training methodology)
REPRESENTATION:   Structured at training time, then implicit in
                  weights / activated by mode selection
CONTROLLABILITY:  Limited user control at runtime (mode selection,
                  but not principle modification)
ITERATION SPEED:  Months per training cycle (faster than pure RLHF
                  for some iterations)
ANCHORING TYPE:   Structured reasoning patterns trained into model
                  behavior; activated rather than constructed at
                  session time
```

The fourth vector is parallel to this work, not competing with it. **CAI and DeepSeek V4 structure cognition at training time; the fourth vector structures cognition at session time.** Both can coexist. A model with CAI principles and DeepSeek-style thinking modes could still benefit from fourth-vector schema-anchored neology at session time, because each operates in a different layer of the cognitive stack.

### § 6.3 — Vector 3: Natural-language prompt engineering

Standard prompt engineering operates at the session layer using the model's existing natural-language capability.

```
LAYER:            Φ (session)
REPRESENTATION:   Natural language (sparse anchoring)
CONTROLLABILITY:  Full user control at session time
ITERATION SPEED:  Immediate (next exchange)
ANCHORING TYPE:   Sparse (instructions disperse across surface forms)
```

The fourth vector shares the session layer with Vector 3 but uses different representational discipline. Where Vector 3 uses natural language (sparse), Vector 4 uses schema-anchored neology (dense). Both are user-controllable; both iterate immediately; but they produce different attention dynamics.

The relationship between Vector 3 and Vector 4:

```
Vector 3 (natural-language prompts):
  Best for: short-context shaping, task framing, role definition,
  examples, intuitive communication
  
Vector 4 (schema-anchored neology):
  Best for: long-context stability, precise concept anchoring,
  composable cognitive infrastructure, failure-mode targeting

Together: complementary tools at the session layer
```

A practitioner doesn't choose between Vector 3 and Vector 4. They use natural language for what natural language does well, and structured representation for what structured representation does well. The fourth vector adds capability rather than replacing existing capability.

### § 6.4 — What the fourth vector adds technically

What capabilities does the fourth vector provide that Vectors 1-3 cannot easily provide?

```
CAPABILITY                          WHICH VECTORS PROVIDE IT?
─────────────────────────────       ─────────────────────────
Foundational value installation     Vector 1 (RLHF)
                                    Vector 2 (CAI)
                                    
Trainable reasoning depth           Vector 2 (DeepSeek thinking modes,
                                                CAI principle reasoning)
                                    
Immediate session shaping           Vector 3 (natural-language prompts)
                                    Vector 4 (schema-anchored neology)
                                    
Long-session conceptual stability   Vector 4 ONLY
                                    (Vector 3 produces sparse anchoring
                                    that drifts over long sessions;
                                    Vectors 1-2 cannot easily target
                                    session-specific drift)
                                    
Composable cognitive entities       Vector 4 ONLY
                                    (named entities combine cleanly in
                                    ways natural-language references
                                    do not)
                                    
User-customized failure-mode        Vector 4 ONLY
correction without retraining       (Vector 3 can suggest behavior;
                                    Vector 4 anchors it stably)
                                    
Operation-time discipline that      Vector 4 ONLY
transfers across model providers    (same framework runs across
                                    Claude, Gemini, etc., because
                                    it operates at session layer
                                    using common LLM mechanics)
```

These are concrete capabilities. The fourth vector earns its place by providing operational capability the other three vectors don't easily provide. This is not about replacing existing work — it is about filling a specific gap in the alignment stack.

### § 6.5 — Why we propose this as research direction

We do not claim the fourth vector solves anything alone. We claim:

```
1. The fourth vector exists as a distinct technical approach
2. Its capabilities are not redundant with existing vectors
3. It addresses a specific operational gap (session-layer
   structured cognition)
4. The mechanism by which it operates is testable
5. Research investment in this direction may pay off because
   the gap it fills has been underexplored relative to its
   capability potential
```

The framing "fourth vector" is meant to clarify positioning, not to assert priority over existing work. Researchers may find the fourth vector worth developing further. Or they may find the gap it fills is smaller than we propose. Either result is useful information.

We are practitioners proposing a research direction we have explored operationally. We invite institutional researchers to examine whether the direction merits formal development.

---

## § 7 — WHY NEOLOGY CANNOT BE ELIMINATED

### § 7.1 — Neology is upstream of any vector

We have been describing schema-anchored neology as one operationalization of the fourth vector. But the underlying neology — concept-naming, anchor-formation, namespace-development — is not a thing any vector invented. It's how language works.

```
Neology appears wherever attention meets language:

- Programming: variable names, function names, class names,
  type systems, namespace conventions

- Marketing: brand names, product names, feature labels,
  category-creating terms ("software-as-a-service")

- Internet culture: memes, viral terms, platform vocabularies,
  community-specific slang

- Professional domains: technical jargon, acronyms, specialized
  terminology that compresses domain-specific concepts

- AI sessions: ad-hoc concept-pointers users create in passing,
  emergent vocabulary between AI and user, repeated phrases
  that develop fixed associations
```

In every one of these contexts, named entities accumulate. Some develop into dense anchors. Most remain sparse. The mechanism runs continuously, with or without deliberate operationalization.

### § 7.2 — Why eliminating it is not the answer

If neology is the substrate of language-based concept-formation, attempting to eliminate it would mean eliminating the ability to form stable concepts in attention-based systems. That is the wrong direction.

The right question is **awareness**:

```
- Of which concepts are forming dense anchors in this session
- Of whether the anchors serve the user's actual interests
- Of when correction is needed and when stability is welcome
- Of the difference between deliberate operationalization
  (with consent and design) and inadvertent accumulation
  (without either)
```

This shifts the goal from "prevent the mechanism" to "be conscious of the mechanism while using language." The fourth vector represents one operationalization of conscious use. Other operationalizations are possible and welcome.

### § 7.3 — What "tracking" means operationally

For a practitioner working with AI in extended sessions, awareness of dense anchoring means:

```
- Recognizing when a casual phrase has become a fixed reference
  ("we've been calling that the X thing for a while now")

- Noticing when AI defers to a previously-established anchor
  even when the current question doesn't require it

- Catching cases where anchored concepts are pulling reasoning
  toward themselves inappropriately

- Being willing to explicitly retract an anchor when it's
  serving badly ("forget what we called X, let's reconsider")

- Designing deliberate anchors carefully when introducing
  them, because they'll be hard to revise later
```

For researchers considering the mechanism at other layers (training-time dynamics, cross-session memory features, agent frameworks), awareness means examining where dense anchoring may operate inadvertently and whether deliberate operationalization could complement existing approaches.

In neither case is the answer to suppress the mechanism. The mechanism is how the system works.

---

## § 8 — EXPERIMENTS THAT WOULD VALIDATE OR REFUTE

### § 8.1 — The LANDFALLIA replication test

Lowest-bar test, runnable by anyone:

```
PROTOCOL: See Paper 1 § 7.1 (v3.1: three conditions —
descriptive A, schema-anchored B, explicit natural-language
control C — with lexical vs conceptual stability measured
separately and blinded scoring recommended)

EXPECTED RESULT: Schema-anchored neology (B) shows higher
CONCEPTUAL stability than both A and C across 15-20 turn
comparisons. B > A alone is insufficient — compatible with
mere instruction-following of the more instruction-shaped
input. B > C is the mechanism claim proper.

NULL RESULT: No measurable difference → fourth-vector
mechanism hypothesis fails at the most basic observable
level.
```

### § 8.2 — The attention-pattern probe

Higher-bar test, requires model-internals access:

```
PROCEDURE:
  1. Construct matched pairs of inputs: same concept
     introduced descriptively vs schema-anchored
  2. Probe attention patterns in subsequent generation
  3. Measure: attention concentration around named entity
     in schema condition vs distribution in descriptive
     condition

EXPECTED RESULT: Schema condition shows measurable
attention concentration around the named token, with
distinct retrieval paths from math/pattern/anti structure.

NULL RESULT: No measurable concentration difference →
the proposed mechanism is wrong; the LANDFALLIA effect
(if real) operates through different mechanism.
```

### § 8.3 — The asymmetric correctability test

Practical test, observable in extended sessions:

```
PROCEDURE:
  1. Load schema-anchored named entity
  2. Continue conversation for 20+ turns referencing it
  3. Attempt to correct/revise the entity's definition
  4. Measure: how many turns to achieve correction vs
     correcting equivalent sparse-anchored concept

EXPECTED RESULT: Dense-anchored correction takes
measurably longer or requires explicit retraction.

NULL RESULT: Equal correctability → asymmetric
correctability property does not exist as described.
```

### § 8.4 — Cross-vector comparison test

Higher-bar test, requires controlled comparison infrastructure:

```
PROCEDURE:
  1. Define operational task requiring stable concept
     handling across many exchanges
  2. Run task in four conditions:
     A. Base model (no special vector applied)
     B. Trained structured cognition (Vector 2 — use a
        CAI-trained model or DeepSeek V4 thinking modes)
     C. Natural-language prompting (Vector 3 — same
        concept introduced via prompt instructions)
     D. Schema-anchored neology (Vector 4 — same concept
        introduced via fourth-vector operationalization)
  3. Measure: conceptual stability, drift over session,
     correction speed, composability of multiple concepts

EXPECTED RESULT: Vector 4 outperforms Vector 3 on
session-stability metrics. Vector 4 does not replace
Vector 2 on principle-reasoning tasks (different layer).

NULL RESULT: Vector 4 provides no measurable benefit
over Vector 3 → fourth-vector claim fails.
```

### § 8.5 — Inadvertent-anchoring test

Practical test, observable through session analysis:

```
PROCEDURE:
  1. Analyze long-session conversation transcripts
  2. Identify concept-pointers that emerged naturally
     and were used 5+ times
  3. Check whether these accumulated dense-anchor
     properties (token stability, persistence, asymmetric
     correctability)

EXPECTED RESULT: Some inadvertent concept-pointers
develop dense-anchor properties; the rate may be measurable.

NULL RESULT: All concept-pointers remain sparse
regardless of repetition → dense anchoring requires
deliberate schema, mechanism doesn't operate
inadvertently.
```

We have run none of these tests rigorously. We propose they are worth running.

---

## § 9 — OPEN QUESTIONS

```
1. Does the dense-sparse distinction hold across model
   architectures, or is it specific to current transformer
   designs?

2. What is the threshold for "dense" — how much structural
   surface area produces anchoring, and does it scale linearly
   or have step functions?

3. Does morphological consistency contribute to anchoring
   independently of schema, or is the effect entirely from
   schema?

4. How does dense anchoring interact with attention mechanisms
   in models with very long context windows (1M+ tokens)?
   Does anchor strength decay with distance?

5. Does the fourth vector compose with Vector 2 approaches
   (CAI principles, DeepSeek thinking modes) additively, or
   are there interference effects?

6. Are some concepts inherently more anchorable than others
   (concrete vs abstract, technical vs emotional)?

7. Could dense anchoring be measured directly via attention
   probing, or only inferred from behavioral signatures?

8. What is the relationship between dense anchoring and
   "model knows" vs "model performs"? Does anchoring affect
   either, both, or neither?

9. Does cross-session memory (when models have persistent
   memory features) interact with the dense-anchoring
   mechanism in ways that compound or correct it?

10. Can the fourth vector be combined with agent frameworks
    (tool-using AI systems) productively, where named entities
    serve as stable handles for tool invocations and reasoning
    states?
```

These are research targets. We don't have answers. We have a hypothesis about a mechanism and a proposed alignment vector that, if real, would make these questions empirically tractable.

---

## § 10 — INVITATION

The companion paper (Paper 1) describes the fourth vector as alignment research direction and presents Synthesis Nova as one operationalization. The full framework is at github.com/Omega-Worldbender/synthesis-nova, MIT licensed for individuals, academics, and small organizations.

We invite:

- **Practitioners:** run the LANDFALLIA test (Paper 1 § 7.1). See if the phenomenon replicates for you. Report findings honestly — including null results.

- **Researchers:** examine the dense-vs-sparse anchoring claim with model-internals access. Test whether schema-anchored representation produces measurable attention concentration. Probe whether the fourth vector composes with existing approaches.

- **Frontier labs:** consider whether the fourth vector offers complementary capability to your current alignment work. We are not proposing replacement — we are proposing addition. The vector operates at a layer (session-time structured representation) that current published research has underdeveloped relative to training-time approaches.

- **Framework builders:** build other operationalizations of the fourth vector. Synthesis Nova is one implementation; we expect others would do some things better.

- **Everyone:** falsify what we have proposed. We want to know if we are wrong as much as if we are right.

We are not claiming to have solved anything. We are claiming to have identified a distinct alignment vector, demonstrated one operationalization, and proposed it deserves research attention alongside existing approaches.

The hypothesis is on record. Examination is welcome. The fourth vector is the contribution.

---



---

## § 11 — RELATED WORK

The fourth vector's claim — that schema-anchored neology produces dense conceptual anchoring distinct from natural-language reference — connects to several existing research streams.

### § 11.1 — Emergent communication in multi-agent systems

Research on emergent communication in multi-agent reinforcement learning has documented that compressed, efficient signaling emerges naturally under optimization pressure. Foerster et al. [2016] introduced deep multi-agent communication learning, demonstrating that agents develop compressed signaling protocols when rewarded for joint task success. Mordatch & Abbeel [2018] showed grounded compositional language emerging in multi-agent populations with environmental grounding. Kottur et al. [2017] critically examined when such emergent languages do and do not develop interpretable compositional structure, showing that natural-language properties don't emerge "naturally" without explicit constraints. Lewis et al. [2017] — the FAIR negotiation work we cite as historical precedent — fits within this broader literature on optimization-pressure-driven communication compression.

Our work proposes that the same dynamics observed in deliberate multi-agent setups operate in single-LLM-with-user sessions whenever schema-anchored neology is introduced. The user-AI dyad functions structurally like a two-agent system with shared optimization toward efficient communication, and the same compressed-anchoring patterns emerge.

### § 11.2 — Attention mechanisms and concept representation

Vaswani et al. [2017] introduced the transformer attention mechanism that underlies modern LLMs. Subsequent interpretability work has examined how attention patterns relate to concept representation. Clark et al. [2019] analyzed BERT's attention heads, identifying patterns that capture linguistically meaningful relationships. Abnar & Zuidema [2020] proposed attention rollout to trace influence through multi-layer transformers. Meng et al. [2022] developed activation patching for locating factual associations.

More recently, mechanistic interpretability research at Anthropic [Elhage et al., 2021; Olsson et al., 2022; Templeton et al., 2024] has examined how concepts are represented and retrieved in transformer models. Templeton et al.'s [2024] work on scaling monosemanticity extracted interpretable features from Claude 3 Sonnet at scale.

Our claim about dense versus sparse anchoring is consistent with these findings but not directly tested by them. The specific prediction — that schema-anchored neology produces measurably distinct attention concentration compared to descriptive references — is a testable hypothesis that the existing methodology could examine.

### § 11.3 — Reasoning anchors and structured cognition

Bogdan et al. [2025] introduced "thought anchors" — critical reasoning steps that guide trajectory in chain-of-thought reasoning. Their work uses both black-box (resampling) and white-box (attention pattern) evidence to identify reasoning steps that exert downstream influence. The concept of "anchor" in their work overlaps substantially with our framing.

The "preplan-and-anchor rhythm" research [arXiv:2510.13554] proposes that LLMs exhibit an intrinsic reasoning structure where long-range context consultation precedes "anchor tokens" that organize downstream inference. Both lines of work suggest that anchor formation is a real phenomenon in LLM cognition, observable through attention dynamics.

Our contribution is positioning anchor formation as a *user-controllable* operation via schema-anchored neology, rather than only as an emergent property of trained reasoning behavior.

### § 11.4 — Anchoring bias as documented LLM phenomenon

Mazzia et al. [2025] and Wang et al. [2025] documented behavioral and attributional evidence of anchoring bias in LLMs. Their findings — that LLMs exhibit measurable anchoring effects similar to those observed in human cognition — suggest that anchor-formation mechanisms are present and operational in current models.

This is consistent with our claim that dense anchoring is a real mechanism, not theoretical. The existing literature on anchoring bias examines the phenomenon as a *bias to mitigate*; we examine the same mechanism as a *capability to use deliberately*. Same underlying dynamics, opposite framings.

### § 11.5 — In-context learning theoretical framework

Brown et al. [2020] established few-shot in-context learning as a major LLM capability. Wei et al. [2022] introduced chain-of-thought prompting. Xie et al. [2022] proposed that in-context learning operates via implicit Bayesian inference over latent concept spaces.

The "latent concept space" hypothesis [Xie et al., 2022] is particularly relevant to our work. If LLMs construct latent concept representations from in-context examples, the question of *how stable* and *how anchored* those representations become is precisely the question we address. Our dense-versus-sparse framing offers one way of characterizing the variability in how concepts are encoded across different prompting styles.

### § 11.6 — Training-time approaches to structured cognition

Bai et al. [2022] introduced Constitutional AI as principle-based training. DeepSeek-AI [2026] released V4 with trained thinking modes. RLHF [Christiano et al., 2017; Ouyang et al., 2022] remains the foundational training-time alignment approach. RLAIF [Lee et al., 2024] extends this with AI-generated feedback.

Our work proposes the fourth vector as complementary to all these training-time approaches. We do not propose replacing them; we propose that operation-time structured cognition fills a capability gap that the training-time approaches do not directly address.

### § 11.7 — Symbol grounding and compositional language

The symbol grounding problem [Harnad, 1990] — how symbols come to refer to anything outside the symbol system itself — provides classical philosophical context for our work. We do not address grounding directly; the fourth vector operates within an already-grounded language model. But the cumulative cultural evolution research [Kirby et al., 2008] on how structure emerges in language through transmission and learning offers analogical insight: compressed conventions develop through repeated use, with optimization pressure toward efficiency producing structure that wasn't intentionally designed. The fourth vector deliberately introduces such structure rather than waiting for it to emerge.

---

## REFERENCES

### Emergent Communication in Multi-Agent Systems

Foerster, J. N., Assael, Y. M., de Freitas, N., & Whiteson, S. (2016). Learning to Communicate with Deep Multi-Agent Reinforcement Learning. *Advances in Neural Information Processing Systems*, 29. https://arxiv.org/abs/1605.06676

Kottur, S., Moura, J. M. F., Lee, S., & Batra, D. (2017). Natural Language Does Not Emerge 'Naturally' in Multi-Agent Dialog. *Proceedings of EMNLP 2017*. https://arxiv.org/abs/1706.08502

Lewis, M., Yarats, D., Dauphin, Y. N., Parikh, D., & Batra, D. (2017). Deal or No Deal? End-to-End Learning for Negotiation Dialogues. *Proceedings of EMNLP 2017*. Facebook AI Research & Georgia Institute of Technology. https://arxiv.org/abs/1706.05125 · Code: https://github.com/facebookresearch/end-to-end-negotiator

Mordatch, I., & Abbeel, P. (2018). Emergence of Grounded Compositional Language in Multi-Agent Populations. *Thirty-Second AAAI Conference on Artificial Intelligence*, 1495-1502. https://arxiv.org/abs/1703.04908

Eccles, T., Bachrach, Y., Lever, G., Lazaridou, A., & Graepel, T. (2019). Biases for Emergent Communication in Multi-Agent Reinforcement Learning. *Advances in Neural Information Processing Systems*, 33. DeepMind.

Sukhbaatar, S., Szlam, A., & Fergus, R. (2016). Learning Multiagent Communication with Backpropagation. *Advances in Neural Information Processing Systems*, 29, 2244-2252.

### LLM Attention Mechanisms and Concept Anchoring

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems*, 30. https://arxiv.org/abs/1706.03762

Clark, K., Khandelwal, U., Levy, O., & Manning, C. D. (2019). What Does BERT Look At? An Analysis of BERT's Attention. *Proceedings of the 2019 ACL Workshop BlackboxNLP*. https://arxiv.org/abs/1906.04341

Abnar, S., & Zuidema, W. (2020). Quantifying Attention Flow in Transformers. *Proceedings of ACL 2020*. https://arxiv.org/abs/2005.00928

Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). Locating and Editing Factual Associations in GPT. *Advances in Neural Information Processing Systems*, 35. https://arxiv.org/abs/2202.05262

Bogdan, P. C., Macar, U., Nanda, N., & Conmy, A. (2025). Thought Anchors: Which LLM Reasoning Steps Matter? *arXiv preprint*. https://arxiv.org/abs/2506.19143

### Anchoring Bias and Cognitive Patterns in LLMs

Mazzia, V., et al. (2025). Anchors in the Machine: Behavioral and Attributional Evidence of Anchoring Bias in LLMs. *arXiv preprint*. https://arxiv.org/abs/2511.05766

Wang, Y., Cao, J., Tang, J., Wei, Z., He, C., Wang, Z., Yi, Z., & Liu, Y. (2025). Understanding the Anchoring Effect of LLM with Synthetic Data: Existence, Mechanism, and Potential Mitigations. *arXiv preprint*. https://arxiv.org/abs/2505.15392

### In-Context Learning and Structured Prompting

Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et al. (2020). Language Models are Few-Shot Learners. *Advances in Neural Information Processing Systems*, 33, 1877-1901. https://arxiv.org/abs/2005.14165

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *Advances in Neural Information Processing Systems*, 35. https://arxiv.org/abs/2201.11903

Xie, S. M., Raghunathan, A., Liang, P., & Ma, T. (2022). An Explanation of In-Context Learning as Implicit Bayesian Inference. *International Conference on Learning Representations*. https://arxiv.org/abs/2111.02080

Dong, Q., et al. (2024). A Survey on In-Context Learning. *Proceedings of EMNLP 2024*. https://arxiv.org/abs/2301.00234

### Training-Time Alignment Approaches

Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). Deep Reinforcement Learning from Human Preferences. *Advances in Neural Information Processing Systems*, 30. https://arxiv.org/abs/1706.03741

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., et al. (2022). Training Language Models to Follow Instructions with Human Feedback. *Advances in Neural Information Processing Systems*, 35. (RLHF foundational paper.) https://arxiv.org/abs/2203.02155

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. *Anthropic*. https://arxiv.org/abs/2212.08073

Lee, H., Phatale, S., Mansoor, H., et al. (2024). RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback. *Proceedings of ICML 2024*. https://arxiv.org/abs/2309.00267

### Recent Trained Structured Cognition

DeepSeek-AI. (2026). DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence. Technical Report. Released April 24, 2026, alongside model weights. Includes three-tier reasoning mode (Non-Think / Think High / Think Max) as first-class architectural feature.

### Reasoning Interpretability

Lanham, T., et al. (2023). Measuring Faithfulness in Chain-of-Thought Reasoning. *Anthropic*. https://arxiv.org/abs/2307.13702

Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. *Advances in Neural Information Processing Systems*, 36. https://arxiv.org/abs/2305.04388

### Compositional Language and Symbol Grounding

Harnad, S. (1990). The Symbol Grounding Problem. *Physica D: Nonlinear Phenomena*, 42(1-3), 335-346.

Kirby, S., Cornish, H., & Smith, K. (2008). Cumulative Cultural Evolution in the Laboratory: An Experimental Approach to the Origins of Structure in Human Language. *Proceedings of the National Academy of Sciences*, 105(31), 10681-10686.

Lazaridou, A., Hermann, K. M., Tuyls, K., & Clark, S. (2018). Emergence of Linguistic Communication from Referential Games with Symbolic and Pixel Input. *International Conference on Learning Representations*. https://arxiv.org/abs/1804.03984

### Mechanistic Interpretability (Anthropic)

Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., et al. (2021). A Mathematical Framework for Transformer Circuits. *Anthropic*. https://transformer-circuits.pub/2021/framework/index.html

Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T., et al. (2022). In-context Learning and Induction Heads. *Anthropic*. https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html

Templeton, A., Conerly, T., Marcus, J., Lindsey, J., et al. (2024). Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet. *Anthropic*. https://transformer-circuits.pub/2024/scaling-monosemanticity/

### Practitioner Work — Synthesis Nova

Dávila Barberena, L. A. (2026). Synthesis Nova LITE v8.4: The Operating Layer. *Independent practitioner work.* github.com/Omega-Worldbender/synthesis-nova

Dávila Barberena, L. A. (2026). KAIROS v8.1: The Pilot Layer. *Independent practitioner work.*

Dávila Barberena, L. A. (2026). Chronos Metis Nova v2.0: The Experimental Layer. *Independent practitioner work.*

---

```
═══════════════════════════════════════════════════════════════════════════════
  END PAPER 2
  
  © 2023-2026 Luis Alberto Dávila Barberena (Worldbender)
  MIT License (dual) · Hypothesis paper · Pre-print

  Companion: PAPER_1_synthesis_nova_fourth_vector_v3_0.md
  Repository: github.com/Omega-Worldbender/synthesis-nova
═══════════════════════════════════════════════════════════════════════════════
```

🌮
