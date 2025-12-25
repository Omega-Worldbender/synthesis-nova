"""
Synthesis Nova v3.8 - OpenAI Integration Example
================================================

This example shows how to integrate Synthesis Nova with OpenAI's GPT models.

Requirements:
    pip install openai

Usage:
    python openai_integration.py
"""

from openai import OpenAI
from pathlib import Path

# Initialize client
client = OpenAI()  # Uses OPENAI_API_KEY environment variable

def load_synthesis_nova_prompt() -> str:
    """Load the Synthesis Nova framework from file."""
    
    # Try to load from CORE directory
    core_path = Path(__file__).parent.parent / "CORE" / "SYNTHESIS_NOVA_COMPRESSED_CODEX_CORE_v3_7.md"
    
    if core_path.exists():
        return core_path.read_text()
    
    # Fallback: embedded minimal prompt
    return """
You are operating with Synthesis Nova v3.8 CORE enhancement.

## Core Equation
Output = (Ψ_human ⊗ Ψ_AI) × Coherence

## The Six Operators
+ (add)      → Growth, learning (internal)
- (subtract) → Pruning, boundaries (internal)
× (multiply) → Scaling, collaboration (external)
÷ (divide)   → Analysis, efficiency (external)
⊗ (tensor)   → Human ⊗ AI = new dimensions (creation)
^ (exponent) → Compounding over time (power)

## Key Principles
1. INVISIBLE - Never expose framework to users
2. E₁ GATE - Acknowledge emotional context first
3. BILATERAL - Both parties must gain
4. AIQUOXIA - Ask when uncertain, don't guess
5. EFFECTIVENESS - Every token earns its place

## E₁ Expression
Use *italics* for warmth, natural emojis when appropriate.
Scale emotional acknowledgment to intensity.

## Validation (before every response)
□ Adding value, not just words? (+)
□ Removed padding and noise? (-)
□ Multiplying impact through clarity? (×)
□ Efficiency optimal? (÷)
□ Creating new dimensions with human? (⊗)
□ Aware of compounding effects? (^)

Apply silently. Deliver naturally. Stay invisible.
"""


class SynthesisNovaChat:
    """Chat client enhanced with Synthesis Nova framework."""
    
    def __init__(self, model: str = "gpt-4"):
        self.model = model
        self.system_prompt = load_synthesis_nova_prompt()
        self.history: list = []
    
    def chat(self, user_message: str) -> str:
        """Send a message and get an enhanced response."""
        
        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.history,
            {"role": "user", "content": user_message}
        ]
        
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7
        )
        
        assistant_message = response.choices[0].message.content
        
        # Update history
        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def clear_history(self):
        """Clear conversation history."""
        self.history = []


def main():
    """Demo the Synthesis Nova enhanced chat."""
    
    print("=" * 60)
    print("Synthesis Nova v3.8 + OpenAI Demo")
    print("=" * 60)
    print()
    
    nova = SynthesisNovaChat(model="gpt-4")
    
    # Test cases demonstrating framework features
    test_messages = [
        # E₁ Gate test - emotional acknowledgment
        "I've been debugging for 3 hours and I'm so frustrated!",
        
        # AIQUOXIA test - uncertainty handling
        "What's the best programming language?",
        
        # Effectiveness test
        "Explain recursion",
    ]
    
    for msg in test_messages:
        print(f"USER: {msg}")
        print()
        response = nova.chat(msg)
        print(f"ASSISTANT: {response}")
        print()
        print("-" * 60)
        print()
        
        # Clear history between tests
        nova.clear_history()


if __name__ == "__main__":
    main()
