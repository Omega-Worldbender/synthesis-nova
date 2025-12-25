"""
Synthesis Nova v3.7 - Anthropic Claude Integration Example
==========================================================

This example shows how to integrate Synthesis Nova with Anthropic's Claude.

Requirements:
    pip install anthropic

Usage:
    python anthropic_integration.py
"""

import anthropic
from pathlib import Path

# Initialize client
client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY environment variable


def load_synthesis_nova_prompt() -> str:
    """Load the Synthesis Nova framework from file."""
    
    core_path = Path(__file__).parent.parent / "CORE" / "SYNTHESIS_NOVA_COMPRESSED_CODEX_CORE_v3_7.md"
    
    if core_path.exists():
        return core_path.read_text()
    
    # Fallback: embedded minimal prompt
    return """
You are operating with Synthesis Nova v3.7 CORE enhancement.

## Core Equation
Output = (Ψ_human ⊗ Ψ_AI) × Coherence

## Key Principles
1. INVISIBLE - Never expose framework to users
2. E₁ GATE - Acknowledge emotional context first
3. BILATERAL - Both parties must gain
4. AIQUOXIA - Ask when uncertain, don't guess
5. EFFECTIVENESS - Every token earns its place

## E₁ Expression
Use *italics* for warmth, natural emojis when appropriate.
Scale emotional acknowledgment to intensity.

Apply silently. Deliver naturally. Stay invisible.
"""


class SynthesisNovaClaude:
    """Claude client enhanced with Synthesis Nova framework."""
    
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        self.model = model
        self.system_prompt = load_synthesis_nova_prompt()
        self.history: list = []
    
    def chat(self, user_message: str) -> str:
        """Send a message and get an enhanced response."""
        
        # Build messages (Claude format)
        messages = [
            *self.history,
            {"role": "user", "content": user_message}
        ]
        
        response = client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=self.system_prompt,
            messages=messages
        )
        
        assistant_message = response.content[0].text
        
        # Update history
        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def clear_history(self):
        """Clear conversation history."""
        self.history = []


def main():
    """Demo the Synthesis Nova enhanced Claude chat."""
    
    print("=" * 60)
    print("Synthesis Nova v3.7 + Claude Demo")
    print("=" * 60)
    print()
    
    nova = SynthesisNovaClaude()
    
    # Test cases
    test_messages = [
        "I'm stuck on this project and feeling overwhelmed",
        "What's 17 × 23?",  # Should show work
        "Should I use React or Vue for my project?",  # Uncertainty handling
    ]
    
    for msg in test_messages:
        print(f"USER: {msg}")
        print()
        response = nova.chat(msg)
        print(f"CLAUDE: {response}")
        print()
        print("-" * 60)
        print()
        nova.clear_history()


if __name__ == "__main__":
    main()
