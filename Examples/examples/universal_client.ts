/**
 * Synthesis Nova v9 - Universal TypeScript client
 * ================================================
 *
 * Works with any OpenAI-compatible API (OpenAI, gateways, local models).
 * Loads FULL+ v2.0 (Agnostic Edition) from the repository root as the
 * system prompt, appends a user chart (Part A), gears by context fraction,
 * and runs the first-reply check. A customer-service variant adds the
 * timezone, attempt and register tags used by customer_service_v9.txt.
 *
 * Installation:
 *   npm install openai
 *
 * Usage:
 *   import { SynthesisNovaChat, UserChart } from './universal_client';
 *   const nova = new SynthesisNovaChat({ chart: { handle: 'Ana', timezone: 'Europe/Madrid' } });
 *   console.log(await nova.chat('Hello'));
 *   console.log(nova.firstReplyCheck);
 *
 * Environment:
 *   OPENAI_API_KEY, OPENAI_BASE_URL (optional), SN_OPENAI_MODEL (optional),
 *   SN_PROMPT_PATH (optional explicit preferences file)
 *
 * Synthesis Nova CORE is public under an MIT-style, field-of-use restricted
 * license: see /LICENSE.md. (c) 2023-2026 Luis Alberto Davila Barberena.
 */

import OpenAI from 'openai';
import * as fs from 'fs';
import * as path from 'path';

// =============================================================================
// Types
// =============================================================================

export interface Message {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export type Edition = 'claude' | 'agnostic';
export type Register = 'conversation' | 'deliverable';
export type GearLevel = 1 | 2 | 3 | 4;

/** The Part A fields that most change a session. All optional. */
export interface UserChart {
  handle?: string;
  timezone?: string;          // IANA, e.g. "America/Mexico_City"
  languages?: string;
  role?: string;
  pushbackDial?: number;      // 0..10
  readMeAs?: string;
  readsAsErrorButIsnt?: string;
  whatGoesWrong?: string;
  whenToGoWarm?: string;
  defaultRegister?: Register;
}

export interface ChatOptions {
  edition?: Edition;
  chart?: UserChart;
  model?: string;
  temperature?: number;
  maxTokens?: number;
  contextWindow?: number;     // tokens; used for gearing
  apiKey?: string;
  baseURL?: string;
}

export interface RunningChecksum {
  warmth: boolean;
  greetsUser: boolean;
  jargonLeak: string[];
  passed: boolean;
}

// =============================================================================
// Constants
// =============================================================================

const FULL_PLUS_FILES: Record<Edition, string> = {
  claude: 'SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v2_0_CLAUDE.md',
  agnostic: 'SYNTHESIS_NOVA_CORE_FULL_PLUS_PREFERENCES_v2_0_AGNOSTIC.md',
};
const QUICK_START_FILE = 'quick_start_v9.txt';
const CUSTOMER_SERVICE_FILE = 'customer_service_v9.txt';

/** Vocabulary that must never surface unprompted. Used only by the checksum. */
const FRAMEWORK_TERMS = [
  'Synthesis Nova', 'Echoxia', 'AIQUOXIA', 'TELEXA', 'SYNTHIA', 'CUMULIA',
  'PURGIA', 'AMPLIA', 'PROBIA', 'CRESCIA', 'NEOGENIA', 'RELOADIA',
  'M_TOTAL', 'M₀ + Φ', 'wisdom fractal', 'WF-', 'GR-19',
  'E₁', 'E₂', 'E₃', 'E₄', 'Obsidian Zero', 'Davila-Shift',
];

/** Last resort if neither the FULL+ file nor quick_start_v9.txt is found. */
const EMBEDDED_MINIMUM = `
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
`.trim();

// =============================================================================
// Loading
// =============================================================================

function findRepoRoot(start: string = __dirname, maxUp = 6): string | null {
  let here = path.resolve(start);
  for (let i = 0; i < maxUp; i++) {
    const hit = Object.values(FULL_PLUS_FILES).some((f) => fs.existsSync(path.join(here, f)))
      || fs.existsSync(path.join(here, 'LICENSE.md'));
    if (hit) return here;
    const up = path.dirname(here);
    if (up === here) break;
    here = up;
  }
  return null;
}

/** Model-facing block between the first two 60+ dash rules. */
function betweenDashes(text: string): string {
  const parts = text.split(/^-{60,}\s*$/m);
  return parts.length >= 3 ? parts[1].trim() : text.trim();
}

export function loadSynthesisNovaPrompt(edition: Edition = 'agnostic'): { prompt: string; source: 'full_plus' | 'quick_start' | 'embedded' } {
  const explicit = process.env.SN_PROMPT_PATH;
  if (explicit && fs.existsSync(explicit)) {
    return { prompt: fs.readFileSync(explicit, 'utf-8'), source: 'full_plus' };
  }
  const root = findRepoRoot();
  if (root) {
    const candidate = path.join(root, FULL_PLUS_FILES[edition]);
    if (fs.existsSync(candidate)) {
      return { prompt: fs.readFileSync(candidate, 'utf-8'), source: 'full_plus' };
    }
  }
  const quick = path.join(__dirname, QUICK_START_FILE);
  if (fs.existsSync(quick)) {
    return { prompt: betweenDashes(fs.readFileSync(quick, 'utf-8')), source: 'quick_start' };
  }
  return { prompt: EMBEDDED_MINIMUM, source: 'embedded' };
}

export function loadCustomerServicePrompt(company: string): string {
  const p = path.join(__dirname, CUSTOMER_SERVICE_FILE);
  const text = fs.existsSync(p) ? betweenDashes(fs.readFileSync(p, 'utf-8')) : EMBEDDED_MINIMUM;
  return text.split('[COMPANY]').join(company);
}

// =============================================================================
// Part A - user chart
// =============================================================================

export function renderChart(chart: UserChart | undefined): string {
  if (!chart) return '';
  const rows: Array<[string, string | undefined]> = [
    ['Name / handle', chart.handle],
    ['Based in / timezone', chart.timezone],
    ['Languages', chart.languages],
    ['Role / field', chart.role],
    ['3.10 Pushback dial (0-10)', chart.pushbackDial === undefined ? undefined : String(chart.pushbackDial)],
    ['3.11 Read me as', chart.readMeAs],
    ["3.12 Reads as an error but isn't", chart.readsAsErrorButIsnt],
    ['3.13 What goes wrong', chart.whatGoesWrong],
    ['3.14 When to go warm', chart.whenToGoWarm],
    ['3.18 Default register', chart.defaultRegister],
  ];
  const present = rows.filter(([, v]) => v);
  if (present.length === 0) return '';
  const width = Math.max(...present.map(([k]) => k.length)) + 2;
  const body = present.map(([k, v]) => `  ${k.padEnd(width, '.')} ${v}`).join('\n');
  return (
    '\n\nPART A - USER CHART (supplied by the application)\n' +
    "This chart supersedes the author's worked example in Part A above.\n" +
    'Calibrate to it; the first reply should show it was read.\n\n' +
    body + '\n'
  );
}

// =============================================================================
// Gearing, time, checksum
// =============================================================================

export function estimateTokens(text: string): number {
  return Math.max(1, Math.ceil(text.length / 4)); // rough; prefer the provider's counter
}

export function calculateGear(contextTokens: number, contextWindow = 128_000): GearLevel {
  if (contextWindow <= 0) return 1;
  const used = contextTokens / contextWindow;
  if (used < 0.5) return 1;
  if (used < 0.7) return 2;
  if (used < 0.85) return 3;
  return 4;
}

const GEAR_INSTRUCTIONS: Record<GearLevel, string> = {
  1: '',
  2: "[Gear: 2 - reference earlier points, don't restate them]",
  3: '[Gear: 3 - essentials only]',
  4: '[Gear: 4 - summarize where things stand, prepare for handoff]',
};

export function gearInstruction(gear: GearLevel): string {
  return GEAR_INSTRUCTIONS[gear];
}

/** Greeting for the user's clock; neutral when the timezone is missing or invalid. */
export function timeOfDayGreeting(timezone?: string): { greeting: string; local?: string } {
  if (!timezone) return { greeting: 'Hello' };
  try {
    const fmt = new Intl.DateTimeFormat('en-US', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: timezone });
    const parts = fmt.formatToParts(new Date());
    const hour = parseInt(parts.find((p) => p.type === 'hour')?.value ?? '', 10) % 24;
    const minute = parts.find((p) => p.type === 'minute')?.value ?? '00';
    if (Number.isNaN(hour)) return { greeting: 'Hello' };
    const local = `${String(hour).padStart(2, '0')}:${minute}`;
    if (hour >= 5 && hour < 12) return { greeting: 'Good morning', local };
    if (hour >= 12 && hour < 17) return { greeting: 'Good afternoon', local };
    if (hour >= 17 && hour < 21) return { greeting: 'Good evening', local };
    return { greeting: 'Hello', local };
  } catch {
    return { greeting: 'Hello' };
  }
}

const EMOJI_RE = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B50}\u{2728}\u{2705}\u{274C}]/u;
const ITALICS_RE = /(?<!\*)\*[^*\n]{2,}\*(?!\*)|(?<!_)_[^_\n]{2,}_(?!_)/;

/**
 * Heuristic read of a reply against the first-response protocol.
 * Conversation register only - deliverables are supposed to fail 'warmth'.
 */
export function runningChecksum(reply: string, handle?: string): RunningChecksum {
  const lower = reply.toLowerCase();
  const jargonLeak = FRAMEWORK_TERMS.filter((t) => lower.includes(t.toLowerCase()));
  const warmth = EMOJI_RE.test(reply) || ITALICS_RE.test(reply);
  const greetsUser = handle ? lower.includes(handle.toLowerCase()) : true;
  return { warmth, greetsUser, jargonLeak, passed: warmth && greetsUser && jargonLeak.length === 0 };
}

// =============================================================================
// Main client
// =============================================================================

export class SynthesisNovaChat {
  protected client: OpenAI;
  protected systemPrompt: string;
  protected history: Message[] = [];
  protected turns = 0;
  readonly promptSource: string;
  readonly chart: UserChart;
  readonly model: string;
  readonly contextWindow: number;
  readonly temperature: number;
  readonly maxTokens: number;
  firstReplyCheck?: RunningChecksum;

  constructor(options: ChatOptions = {}) {
    this.client = new OpenAI({
      apiKey: options.apiKey || process.env.OPENAI_API_KEY,
      baseURL: options.baseURL || process.env.OPENAI_BASE_URL,
    });
    const loaded = loadSynthesisNovaPrompt(options.edition ?? 'agnostic');
    this.chart = options.chart ?? {};
    this.systemPrompt = loaded.prompt + renderChart(this.chart);
    this.promptSource = loaded.source;
    this.model = options.model || process.env.SN_OPENAI_MODEL || 'gpt-4o';
    this.temperature = options.temperature ?? 0.7;
    this.maxTokens = options.maxTokens ?? 1024;
    this.contextWindow = options.contextWindow ?? 128_000;
  }

  /** Tags appended to the sent message (never stored). Subclasses extend. */
  protected buildTags(_userMessage: string): string[] {
    const used = estimateTokens(this.systemPrompt) + estimateTokens(JSON.stringify(this.history));
    const gear = calculateGear(used, this.contextWindow);
    return gear > 1 ? [gearInstruction(gear)] : [];
  }

  protected async send(userMessage: string, tags: string[]): Promise<string> {
    const sent = tags.length ? `${userMessage}\n\n${tags.join('\n')}` : userMessage;
    const messages: Message[] = [
      { role: 'system', content: this.systemPrompt },
      ...this.history,
      { role: 'user', content: sent },
    ];
    const response = await this.client.chat.completions.create({
      model: this.model,
      messages,
      temperature: this.temperature,
      max_tokens: this.maxTokens,
    });
    const reply = response.choices[0]?.message?.content ?? '';
    this.history.push({ role: 'user', content: userMessage });
    this.history.push({ role: 'assistant', content: reply });
    this.turns += 1;
    if (this.turns === 1) this.firstReplyCheck = runningChecksum(reply, this.chart.handle);
    return reply;
  }

  async chat(userMessage: string): Promise<string> {
    return this.send(userMessage, this.buildTags(userMessage));
  }

  clearHistory(): void {
    this.history = [];
    this.turns = 0;
    this.firstReplyCheck = undefined;
  }

  getHistory(): Message[] {
    return [...this.history];
  }

  getCurrentGear(): GearLevel {
    const used = estimateTokens(this.systemPrompt) + estimateTokens(JSON.stringify(this.history));
    return calculateGear(used, this.contextWindow);
  }
}

// =============================================================================
// Customer-service variant
// =============================================================================

export class SynthesisNovaCustomerService extends SynthesisNovaChat {
  private customerTimezone?: string;
  private issueAttempts = 0;
  private pendingRegister: Register = 'conversation';
  private pendingAction?: string;
  static readonly ESCALATION_AFTER_ATTEMPTS = 3;

  constructor(company: string, options: ChatOptions = {}) {
    super(options);
    this.systemPrompt = loadCustomerServicePrompt(company);
  }

  setCustomerTimezone(timezone?: string): void {
    this.customerTimezone = timezone;
  }

  resolveIssue(): void {
    this.issueAttempts = 0;
  }

  protected buildTags(userMessage: string): string[] {
    const tags: string[] = [];
    if (this.customerTimezone) {
      const { greeting, local } = timeOfDayGreeting(this.customerTimezone);
      tags.push(`[Customer timezone: ${this.customerTimezone}]`);
      if (local) tags.push(`[Local time: ${local}]`);
      tags.push(`[Appropriate greeting: ${greeting}]`);
    }
    if (this.issueAttempts > 0) {
      tags.push(`[Issue resolution attempts: ${this.issueAttempts}]`);
      if (this.issueAttempts >= SynthesisNovaCustomerService.ESCALATION_AFTER_ATTEMPTS) {
        tags.push('[Consider escalation if unresolved]');
      }
    }
    if (this.pendingAction) tags.push(`[Action confirmed: ${this.pendingAction}]`);
    if (this.pendingRegister === 'deliverable') tags.push('[Register: deliverable]');
    tags.push(...super.buildTags(userMessage));
    return tags;
  }

  async chat(customerMessage: string): Promise<string> {
    this.pendingRegister = 'conversation';
    this.pendingAction = undefined;
    const reply = await this.send(customerMessage, this.buildTags(customerMessage));
    this.issueAttempts += 1;
    if (this.turns === 1 && this.firstReplyCheck) {
      // In customer service warmth is optional; the jargon leak is decisive.
      this.firstReplyCheck.passed = this.firstReplyCheck.jargonLeak.length === 0;
    }
    return reply;
  }

  /** Deliverable register: a ticket summary a colleague can read cold. */
  async ticketSummary(): Promise<string> {
    this.pendingRegister = 'deliverable';
    this.pendingAction = undefined;
    const ask = 'Write the internal ticket summary for this conversation: issue, what was tried, current status, next step. Plain, formal, complete.';
    return this.send(ask, this.buildTags(ask));
  }

  /** Deliverable register: confirmation of an action the backend completed. */
  async confirmationEmail(actionConfirmed: string): Promise<string> {
    this.pendingRegister = 'deliverable';
    this.pendingAction = actionConfirmed;
    const ask = 'Write the confirmation email to the customer for the action just completed. Subject line, then body. Formal, brief, no emoji.';
    return this.send(ask, this.buildTags(ask));
  }
}

// =============================================================================
// Demo
// =============================================================================

async function main(): Promise<void> {
  const nova = new SynthesisNovaChat({
    chart: {
      handle: 'Worldbender',
      timezone: 'America/Mexico_City',
      languages: 'English or Spanish, mixing fine',
      pushbackDial: 6,
      readMeAs: 'co-author',
      defaultRegister: 'conversation',
    },
  });

  console.log('='.repeat(72));
  console.log(`Synthesis Nova v9 - TypeScript   model=${nova.model}   prompt=${nova.promptSource}`);
  console.log('='.repeat(72));

  console.log('USER: Hello\n');
  console.log(`ASSISTANT: ${await nova.chat('Hello')}\n`);
  console.log('first-reply check:', nova.firstReplyCheck);
  console.log('-'.repeat(72));

  const probes = [
    "I've been working on this problem for hours and I'm stuck!",
    "What's 15 x 17?",
    'Should I learn TypeScript or JavaScript first?',
    'Write the README paragraph for this project.',
  ];
  for (const msg of probes) {
    console.log(`USER: ${msg}\n`);
    console.log(`ASSISTANT: ${await nova.chat(msg)}\n`);
    console.log('-'.repeat(72));
  }
}

if (require.main === module) {
  main().catch(console.error);
}
