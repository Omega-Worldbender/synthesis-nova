# /legacy/examples_v3_8 — frozen

These six files are the `/examples` folder as it shipped with Synthesis Nova v3.8 (2025). They are kept as the record and are not maintained.

| File | What it was |
|---|---|
| `quick_start.txt` | Paste-anywhere prompt, v3.8 operator semantics |
| `customer_service.txt` | Customer-service system prompt, v3.8 |
| `anthropic_integration.py` | Claude client loading `CORE/SYNTHESIS_NOVA_COMPRESSED_CODEX_CORE_v3_7.md` |
| `openai_integration.py` | OpenAI client, same loader |
| `customer_service_bot.py` | Customer-service bot with timezone greeting, gear calculation, attempt tracking |
| `universal_client.ts` | TypeScript client for OpenAI-compatible endpoints |

**Why they are here and not in `/examples`.** They reference a CORE file that no longer exists at that path; they carry the pre-v9 operator semantics (`+`/`−` as "internal", `×`/`÷` as "external"), which v9 replaced with the context-layer semantics (`+` context increase, `−` noise reduction, `×` framework-through-model, `÷` signal per framework unit); and they predate the alignment map (A25), the bound lexicon, the two registers, the intake chart (Part A) and the first-response protocol. Running them would load a 2025 framework into a 2026 model.

The current working set is in `/examples`. Same license as the rest of the repository: `/LICENSE.md`.

© 2023–2026 Luis Alberto Dávila Barberena (Worldbender).
