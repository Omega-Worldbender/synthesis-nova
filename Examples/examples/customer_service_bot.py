"""
Synthesis Nova v9 - Customer service bot
========================================

A complete customer-service agent on the v9 kit:

    - system prompt from customer_service_v9.txt (model-facing block)
    - customer-timezone greeting, neutral when unknown (never the system clock)
    - resolution attempt tracking and escalation tags
    - gearing by fraction of context window in use
    - two registers: conversation replies vs. deliverables (ticket summary,
      confirmation email) produced with a [Register: deliverable] tag
    - action tags: the model only states a refund/credit as done when the
      backend confirmed it
    - first-reply check (running_checksum)

Provider: any OpenAI-compatible endpoint. Swap the client for Anthropic's
by following anthropic_integration.py; the prompt and the tags don't change.

Requirements:
    pip install openai
    Python 3.9+ (zoneinfo; no pytz needed)

Environment:
    OPENAI_API_KEY, OPENAI_BASE_URL (optional), SN_OPENAI_MODEL (optional)

Usage:
    python customer_service_bot.py

Synthesis Nova CORE is public under an MIT-style, field-of-use restricted
license: see /LICENSE.md. (c) 2023-2026 Luis Alberto Davila Barberena.
"""

from __future__ import annotations

import os
from typing import Optional

from openai import OpenAI

from sn_loader import (
    calculate_gear,
    estimate_tokens,
    gear_instruction,
    load_customer_service_prompt,
    running_checksum,
    time_of_day_greeting,
)

DEFAULT_MODEL = os.environ.get("SN_OPENAI_MODEL", "gpt-4o")
ESCALATION_AFTER_ATTEMPTS = 3


class CustomerServiceBot:
    """Customer-service agent running the Synthesis Nova CORE layer."""

    def __init__(
        self,
        company: str = "the company",
        model: str = DEFAULT_MODEL,
        context_window: int = 128_000,
        temperature: float = 0.5,
    ):
        self.client = OpenAI()
        self.model = model
        self.context_window = context_window
        self.temperature = temperature
        self.system_prompt = load_customer_service_prompt().replace("[COMPANY]", company)
        self.history: list[dict] = []
        self.issue_attempts = 0
        self.customer_timezone: Optional[str] = None
        self.turns = 0
        self.first_reply_check: Optional[dict] = None

    # -- session state ----------------------------------------------------------

    def set_customer_timezone(self, timezone: Optional[str]) -> None:
        """IANA name, e.g. 'America/Mexico_City'. None -> neutral greetings."""
        self.customer_timezone = timezone

    def resolve_issue(self) -> None:
        """Call when the customer confirms the fix worked."""
        self.issue_attempts = 0

    def clear_session(self) -> None:
        self.history = []
        self.issue_attempts = 0
        self.turns = 0
        self.first_reply_check = None

    # -- context tags (appended to the sent message, never stored) --------------

    def _tags(self, register: str, action_confirmed: Optional[str]) -> list[str]:
        tags: list[str] = []
        if self.customer_timezone:
            greeting, local = time_of_day_greeting(self.customer_timezone)
            tags.append(f"[Customer timezone: {self.customer_timezone}]")
            if local:
                tags.append(f"[Local time: {local}]")
            tags.append(f"[Appropriate greeting: {greeting}]")
        if self.issue_attempts > 0:
            tags.append(f"[Issue resolution attempts: {self.issue_attempts}]")
            if self.issue_attempts >= ESCALATION_AFTER_ATTEMPTS:
                tags.append("[Consider escalation if unresolved]")
        if action_confirmed:
            tags.append(f"[Action confirmed: {action_confirmed}]")
        if register == "deliverable":
            tags.append("[Register: deliverable]")
        used = estimate_tokens(self.system_prompt) + estimate_tokens(str(self.history))
        gear = calculate_gear(used, self.context_window)
        if gear > 1:
            tags.append(gear_instruction(gear))
        return tags

    # -- core -------------------------------------------------------------------

    def chat(
        self,
        customer_message: str,
        register: str = "conversation",
        action_confirmed: Optional[str] = None,
    ) -> str:
        tags = self._tags(register, action_confirmed)
        sent = customer_message + ("\n\n" + "\n".join(tags) if tags else "")

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

        # Store the customer's words, not the tagged message.
        self.history.append({"role": "user", "content": customer_message})
        self.history.append({"role": "assistant", "content": reply})
        self.turns += 1
        if register == "conversation":
            self.issue_attempts += 1
        if self.turns == 1 and register == "conversation":
            # Loading check: no framework vocabulary; warmth is optional in CS,
            # so only the jargon leak is decisive here.
            check = running_checksum(reply)
            check["passed"] = not check["jargon_leak"]
            self.first_reply_check = check
        return reply

    # -- deliverables -----------------------------------------------------------

    def ticket_summary(self) -> str:
        """Deliverable register: a ticket summary a colleague can read cold."""
        return self.chat(
            "Write the internal ticket summary for this conversation: issue, "
            "what was tried, current status, next step. Plain, formal, complete.",
            register="deliverable",
        )

    def confirmation_email(self, action_confirmed: str) -> str:
        """Deliverable register: confirmation of an action the backend completed."""
        return self.chat(
            "Write the confirmation email to the customer for the action just "
            "completed. Subject line, then body. Formal, brief, no emoji.",
            register="deliverable",
            action_confirmed=action_confirmed,
        )


# -----------------------------------------------------------------------------
# Demo
# -----------------------------------------------------------------------------

def main() -> None:
    bot = CustomerServiceBot(company="Acme Cloud")
    bot.set_customer_timezone("America/Mexico_City")

    print("=" * 72)
    print(f"Synthesis Nova v9 - Customer Service Bot   model={bot.model}")
    print("=" * 72)

    # 1. Frustrated customer, resolved, exit signal respected.
    for msg in [
        "I've been trying to reset my password for an hour and nothing works!",
        "I tried that already, it says my email isn't recognized",
        "Oh wait, I might have used a different email. Let me check... yes that worked! Thanks!",
    ]:
        print(f"CUSTOMER: {msg}")
        print(f"AGENT: {bot.chat(msg)}\n")
    bot.resolve_issue()
    print(f"first-reply check: {bot.first_reply_check}")
    print("-" * 72)
    bot.clear_session()

    # 2. Simple inquiry - acknowledgment should be one word or none.
    msg = "What are your business hours?"
    print(f"CUSTOMER: {msg}")
    print(f"AGENT: {bot.chat(msg)}\n")
    print("-" * 72)
    bot.clear_session()

    # 3. Billing dispute - escalation as a service, then two deliverables.
    for msg in [
        "I was charged twice for my subscription",
        "I already checked my bank statement, there are definitely two charges",
        "No, I only have one account with you",
        "Can I speak to someone about getting a refund?",
    ]:
        print(f"CUSTOMER: {msg}")
        print(f"AGENT: {bot.chat(msg)}\n")

    print("--- deliverable: ticket summary ---")
    print(bot.ticket_summary(), "\n")

    # Only after the backend actually issued it:
    print("--- deliverable: confirmation email ---")
    print(bot.confirmation_email("duplicate charge of 12.00 USD refunded to original card, 3-5 business days"))
    print("-" * 72)


if __name__ == "__main__":
    main()
