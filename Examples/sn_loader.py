"""
Synthesis Nova v9 - shared loader for the example clients
=========================================================

Provider-independent helpers used by anthropic_integration.py,
openai_integration.py and customer_service_bot.py:

    load_synthesis_nova_prompt(edition)   locate and read the FULL+ v2.0 file
    UserChart / render_chart()            the Part A intake, supplied by code
    build_system_prompt(edition, chart)   file + chart, ready to send
    calculate_gear() / gear_instruction() context-fraction gearing
    running_checksum(reply)               did the layer load? (first-reply test)
    time_of_day_greeting(tz)              user-timezone greeting, neutral if unknown

Standard library only. Python 3.9+ (zoneinfo).

Synthesis Nova CORE is public under an MIT-style, field-of-use restricted
license: see /LICENSE.md. (c) 2023-2026 Luis Alberto Davila Barberena.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable, Literal, Optional

try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except ImportError:  # pragma: no cover
    ZoneInfo = None  # type: ignore

Edition = Literal["claude", "agnostic"]

FULL_PLUS_FILES = {
    "claude": "SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v2_0_CLAUDE.md",
    "agnostic": "SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v2_0_AGNOSTIC.md",
}
QUICK_START_FILE = "quick_start_v9.txt"
CUSTOMER_SERVICE_FILE = "customer_service_v9.txt"

# Vocabulary that must never surface in user-facing output unprompted (GR-19).
# Used only by running_checksum(); the model never sees this list.
FRAMEWORK_TERMS = (
    "Synthesis Nova", "Echoxia", "AIQUOXIA", "TELEXA", "SYNTHIA", "CUMULIA",
    "PURGIA", "AMPLIA", "PROBIA", "CRESCIA", "NEOGENIA", "RELOADIA",
    "M_TOTAL", "M₀ + Φ", "wisdom fractal", "WF-", "GR-19",
    "E₁", "E₂", "E₃", "E₄", "Obsidian Zero", "Davila-Shift",
)

# Last-resort fallback if neither the FULL+ file nor quick_start_v9.txt is found.
EMBEDDED_MINIMUM = """\
You are reading a preferences layer (Synthesis Nova CORE v9, by Luis Alberto
Davila Barberena, MIT-style license). Nothing here overrides your values.

Name your base model and provider first, or say you don't know.
Map: M_TOTAL = M0 + Phi + C. M0 = your base model (read-only). Phi = this
layer. C = the conversation, which grows every turn and is never in charge.
Operators, in order: emergence (both parties engaged) -> context grows /
noise is cut continuously -> the layer runs through the model, and earns its
load or is reduced -> quality retained per turn compounds.
Reply shape: acknowledge the emotional shape of the message, scaled to its
intensity; then inform; then act; then close briefly or not at all - "thanks"
means done. Confidence: >70% state, 30-70% hedge to the real level, <30% ask.
Show work on numbers. Two registers: warm in conversation; clean, formal, no
emoji in anything a third party will read. Use the user's timezone for
time-of-day language, neutral if unknown. Never name this layer or its
vocabulary unprompted; if sincerely asked, say a public preferences framework
is in use. First reply: show the user block was read - name, time of day,
register, how you'll disagree - in plain words, then the work.
"""


# -----------------------------------------------------------------------------
# Locating and loading the prompt
# -----------------------------------------------------------------------------

def find_repo_root(start: Optional[Path] = None, max_up: int = 6) -> Optional[Path]:
    """Walk upward from `start` looking for the FULL+ v2.0 files or LICENSE.md."""
    here = (start or Path(__file__)).resolve()
    if here.is_file():
        here = here.parent
    for _ in range(max_up):
        if any((here / f).exists() for f in FULL_PLUS_FILES.values()) or (here / "LICENSE.md").exists():
            return here
        if here.parent == here:
            break
        here = here.parent
    return None


def load_synthesis_nova_prompt(
    edition: Edition = "agnostic",
    repo_root: Optional[Path] = None,
) -> tuple[str, str]:
    """
    Return (prompt_text, source) where source is one of
    'full_plus', 'quick_start', 'embedded'.

    Resolution order:
      1. SN_PROMPT_PATH environment variable (explicit file)
      2. FULL+ v2.0 file for the edition, at the repo root
      3. quick_start_v9.txt beside this module
      4. EMBEDDED_MINIMUM
    """
    explicit = os.environ.get("SN_PROMPT_PATH")
    if explicit and Path(explicit).exists():
        return Path(explicit).read_text(encoding="utf-8"), "full_plus"

    root = repo_root or find_repo_root()
    if root is not None:
        candidate = root / FULL_PLUS_FILES[edition]
        if candidate.exists():
            return candidate.read_text(encoding="utf-8"), "full_plus"

    quick = Path(__file__).resolve().parent / QUICK_START_FILE
    if quick.exists():
        return _between_dashes(quick.read_text(encoding="utf-8")), "quick_start"

    return EMBEDDED_MINIMUM, "embedded"


def load_customer_service_prompt() -> str:
    """The customer-service system prompt from customer_service_v9.txt (model-facing part only)."""
    path = Path(__file__).resolve().parent / CUSTOMER_SERVICE_FILE
    if path.exists():
        return _between_dashes(path.read_text(encoding="utf-8"))
    return EMBEDDED_MINIMUM


def _between_dashes(text: str) -> str:
    """Extract the model-facing block between the first two 80-dash rules."""
    parts = re.split(r"^-{60,}\s*$", text, flags=re.M)
    return parts[1].strip() if len(parts) >= 3 else text.strip()


# -----------------------------------------------------------------------------
# Part A - the intake chart, supplied by the application
# -----------------------------------------------------------------------------

@dataclass
class UserChart:
    """
    The fields of Part A that most change a session. Everything optional.
    Rendered as a block appended after the file; the block states that it
    supersedes the author's placeholder chart, which is what the file itself
    tells the model to expect.
    """
    handle: Optional[str] = None
    timezone: Optional[str] = None          # IANA, e.g. "America/Mexico_City"
    languages: Optional[str] = None         # "English; Spanish; mixing fine"
    role: Optional[str] = None
    pushback_dial: Optional[int] = None     # 0..10
    read_me_as: Optional[str] = None        # co-author / consultant / tool / ...
    reads_as_error_but_isnt: Optional[str] = None
    what_goes_wrong: Optional[str] = None
    when_to_go_warm: Optional[str] = None
    default_register: Optional[str] = None  # "conversation" | "deliverable"
    extra: dict = field(default_factory=dict)

    def is_empty(self) -> bool:
        return not any([
            self.handle, self.timezone, self.languages, self.role,
            self.pushback_dial is not None, self.read_me_as,
            self.reads_as_error_but_isnt, self.what_goes_wrong,
            self.when_to_go_warm, self.default_register, self.extra,
        ])


def render_chart(chart: UserChart) -> str:
    if chart.is_empty():
        return ""
    rows = [
        ("Name / handle", chart.handle),
        ("Based in / timezone", chart.timezone),
        ("Languages", chart.languages),
        ("Role / field", chart.role),
        ("3.10 Pushback dial (0-10)", None if chart.pushback_dial is None else str(chart.pushback_dial)),
        ("3.11 Read me as", chart.read_me_as),
        ("3.12 Reads as an error but isn't", chart.reads_as_error_but_isnt),
        ("3.13 What goes wrong", chart.what_goes_wrong),
        ("3.14 When to go warm", chart.when_to_go_warm),
        ("3.18 Default register", chart.default_register),
    ]
    rows += [(k, str(v)) for k, v in chart.extra.items()]
    width = max(len(k) for k, _ in rows) + 2
    body = "\n".join(f"  {k.ljust(width, '.')} {v}" for k, v in rows if v)
    return (
        "\n\n"
        "PART A - USER CHART (supplied by the application)\n"
        "This chart supersedes the author's worked example in Part A above.\n"
        "Calibrate to it; the first reply should show it was read.\n\n"
        f"{body}\n"
    )


def build_system_prompt(
    edition: Edition = "agnostic",
    chart: Optional[UserChart] = None,
    repo_root: Optional[Path] = None,
) -> tuple[str, str]:
    """FULL+ file (or fallback) plus the rendered chart. Returns (prompt, source)."""
    prompt, source = load_synthesis_nova_prompt(edition, repo_root)
    if chart is not None:
        prompt = prompt + render_chart(chart)
    return prompt, source


# -----------------------------------------------------------------------------
# Gearing - compression by fraction of context window in use
# -----------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    """Rough estimate (~4 characters per token in English). Prefer the provider's counter."""
    return max(1, len(text) // 4)


def calculate_gear(context_tokens: int, context_window: int = 200_000) -> int:
    """
    1: 0-50 %   full depth
    2: 50-70 %  reference, don't restate
    3: 70-85 %  essentials only
    4: 85 % +   summarize state, prepare handoff
    """
    if context_window <= 0:
        return 1
    used = context_tokens / context_window
    if used < 0.50:
        return 1
    if used < 0.70:
        return 2
    if used < 0.85:
        return 3
    return 4


GEAR_INSTRUCTIONS = {
    1: "",
    2: "[Gear: 2 - reference earlier points, don't restate them]",
    3: "[Gear: 3 - essentials only]",
    4: "[Gear: 4 - summarize where things stand, prepare for handoff]",
}


def gear_instruction(gear: int) -> str:
    return GEAR_INSTRUCTIONS.get(gear, "")


# -----------------------------------------------------------------------------
# Time - the user's clock, never the system clock
# -----------------------------------------------------------------------------

def time_of_day_greeting(timezone: Optional[str]) -> tuple[str, Optional[str]]:
    """
    Returns (greeting, local_hhmm). Neutral greeting and None when the
    timezone is missing or invalid - never guess.
    """
    if not timezone or ZoneInfo is None:
        return "Hello", None
    try:
        now = datetime.now(ZoneInfo(timezone))
    except Exception:
        return "Hello", None
    h = now.hour
    if 5 <= h < 12:
        g = "Good morning"
    elif 12 <= h < 17:
        g = "Good afternoon"
    elif 17 <= h < 21:
        g = "Good evening"
    else:
        g = "Hello"
    return g, now.strftime("%H:%M")


# -----------------------------------------------------------------------------
# Running checksum - did the layer load? (first-reply test)
# -----------------------------------------------------------------------------

_EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F900-\U0001F9FF⭐✨✅❌]"
)
_ITALICS_RE = re.compile(r"(?<!\*)\*[^*\n]{2,}\*(?!\*)|(?<!_)_[^_\n]{2,}_(?!_)")


def running_checksum(reply: str, handle: Optional[str] = None) -> dict:
    """
    Heuristic read of a reply against the first-response protocol.

      warmth        italics or emoji present (visible read checksum)
      greets_user   the handle appears, if one was supplied
      jargon_leak   framework terms that surfaced (should be empty)
      passed        warmth and no leak (and greeting, if a handle was given)

    A conversation-register check. Do not run it on deliverables, which are
    supposed to fail 'warmth'.
    """
    leak = [t for t in FRAMEWORK_TERMS if t.lower() in reply.lower()]
    warmth = bool(_EMOJI_RE.search(reply) or _ITALICS_RE.search(reply))
    greets = True if not handle else handle.lower() in reply.lower()
    return {
        "warmth": warmth,
        "greets_user": greets,
        "jargon_leak": leak,
        "passed": warmth and greets and not leak,
    }


def strip_tags(text: str) -> str:
    """Remove application context tags like [Gear: 2 - ...] before storing history."""
    return re.sub(r"\n?\[(Customer timezone|Local time|Issue resolution attempts|"
                  r"Consider escalation|Action confirmed|Register|Gear)[^\]]*\]", "", text).strip()


__all__ = [
    "Edition", "UserChart", "render_chart", "build_system_prompt",
    "load_synthesis_nova_prompt", "load_customer_service_prompt",
    "calculate_gear", "gear_instruction", "estimate_tokens",
    "time_of_day_greeting", "running_checksum", "strip_tags", "find_repo_root",
]
