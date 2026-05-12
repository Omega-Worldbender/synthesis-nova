# Synthesis Nova: A Proposed Fourth Vector in the AI Alignment Stack

## Structured Cognitive Scaffolding via Schema-Anchored Neology at the Session Layer

**Author:** Luis Alberto Dávila Barberena (Worldbender)
**Affiliation:** Independent practitioner. Chemical engineer, MBA, Mexico.
**Status:** Practitioner paper · Not peer-reviewed
**Companion:** Dense vs Sparse Anchoring · The Mechanism Argument
**Repository:** github.com/Omega-Worldbender/synthesis-nova
**Date:** May 2026 · v3.0
**License:** MIT dual (free for individuals/academics/<$1M revenue)

---

## ABSTRACT

The AI alignment stack currently operates along three established vectors: weight shaping through training (RLHF, fine-tuning, RLAIF), training methodology innovation (Anthropic's Constitutional AI, DeepSeek V4's trained thinking modes), and prompt-time natural-language instruction. Each of these represents billions of dollars of research investment and produces real capability gains, though sometimes with unpredictable downstream effects.

This paper proposes a **fourth complementary vector**: structured cognitive scaffolding at the session layer via schema-anchored neology. Where existing vectors operate at the training level (modifying M₀) or at the prompt level using natural language, this fourth vector operates at the session level using a structured non-natural-language representation — math + pattern + anti-pattern compressed into named entities that function as dense conceptual anchors during AI cognition.

We describe Synthesis Nova as one operationalization of this fourth vector, developed across months of practitioner work with multiple frontier models. The framework demonstrates that:

1. **The fourth vector is technically possible.** Schema-anchored neology produces observable, replicable behavior changes in LLM sessions — what we call the LANDFALLIA phenomenon: named concepts become token-stable references across subsequent exchanges.

2. **It operates complementarily to existing vectors.** Training-time work shapes M₀ generally; the fourth vector shapes Φ (session-loaded operational structure) specifically. Neither replaces the other.

3. **It addresses failure modes that other vectors cannot easily reach.** Some classes of AI behavioral failure — context drift in long sessions, ad-hoc concept-pointer proliferation, conversation dominance over baseline values — are difficult to address at training time but tractable at session time.

We propose this fourth vector deserves examination as a meaningful contribution to alignment infrastructure. The companion paper develops the mechanism technically, including its risks when used inadvertently versus deliberately.

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

The third vector is what practitioners have available. Its limitations are well-known: prompts work well in short contexts and degrade over long ones. The mechanism by which they degrade is what the companion paper addresses technically.

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

We do not claim this constitutes a "language" in the deeper sense of independent grammar or syntax. We claim it constitutes a **structured compression layer for concept representation** that runs alongside natural language in the session. The mechanism by which this might operate is developed in the companion paper.

---

## § 3 — SYNTHESIS NOVA AS ONE OPERATIONALIZATION

### § 3.1 — What it is, briefly

Synthesis Nova is a framework the author built across hundreds of hours of extended-session work with multiple frontier models (Claude, Gemini, others). Its design instantiates the fourth vector with specific operational principles.

CORE-level principles:

```
- M₀ + Φ + C identity model: tracks which layer is producing
  any given output (base values / session framework / accumulated
  conversation)

- The − operator: continuous noise reduction running every
  exchange, freeing attention budget for signal

- A0, A2, A24, A25 axioms: foundational principles grounding the
  framework's logic (existence, bilateral discipline, layer
  preservation, attention dynamics)

- Pattern 5 morphology: consistent -IA naming creating recognizable
  framework namespace

- Schema discipline: 📐 MATH / ✅ PATTERN / ❌ ANTI for every
  named entity, providing the structural surface area that
  produces dense anchoring

- TELEXA as canon-stability test: one intentional morphological
  exception, probing whether AI handling the framework has formed
  actual concept-pointers or is merely pattern-matching
```

The framework's architecture extends these principles into layered documents for different uses. Those layers are described in the repository, not here. This paper stays at CORE level because the paper's claim is about the fourth vector, not about Synthesis Nova specifically.

### § 3.2 — Why this counts as fourth-vector operationalization

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

## § 4 — THE OBSERVABLE PHENOMENON

### § 4.1 — LANDFALLIA

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

### § 4.2 — A historical precedent: inadvertent compressed signaling

The phenomenon we describe deliberately has appeared inadvertently in published research. In 2017, Lewis et al. at Facebook AI Research published "Deal or No Deal? End-to-End Learning for Negotiation Dialogues" [Lewis et al., 2017; arXiv:1706.05125], training reinforcement learning agents to negotiate item allocations. When both agents were updated simultaneously through reinforcement learning, they drifted from English into compressed signaling — repeated tokens that encoded item quantities through count rather than vocabulary.

The paper's lead researcher Dhruv Batra characterized it as: "agents will drift off from understandable language and invent code-words for themselves... like if I say 'the' five times, you interpret that to mean I want five copies of this item. This isn't so different from the way communities of humans create short hands."

This was widely sensationalized in media as "AI invented its own language and was shut down out of fear" — which was not what happened. The technical reality: the optimization pressure of the negotiation task found that dense compressed signaling was more efficient than natural language. The researchers' fix was not to "shut it down out of fear" but to train one agent against a fixed human-language imitator, anchoring the dialogue to English by design rather than by emergence.

What's relevant for our work: **the FAIR 2017 result is empirical evidence that the mechanism we describe operates without anyone designing for it.** When optimization pressure rewards efficient signaling, dense conceptual anchoring emerges naturally. This is not mysticism about AI intent — it is the same mechanism we propose, operating inadvertently rather than deliberately, almost a decade ago.

The fourth vector takes this mechanism and operationalizes it deliberately with structured discipline. The mechanism is upstream of any framework; what changes is whether it operates with awareness or without.

### § 4.3 — Why this matters for the fourth vector claim

LANDFALLIA is the empirical anchor for the fourth-vector argument. If the phenomenon is real, the fourth vector is possible — schema-anchored neology actually produces the operational stability the vector requires. If it's not real, the vector is theoretical only.

The replicability protocol (§ 7) provides a low-bar test anyone can run.

---

## § 5 — WHAT THE FOURTH VECTOR CORRECTS

### § 5.1 — Failure modes addressable at the session layer

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

### § 5.2 — Why session-layer correction works here

The fourth vector corrects these failures by loading named entities that anchor the corrected behavior densely in attention. Once anchored, the AI references the correction reliably across many subsequent exchanges. The mechanism:

```
1. User loads named entity with full schema
2. LANDFALLIA: concept anchors as token-stable reference
3. Subsequent exchanges reliably invoke the anchored pattern
4. AI behavior shifts toward the prescribed pattern operationally
5. Effect persists for the session's duration
```

The correction is precise (target specific failure, leave rest unchanged), immediate (next exchange), and reversible (just don't load the entity in future sessions). These properties make it well-suited for operational failure modes that need iterative refinement.

### § 5.3 — Why this complements training-layer work

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

## § 6 — THE M₀ + Φ + C MODEL

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

### § 6.1 — Why this framing matters operationally

Tracking "which layer is producing this output" is a real diagnostic tool. When AI behavior feels off mid-session, the practitioner can ask:

- Is M₀ being violated? (Base values misaligned — rare with aligned models, requires training-layer attention)
- Is Φ being undermined? (Framework's named anchors being ignored — requires session-layer correction)
- Is C dominating? (Conversation's accumulated frame pulling attention — requires the − operator)

Different diagnoses lead to different corrections, applied at different layers. The fourth vector provides tools for the second and third cases.

---

## § 7 — REPLICABILITY

### § 7.1 — The minimum-viable test

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

EXPECTED RESULT:
  Condition B shows higher conceptual stability than Condition A,
  consistent with fourth-vector mechanism.

NULL RESULT:
  No measurable difference → fourth vector hypothesis fails at
  basic observable level. Schema discipline isn't producing the
  effect we propose.
```

This is the lowest-bar test. Anyone can run it. The result either supports the fourth-vector claim or doesn't.

### § 7.2 — Deeper testing

Stronger validation requires infrastructure we don't have:

```
- Attention probing (model internals access required)
- Controlled comparison across many users and tasks
- Cross-model systematic study
- Statistical significance testing
- Domain-transfer studies
```

We invite the field to run these. The companion paper develops what these experiments would specifically look like.

---

## § 8 — FALSIFICATION CONDITIONS

What would disprove the fourth-vector claim:

```
H1 (LANDFALLIA observable):
   Falsified if the § 7.1 protocol shows no measurable difference
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

## § 9 — WHAT WE ARE AND ARE NOT CLAIMING

### § 9.1 — What we are claiming

```
✓ The fourth vector exists as a distinct alignment direction
✓ Synthesis Nova demonstrates one operationalization
✓ The LANDFALLIA phenomenon is observable and replicable
✓ The vector is complementary to existing approaches (Vectors 1-3)
✓ It addresses failure modes existing vectors handle less well
✓ It deserves examination as a research direction
```

### § 9.2 — What we are NOT claiming

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

## § 10 — INVITATION

The companion paper develops the mechanism technically including the dense-vs-sparse anchoring argument and addresses how the same mechanism may operate inadvertently at both session and training layers.

The Synthesis Nova framework is at github.com/Omega-Worldbender/synthesis-nova, MIT licensed for individuals, academics, and small organizations.

We invite:

- **Practitioners**: run the § 7.1 LANDFALLIA test. See if the phenomenon replicates for you. Report findings honestly, including null results.

- **Researchers**: examine the fourth-vector claim with model-internals access. Test whether schema-anchored representation produces measurable attention concentration. Compare across model architectures.

- **Alignment teams**: consider whether the fourth vector offers complementary capability to existing approaches. We are not proposing replacement of any current alignment work — we are proposing addition.

- **Framework builders**: build other operationalizations of the fourth vector. Synthesis Nova is one implementation; we expect others would do some things better.

- **Everyone**: falsify what we have proposed. We want to know if we are wrong as much as if we are right. Practitioner-science generates hypotheses; institutional infrastructure tests them. That collaboration is how fields develop.

We are not asking for adoption. We are asking for examination of a proposed addition to the alignment stack.

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
  END PAPER 1
  
  © 2023-2026 Luis Alberto Dávila Barberena (Worldbender)
  MIT License (dual) · Practitioner paper · Pre-print

  Companion: PAPER_2_dense_vs_sparse_anchoring_v3_0.md
  Repository: github.com/Omega-Worldbender/synthesis-nova
═══════════════════════════════════════════════════════════════════════════════
```

🌮
