"""
Synthesis Nova v9 - Anthropic Claude integration
================================================

Loads the Claude Edition of FULL+ v2.0 from the repository root as the system
prompt, appends a user chart (Part A), and runs the first-reply check.

Requirements:
    pip install anthropic

Environment:
    ANTHROPIC_API_KEY       required
    SN_ANTHROPIC_MODEL      optional, default "claude-sonnet-5" - check your
                            provider's current model list
    SN_PROMPT_PATH          optional, explicit path to a preferences file

Usage:
    python anthropic_integration.py

Synthesis Nova CORE is public under an MIT-style, field-of-use restricted
license: see /LICENSE.md. (c) 2023-2026 Luis Alberto Davila Barberena.
"""

from __future__ import annotations

import os

import anthropic

from sn_loader import (
    UserChart,
    build_system_prompt,
    calculate_gear,
    estimate_tokens,
    gear_instruction,
    running_checksum,
)

DEFAULT_MODEL = os.environ.get("SN_ANTHROPIC_MODEL", "claude-sonnet-5")


class SynthesisNovaClaude:
    """Claude client running the Synthesis Nova CORE layer."""

    def __init__(
        self,
        chart: UserChart | None = None,
        model: str = DEFAULT_MODEL,
        context_window: int = 200_000,
        max_tokens: int = 1024,
    ):
        self.client = anthropic.Anthropic()  # ANTHROPIC_API_KEY
        self.model = model
        self.context_window = context_window
        self.max_tokens = max_tokens
        self.chart = chart or UserChart()
        self.system_prompt, self.prompt_source = build_system_prompt("claude", self.chart)
        self.history: list[dict] = []
        self.turns = 0

    # -- core -----------------------------------------------------------------

    def chat(self, user_message: str) -> str:
        # Gear by fraction of the window in use (system prompt + history + message).
        used = estimate_tokens(self.system_prompt) + estimate_tokens(str(self.history)) \
            + estimate_tokens(user_message)
        gear = calculate_gear(used, self.context_window)
        sent = user_message if gear == 1 else f"{user_message}\n\n{gear_instruction(gear)}"

        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=[*self.history, {"role": "user", "content": sent}],
        )
        reply = "".join(block.text for block in response.content if getattr(block, "type", "") == "text")

        # Store the original message, not the tagged one.
        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": reply})
        self.turns += 1

        if self.turns == 1:
            self.first_reply_check = running_checksum(reply, self.chart.handle)
        return reply

    def clear_history(self) -> None:
        self.history = []
        self.turns = 0


# -----------------------------------------------------------------------------
# Demo
# -----------------------------------------------------------------------------

def main() -> None:
    chart = UserChart(
        handle="Worldbender",
        timezone="America/Mexico_City",
        languages="English or Spanish, mixing fine",
        role="chemical engineer, water treatment; building an LLM middleware",
        pushback_dial=6,
        read_me_as="co-author",
        reads_as_error_but_isnt="intentional misspellings, 'jeje', Spanglish mid-sentence",
        when_to_go_warm="always, in conversation; never in a deliverable",
        default_register="conversation",
    )

    nova = SynthesisNovaClaude(chart=chart)
    print("=" * 72)
    print(f"Synthesis Nova v9 + Claude   model={nova.model}   prompt={nova.prompt_source}")
    print("=" * 72)

    # 1. Loading check: the first reply should read the chart back in behavior.
    hello = nova.chat("Hello")
    print("USER: Hello\n")
    print(f"CLAUDE: {hello}\n")
    print(f"first-reply check: {nova.first_reply_check}")
    print("-" * 72)

    # 2. Same session, three probes - continuity is the point, so no clearing.
    probes = [
        "I'm stuck on this project and feeling overwhelmed.",         # acknowledgment, scaled
        "What's 17 x 23?",                                           # show the work
        "Should I use React or Vue for my project?",                 # ask before guessing
        "Write me a two-paragraph memo to my team about the delay.",  # deliverable register
    ]
    for msg in probes:
        print(f"USER: {msg}\n")
        print(f"CLAUDE: {nova.chat(msg)}\n")
        print("-" * 72)


if __name__ == "__main__":
    main()
