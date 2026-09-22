# Unipile MCP

Use the Unipile API — LinkedIn (Classic, Sales Navigator, Recruiter), WhatsApp, Instagram, Telegram, Gmail, Outlook, IMAP and Google/Outlook Calendar — straight from your coding agent while you build. One hosted MCP server, one scoped API key, no glue code to keep in sync with the API.

```
https://developer.unipile.com/mcp
```

This repository is the distribution kit for that server: registry manifests, directory listing copy and setup notes. It does not run a second server — the server above, documented at [developer.unipile.com/docs/mcp](https://developer.unipile.com/docs/mcp), is the only one. Full walkthroughs per client live on the Unipile site:

- [Unipile MCP overview](https://www.unipile.com/mcp)
- [Cursor](https://www.unipile.com/mcp/cursor) · [Claude Code](https://www.unipile.com/mcp/claude-code) · [Codex](https://www.unipile.com/mcp/codex) · [Gemini CLI](https://www.unipile.com/mcp/gemini-cli)
- [LinkedIn on the MCP server](https://www.unipile.com/mcp/linkedin)
- [Webhooks](https://www.unipile.com/mcp/webhooks) · [Hosted Auth](https://www.unipile.com/mcp/hosted-auth)

## What it is

Unipile's whole API surface — every channel, every operation — is readable and callable by your agent through one MCP server. It isn't a curated subset: what the agent can build with is what the API does. The server ships four tools:

- `search-endpoints` / `list-endpoints` / `get-endpoint` — find the right operation and read its exact request/response schema before writing a line of code.
- `execute-request` — run that request for real, against your own Development or Production application, from inside the editor.

Point your agent at it, describe the feature, and it reads the contract, writes the integration in your stack, and can test the call live before you commit the code. The request it runs is the exact same HTTP call your backend will make in production — nothing agent-specific to unwind later.

## Setup

Every client below takes a scoped **Account API key** in an `X-API-KEY` header. Get one from your Unipile dashboard, keep it out of anything committed to a shared repository.

The URL carries a `branch` query parameter selecting the documentation/API version the server reads from: use `v2.0` unless you specifically integrate against the v1 API, in which case `v1.0` works the same way.

<details>
<summary>Cursor — <code>~/.cursor/mcp.json</code> or <code>.cursor/mcp.json</code></summary>

```json
{
  "mcpServers": {
    "unipile": {
      "url": "https://developer.unipile.com/mcp?branch=v2.0",
      "headers": { "X-API-KEY": "your-scoped-api-key" }
    }
  }
}
```
</details>

<details>
<summary>Claude Code — <code>claude mcp add</code></summary>

```bash
claude mcp add --transport http unipile "https://developer.unipile.com/mcp?branch=v2.0" --header "X-API-KEY: your-scoped-api-key"
```
</details>

<details>
<summary>Codex — <code>~/.codex/config.toml</code> or <code>.codex/config.toml</code></summary>

```toml
[mcp_servers.unipile]
url = "https://developer.unipile.com/mcp?branch=v2.0"
http_headers = { "X-API-KEY" = "your-scoped-api-key" }
```
</details>

<details>
<summary>Gemini CLI — <code>~/.gemini/settings.json</code></summary>

```json
{
  "mcpServers": {
    "unipile": {
      "httpUrl": "https://developer.unipile.com/mcp?branch=v2.0",
      "headers": { "X-API-KEY": "your-scoped-api-key" }
    }
  }
}
```
</details>

<details>
<summary>Windsurf / Claude Desktop — same JSON block as Cursor</summary>

```json
{
  "mcpServers": {
    "unipile": {
      "url": "https://developer.unipile.com/mcp?branch=v2.0",
      "headers": { "X-API-KEY": "your-scoped-api-key" }
    }
  }
}
```
</details>

Any other MCP-speaking framework (OpenAI Agents SDK, Claude Agent SDK, LangChain, LlamaIndex, CrewAI, a custom client) works the same way: Streamable HTTP, header auth.

## What you can build, channel by channel

The server exposes the full Unipile API v2: 179 operations across nine channels, one base URL (`https://api.unipile.com`), one scoped key. A short, non-exhaustive map of what agents commonly build with each channel — ask your agent to search for the exact operation and its schema before writing code, don't guess a path from this list.

**LinkedIn — Classic, Sales Navigator, Recruiter accounts kept distinct**
- Classic: search people/companies/jobs/posts with the classic filters or a LinkedIn search URL, read a profile, send/accept a connection request, list invitations, relations and followers.
- Sales Navigator: lead and account search with Sales Navigator filters, saved lead/account lists.
- Recruiter: talent pool and candidate search, applicants and resumes, hiring projects, job postings, InMail credits.
- Messaging (shared with WhatsApp/Instagram/Telegram, see below) covers LinkedIn chats and InMail on a Recruiter/Sales Navigator seat.

**Messaging — WhatsApp, Instagram, Telegram, LinkedIn share the same routes**
List an inbox, read a thread, start a chat, send/forward a message, react, manage group participants.

**Email — Gmail, Outlook, any IMAP mailbox, one schema**
List and search emails and threads, read, send, reply and forward, create drafts, manage folders and attachments, list contacts.

**Calendar — Google and Outlook**
List calendars and events, create/update/cancel an event, respond to an invitation, find free slots.

**Accounts, Hosted Auth, webhooks**
Connect a user's own account through Hosted Auth, read account/connection status, register a webhook destination for realtime events instead of polling.

## No-code and SDKs

- n8n: [`@unipile/n8n-nodes-unipile`](https://github.com/unipile/n8n-nodes-unipile) — a dedicated community node with the same channels above as first-class resources/operations, for building without an agent in the loop.
- Official SDKs: [Node.js/TypeScript](https://github.com/unipile/unipile-node-sdk), [Python](https://github.com/unipile/unipile-python) — the same endpoints the agent discovers through MCP, for the code it writes into your product.

## Notes

- The MCP server itself is generated from the live OpenAPI spec, so it never drifts from the API. This repository only carries the distribution/registry metadata below; nothing here needs to track individual endpoint changes.
- Only this organization's repositories (`github.com/unipile/*`) are official. A repository built on the Unipile API elsewhere on GitHub is a third-party project, not maintained by Unipile.

## Registry manifest

[`server.json`](./server.json) is the [MCP registry](https://github.com/modelcontextprotocol/registry) manifest for this server, used for the official registry submission and for directories that ingest it (Glama, PulseMCP, mcp.so, …).
