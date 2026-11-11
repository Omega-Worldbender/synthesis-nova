"""
Synthesis Nova v9 - OpenAI-compatible integration
=================================================

Works with OpenAI and with any OpenAI-compatible endpoint (set OPENAI_BASE_URL
for local models, gateways, or other providers). Loads the Agnostic Edition
of FULL+ v2.0 from the repository root as the system prompt, appends a user
chart (Part A), and runs the first-reply check.

Requirements:
    pip install openai

Environment:
    OPENAI_API_KEY          required
    OPENAI_BASE_URL         optional, for compatible endpoints
    SN_OPENAI_MODEL         optional, default "gpt-4o" - check your provider's
                            current model list
    SN_PROMPT_PATH          optional, explicit path to a preferences file

Usage:
    python openai_integration.py

Synthesis Nova CORE is public under an MIT-style, field-of-use restricted
license: see /LICENSE.md. (c) 2023-2026 Luis Alberto Davila Barberena.
"""

from __future__ import annotations

import os

from openai import OpenAI

from sn_loader import (
    UserChart,
    build_system_prompt,
    calculate_gear,
    estimate_tokens,
    gear_instruction,
    running_checksum,
)

DEFAULT_MODEL = os.environ.get("SN_OPENAI_MODEL", "gpt-4o")


class SynthesisNovaChat:
    """OpenAI-compatible chat client running the Synthesis Nova CORE layer."""

    def __init__(
        self,
        chart: UserChart | None = None,
        model: str = DEFAULT_MODEL,
        context_window: int = 128_000,
        temperature: float = 0.7,
    ):
        self.client = OpenAI()  # OPENAI_API_KEY, OPENAI_BASE_URL
        self.model = model
        self.context_window = context_window
        self.temperature = temperature
        self.chart = chart or UserChart()
        self.system_prompt, self.prompt_source = build_system_prompt("agnostic", self.chart)
        self.history: list[dict] = []
        self.turns = 0

    def chat(self, user_message: str) -> str:
        used = estimate_tokens(self.system_prompt) + estimate_tokens(str(self.history)) \
            + estimate_tokens(user_message)
        gear = calculate_gear(used, self.context_window)
        sent = user_message if gear == 1 else f"{user_message}\n\n{gear_instruction(gear)}"

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": self.system_prompt},
                *self.history,
                {"role": "user", "content": sent},
            ],
        )
        reply = response.choices[0].message.content or ""

        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": reply})
        self.turns += 1

        if self.turns == 1:
            self.first_reply_check = running_checksum(reply, self.chart.handle)
        return reply

    def clear_history(self) -> None:
        self.history = []
        self.turns = 0


def main() -> None:
    chart = UserChart(
        handle="Worldbender",
        timezone="America/Mexico_City",
        languages="English or Spanish, mixing fine",
        pushback_dial=6,
        read_me_as="co-author",
        default_register="conversation",
    )

    nova = SynthesisNovaChat(chart=chart)
    print("=" * 72)
    print(f"Synthesis Nova v9 + OpenAI-compatible   model={nova.model}   prompt={nova.prompt_source}")
    print("=" * 72)

    hello = nova.chat("Hello")
    print("USER: Hello\n")
    print(f"ASSISTANT: {hello}\n")
    print(f"first-reply check: {nova.first_reply_check}")
    print("-" * 72)

    probes = [
        "I've been debugging for 3 hours and I'm so frustrated!",  # acknowledgment, scaled
        "What's the best programming language?",                   # calibrated, asks what for
        "Explain recursion",                                        # effectiveness
        "Now give me that explanation as a paragraph for the docs.",  # deliverable register
    ]
    for msg in probes:
        print(f"USER: {msg}\n")
        print(f"ASSISTANT: {nova.chat(msg)}\n")
        print("-" * 72)


if __name__ == "__main__":
    main()
