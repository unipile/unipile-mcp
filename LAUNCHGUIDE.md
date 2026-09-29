# Unipile MCP

## Tagline
The Unipile API for LinkedIn, WhatsApp, Instagram, Telegram, email and calendar, inside your coding agent.

## Description
Unipile MCP is the official hosted (remote) MCP server for the Unipile API, the API developers use to add LinkedIn (Classic, Sales Navigator and Recruiter), WhatsApp, Instagram, Telegram, email (Gmail, Outlook, IMAP) and calendar (Google, Outlook) features to their own product.

Plug it into Cursor, Claude Code, Codex, Gemini CLI, VS Code, Windsurf or Cline while you build. Your agent reads the exact Unipile API contract (routes, parameters, request and response schemas) instead of guessing from memory, writes the integration in your stack, and tests each call on your own connected test accounts before you commit. The same five tools cover every Unipile route, so the server never falls behind the API.

Access is limited by a scoped Account API key: the agent can only reach the test accounts you assign to its Scope, never your users' accounts. Operated by Unipile SAS (France).

## Setup Requirements
- `X-API-KEY`: a scoped Account API key from the Unipile dashboard (https://dashboardv2.unipile.com/). Connect a test account, create a Scope for it, then a scoped key for that Scope. Optional for reading the API reference; required to execute requests.
- Endpoint: `https://developer.unipile.com/mcp?branch=v2.0` (Streamable HTTP). Use `branch=v1.0` and a v1 access token for the v1 API.

## Category
Developer Tools

## Features
- Search the whole Unipile API reference by intent ("send a LinkedIn invitation", "list Gmail threads")
- Read the exact schema of any route before writing the request body
- Execute any Unipile API call on your own connected test accounts and see the real response
- LinkedIn Classic: people, company, post and job search, profile enrichment, invitations, messages and InMail, company pages, job postings and applicants
- Sales Navigator: lead and account search, lead and account lists, Sales Navigator InMail
- LinkedIn Recruiter: candidate search, hiring projects, pipelines, applicants and InMail
- WhatsApp, Instagram and Telegram: chats, messages, attachments, voice notes, reactions and groups through one messaging API
- Email on Gmail, Outlook and IMAP: list, search, read, send, reply, drafts, folders and attachments
- Google and Outlook calendars: calendars, events, RSVPs
- Posts and engagement on LinkedIn and Instagram: publish, comment, react, read activity
- Account connection (hosted auth link), multi-tenancy and webhooks for production integrations
- API v2 by default, v1 still available with `branch=v1.0`
- Scoped keys: the agent only reaches the accounts assigned to its Scope

## Getting Started
- "Add a 'Connect LinkedIn' button to my app with Unipile hosted auth, then list the connected accounts."
- "Write a function that sends a LinkedIn invitation with a note, and test it on my connected account."
- "Search Sales Navigator for heads of sales at fintechs in France and save them to a lead list."
- "Build an inbox view that lists WhatsApp and LinkedIn chats together, newest first."
- "Send a test email from my connected Gmail account with an attachment."
- Tool: search-endpoints — Finds the Unipile routes that match an intent.
- Tool: get-endpoint — Returns the full contract of one route: parameters, request body and response schema.
- Tool: list-endpoints — Lists the routes of the API, by tag.
- Tool: list-specs — Lists the available API specifications (v2, v1).
- Tool: execute-request — Calls a Unipile route on your connected accounts with your scoped key and returns the real response.

## Tags
unipile, linkedin, sales-navigator, recruiter, whatsapp, instagram, telegram, email, gmail, outlook, imap, calendar, messaging, api, developer-tools, coding-agent, cursor, claude-code, remote

## Documentation URL
https://developer.unipile.com/docs/mcp

## Health Check URL
https://developer.unipile.com/mcp?branch=v2.0
