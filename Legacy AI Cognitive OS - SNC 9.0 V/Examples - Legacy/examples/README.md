# /examples — the v9 kit, in code

Working prompts and clients for the current stack (CORE Dictionary v9.0 · FULL+ Preferences v2.0). Everything here loads the same files a person would paste by hand; the code only adds what a person can't do by hand — fill Part A from data, tag the context, gear by window usage, and check the first reply.

The prior set (v3.8) is frozen in `/legacy/examples_v3_8/`.

## What's here

| File | Use it when |
|---|---|
| `quick_start_v9.txt` | You want to paste one page into any model and see whether it loads. Fill the four USER lines, paste, say hello. |
| `customer_service_v9.txt` | You are building a customer-facing bot. System prompt plus the context tags it expects from your application. |
| `sn_loader.py` | Shared helpers, standard library only: locate and load FULL+ v2.0, render a user chart, gear by context fraction, greet in the user's timezone, run the first-reply check. |
| `anthropic_integration.py` | Claude, via the Anthropic SDK. Loads the Claude Edition. |
| `openai_integration.py` | OpenAI or any OpenAI-compatible endpoint (`OPENAI_BASE_URL`). Loads the Agnostic Edition. |
| `customer_service_bot.py` | Complete customer-service agent: timezone tags, attempt tracking, escalation, two registers (chat replies vs. ticket summary / confirmation email), action-confirmed tags. |
| `universal_client.ts` | The same in TypeScript for OpenAI-compatible APIs, with the customer-service variant. |

## Run

```
pip install -r requirements.txt          # anthropic, openai
export ANTHROPIC_API_KEY=...             # for anthropic_integration.py
export OPENAI_API_KEY=...                # for the others
python anthropic_integration.py
python openai_integration.py
python customer_service_bot.py

npm install openai typescript ts-node   # TypeScript
npx ts-node universal_client.ts
```

Model names default to `claude-sonnet-5` / `gpt-4o` and can be overridden with `SN_ANTHROPIC_MODEL` / `SN_OPENAI_MODEL`. Check your provider's current list; names change faster than this folder does.

## How the clients load the framework

```
1. SN_PROMPT_PATH                       explicit file, if set
2. <repo root>/SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v2_0_{CLAUDE,AGNOSTIC}.md
3. examples/quick_start_v9.txt          the one-page version
4. an embedded minimum                  last resort, so the client never runs bare
```

`prompt_source` on the client tells you which one landed. If it says `embedded`, you are running the kit at its thinnest; put the FULL+ file where the loader can find it.

## Part A from code

The FULL+ file ships with the author's chart as a worked example in Part A. The clients append a **USER CHART** block that supersedes it, built from a `UserChart` (Python) or `UserChart` (TypeScript): handle, timezone, languages, pushback dial, how to read the user, what reads as an error but isn't, when to go warm, default register. Only the fields you set are rendered. The model is told the block supersedes the example, which is what the file itself says to expect.

## The first-reply check

```python
nova = SynthesisNovaClaude(chart=UserChart(handle="Ana", timezone="Europe/Madrid"))
nova.chat("Hello")
nova.first_reply_check
# {'warmth': True, 'greets_user': True, 'jargon_leak': [], 'passed': True}
```

`running_checksum()` is a heuristic read of the first reply against the first-response protocol: warmth present (italics or emoji), the user greeted by handle, and none of the framework's vocabulary surfaced. It is a conversation-register check. Deliverables are supposed to fail `warmth`; the customer-service bot treats only the jargon leak as decisive.

## Context tags

The clients append tags to the message they send and store the untagged message in history, so the tags never accumulate:

```
[Customer timezone: America/Mexico_City]   [Local time: 15:42]
[Issue resolution attempts: 2]             [Consider escalation if unresolved]
[Action confirmed: refund 12.00 USD issued]
[Register: deliverable]
[Gear: 2 - reference earlier points, don't restate them]
```

Gear bands (1: < 50 % of the window · 2: 50–70 % · 3: 70–85 % · 4: 85 % +) are computed from a character-count estimate. Use your provider's token counter when it offers one. The default windows (200k Claude, 128k OpenAI-compatible) are parameters; set them to your model's.

## Register

Everything in this folder is a deliverable and is written in that register. The warmth belongs to the conversation the model has with your user, not to the code that starts it.

## License

Synthesis Nova CORE, including these files, is public under an MIT-style, field-of-use restricted license: free for individuals, academics and organizations under USD 1M revenue; commercial license above that. See `/LICENSE.md` and `/LEGAL_NOTICE.md`. Loading any part of the kit into an LLM context is the licensed application.

© 2023–2026 Luis Alberto Dávila Barberena (Worldbender).
