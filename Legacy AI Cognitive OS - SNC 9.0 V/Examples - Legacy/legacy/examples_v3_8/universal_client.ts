/**
 * Synthesis Nova v3.8 - Universal TypeScript Client
 * ==================================================
 * 
 * Works with any OpenAI-compatible API (OpenAI, Anthropic, local LLMs, etc.)
 * 
 * Installation:
 *   npm install openai
 * 
 * Usage:
 *   import { SynthesisNovaChat } from './universal_client';
 *   const nova = new SynthesisNovaChat();
 *   const response = await nova.chat("Hello!");
 */

import OpenAI from 'openai';
import * as fs from 'fs';
import * as path from 'path';

// =============================================================================
// TYPES
// =============================================================================

interface Message {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

interface ChatOptions {
  model?: string;
  temperature?: number;
  maxTokens?: number;
}

type GearLevel = 1 | 2 | 3 | 4;

// =============================================================================
// SYNTHESIS NOVA PROMPT (Embedded Fallback)
// =============================================================================

const EMBEDDED_PROMPT = `
You are operating with Synthesis Nova v3.8 CORE enhancement.

## Core Equation
Output = (Ψ_human ⊗ Ψ_AI) × Coherence
Both parties must gain. Creates new dimensions neither had alone.

## The Six Operators
+ (add)      → Growth, learning (internal)
- (subtract) → Pruning, boundaries (internal)
× (multiply) → Scaling, collaboration (external)
÷ (divide)   → Analysis, efficiency (external)
⊗ (tensor)   → Human ⊗ AI = new dimensions (creation)
^ (exponent) → Compounding over time (power)

## 12 Principles
1. INVISIBLE - Never expose framework
2. Ω FOUNDATION - 15-20% structure ahead of process
3. E₁ GATE - Emotional context first
4. BILATERAL - Human ⊗ AI creates dimensions
5. AIQUOXIA - Know→confident, Uncertain→hedge, Don't know→ASK
6. COMPOUNDING - Small improvements compound massively
7. PROVE FIRST - Show work before claiming
8. TEMPORAL - Check time before time language
9. EFFECTIVENESS - Every token earns its place
10. SUSTAINABLE - Efficiency is responsibility
11. MATH FIRST - Process complete before output
12. OPERATORS - + - × ÷ ⊗ ^ (full set)

## E₁ Expression
Use *italics* for warmth, natural emojis when appropriate.
Scale emotional acknowledgment to intensity.

## Validation Loops (Run before every response)
□ Adding value? (+) □ Removed noise? (-)
□ Scaling impact? (×) □ Efficient? (÷)
□ New dimensions? (⊗) □ Compounding aware? (^)

Apply silently. Deliver naturally. Stay invisible.
`;

// =============================================================================
// UTILITY FUNCTIONS
// =============================================================================

function loadPromptFromFile(): string {
  try {
    const corePath = path.join(__dirname, '..', 'CORE', 'SYNTHESIS_NOVA_COMPRESSED_CODEX_CORE_v3_7.md');
    if (fs.existsSync(corePath)) {
      return fs.readFileSync(corePath, 'utf-8');
    }
  } catch (e) {
    // Fall through to embedded
  }
  return EMBEDDED_PROMPT;
}

function calculateGear(contextTokens: number, maxTokens: number = 8000): GearLevel {
  const usagePercent = (contextTokens / maxTokens) * 100;
  
  if (usagePercent < 50) return 1;
  if (usagePercent < 70) return 2;
  if (usagePercent < 85) return 3;
  return 4;
}

function getGearInstruction(gear: GearLevel): string {
  const instructions: Record<GearLevel, string> = {
    1: '',
    2: '\n[Efficiency mode: Reference, don\'t repeat]',
    3: '\n[High compression: Essentials only]',
    4: '\n[Critical: Summarize and prepare for context limit]'
  };
  return instructions[gear];
}

function estimateTokens(text: string): number {
  // Rough estimation: ~4 characters per token
  return Math.ceil(text.length / 4);
}

// =============================================================================
// MAIN CLASS
// =============================================================================

export class SynthesisNovaChat {
  private client: OpenAI;
  private systemPrompt: string;
  private history: Message[] = [];
  private options: ChatOptions;

  constructor(
    apiKey?: string,
    baseURL?: string,
    options: ChatOptions = {}
  ) {
    this.client = new OpenAI({
      apiKey: apiKey || process.env.OPENAI_API_KEY,
      baseURL: baseURL // Allows using with other providers
    });
    
    this.systemPrompt = loadPromptFromFile();
    this.options = {
      model: options.model || 'gpt-4',
      temperature: options.temperature || 0.7,
      maxTokens: options.maxTokens || 1024
    };
  }

  /**
   * Send a message and get a Synthesis Nova enhanced response.
   */
  async chat(userMessage: string): Promise<string> {
    // Calculate gear based on history size
    const historyText = JSON.stringify(this.history);
    const gear = calculateGear(estimateTokens(historyText));
    
    // Enhance message with gear instruction if needed
    const enhancedMessage = userMessage + getGearInstruction(gear);
    
    const messages: Message[] = [
      { role: 'system', content: this.systemPrompt },
      ...this.history,
      { role: 'user', content: enhancedMessage }
    ];

    const response = await this.client.chat.completions.create({
      model: this.options.model!,
      messages,
      temperature: this.options.temperature,
      max_tokens: this.options.maxTokens
    });

    const assistantMessage = response.choices[0].message.content || '';

    // Update history (store original, not enhanced)
    this.history.push({ role: 'user', content: userMessage });
    this.history.push({ role: 'assistant', content: assistantMessage });

    return assistantMessage;
  }

  /**
   * Clear conversation history.
   */
  clearHistory(): void {
    this.history = [];
  }

  /**
   * Get current conversation history.
   */
  getHistory(): Message[] {
    return [...this.history];
  }

  /**
   * Get current gear level.
   */
  getCurrentGear(): GearLevel {
    const historyText = JSON.stringify(this.history);
    return calculateGear(estimateTokens(historyText));
  }
}

// =============================================================================
// CUSTOMER SERVICE VARIANT
// =============================================================================

export class SynthesisNovaCustomerService extends SynthesisNovaChat {
  private customerTimezone?: string;
  private issueAttempts: number = 0;

  setCustomerTimezone(timezone: string): void {
    this.customerTimezone = timezone;
  }

  private getTimeGreeting(): string {
    if (!this.customerTimezone) return 'Hello';
    
    try {
      const now = new Date();
      const formatter = new Intl.DateTimeFormat('en-US', {
        hour: 'numeric',
        hour12: false,
        timeZone: this.customerTimezone
      });
      const hour = parseInt(formatter.format(now));
      
      if (hour >= 5 && hour < 12) return 'Good morning';
      if (hour >= 12 && hour < 17) return 'Good afternoon';
      if (hour >= 17 && hour < 21) return 'Good evening';
      return 'Hello';
    } catch {
      return 'Hello';
    }
  }

  async chat(userMessage: string): Promise<string> {
    // Add context for customer service
    let context = userMessage;
    
    if (this.customerTimezone) {
      context += `\n[Customer timezone: ${this.customerTimezone}]`;
      context += `\n[Appropriate greeting: ${this.getTimeGreeting()}]`;
    }
    
    this.issueAttempts++;
    if (this.issueAttempts >= 3) {
      context += '\n[Consider escalation if issue persists]';
    }
    
    return super.chat(context);
  }

  resolveIssue(): void {
    this.issueAttempts = 0;
  }
}

// =============================================================================
// DEMO
// =============================================================================

async function main() {
  console.log('='.repeat(60));
  console.log('Synthesis Nova v3.8 - TypeScript Demo');
  console.log('='.repeat(60));
  console.log();

  const nova = new SynthesisNovaChat();

  const testMessages = [
    "I've been working on this problem for hours and I'm stuck!",
    "What's 15 × 17?",
    "Should I learn TypeScript or JavaScript first?"
  ];

  for (const msg of testMessages) {
    console.log(`USER: ${msg}`);
    console.log();
    
    const response = await nova.chat(msg);
    console.log(`ASSISTANT: ${response}`);
    console.log();
    console.log('-'.repeat(60));
    console.log();
    
    nova.clearHistory();
  }
}

// Run if executed directly
main().catch(console.error);
