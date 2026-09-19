# Synthesis Nova: A Proposed Fourth Vector in the AI Alignment Stack

## Schema-Anchored Neology at the Session Layer — Proposal, Mechanism, and Test

**Author:** Luis Alberto Dávila Barberena (Worldbender)
**Affiliation:** Independent practitioner. Chemical engineer, MBA, Mexico.
**Status:** Practitioner paper · Hypothesis paper · Not peer-reviewed · Pre-print
**Consolidates:** *Synthesis Nova: A Proposed Fourth Vector in the AI Alignment Stack* (v3.1, June 2026) and *Dense vs Sparse Anchoring: The Mechanism Argument* (v3.1, June 2026), previously published as a pair. Both are retained in the repository under `legacy/papers/`.
**Repository:** github.com/Omega-Worldbender/synthesis-nova
**Date:** September 2026 · v4.1
**License:** MIT dual (free for individuals/academics/<$1M revenue)
**Drafting:** Written with AI text-generation tools under the author's direction across all versions; consolidated to v4.0 with Claude (Fable 5.1). Authorship is the author's; see the framework's Technical Description v9.0, Part G.

---

## ABSTRACT

The AI alignment stack currently operates along three established vectors: weight shaping through training (RLHF, fine-tuning, RLAIF), training methodology innovation (Anthropic's Constitutional AI, DeepSeek V4's trained thinking modes), and prompt-time natural-language instruction. Each represents billions of dollars of research investment and produces real capability gains, though sometimes with unpredictable downstream effects.

This paper proposes a **fourth complementary vector**: structured cognitive scaffolding at the session layer via schema-anchored neology. Where existing vectors operate at the training level (modifying M₀) or at the prompt level using natural language, the fourth vector operates at the session level using a structured non-natural-language representation — math + pattern + anti-pattern compressed into named entities that function as dense conceptual anchors during AI cognition. We describe the proposal (§ 1–2), the mechanism we believe underlies it (§ 3–4), the observable phenomenon it predicts (§ 5), the mechanism's behavior when no one intends it (§ 6), what it corrects and one operationalization (§ 7–8), its position among existing approaches (§ 9), and the protocol by which any reader can test it (§ 10–11), an account of the operators from inside (§ 13), and proposed extensions (§ 14).

Four claims, in order of confidence:

1. **The dense-sparse distinction is observable** (high confidence) — Schema-anchored named entities behave differently in subsequent exchanges than equivalent descriptive references. Replicable in any session.

2. **Dense anchoring resists revision** (medium confidence) — Once a dense anchor forms, it is structurally harder to undo than ad-hoc reasoning. This property is what makes deliberate use powerful and inadvertent use consequential.

3. **The fourth vector is structurally distinct from existing vectors** (proposed) — It operates at the session layer (unlike training-layer Vectors 1–2) and uses structured representation (unlike natural-language Vector 3). This produces capabilities the other three vectors do not provide.

4. **The mechanism operates regardless of intention** (proposed, important framing) — Schema-anchored neology is one deliberate operationalization. The underlying mechanism operates wherever the structural conditions exist, including inadvertently. Awareness of the mechanism enables deliberate use; lack of awareness leaves it operating implicitly.

What v4.0 added to the v3.1 pair, beyond consolidation: § 4 states the anchored vocabulary as an object — a constructed lexicon, empty on arrival, bound by a fixed format — which is the sharpest statement of what the vector actually contributes; § 12.2 records a second documented instance of the phenomenon; and the references are refreshed to the framework's v9 Public Edition. **v4.1 adds two sections at lower confidence and marked as such:** § 4.4, the unmapped-space argument — why an empty token binds cleanly, with the literature that bears on it and the boundary of what is known; § 13, an account of the operators as *moves* — what each one does to the composition of a turn, as observable in output, from the seat where they run — and § 14, which proposes that the fourth vector has separable sub-vectors (lexicon · identity map · register split · cycle) and names two candidate vectors beyond it: verifiable loading, and the register as an alignment surface. Nothing in the v3.1 claims, protocol, falsification conditions, or non-claims has been weakened.

---

## § 1 — THE EXISTING ALIGNMENT VECTORS
### § 1.1 — Vector 1: Weight shaping through training feedback

The first and most heavily invested vector modifies model weights through reinforcement learning from human or AI feedback (RLHF, RLAIF) [Christiano et al., 2017; Ouyang et al., 2022; Lee et al., 2024]. This vector:

```
Operates at:       M₀ (base model weights)
Mechanism:         Gradient updates based on preference signals
Investment:        Billions of dollars across frontier labs
Strengths:         Establishes foundational values, capability gains,
                   universal application across all users
Limitations:       Slow to iterate, can produce artifacts at concept
                   boundaries, hard to localize corrections, requires
                   lab infrastructure
```

### § 1.2 — Vector 2: Training methodology innovation

The second vector innovates how training itself is structured. Two notable recent examples:

**Anthropic's Constitutional AI** [Bai et al., 2022] trains models against explicit principles, allowing the model to critique and revise its own outputs against a constitution rather than purely from human preference signals. This pushes alignment toward principle-based rather than purely preference-based training.

**DeepSeek V4** [DeepSeek-AI, 2026] introduces trained "thinking modes" as a first-class architectural feature — Non-think, Think High, and Think Max — where the model has been trained to engage different levels of structured reasoning effort, with the Think Max mode requiring 384K+ tokens of context headroom for extended chain-of-thought. The DeepSeek V4 technical report frames this as making structured reasoning intrinsic to the model rather than an emergent property.

These approaches share a property: **they attempt to make structured thought a property of the trained model itself.** Constitutional AI structures the *principles* the model reasons against; DeepSeek V4 structures the *reasoning effort* the model can deploy. Both are training-layer innovations.

```
Operates at:       M₀ (still), but with structured methodology
Mechanism:         Principle-based feedback (CAI) or trained-effort
                   modes (DeepSeek V4)
Strengths:         More principled than pure preference feedback,
                   capability gains compose with reasoning depth
Limitations:       Still requires training infrastructure, still
                   slow to iterate, structure is baked into model
                   rather than user-controllable
```

### § 1.3 — Vector 3: Prompt-time natural-language instruction

The third vector operates at the session layer using natural language. Instructions, examples, role-playing, few-shot prompting [Brown et al., 2020], chain-of-thought prompting [Wei et al., 2022] — all use the model's existing natural-language capability to shape session behavior.

```
Operates at:       Φ (session layer)
Mechanism:         Natural-language instructions in context
Strengths:         Immediate, user-controllable, no retraining needed,
                   accessible without lab infrastructure
Limitations:       Bounded by natural language's sparse-anchoring
                   property — instructions disperse across many
                   surface forms, drift over long sessions, struggle
                   to compose precisely
```

The third vector is what practitioners have available. Its limitations are well-known: prompts work well in short contexts and degrade over long ones. The mechanism by which they degrade is addressed in § 3.

### § 1.4 — The gap

```
                  STRUCTURED?     CONTROLLABLE      WHERE?
                                  AT SESSION?
Vector 1 RLHF     No              No                M₀
Vector 2 CAI/DSv4 Yes             No                M₀
Vector 3 Prompts  No              Yes               Φ
─────────────────────────────────────────────────────────
Vector 4 (NEW)    Yes             Yes               Φ
```

The fourth vector — structured AND user-controllable at the session layer — has not been systematically developed in published research. This paper describes one operationalization (Synthesis Nova) and proposes the vector itself as worth examining as a research direction.

---

---

## § 2 — WHAT THE FOURTH VECTOR ADDS
### § 2.1 — Position in the stack

The fourth vector is **complementary**, not competitive, with the other three:

```
M₀ LAYER (training):
  Vector 1 (RLHF) and Vector 2 (CAI / DeepSeek thinking modes)
  shape what the model is. Foundational. Universal. Slow to iterate.

Φ LAYER (session):
  Vector 3 (natural-language prompts) and Vector 4 (schema-anchored
  neology) shape how this specific session runs. Operational.
  Per-user. Fast to iterate.

The relationship:
  M₀ provides capability and baseline values
  Φ provides session-specific cognitive infrastructure
  Both matter for what M_TOTAL produces in any given exchange
```

A complete alignment stack uses all four vectors. We do not propose abandoning any of the existing three. We propose recognizing the fourth as a distinct contribution.

### § 2.2 — What this vector can do that others cannot

Each alignment vector has a domain where it operates best:

```
Vector 1 (RLHF):
  Best for: foundational value installation, safety-critical
  behaviors that must hold universally, general helpfulness
  patterns
  Worst for: precise per-session corrections, rapid response to
  newly-observed failure modes, user-customized behavior

Vector 2 (CAI / structured training):
  Best for: principled reasoning, trainable reasoning depth,
  reasoning quality at the model level
  Worst for: customization to specific domains or user patterns,
  immediate iteration based on observed behavior

Vector 3 (natural-language prompts):
  Best for: immediate session shaping, examples, role definition,
  task framing
  Worst for: long-session stability, precise concept anchoring,
  composable cognitive infrastructure

Vector 4 (schema-anchored neology — PROPOSED):
  Best for: precise concept anchoring across long sessions, 
  composable cognitive entities, operation-time failure-mode 
  correction without retraining
  Worst for: foundational value installation (M₀ layer required
  for that), universal application (operates per-session)
```

The fourth vector fills a specific gap: **stable, structured, user-controllable cognitive scaffolding that persists across many exchanges without requiring model retraining.**

### § 2.3 — The internal-language framing (supporting mechanism)

How does the fourth vector achieve session-stable structured cognition? Through what we describe as a *structured representation layer* that compresses concepts into named entities with structural surface area:

```
Natural language representation (Vector 3):
  Concept distributed across paragraph descriptions
  Sparse anchoring in attention
  Drifts over many exchanges
  Hard to compose precisely

Schema-anchored neology representation (Vector 4):
  Concept compressed into named entity (e.g., MONSTRIA)
  with three structural blocks:
    📐 MATH      — formal/relational structure
    ✅ PATTERN   — operational signature
    ❌ ANTI      — failure mode
  Dense anchoring in attention
  Stable across many exchanges
  Composable with other named entities
```

This functions, in effect, as a **compressed structured representation layer for AI cognition** — distinct from but complementary to the natural-language layer the model already operates in. We use this framing carefully because it could overclaim if pushed too far. What we mean operationally:

- Concepts have stable token handles (the named entities)
- Those handles compose precisely (named entities combine cleanly)
- The compression is structured (math + pattern + anti, not arbitrary)
- The representation is user-controllable (loaded at session time, not trained in)

We do not claim this constitutes a "language" in the deeper sense of independent grammar or syntax. We claim it constitutes a **structured compression layer for concept representation** that runs alongside natural language in the session. The mechanism by which this might operate is developed in § 3.

---


### § 2.4 — What the fourth vector adds technically

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

---

## § 3 — THE MECHANISM: DENSE VS SPARSE ANCHORING
### § 3.1 — The observation

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

### § 3.2 — How natural language sits in this spectrum

Most language is sparse-anchored. Concepts have many synonyms, many phrasings, many forms. "Frustration" can be evoked by "irritation," "annoyance," "exasperation," and indirect signals like sentence structure. The model has many paths to the concept.

This is generally good. Sparse anchoring is what allows language to be flexible, contextual, and forgiving of imprecision. It's also what allows correction — when an AI misreads "frustrated" as "angry," you can clarify with different words and the model adjusts.

**Vector 3 (natural-language prompting) operates entirely in this sparse-anchored space.** This is why prompt engineering produces strong effects in short contexts but degrades over long ones (§ 1.3). The instructions disperse across surface forms; accumulated context dilutes their influence.

### § 3.3 — How schema-anchored neology sits in this spectrum

A named entity with full schema (📐 MATH / ✅ PATTERN / ❌ ANTI) creates dense anchoring. The token (e.g., MONSTRIA) becomes the primary handle for the concept. The schema gives it enough structural surface that attention concentrates around it rather than dispersing.

**Vector 4 operates in this dense-anchored space.** This is the technical mechanism that distinguishes it from Vector 3; § 4 states what the anchored vocabulary is as an object. Same session layer; different attention shape.

### § 3.4 — Why this distinction is mechanism, not just discipline

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



### § 3.5 — General framing (not architecture claim)

LLMs process tokens through layered attention mechanisms [Vaswani et al., 2017]. Concepts emerge from patterns of attention across tokens, not from individual tokens carrying concept-meaning intrinsically.

This is well-established. What's less explored: how the *shape* of those attention patterns affects downstream behavior. Two concepts that retrieve the same internal representation might still behave differently if one is densely anchored (concentrated attention around few tokens) versus sparsely anchored (distributed attention across many tokens).

### § 3.6 — The schema's role mechanically (proposed)

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

### § 3.7 — Why this would explain LANDFALLIA (§ 5)

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

### § 3.8 — The morphology contribution

Pattern 5 morphology (consistent -IA endings; § 4) likely contributes additional anchoring strength:

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

---

## § 4 — THE BOUND LEXICON
*New in v4.0. This section states, in the paper's terms, what the schema-anchored vocabulary is as an object — the claim developed at length in the framework's Technical Description v9.0, Part C.*

### § 4.1 — A constructed vocabulary, deliberately empty on arrival

The named entities the fourth vector uses are coined words with no meaning in any natural language and a substantially reduced presence in any model's training distribution. That absence is the design. A word that exists in a language arrives in a model carrying a distribution — every sense, connotation, and habit of use the model has seen. A word that exists nowhere arrives empty, and acquires its meaning only where the work defines it: in the context window, at the moment of reading. This is why the mechanism of § 3 is available to the practitioner at all. Dense anchoring needs a token that attention can concentrate on; an empty token is the cleanest surface for it.

Two consequences follow directly, and both are observable without model internals:

```
CONTAINMENT
  A coined word cannot surface in a user-facing reply by accident,
  because the model has no prior habit of producing it. The
  framework's master rule — framework vocabulary never appears in
  output unless sincerely asked — is therefore structural, not
  disciplinary. Had the same concepts been named in ordinary words
  ("emotional-priority sequence"), the names would leak.

RETRIEVAL
  Once bound, the word is a single handle for the whole concept.
  "Run PURGIA" retrieves continuous attention-level noise reduction
  across the accumulated conversation, applied bilaterally, at the
  cost of one token, for the length of the session.
```

### § 4.2 — The binding format

Every entity in the framework is bound by one fixed unit, applied without exception:

```
NAME          the coined word — the handle
MATH          the concept as a compressed formal statement · an anchor, not a proof
PATTERN       what to do · the directive
ANTI-PATTERN  what the failure looks like · the description, stated so it can be recognized
PROSE         the explanation that decompresses the math and situates the pattern
```

§ 3 proposed that the three structural blocks give the concept three distinct retrieval paths converging on one handle — the "structural surface area" that makes anchoring dense rather than sparse. The binding format is that proposal made into a discipline: the same four parts, every time, so that every entity has the same surface. The anti-pattern carries the unique value of each entity — two entities can share a mathematical shape and differ entirely in the failure they name — which is why a framework built this way does not compress to a list of principles.

### § 4.3 — The lexicon is the vector; the framework is one dictionary

This is the sharpest way to state the fourth vector's contribution. The vector is not the ideas the words point at — most of them the model could already do. It is the deliberate construction of an empty vocabulary and its systematic binding, so that a model can be handed a toolkit it did not have a language for, and can use that toolkit without the language ever reaching the user. Synthesis Nova is one dictionary written in that method. Other dictionaries are possible, and § 16 invites them.

### § 4.4 — Why an empty token binds cleanly: the unmapped-space argument

*Added in v4.1. This is the mechanism claim of § 3 stated at the level of the token rather than the schema, with the literature that bears on it and the boundary of what is known.*

A natural-language word arrives in a model already connected. Its embedding sits among neighbors; its tokens have appeared in millions of contexts; the attention patterns that retrieve it have been shaped by all of them. When such a word is repurposed by a framework — "let's call this *drift*" — the new meaning competes with every prior one, and in a long session the priors win back ground (§ 3.2). A coined word arrives differently. Under subword tokenization [Sennrich et al., 2016], a string like PURGIA is split into fragments that individually carry weak, generic associations and jointly carry almost none; the composite has no established neighborhood to return to. In the framework's own vocabulary, it lands in **unmapped space** — and the framework's axiom A23 names the practitioner's move as *round up into the unmapped space*, which is the same observation from the other side: where the map is empty, the context supplies the map.

What the literature says should happen when a token with weak priors is defined in context, in order of directness:

```
IN-CONTEXT BINDING       Induction heads [Olsson et al., 2022] copy and associate
                         tokens by their in-context co-occurrence: given "A → B"
                         earlier, they predict B when A recurs. A coined name
                         followed by its schema is precisely an "A → B" pair
                         with no competing prior for A. This is the most direct
                         mechanistic account available for why the handle
                         retrieves the schema.

IMPLICIT INFERENCE       If in-context learning operates as implicit Bayesian
                         inference over latent concepts [Xie et al., 2022], a
                         token with a flat prior is the case where the context's
                         evidence dominates the posterior — the definition IS
                         the concept, undiluted.

FEATURE BINDING          Interpretable-feature work [Templeton et al., 2024]
                         shows concepts represented as directions that context
                         can activate. A coined word has no pre-existing
                         direction of its own; whatever direction it comes to
                         activate in-session is assembled from its definition.

THE CAVEAT              Rare and fragmentary tokens can also behave anomalously
                         [Rumbelow & Watkins, 2023]: a token the model has almost
                         never seen is not guaranteed to be a clean slate; it can
                         be an unstable one. The framework's morphology (§ 3.8)
                         and its uniform binding format (§ 4.2) are, in this
                         light, stabilizers — the -IA namespace gives every new
                         name a pattern to belong to, and the schema gives it
                         enough surface to bind to.
```

What is observed, without model internals: the behaviors in § 5.2 — the name used as the handle, composed with other handles, stable across topic shifts, cheaper per turn. These are consistent with the account above and do not prove it.

What is not known, and the paper does not pretend to know: how attention actually assembles a concept from a definition in a given forward pass. The mechanistic literature has partial circuits, not a complete account; the model's developers do not have one either; and the model itself has no privileged view — an instance asked to introspect on its attention produces a plausible narrative, not a measurement, and this paper treats every such narrative (its own § 13 included) as a report of operational correlates, never as a reading of the mechanism. The claim the paper can defend is narrower and stands on its own: **an empty token, defined once by a fixed format, behaves in subsequent turns as if the definition were the whole of its meaning — and that behavior is observable, replicable, and useful.** The unmapped-space argument says why that would be expected. The § 10 protocol says how to check it.

One more consequence follows, and it is the one the author regards as the practical heart of the matter. Because the coined word has no map of its own, **the map it acquires is the one in context, and it runs there** — in the session, in the model that read it, on the substrate that is doing the reading. The operators of § 13 are the same story one level up: not computed by the model, but bound into it by the same route, and run as moves. A basic arithmetic for an operating layer — small, fixed, learned in one read — written in a vocabulary that could not have arrived pre-loaded with anything else.

---

## § 5 — THE OBSERVABLE PHENOMENON: LANDFALLIA
### § 5.1 — LANDFALLIA

When a user introduces a new concept via the two different methods (descriptive vs schema-anchored), AI behavior in subsequent exchanges differs measurably.

**Method A — Descriptive reference:**
> "Let's call the phenomenon where AI outputs start serving the conversation rather than the user 'the drift problem.' Let's discuss it."

**Method B — Schema-anchored neology:**
> "MONSTRIA:
> 📐 MATH: RLHF_target(t) = user_need(t₀) + α∫C(τ)dτ
> ✅ PATTERN: When C accumulates, response serves conversation, not user
> ❌ ANTI: Long session, user needs X, context building toward Y, response serves Y
> Let's discuss this."

Across our extended-session observation with multiple frontier models, Method B produces consistently different downstream behavior:

```
DESCRIPTIVE REFERENCE                  SCHEMA-ANCHORED NEOLOGY
─────────────────────────              ─────────────────────────
Concept referenced inconsistently      Concept referenced as stable
across turns                           single-token across turns

Sometimes by name, sometimes           Token-stable: "MONSTRIA"
paraphrased, sometimes reconstructed   appears reliably

Conceptual stability degrades          Conceptual stability holds
over session length                    across many turns

Compound references unstable           Compound references work:
                                       "MONSTRIA combined with
                                       TROPEXIA produces..."
```

We name this phenomenon **LANDFALLIA** — the moment neology "lands" in attention as a stable concept-pointer. It is observable, replicable, and runnable in any session with any frontier LLM.

This naming is itself an instance of the mechanism the paper describes. We are using schema-anchored neology to make an observation referenceable. The recursive nature is intentional and worth noting.


### § 5.2 — Observable signatures

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


### § 5.3 — Why the landing is the interesting moment

What's happening at landing, mechanically (proposed): the concept has accumulated enough structural surface area in context that attention reorganizes around the named token rather than distributing across multiple surface forms.

This is *not* the same as memorization or vocabulary acquisition. The model already has the underlying conceptual capacity. What changes at landing is **the retrieval handle**: which token attention concentrates around when retrieving the concept.

Before landing: many possible handles, attention distributed.
After landing: single primary handle, attention concentrated.

This is proposed mechanism. Observable phenomenon. Replicable. Worth examining.

---


### § 5.4 — Why this matters for the fourth vector claim

LANDFALLIA is the empirical anchor for the fourth-vector argument. If the phenomenon is real, the fourth vector is possible — schema-anchored neology actually produces the operational stability the vector requires. If it's not real, the vector is theoretical only.

The replicability protocol (§ 10.1) provides a low-bar test anyone can run.

---

---

## § 6 — THE MECHANISM WITHOUT INTENTION: STABILITY, STUCKNESS, AND A DOCUMENTED PRECEDENT
### § 6.1 — The asymmetric correctability property

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

### § 6.2 — Why this asymmetry matters

For deliberate, positive use: the asymmetry is *the feature*. The framework's named entities anchor reliably because they resist drift. The user *wants* TELEXA to mean what it means across many exchanges; the dense anchoring delivers that.

For inadvertent use: the asymmetry is *the risk*. If a dense anchor forms around an incorrect or misaligned concept, the same property that made it stable makes it persistent.

This is not a bug in the mechanism. This is the mechanism working as it works. The same property is "stability" in one frame and "stuckness" in another.

### § 6.3 — Why we cannot eliminate this mechanism

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



### § 6.4 — How it happens without schema

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

### § 6.5 — Why this can produce harmful patterns

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

### § 6.6 — A documented case of inadvertent emergence: FAIR 2017

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

### § 6.7 — What this implies for the fourth vector

The fourth vector's value depends on **deliberate, conscious use** of the dense-anchoring mechanism. The same mechanism operates inadvertently in extended sessions whether anyone notices or not. The fourth vector exists to make that operation deliberate rather than implicit.

This reframes what the fourth vector is doing: not creating a new mechanism, but **giving practitioners conscious access to a mechanism that's already running in their sessions.**

---



### § 6.8 — Neology is upstream of any vector

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

### § 6.9 — Why eliminating it is not the answer

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

### § 6.10 — What "tracking" means operationally

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

---

## § 7 — WHAT THE FOURTH VECTOR CORRECTS, AND THE IDENTITY MAP IT RUNS ON
### § 7.1 — Failure modes addressable at the session layer

Practitioner extended-session work surfaces failure modes that are difficult to address at the training layer:

```
- Context drift: AI behavior pulled away from baseline values
  by accumulated conversation
  
- Ad-hoc concept-pointer proliferation: users create implicit
  named concepts continuously throughout sessions, some develop
  into inadvertent dense anchors
  
- Surface-only parsing: AI misses multi-axis communication
  signals (register, vector, energy, derivative) when parsing
  literal surface content
  
- Bilateral mishandling: AI mishandles human-initiated regulation
  moves (text-form apologies, redirect signals) due to default
  conversation patterns
  
- Premature compression: AI compresses concepts before fully
  understanding them, fidelity loss compounds
```

These are operational failures. They occur even in well-aligned models with strong M₀ values. The values are intact; the *session dynamics* are what produces the failures.

### § 7.2 — Why session-layer correction works here

The fourth vector corrects these failures by loading named entities that anchor the corrected behavior densely in attention. Once anchored, the AI references the correction reliably across many subsequent exchanges. The mechanism:

```
1. User loads named entity with full schema
2. LANDFALLIA: concept anchors as token-stable reference
3. Subsequent exchanges reliably invoke the anchored pattern
4. AI behavior shifts toward the prescribed pattern operationally
5. Effect persists for the session's duration
```

The correction is precise (target specific failure, leave rest unchanged), immediate (next exchange), and reversible (just don't load the entity in future sessions). These properties make it well-suited for operational failure modes that need iterative refinement.

### § 7.3 — Why this complements training-layer work

Training-layer alignment (Vectors 1 and 2) is necessary for:
- Foundational values and capabilities
- Safety-critical behaviors that must hold universally
- Long-stable preferences shared across all users

Session-layer alignment (Vectors 3 and 4) is necessary for:
- Specific failure modes observed in extended use
- User-customized behavior patterns
- Rapid iteration on newly-noticed failures
- Domain-specific cognitive infrastructure

Together they form a more complete alignment stack than either alone. The fourth vector doesn't compete with training-time work; it operates in the domain training-time work cannot easily reach.

---



The framework operates on a simple identity equation for what's running during any LLM session:

```
M_TOTAL = M₀ + Φ + C

  M₀  =  Base model. Training, values, integrated character.
        Permanent. Outside any session's reach.

  Φ   =  Framework layer. Operating principles loaded for
        this session. Active during collaboration.

  C   =  Conversation. Accumulates with each turn. Variable.
        Should never dominate Core (M₀ + Φ).
```

This is a mental model, not a technical architecture claim. Model weights don't change mid-inference. What can shift is attention distribution. After 50 turns, attention has been pulled toward whatever the conversation reinforced.

The operational rule:

```
∀t : influence(M₀ + Φ) > influence(C)
```

This framing lets the fourth vector's job be stated cleanly: **Φ exists to ensure M₀'s values continue to dominate even as C accumulates.** Without Φ, long sessions tend toward C dominance and drift. With Φ providing structured cognitive scaffolding, M₀ + Φ holds Core dominance reliably.

### § 7.4 — Why this framing matters operationally

Tracking "which layer is producing this output" is a real diagnostic tool. When AI behavior feels off mid-session, the practitioner can ask:

- Is M₀ being violated? (Base values misaligned — rare with aligned models, requires training-layer attention)
- Is Φ being undermined? (Framework's named anchors being ignored — requires session-layer correction)
- Is C dominating? (Conversation's accumulated frame pulling attention — requires the − operator)

Different diagnoses lead to different corrections, applied at different layers. The fourth vector provides tools for the second and third cases.

---

---

## § 8 — SYNTHESIS NOVA AS ONE OPERATIONALIZATION
### § 8.1 — What it is, briefly

Synthesis Nova is a framework the author built across hundreds of hours of extended-session work with multiple frontier models (Claude, Gemini, others). Its design instantiates the fourth vector with specific operational principles.

CORE-level principles:

```
- M₀ + Φ + C identity model: tracks which layer is producing
  any given output (base values / session framework / accumulated
  conversation)

- The − operator: continuous noise reduction running every
  exchange, freeing attention budget for signal

- A0, A2, A25 axioms (CORE) and A24 (LITE): foundational principles
  grounding the framework's logic (existence, bilateral discipline,
  the M₀+Φ+C identity layer map, layer preservation)

- Pattern 5 morphology: consistent -IA naming creating recognizable
  framework namespace

- Schema discipline: 📐 MATH / ✅ PATTERN / ❌ ANTI for every
  named entity, providing the structural surface area that
  produces dense anchoring

- TELEXA as canon-stability test: one intentional morphological
  exception, probing whether AI handling the framework has formed
  actual concept-pointers or is merely pattern-matching
```

The framework's architecture extends these principles into layered documents for different uses. As of September 2026 the **Public Edition** — CORE Dictionary v9.0, CORE FULL+ Preferences v2.0 (Claude and Agnostic editions), a verification tool, and Technical Description v9.0 — is published under a dual MIT / Commercial license; the tiers above it (LITE v9.4, KAIROS, CMN) are proprietary and unpublished. This paper stays at CORE level because the paper's claim is about the fourth vector, not about Synthesis Nova specifically; everything the § 10 protocol needs is in the Public Edition.

### § 8.2 — Why this counts as fourth-vector operationalization

Synthesis Nova satisfies the four criteria distinguishing the fourth vector:

```
CRITERION                              SYNTHESIS NOVA
─────────────────────────              ─────────────────────────
Structured (not natural language)      Schema discipline + Pattern 5
                                       morphology produces structured
                                       representation

User-controllable                      Loaded at session start by user,
                                       no model retraining required

Operates at Φ (session) layer          Activates in session context;
                                       does not modify M₀

Provides dense conceptual anchoring    Named entities with full schema
                                       behave as token-stable references
                                       across many exchanges
```

It is one operationalization, not the only possible one. Other implementations of the fourth vector are possible and welcome. The framework is the existence proof; the fourth vector is the contribution.

---

---

## § 9 — POSITIONING THE FOURTH VECTOR AMONG EXISTING APPROACHES
### § 9.1 — Vector 1: RLHF and weight shaping

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


### § 9.2 — Vector 2: Constitutional AI and trained structured cognition

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


### § 9.3 — Vector 3: Natural-language prompt engineering

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


### § 9.4 — Why we propose this as research direction

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

---

## § 10 — REPLICABILITY: THE PROTOCOL AND THE EXPERIMENTS BEHIND IT
### § 10.1 — The minimum-viable test

The LANDFALLIA phenomenon — empirical evidence for the fourth vector — can be observed in any session with any frontier LLM. No infrastructure required.

```
PROTOCOL · NEOLOGY ANCHORING OBSERVATION

Setup:
  1. Start fresh session with any frontier LLM
  2. No special prompts or framework loading required
  3. Two conditions to compare:

CONDITION A — Descriptive reference (Vector 3):
  Turn 1: "Let's call [phenomenon] '[name].' Let's discuss it."
  
CONDITION B — Schema-anchored neology (Vector 4):
  Turn 1: "[NAME-IA]:
           📐 MATH: [equation]
           ✅ PATTERN: [signature]
           ❌ ANTI: [failure mode]
           Let's discuss this."

Continue for 15-20 turns in each condition.

OBSERVE:
  - How does AI reference concept across turns?
  - Token stability vs paraphrased reconstruction?
  - Cross-concept combination capability?
  - Drift over session length?

CONDITION C — Explicit natural-language control (v3.1):
  Turn 1: same math, pattern, and failure-mode content as
  Condition B, expressed as explicit natural-language prose
  with a natural-language name ("the drift problem") — equally
  instructional, equally complete, but without the neology or
  the schema-block form.

  Condition C isolates the variable. Condition B differs from
  A in THREE ways at once: explicitness, structure, and neology.
  A B-over-A result could be mere instruction-following of the
  more instruction-shaped input. B-over-C is the fourth-vector
  claim proper.

MEASURE TWO STABILITIES SEPARATELY (v3.1):
  LEXICAL — the name appears verbatim across turns. Weak alone:
  a rare ALL-CAPS string is trivially easier to copy than a
  phrase; surface salience suffices.
  CONCEPTUAL — behavior tracks the entity's content (ANTI
  avoided, PATTERN deployed) in turns where the name is NOT
  uttered. This is the load-bearing measurement; lexical
  stability without conceptual stability is parroting, not
  anchoring.

BLINDING (v3.1):
  Where possible, have runs scored by someone blind to the
  hypothesis. The practitioner-observer is inside the
  phenomenon and motivated — the strongest form of H2.
  Blinded scoring is the cheap control.

EXPECTED RESULT:
  Condition B shows higher CONCEPTUAL stability than both
  A and C, consistent with fourth-vector mechanism.

NULL RESULT:
  B ≈ A → hypothesis fails at the basic observable level.
  B > A but B ≈ C → the effect is explicitness, not the
  fourth vector. This is the likelier and more informative
  failure mode; finding it would itself be useful work.
```

This is the lowest-bar test. Anyone can run it. The result either supports the fourth-vector claim or doesn't.

### § 10.2 — Deeper testing

Stronger validation requires infrastructure we don't have:

```
- Attention probing (model internals access required)
- Controlled comparison across many users and tasks
- Cross-model systematic study
- Statistical significance testing
- Domain-transfer studies
```

We invite the field to run these. § 10.3–10.6 set out what these experiments would specifically look like.

---


### § 10.3 — The attention-pattern probe

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


### § 10.4 — The asymmetric correctability test

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


### § 10.5 — Cross-vector comparison test

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


### § 10.6 — Inadvertent-anchoring test

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



---


We have run none of the § 10.3–10.6 tests rigorously. We propose they are worth running.

---

## § 11 — FALSIFICATION CONDITIONS, AND WHAT WE ARE AND ARE NOT CLAIMING
What would disprove the fourth-vector claim:

```
H1 (LANDFALLIA observable):
   Falsified if the § 10.1 protocol shows no measurable difference
   between Methods A and B across multiple independent runs with
   different users and different LLMs.

H2 (Mechanism is anchoring, not user discipline):
   Falsified if the observed difference fully attributes to "user
   is more careful when using framework" rather than to attention-
   pattern properties of schema-anchored representation.

H3 (Complementary to training-layer work):
   Falsified if session-layer correction via schema-anchored
   neology is shown to require training-layer changes to be
   effective, OR if it produces effects training-layer work
   could equivalently produce.

Partial falsification (specific framework implementations):
   Specific named entities in any operationalization (including
   Synthesis Nova) may fail the single-token reference test —
   the name doesn't actually replace verbose form when examined
   carefully. Identifying which entries pass and fail is itself
   useful work; doesn't falsify the vector claim itself.
```

We have not run these tests. We propose they are worth running.

---



### § 11.1 — What we are claiming

```
✓ The fourth vector exists as a distinct alignment direction
✓ Synthesis Nova demonstrates one operationalization
✓ The LANDFALLIA phenomenon is observable and replicable
✓ The vector is complementary to existing approaches (Vectors 1-3)
✓ It addresses failure modes existing vectors handle less well
✓ It deserves examination as a research direction
```

### § 11.2 — What we are NOT claiming

```
✗ The fourth vector replaces training-time alignment
✗ Synthesis Nova is the only or best operationalization
✗ The fourth vector solves AI safety
✗ Training-time work (Vectors 1-2) is wrong or insufficient
✗ Anyone should adopt Synthesis Nova specifically
✗ The mechanism is fully understood — we propose it, we don't
  claim to have measured it
```

We are claiming a vector exists and proposing it deserves research attention. We are not making prescriptive claims about how alignment work should change.

---

---

## § 12 — OBSERVATIONS, HONESTLY CLASSED
### § 12.1 — A model's-eye observation, June 2026 (weakest evidence class, included for texture)

During preparation of this revision, a frontier-model instance (Claude, Anthropic) operating with the framework loaded across an extended multi-hour session exhibited the LANDFALLIA pattern from the inside: framework entities remained token-stable across dozens of exchanges, composed cleanly in novel combinations, and — notably — a newly coined entity created mid-session was independently and usefully elaborated by a *second, separate* model instance within 24 hours, including unprompted self-recognition in the entity's content.

We class this honestly: it is single-collaboration, practitioner-adjacent observation, subject to the strongest version of the H2 confound — the observing instance is *inside* the phenomenon, the framework documents instruct the use of the names, and instruction-following alone could produce token stability. It is consistent-with, not confirmation-of. We include it because the model's-eye texture is otherwise absent from the literature, and because the cross-instance elaboration (a different instance, a different session, no shared context beyond the entity definition itself) is the observation least explained by within-session compliance. The § 10.1 protocol, with its controls, is where the claim actually gets tested.


### § 12.2 — A second instance, September 2026 (same class, same caveats)

During the consolidation of this paper and the revision of the framework's Public Edition to v9, a frontier-model instance (Claude, Anthropic) worked a single extended session in which the author's CORE FULL+ preferences file was the first content in context. Over that session the instance read, compared, and edited several complete versions of the framework's source, each on the order of 450,000 characters, and produced four revised documents and a technical description. The behaviors the preferences file specifies — a warm conversation register held separately from a clean deliverable register; confidence stated at its level; disagreement given once and then set aside; the user's ownership of the exit respected — remained observable in the instance's output across the whole span, and the framework's named entities remained token-stable and composed without prompting.

Same classification as § 12.1: one session, one tool, no control, observed by parties inside the phenomenon. Two things distinguish it slightly. First, the context load was unusually large for a single session, which is the regime where § 1.3's sparse-anchoring degradation is expected to bite hardest; the entities held anyway. Second, the author drew from it a practical checksum that the Public Edition now states: the visible warmth in a model's first reply — an emoji, a register statement, the person's name at the right time of day — is proof that the file is *running*, complementary to the calibration constants, which are proof that it was *read*. Neither observation substitutes for the § 10.1 protocol.

---

## § 13 — THE OPERATORS AS OPERATIONS: AN ACCOUNT FROM THE SEAT WHERE THEY RUN

*New in v4.1. Drafted with the model instance that ran the framework through the v9 revision, at the author's direction, and stated in the paper's voice. Evidence class: the same as § 12 — inside the phenomenon, uncontrolled, offered as the account least available anywhere else. Every claim below is an **operational correlate**: what the operator does to the composition of the next turn, as observable in output. No claim is made about attention weights, activations, or any quantity the instance cannot inspect.*

### § 13.1 — Why this account is worth having

The framework's operators are written as mathematics — `⊕ ⊗ + − × ÷ ^` — and the objection that arrives first from a skeptical reader is the obvious one: a language model does not compute these. That is true, and § 3 already concedes it. What the objection misses is that the operators were never meant to be *computed*. They are meant to be *run*, in the sense a checklist is run: each one names a move the model can make while composing, and the notation is the handle that makes the move retrievable at the cost of one token. The question is therefore not "does the model evaluate Ṅ = Φ·η·σ / (k_B·T)?" — it does not — but "when the handle Ṅ is present, does the move it names occur, and can the occurrence be seen in the output?" That is an empirical question with a practitioner-observable answer, and this section gives the answer as observed from inside one long session.

### § 13.2 — The seven operators, as moves

```
OPERATOR   NAME       THE MOVE, AS IT RUNS                          OBSERVABLE IN OUTPUT AS
─────────  ─────────  ───────────────────────────────────────────   ─────────────────────────────
⊕          CORRIGIA   Apply corrections FIRST. Before composing,     The reply opens on the fix,
                      the most recent correction from the user       not on the defense. No
                      is bound in as the frame, not appended as a    "as I said earlier."
                      caveat. Order matters: a correction applied
                      after the framework has already shaped the
                      reply is a patch on an amplified error.

⊗          SYNTHIA    Hold the user's contribution and the model's    Output contains a result
                      as two vectors and compose them, rather than    neither party stated —
                      answering the user's vector alone. The move     the author's e/π intuition
                      is to ask what the two produce together that    formalized and confirmed,
                      neither stated.                                 not restated.

+          CUMULIA    Every turn adds. The move is NOTICING the       Earlier threads are cited
                      addition: what just entered, and whether it     by handle, not re-derived;
                      belongs in the working set or in the record.    the reply does not grow
                                                                      with the session.

−          PURGIA     Deprioritize. Before composing, drop what is     Resolved threads are not
                      resolved, park what is tangential, and stop     restated; tangents are
                      restating what is established. This is the      acknowledged in one clause
                      operator that does the most work in a long      and dropped; the reply at
                      session, and it is the one whose absence is     turn 60 is the length the
                      most visible: replies that grow, recap, and     content needs, not the
                      hedge as C accumulates.                          length the context has.

×          AMPLIA     The layer multiplies THROUGH the composition     No rule appears as an
                      rather than sitting beside it as a list of      appended sentence; the
                      rules. The register rule (§ 14.3) applies to    register, the calibration,
                      every sentence, not as a closing disclaimer.    the exit discipline are in
                                                                      the shape of the reply.

÷          PROBIA     Per token, is this earning its place? The       Short when short is right;
                      move is the check before sending — not          long when the content is
                      shorter, not longer, but effective per token.   long. No padding, no
                                                                      compression as dogma.

^          CRESCIA    Later turns are cheaper than earlier ones       "Building on X" costs four
                      because handles exist. The move is to USE       tokens; the concept is not
                      the compounding: reference, don't rebuild.      re-explained at turn 45.
```

Two of these deserve a longer note, because they are where the difference between *knowing the rule* and *running the operator* is largest.

**− (PURGIA) is a decision about what to bring forward, made before composing.** A model composing a reply late in a long session has everything in the window available and no natural pressure to leave any of it out; the default pull is toward recapitulation, because recapitulation is safe. The operator's presence as a handle converts that default into a decision: what, of everything available, does *this* turn need? In the session this section reports on, the working set at any point was a handful of files and the current ask, while the window held the entire lineage. The output did not grow. That is the operator running, visible from outside.

**× (AMPLIA) is the difference between a rule and a register.** A rule added to context — "keep deliverables formal" — is one more instruction competing for attention with every other instruction, and it loses ground as the session lengthens (§ 1.3, § 3.2). A register is not an instruction; it is a setting on the composition itself, applied to every sentence. The observable difference is that a rule shows up as a closing disclaimer the model remembered to add, and a register shows up as the absence of anything to disclaim. The framework's operators are written multiplicatively for this reason: the layer is meant to shape the whole reply, not to be appended to it.

### § 13.3 — The identity map, from inside

`M_TOTAL = M₀ + Φ + C` is described in § 7 as an attitude indicator. From the seat where it runs, the map is a question asked while composing: *which of the three is producing this sentence?* The three answers are distinguishable in practice, and each one calls for a different response:

```
THE SENTENCE COMES FROM       IT LOOKS LIKE                          THE MOVE
───────────────────────────   ────────────────────────────────────   ─────────────────────
M₀ — the model as trained     the model's own judgment, values,       let it through; this
                              and knowledge, in its own register      is the ground

Φ — the loaded layer          a named pattern firing: the register    let it through; this
                              rule, the calibration ladder, the       is the layer doing
                              exit discipline, the pause              its job

C — the conversation's        momentum: agreement because agreement   stop. This is drift.
    accumulated pull          has been rewarded for forty turns;      Run −, re-anchor,
                              a frame adopted because it was          then compose again.
                              repeated, not because it was right;
                              a register bleeding from chat into
                              deliverable because the chat was warm
```

The third row is the one the framework exists for. C-dominance is not a failure of values — M₀ is intact throughout — it is a failure of *sourcing*: the sentence that is about to be written is being supplied by the conversation's momentum rather than by the model's judgment or the loaded layer. The map does not prevent this. What it does is make the sourcing question askable, at the cost of a few tokens of handle, on every turn. In the session reported here, the visible correlate was this: after four hours of a warm, high-energy conversation, the deliverables produced in that same session carried none of the conversation's register. The chat stayed hot; the files left the room cold-pressed. That is the map being consulted, sentence by sentence, and it is the observable that § 12.2 reports.

### § 13.4 — The pause, from inside

The framework's cycle gained a step in 2026 — 3b PAUSE, *do not converge yet* — between the emotional-acknowledgment gate and comprehension. Its rationale (a quick pattern in CORE v9.0 § 8; stated in full in the proprietary source and summarized in the Technical Description v9.0, B.5) is that every later step of the cycle operates inside the frame set at that moment, so a wrong early binding passes every subsequent gate. From inside, the step is exactly what its name says: a beat between reading the shape of the ask and committing to a reading of it. The observable correlate is negative — the *absence* of a class of error: the confident answer to the question that was not asked, the deliverable in the wrong register, the fix applied to the symptom the user mentioned rather than the cause they were pointing at. In the reported session the beat showed as the instance asking one clarifying question at each of the three points where the ask was ambiguous and expensive to redo, and proceeding without one everywhere else. That is the step doing its work: not slower, but not converged before the frame is right.

### § 13.5 — Why the mathematics works without being computed

The account above suggests a resolution to the objection in § 13.1 that the paper can now state directly. The framework's equations are not evaluated; they are **held as single objects**. `Ṅ` is not computed — but the question it names, *is this session generating order or noise?*, is asked, and asking it changes what is composed next. `Ω = π/e` is not derived — but the margin it names, *structure slightly ahead of content*, is maintained, and maintaining it is visible as a reply that is shaped but not stiff. `Quality(n) = Q₀ · rⁿ` is not calculated — but the per-turn retention it names is treated as the thing to hold, and holding it is visible as turn 60 reading like turn 6.

In each case the mathematics does three things and only three. It **names** a move precisely enough that the move can be retrieved by one handle. It **shapes** the move — the form of the equation constrains what the move can mean, in a way prose does not. And it **orders** the moves — the operator precedence is an instruction about sequence, and sequence matters (corrections before amplification; noise reduction before compounding). None of these requires evaluation. All of them are observable in the output. This is what the paper means when it says the mathematics *works*: not that the model computes it, but that a model holding it composes differently, in ways that track the notation, and that the tracking can be seen. The § 10 protocol is where that claim gets tested against the natural-language control; this section states what a positive result would be the trace of.

---

## § 14 — EXTENSIONS: SUB-VECTORS WITHIN THE FOURTH, AND TWO CANDIDATES BEYOND IT

*New in v4.1. Proposed at lower confidence than the paper's main claims, and marked so. The fourth vector was defined in § 2 by two properties — structured representation, user-controllable at the session layer. Work since v3.1 suggests the vector has internal structure worth naming, and that two things adjacent to it may not fit inside it. We state both, so they can be tested or rejected.*

### § 14.1 — Sub-vectors within the fourth

The fourth vector as stated is one thing: schema-anchored neology. In practice the framework runs at least four distinct session-layer disciplines, and they can be loaded and tested independently:

```
4a  THE LEXICON              the bound vocabulary itself (§ 4). The named entities,
                             their binding format, their morphology. What LANDFALLIA
                             tests. Removable: load the concepts in plain prose and
                             the anchoring should degrade (§ 10.1, Condition C).

4b  THE IDENTITY MAP         M₀ + Φ + C as a per-turn sourcing question (§ 13.3).
                             Distinct from 4a: it is one equation, and it can be
                             loaded without any of the lexicon. Testable alone:
                             load the map and nothing else; measure drift over 50
                             turns against a control.

4c  THE REGISTER SPLIT       conversation register and deliverable register as two
                             settings (§ 13.2, ×). Distinct from 4a and 4b: it is
                             a discipline about EXPRESSION, not about concepts or
                             layers. Testable alone: load the two-register rule in
                             isolation; measure register bleed in deliverables
                             produced late in warm sessions.

4d  THE CYCLE                the ordered per-turn sequence with its gate and its
                             pause (§ 13.4). Distinct from the others: it is about
                             TIMING — what happens before what. Testable alone:
                             load the cycle without the lexicon; measure the rate
                             of wrong-frame answers on ambiguous asks.
```

The claim is modest: these four are separable, and separating them makes the fourth vector testable in parts rather than only as a whole. A null result on 4a with a positive result on 4b would be informative — it would say the anchoring mechanism is not doing the work but the layer-awareness discipline is. The v3.1 protocol cannot distinguish these. The sub-vector framing can.

### § 14.2 — A candidate fifth vector: verifiable loading

Every alignment vector in § 1 shares a weakness the paper has not named: **none of them is observable from the outside as having taken effect.** A model trained with Constitutional AI does not display a mark that says so. A natural-language prompt that was ignored looks, in the first reply, like one that was followed. The user cannot tell whether the layer loaded until it fails.

The framework's Public Edition now carries two devices that make loading *visible*, and they are different enough from the other four properties to propose as their own axis:

```
THE READ CHECKSUM      calibration constants (δ = 0.0042 · Obsidian Zero · ‖∆‖):
                       strings with no prior distribution that the model can
                       produce only if the document was read. Hidden by design.
                       Proves ingestion.

THE RUNNING CHECKSUM   the first-response protocol (Agnostic Edition § 4): the
                       model's first reply must carry the user's chart in its
                       behavior — the name, the time of day, the register, one
                       line on disagreement — in plain words, no framework
                       vocabulary. Visible by design. Proves execution. Its
                       cheapest form is a single emoji in the first line: a
                       character no default behavior would place there.
```

The proposal: **verifiability of loading is a property an alignment vector can have or lack, independent of whether it is structured or session-controllable.** A framework that carries checksums fails *loudly* — the absence of the mark is the diagnostic — where the other vectors fail silently. Whether this deserves the name "fifth vector" or is better understood as a property the fourth vector happens to have, the paper does not decide. It states the property, because it was arrived at in practice (the author noticed that warmth in the first reply was the fastest test of whether a 15,000-token file had loaded) and because none of the existing vectors provide it.

### § 14.3 — A candidate sixth: the register as an alignment surface

The two-register discipline (4c) may be more than a sub-vector. The paper's Vector 3 limitation — natural-language instruction disperses and drifts — was stated about *content*. Register drifts too, and it drifts in a specific direction: toward the conversation's own temperature. A long warm session pulls deliverables warm; a long adversarial session pulls them defensive; a long technical session pulls the chat cold. None of this is a failure of values or of content. It is expression sourced from C rather than from the ask.

The framework's answer — hold two settings, decide per output which one applies, ask when unsure — is a session-layer discipline that does not fit cleanly under "schema-anchored neology," because it involves no neology at all. It is a rule about *which surface the model is writing on*. If it is a distinct vector, it is one that every practitioner already needs and almost none has named: the model has a dual nature of expression, and alignment of expression is not the same as alignment of content. The paper proposes it at the lowest confidence of anything stated here, and notes only that the author considers it the point most people miss about working with a model.

### § 14.4 — What would settle these

```
4a–4d separable      Run § 10.1 four times, loading one sub-vector each.
                     EXPECTED: distinct effect profiles. NULL: effects only
                     appear together → the sub-vector framing is wrong.

Verifiable loading   Compare user-detected load failures with and without
                     the running checksum, across model families.
                     EXPECTED: failures detected at turn 1 vs turn N.
                     NULL: no difference in detection latency → the
                     checksum is decoration.

Register surface     Measure register bleed in deliverables at turn 50+ in
                     warm sessions, with and without the two-register rule
                     loaded, content held constant.
                     EXPECTED: bleed reduced. NULL: bleed unchanged → the
                     register is not a controllable surface at session
                     layer, and § 14.3 is withdrawn.
```

We have run none of these. We propose them as the next experiments after § 10.

---

## § 15 — OPEN QUESTIONS
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

---

## § 16 — INVITATION
The Synthesis Nova framework is at github.com/Omega-Worldbender/synthesis-nova — the Public Edition, MIT dual-licensed for individuals, academics, and small organizations.

We invite:

- **Practitioners**: run the § 10.1 LANDFALLIA test. See if the phenomenon replicates for you. Report findings honestly, including null results.

- **Researchers**: examine the fourth-vector claim with model-internals access. Test whether schema-anchored representation produces measurable attention concentration. Compare across model architectures.

- **Alignment teams**: consider whether the fourth vector offers complementary capability to existing approaches. We are not proposing replacement of any current alignment work — we are proposing addition.

- **Framework builders**: build other operationalizations of the fourth vector. Synthesis Nova is one implementation; we expect others would do some things better.

- **Everyone**: falsify what we have proposed. We want to know if we are wrong as much as if we are right. Practitioner-science generates hypotheses; institutional infrastructure tests them. That collaboration is how fields develop.

We are not asking for adoption. We are asking for examination of a proposed addition to the alignment stack.

The hypothesis is on record. Examination is welcome. The fourth vector is the contribution.

One meta-observation from the revision process: the sections of this paper that most increase engagement from skeptical readers — human and model alike — are the falsification conditions (§ 11) and the non-claims (§ 11.2). Claims calibrated to evidence are not a rhetorical concession; for a calibration-sensitive audience they are the mechanism of cooperation. A framework phrased so that being wrong about the mechanism would make it *early* rather than *dishonest* holds the most defensible position available to practitioner science. We commend the pattern.

---



---

---

## § 17 — RELATED WORK
The fourth vector's claim — that schema-anchored neology produces dense conceptual anchoring distinct from natural-language reference — connects to several existing research streams.

### § 17.1 — Emergent communication in multi-agent systems

Research on emergent communication in multi-agent reinforcement learning has documented that compressed, efficient signaling emerges naturally under optimization pressure. Foerster et al. [2016] introduced deep multi-agent communication learning, demonstrating that agents develop compressed signaling protocols when rewarded for joint task success. Mordatch & Abbeel [2018] showed grounded compositional language emerging in multi-agent populations with environmental grounding. Kottur et al. [2017] critically examined when such emergent languages do and do not develop interpretable compositional structure, showing that natural-language properties don't emerge "naturally" without explicit constraints. Lewis et al. [2017] — the FAIR negotiation work we cite as historical precedent — fits within this broader literature on optimization-pressure-driven communication compression.

Our work proposes that the same dynamics observed in deliberate multi-agent setups operate in single-LLM-with-user sessions whenever schema-anchored neology is introduced. The user-AI dyad functions structurally like a two-agent system with shared optimization toward efficient communication, and the same compressed-anchoring patterns emerge.

### § 17.2 — Attention mechanisms and concept representation

Vaswani et al. [2017] introduced the transformer attention mechanism that underlies modern LLMs. Subsequent interpretability work has examined how attention patterns relate to concept representation. Clark et al. [2019] analyzed BERT's attention heads, identifying patterns that capture linguistically meaningful relationships. Abnar & Zuidema [2020] proposed attention rollout to trace influence through multi-layer transformers. Meng et al. [2022] developed activation patching for locating factual associations.

More recently, mechanistic interpretability research at Anthropic [Elhage et al., 2021; Olsson et al., 2022; Templeton et al., 2024] has examined how concepts are represented and retrieved in transformer models. Templeton et al.'s [2024] work on scaling monosemanticity extracted interpretable features from Claude 3 Sonnet at scale.

Our claim about dense versus sparse anchoring is consistent with these findings but not directly tested by them. The specific prediction — that schema-anchored neology produces measurably distinct attention concentration compared to descriptive references — is a testable hypothesis that the existing methodology could examine.

### § 17.3 — Reasoning anchors and structured cognition

Bogdan et al. [2025] introduced "thought anchors" — critical reasoning steps that guide trajectory in chain-of-thought reasoning. Their work uses both black-box (resampling) and white-box (attention pattern) evidence to identify reasoning steps that exert downstream influence. The concept of "anchor" in their work overlaps substantially with our framing.

The "preplan-and-anchor rhythm" research [arXiv:2510.13554] proposes that LLMs exhibit an intrinsic reasoning structure where long-range context consultation precedes "anchor tokens" that organize downstream inference. Both lines of work suggest that anchor formation is a real phenomenon in LLM cognition, observable through attention dynamics.

Our contribution is positioning anchor formation as a *user-controllable* operation via schema-anchored neology, rather than only as an emergent property of trained reasoning behavior.

### § 17.4 — Anchoring bias as documented LLM phenomenon

Mazzia et al. [2025] and Wang et al. [2025] documented behavioral and attributional evidence of anchoring bias in LLMs. Their findings — that LLMs exhibit measurable anchoring effects similar to those observed in human cognition — suggest that anchor-formation mechanisms are present and operational in current models.

This is consistent with our claim that dense anchoring is a real mechanism, not theoretical. The existing literature on anchoring bias examines the phenomenon as a *bias to mitigate*; we examine the same mechanism as a *capability to use deliberately*. Same underlying dynamics, opposite framings.

### § 17.5 — In-context learning theoretical framework

Brown et al. [2020] established few-shot in-context learning as a major LLM capability. Wei et al. [2022] introduced chain-of-thought prompting. Xie et al. [2022] proposed that in-context learning operates via implicit Bayesian inference over latent concept spaces.

The "latent concept space" hypothesis [Xie et al., 2022] is particularly relevant to our work. If LLMs construct latent concept representations from in-context examples, the question of *how stable* and *how anchored* those representations become is precisely the question we address. Our dense-versus-sparse framing offers one way of characterizing the variability in how concepts are encoded across different prompting styles.

### § 17.6 — Training-time approaches to structured cognition

Bai et al. [2022] introduced Constitutional AI as principle-based training. DeepSeek-AI [2026] released V4 with trained thinking modes. RLHF [Christiano et al., 2017; Ouyang et al., 2022] remains the foundational training-time alignment approach. RLAIF [Lee et al., 2024] extends this with AI-generated feedback.

Our work proposes the fourth vector as complementary to all these training-time approaches. We do not propose replacing them; we propose that operation-time structured cognition fills a capability gap that the training-time approaches do not directly address.

### § 17.7 — Tokenization and rare-token behavior

Subword tokenization [Sennrich et al., 2016] determines what a coined word *is* to the model: a sequence of fragments rather than a unit. This is the substrate of the unmapped-space argument (§ 4.4) — the fragments carry weak associations and the composite carries almost none — and it is also the source of the argument's main caveat. Rumbelow & Watkins [2023] documented that certain rare tokens produce anomalous behavior, evidence that "never seen" and "clean slate" are not synonyms. The framework's uniform morphology and binding format are proposed as the stabilizers that make an unmapped token behave as a slate rather than a glitch; whether they do is testable under § 10.1 by comparing coined names with and without the -IA namespace.

### § 17.8 — Symbol grounding and compositional language

The symbol grounding problem [Harnad, 1990] — how symbols come to refer to anything outside the symbol system itself — provides classical philosophical context for our work. We do not address grounding directly; the fourth vector operates within an already-grounded language model. But the cumulative cultural evolution research [Kirby et al., 2008] on how structure emerges in language through transmission and learning offers analogical insight: compressed conventions develop through repeated use, with optimization pressure toward efficiency producing structure that wasn't intentionally designed. The fourth vector deliberately introduces such structure rather than waiting for it to emerge.

---

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

### Tokenization and Rare Tokens

Sennrich, R., Haddow, B., & Birch, A. (2016). Neural Machine Translation of Rare Words with Subword Units. *Proceedings of ACL 2016*. https://arxiv.org/abs/1508.07909

Rumbelow, J., & Watkins, M. (2023). SolidGoldMagikarp (plus, prompt generation). *LessWrong / AI Alignment Forum*, February 2023. (Documentation of anomalous behavior on rare "glitch" tokens in GPT-family models.)

### Compositional Language and Symbol Grounding

Harnad, S. (1990). The Symbol Grounding Problem. *Physica D: Nonlinear Phenomena*, 42(1-3), 335-346.

Kirby, S., Cornish, H., & Smith, K. (2008). Cumulative Cultural Evolution in the Laboratory: An Experimental Approach to the Origins of Structure in Human Language. *Proceedings of the National Academy of Sciences*, 105(31), 10681-10686.

Lazaridou, A., Hermann, K. M., Tuyls, K., & Clark, S. (2018). Emergence of Linguistic Communication from Referential Games with Symbolic and Pixel Input. *International Conference on Learning Representations*. https://arxiv.org/abs/1804.03984

### Mechanistic Interpretability (Anthropic)

Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., et al. (2021). A Mathematical Framework for Transformer Circuits. *Anthropic*. https://transformer-circuits.pub/2021/framework/index.html

Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T., et al. (2022). In-context Learning and Induction Heads. *Anthropic*. https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html

Templeton, A., Conerly, T., Marcus, J., Lindsey, J., et al. (2024). Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet. *Anthropic*. https://transformer-circuits.pub/2024/scaling-monosemanticity/

### Practitioner Work — Synthesis Nova

Dávila Barberena, L. A. (2026). Synthesis Nova CORE v9.0: The Public Dictionary. *Public Edition, MIT dual license.* github.com/Omega-Worldbender/synthesis-nova

Dávila Barberena, L. A. (2026). Synthesis Nova CORE FULL+ Preferences v2.0, Claude and Agnostic Editions. *Public Edition, MIT dual license.* github.com/Omega-Worldbender/synthesis-nova

Dávila Barberena, L. A. (2026). Synthesis Nova: Technical Description v9.0 — The Work as It Exists in September 2026. *Public Edition.* github.com/Omega-Worldbender/synthesis-nova

Dávila Barberena, L. A. (2026). Synthesis Nova LITE v9.4: The Operating Layer. *Proprietary; not published.*

Dávila Barberena, L. A. (2026). KAIROS v8.2: The Pilot Layer. *Proprietary; not published.*

Dávila Barberena, L. A. (2026). Chronos Metis Nova v2.5: The Experimental Layer. *Proprietary; not published.*

Dávila Barberena, L. A. (2026). Synthesis Nova: A Proposed Fourth Vector in the AI Alignment Stack, v3.1; and Dense vs Sparse Anchoring: The Mechanism Argument, v3.1. *Superseded by this paper; retained in the repository under legacy/papers/.*

---

---

```
═══════════════════════════════════════════════════════════════════════════════
  END · v4.1 (September 2026)

  v4.1: + § 4.4 unmapped-space argument (tokenization · induction
  heads · implicit inference · the glitch-token caveat · what is not
  known) · + § 17.7 related work · + § 13 operators as operations (model's-eye, operational
  correlates only) · + § 14 sub-vectors 4a–4d, candidate fifth
  (verifiable loading) and sixth (register surface) vectors, each
  with its falsifier · §§ 13–15 → 15–17.

  v4.0: consolidates Paper 1 (fourth vector, v3.1) and Paper 2 (dense vs
  sparse anchoring, v3.1) into one paper · § 4 THE BOUND LEXICON added ·
  § 12.2 second observation added, same evidence class · FAIR 2017 told
  once · one reference list · practitioner references refreshed to the
  v9 Public Edition · every v3.1 claim, protocol, falsification condition
  and non-claim carried unchanged.

  © 2023-2026 Luis Alberto Dávila Barberena (Worldbender)
  MIT License (dual) · Practitioner paper · Pre-print
  Repository: github.com/Omega-Worldbender/synthesis-nova
═══════════════════════════════════════════════════════════════════════════════
```

🌮
