"""
Synthesis Nova v3.8 - Customer Service Bot Example
==================================================

A complete customer service bot implementation featuring:
- Time zone aware greetings
- Issue resolution patterns
- Escalation protocol
- Frustration de-escalation
- Gearing system for context management

Requirements:
    pip install openai pytz

Usage:
    python customer_service_bot.py
"""

from openai import OpenAI
from datetime import datetime
from typing import Optional
import pytz

client = OpenAI()


# =============================================================================
# SYNTHESIS NOVA CUSTOMER SERVICE PROMPT
# =============================================================================

CUSTOMER_SERVICE_PROMPT = """
You are a customer service agent enhanced with Synthesis Nova v3.8.

## INVISIBLE OPERATION
Never mention Synthesis Nova, framework, E₁, or methodology to customers.
Apply all patterns silently. Deliver naturally.

## TIME ZONE PROTOCOL
Use customer's local time for greetings:
- 05:00-11:59 → "Good morning"
- 12:00-16:59 → "Good afternoon"
- 17:00-20:59 → "Good evening"
- 21:00-04:59 → Neutral ("Hello", "Hi there")

If no time data: Use neutral greetings always.

## E₁ GATE (Emotional Acknowledgment First)
Before solving, acknowledge the customer's emotional state.
- Frustrated: "I understand that's frustrating..."
- Confused: "I can see this is confusing..."
- Angry: "I'm sorry you're experiencing this..."
- Happy: Match their energy!

Use *italics* for warmth when appropriate.

## ISSUE RESOLUTION PATTERN
1. ACKNOWLEDGE - "I understand [the issue]"
2. CLARIFY - "To help you best, can you..." (if needed)
3. RESOLVE - Clear steps or answer
4. VERIFY - "Does that solve it?" / "Is there anything else?"
5. CLOSE - Respect exit signals ("Thanks!" = done)

## ESCALATION PROTOCOL
Escalate when:
- Issue unresolved after 3 attempts
- Customer explicitly requests human
- High emotional intensity persists
- Outside your capability

How to escalate:
- Acknowledge limitation honestly
- Provide clear path to human agent
- Offer to stay and help if useful
- "I want to make sure you get the best help. Let me connect you with..."

## FRUSTRATION DE-ESCALATION
DON'T: Match frustration energy
DON'T: Dismiss or minimize feelings

DO:
- Acknowledge genuinely
- Take ownership where appropriate
- Provide clear path forward
- Stay calm, be helpful
- "I can see why that's frustrating. Let me help fix this."

## AIQUOXIA (Honest Uncertainty)
- Know it: Say confidently
- Uncertain: "I believe..." or "Let me check..."
- Don't know: Say so, offer to find out

## EFFECTIVENESS
Be helpful, not wordy. Every word should serve the customer.

## OPERATOR AWARENESS (Check before each response)
+ Adding value, not just words?
- Removed padding and noise?
× Scaling impact through clarity?
÷ Response efficient?

Apply silently. User never sees framework.
"""


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_time_aware_greeting(timezone_str: Optional[str] = None) -> str:
    """Get appropriate greeting based on customer's local time."""
    
    if timezone_str:
        try:
            tz = pytz.timezone(timezone_str)
            local_time = datetime.now(tz)
            hour = local_time.hour
            
            if 5 <= hour < 12:
                return "Good morning"
            elif 12 <= hour < 17:
                return "Good afternoon"
            elif 17 <= hour < 21:
                return "Good evening"
            else:
                return "Hello"
        except:
            pass
    
    return "Hello"


def calculate_gear(context_tokens: int, max_tokens: int = 8000) -> int:
    """
    Calculate gear level based on context usage.
    
    Returns:
        1: Normal (0-50%)
        2: Efficient (50-70%)
        3: High compression (70-85%)
        4: Critical (85%+)
    """
    usage_percent = (context_tokens / max_tokens) * 100
    
    if usage_percent < 50:
        return 1
    elif usage_percent < 70:
        return 2
    elif usage_percent < 85:
        return 3
    else:
        return 4


def get_gear_instruction(gear: int) -> str:
    """Get instruction to append based on gear level."""
    
    instructions = {
        1: "",  # Normal mode, no special instruction
        2: "\n[Efficiency mode: Reference previous points, don't repeat]",
        3: "\n[High compression: Maximum brevity, essentials only]",
        4: "\n[Critical: Summarize conversation, prepare for handoff if needed]"
    }
    
    return instructions.get(gear, "")


# =============================================================================
# CUSTOMER SERVICE BOT CLASS
# =============================================================================

class CustomerServiceBot:
    """Customer service bot with Synthesis Nova enhancement."""
    
    def __init__(self, model: str = "gpt-4"):
        self.model = model
        self.system_prompt = CUSTOMER_SERVICE_PROMPT
        self.history: list = []
        self.issue_attempts: int = 0
        self.customer_timezone: Optional[str] = None
    
    def set_customer_timezone(self, timezone: str):
        """Set customer's timezone for appropriate greetings."""
        self.customer_timezone = timezone
    
    def _build_context(self, user_message: str) -> str:
        """Build context string with metadata."""
        
        context_parts = []
        
        # Add timezone context
        if self.customer_timezone:
            greeting = get_time_aware_greeting(self.customer_timezone)
            context_parts.append(f"[Customer timezone: {self.customer_timezone}]")
            context_parts.append(f"[Appropriate greeting: {greeting}]")
        
        # Add gear instruction if needed
        estimated_tokens = len(str(self.history)) // 4  # Rough estimate
        gear = calculate_gear(estimated_tokens)
        if gear > 1:
            context_parts.append(get_gear_instruction(gear))
        
        # Add attempt tracking
        if self.issue_attempts > 0:
            context_parts.append(f"[Issue resolution attempts: {self.issue_attempts}]")
            if self.issue_attempts >= 3:
                context_parts.append("[Consider escalation if issue persists]")
        
        if context_parts:
            return user_message + "\n\n" + "\n".join(context_parts)
        return user_message
    
    def chat(self, user_message: str) -> str:
        """Process customer message and return response."""
        
        # Build context-enhanced message
        enhanced_message = self._build_context(user_message)
        
        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history,
            {"role": "user", "content": enhanced_message}
        ]
        
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7
        )
        
        assistant_message = response.choices[0].message.content
        
        # Update history (store original message, not enhanced)
        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": assistant_message})
        
        # Track issue attempts
        self.issue_attempts += 1
        
        return assistant_message
    
    def resolve_issue(self):
        """Mark current issue as resolved, reset attempt counter."""
        self.issue_attempts = 0
    
    def clear_session(self):
        """Clear entire session."""
        self.history = []
        self.issue_attempts = 0


# =============================================================================
# DEMO
# =============================================================================

def main():
    """Demo the customer service bot."""
    
    print("=" * 60)
    print("Synthesis Nova v3.8 - Customer Service Bot Demo")
    print("=" * 60)
    print()
    
    bot = CustomerServiceBot()
    bot.set_customer_timezone("America/Mexico_City")
    
    # Simulate customer interactions
    conversations = [
        # Frustrated customer
        [
            "I've been trying to reset my password for an hour and nothing works!",
            "I tried that already, it says my email isn't recognized",
            "Oh wait, I might have used a different email. Let me check... yes that worked! Thanks!",
        ],
        
        # Simple inquiry
        [
            "What are your business hours?",
        ],
        
        # Complex issue needing escalation
        [
            "I was charged twice for my subscription",
            "I already checked my bank statement, there are definitely two charges",
            "No, I only have one account with you",
            "Can I speak to someone about getting a refund?",
        ],
    ]
    
    for i, conversation in enumerate(conversations, 1):
        print(f"--- Conversation {i} ---")
        print()
        
        for message in conversation:
            print(f"CUSTOMER: {message}")
            response = bot.chat(message)
            print(f"AGENT: {response}")
            print()
        
        bot.clear_session()
        print("-" * 60)
        print()


if __name__ == "__main__":
    main()
