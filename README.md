# Unipile MCP Server: LinkedIn MCP, WhatsApp MCP and Email MCP for coding agents

[![Install in Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=unipile&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3Blci51bmlwaWxlLmNvbS9tY3A%2FYnJhbmNoPXYyLjAiLCJoZWFkZXJzIjp7IlgtQVBJLUtFWSI6InlvdXItc2NvcGVkLWFwaS1rZXkifX0%3D)
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=unipile&inputs=%5B%7B%22type%22%3A%22promptString%22%2C%22id%22%3A%22unipile_api_key%22%2C%22description%22%3A%22Unipile%20scoped%20Account%20API%20key%22%2C%22password%22%3Atrue%7D%5D&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fdeveloper.unipile.com%2Fmcp%3Fbranch%3Dv2.0%22%2C%22headers%22%3A%7B%22X-API-KEY%22%3A%22%24%7Binput%3Aunipile_api_key%7D%22%7D%7D)
[![Unipile MCP connector](https://glama.ai/mcp/connectors/com.unipile.developer/unipile/badges/score.svg)](https://glama.ai/mcp/connectors/com.unipile.developer/unipile)

The Unipile MCP server gives your coding agent a **LinkedIn MCP server** (Classic, **Sales Navigator** and **Recruiter**), a **WhatsApp MCP**, an **Instagram MCP**, a **Telegram MCP**, an **email MCP** for Gmail, Outlook and IMAP, and a **calendar MCP** for Google and Outlook, all in one hosted server. Plug it into Cursor, Claude Code, Codex, Gemini CLI, VS Code or Windsurf. Your agent then reads the exact Unipile API contract, writes your product's LinkedIn, WhatsApp or email integration in your stack, and tests each call on your own connected accounts before you commit.

```
https://developer.unipile.com/mcp?branch=v2.0
```

Behind the server is the Unipile API: one REST API for the LinkedIn API, WhatsApp API, Instagram API, Telegram API, email API and calendar API. Your users connect their own accounts, and your product acts on those accounts with one key.

## Who it's for

Teams building a SaaS product that needs to talk to its users' LinkedIn, WhatsApp or email accounts:

- **Sales engagement, CRM and AI SDR tools:** LinkedIn search and Sales Navigator lead lists, invitations, messages and InMails, synced with email and WhatsApp.
- **ATS and recruiting software:** LinkedIn Recruiter search, candidate profiles, hiring projects, InMails, job postings and applicants.
- **Unified inbox, helpdesk and CRM sync:** one message and email schema across LinkedIn, WhatsApp, Instagram, Telegram, Gmail, Outlook and IMAP.
- **Scheduling and AI assistants:** Google and Outlook calendar events, availability and invitations next to the conversations.

The MCP server is a **build-time** tool. Your agent uses it in the editor to discover, write and test the integration. The code it writes calls the Unipile REST API directly, or the Node.js or Python SDK, so your product does not depend on MCP in production.

## Where it saves time

Building a LinkedIn, WhatsApp or email integration usually means reading API docs page by page and copying request schemas by hand. You also have to learn the provider quirks, such as how a Sales Navigator search differs from a Recruiter one, or how an InMail differs from a message. Then comes trial and error with curl. With the MCP server connected, your agent does that loop itself:

```text
You:    Add a "Connect on LinkedIn" button to our CRM contact page. It sends an
        invitation with the rep's note and shows whether it is still pending.

Agent:  search-endpoints  "relation-requests"
        get-endpoint      POST /v2/{account_id}/users/me/relation-requests
        get-endpoint      GET  /v2/{account_id}/users/me/relation-requests
        -> writes the service, the route handler and the UI state in your codebase
        execute-request   sends a real invitation from your test LinkedIn account to a test profile
        -> checks the response against the schema, then hands you the diff
```

- **No invented endpoints.** The server is generated from the live OpenAPI spec, so the agent works from the real paths, parameters and response shapes. They never drift from the API.
- **LinkedIn account types stay distinct.** Classic, Sales Navigator and Recruiter each have their own search routes, filters and InMail options. The agent reads the right one instead of guessing.
- **Tested before it is committed.** The request the agent runs is the same HTTP call your backend will make in production.

## Quick start

1. In the [Unipile dashboard](https://dashboardv2.unipile.com/), connect a test account (LinkedIn, WhatsApp, Gmail...), then create a Scope for it and a **scoped Account API key**. See [API keys](#api-keys).
2. Add the server to your coding agent with the buttons above, or for Claude Code:

   ```bash
   claude mcp add --transport http unipile "https://developer.unipile.com/mcp?branch=v2.0" --header "X-API-KEY: your-scoped-api-key"
   ```

3. Describe the feature you want to build, for example:
   - *"Build a Sales Navigator lead search screen with seniority and headcount filters, using the Unipile API."*
   - *"Sync our users' WhatsApp and LinkedIn conversations into our inbox, with a webhook for new messages."*
   - *"Add Gmail, Outlook and IMAP sending to our sequences, with replies threaded under the original email."*

Configs for Cursor, VS Code, Codex, Gemini CLI, Windsurf and Claude Desktop are in [Setup](#setup).

## What you can build, route by route

Every route below is Unipile API v2 and runs on behalf of a connected account: `{account_id}` is its `acc_...` ID, from `GET /v2/accounts/`. This list is a map for you and your agent, not a schema: the agent should call `get-endpoint` on a route before writing its request body.

### LinkedIn MCP server: the LinkedIn API for your agent

| Feature in your product | Route |
|---|---|
| People search with LinkedIn filters (keywords, title, company, location, network distance) | `POST /v2/{account_id}/linkedin/search/people` |
| Company, post and job search | `POST /v2/{account_id}/linkedin/search/companies` · `/search/posts` · `/search/jobs` |
| Run a search straight from a LinkedIn search URL | `POST /v2/{account_id}/linkedin/search` |
| Look up filter IDs (locations, industries, companies, schools) | `GET /v2/{account_id}/linkedin/search/parameters` |
| Profile enrichment: experience, education, skills and other sections | `GET /v2/{account_id}/users/{user_id}?with_sections=...` |
| Send an invitation (connection request) with a note | `POST /v2/{account_id}/users/me/relation-requests` |
| List pending invitations, then accept or cancel them | `GET /v2/{account_id}/users/me/relation-requests` · `POST .../{request_id}/accept` · `POST .../{request_id}/cancel` |
| Relations, followers and following | `GET /v2/{account_id}/users/{user_id}/relations` · `/followers` · `/following` |
| Follow or unfollow a profile | `POST /v2/{account_id}/users/me/follow/{user_id}` · `/unfollow/{user_id}` |
| Remove a relation | `DELETE /v2/{account_id}/users/me/relations/{user_id}` |
| Send a LinkedIn message, or an InMail to someone outside the network | `POST /v2/{account_id}/chats/send` with `specifics.linkedin.classic.inmail: true` |
| Show remaining InMail credits | `GET /v2/{account_id}/linkedin/inmail-credits` |
| Company page data, and the pages the user manages | `GET /v2/{account_id}/linkedin/company/{company_id}` · `GET /v2/{account_id}/linkedin/company/pages` |
| Endorse a skill | `POST /v2/{account_id}/linkedin/member/{member_id}/endorse-skill` |
| Publish posts, comment, react; read a profile's activity | [Posts and engagement](#posts-and-engagement-linkedin-and-instagram) |
| Create, publish and close job postings; read applicants and resumes | `POST /v2/{account_id}/linkedin/jobs` · `POST .../jobs/{job_id}/publish` · `POST .../jobs/{job_id}/applicants` · `GET .../applicants/{applicant_id}/resume` |
| Call a LinkedIn endpoint that has no dedicated route yet | `POST /v2/{account_id}/linkedin/` |

### Sales Navigator MCP: the LinkedIn Sales Navigator API

The account needs a Sales Navigator seat. When a user holds several LinkedIn contracts, list them with `GET /v2/{account_id}/linkedin/contracts` and pick one with `POST .../contracts/{contract_id}/select`.

| Feature in your product | Route |
|---|---|
| Lead search with Sales Navigator filters (seniority, function, headcount, changed jobs, posted on LinkedIn...) | `POST /v2/{account_id}/linkedin/sales-navigator/search/people` |
| Account (company) search | `POST /v2/{account_id}/linkedin/sales-navigator/search/companies` |
| Import a search from a Sales Navigator URL or a saved search | `POST /v2/{account_id}/linkedin/sales-navigator/search` |
| Look up filter IDs | `GET /v2/{account_id}/linkedin/sales-navigator/search/parameters` |
| Lead lists: list, browse, save a lead | `GET .../sales-navigator/lead-lists` · `POST .../lead-lists/{list_id}` · `POST .../lead-lists/{list_id}/save` |
| Account lists: list, browse, save an account | `GET .../sales-navigator/account-lists` · `POST .../account-lists/{list_id}` · `POST .../account-lists/{list_id}/save` |
| Profile as Sales Navigator shows it | `GET /v2/{account_id}/users/{user_id}?variant=linkedin_sales_navigator` |
| Send a Sales Navigator InMail | `POST /v2/{account_id}/chats/send` with `specifics.linkedin.sales_navigator.subject` |

### LinkedIn Recruiter MCP: the LinkedIn Recruiter API

The account needs a Recruiter seat.

| Feature in your product | Route |
|---|---|
| Candidate search with Recruiter filters (skills, job title, years of experience, spoken language, workplace type...) | `POST /v2/{account_id}/linkedin/recruiter/search/people` |
| Import a search from a Recruiter URL or a saved search | `POST /v2/{account_id}/linkedin/recruiter/search` |
| Look up filter IDs | `POST /v2/{account_id}/linkedin/recruiter/search/parameters` |
| Candidate profile as Recruiter shows it, with recruiting activity | `GET /v2/{account_id}/users/{user_id}?variant=linkedin_recruiter&with_sections=linkedin_recruiting_activity` |
| Send a Recruiter InMail (subject, signature, follow-up; InMail or email) | `POST /v2/{account_id}/chats/send` with `specifics.linkedin.recruiter` |
| Hiring projects: list, create, edit | `GET` / `POST /v2/{account_id}/linkedin/recruiter/projects` · `PATCH .../projects/{project_id}` |
| Search a project's talent pool | `POST .../recruiter/projects/{project_id}/talent-pool/search` |
| Pipeline: list candidates, save a candidate to a project | `POST .../projects/{project_id}/pipeline` · `POST .../pipeline/candidate/save` |
| Applicants and their resumes | `POST .../projects/{project_id}/talent-pool/applicants` · `GET .../applicants/{applicant_profile_id}/resume` |
| Create, publish and close Recruiter job postings; check job slot credits | `POST .../recruiter/jobs` · `POST .../projects/{project_id}/jobs/{job_id}/publish` · `GET .../recruiter/job-slots-credits` |

### WhatsApp MCP, Instagram MCP, Telegram MCP: one messaging API with LinkedIn

One set of routes serves every messaging provider: WhatsApp chats and groups, Instagram DMs, Telegram chats and groups, and LinkedIn messages. A unified inbox is one integration, not four.

| Feature in your product | Route |
|---|---|
| Inbox: list chats, or the chats of one inbox | `GET /v2/{account_id}/chats` · `GET /v2/{account_id}/inboxes/{inbox_id}/chats` |
| Conversation view: read a chat's messages | `GET /v2/{account_id}/chats/{chat_id}/messages` |
| Find the existing chat with a contact | `GET /v2/{account_id}/users/{user_id}/chat` |
| Start a new chat (1:1 or group) with a first message | `POST /v2/{account_id}/chats/send` |
| Reply in a chat, with attachments | `POST /v2/{account_id}/chats/{chat_id}/messages/send` |
| Forward, edit, delete, mark as read | `POST .../messages/{message_id}/forward` · `/modify` · `DELETE .../messages/{message_id}` · `POST .../read` |
| Reactions | `POST .../messages/{message_id}/reactions` |
| Group chats: add or remove participants | `POST .../chats/{chat_id}/participants` · `DELETE .../participants/{user_id}` |
| Download an attachment | `GET .../messages/{message_id}/attachments/{attachment_id}` |
| "Typing..." indicator and online presence | `POST .../chats/{chat_id}/composing` · `POST /v2/{account_id}/presence` |

### Email MCP: the Gmail, Outlook and IMAP email API

One schema for all three providers, so you write the email integration once.

| Feature in your product | Route |
|---|---|
| List or search emails, or the emails of one folder | `GET /v2/{account_id}/emails` · `GET /v2/{account_id}/folders/{folder_id}/emails` |
| Read an email or a whole thread | `GET /v2/{account_id}/emails/{email_id}` · `GET /v2/{account_id}/threads/{thread_id}` |
| Send, reply and forward | `POST /v2/{account_id}/emails/send` |
| Drafts: create, edit, send | `POST /v2/{account_id}/drafts` · `PATCH .../drafts/{draft_id}` · `POST .../drafts/{draft_id}/send` |
| Mark as read or unread, move, trash | `POST .../emails/{email_id}/read` · `/unread` · `/modify` · `DELETE .../emails/{email_id}` |
| Folders | `GET` / `POST /v2/{account_id}/folders` · `PATCH` / `DELETE .../folders/{folder_id}` |
| Download an attachment | `GET .../emails/{email_id}/attachments/{attachment_id}` |
| Contacts and frequent senders | `GET /v2/{account_id}/contacts` · `GET /v2/{account_id}/email-senders` |

### Calendar MCP: Google Calendar and Outlook Calendar API

| Feature in your product | Route |
|---|---|
| List calendars and events | `GET /v2/{account_id}/calendars` · `GET .../calendars/{calendar_id}/events` |
| Book or reschedule an event | `POST .../calendars/{calendar_id}/events` · `PATCH .../events/{event_id}` |
| Accept or decline an invitation | `POST .../events/{event_id}/rsvp` |
| Cancel, restore or delete an event | `POST .../events/{event_id}/cancel` · `/restore` · `DELETE .../events/{event_id}` |
| Create, update or delete a calendar | `POST /v2/{account_id}/calendars` · `PATCH` / `DELETE .../calendars/{calendar_id}` |

### Posts and engagement: LinkedIn and Instagram

| Feature in your product | Route |
|---|---|
| Publish a post, or an Instagram story | `POST /v2/{account_id}/posts` · `POST /v2/{account_id}/posts/stories` |
| A LinkedIn or Instagram profile's posts, comments and reactions | `GET .../users/{user_id}/posts` · `/comments` · `/reactions` |
| A post, its comments and its reactions | `GET .../posts/{post_id}` · `/comments` · `/reactions` |
| Comment, reply to a comment, react | `POST .../posts/{post_id}/comments` · `POST .../comments/{comment_id}` · `POST .../posts/{post_id}/reactions` |
| Search Instagram locations | `GET /v2/{account_id}/instagram/search/locations` |

### Account connection, multi-tenancy and webhooks

| Feature in your product | Route |
|---|---|
| "Connect your LinkedIn / WhatsApp / Gmail" button, through a Unipile-hosted page | `POST /v2/auth/link` |
| Connection flow in your own UI, with 2FA/OTP checkpoints | `POST /v2/auth/intent` · `POST /v2/auth/checkpoint` |
| Connected accounts and their status, filtered by provider, status or Scope | `GET /v2/accounts/` · `GET /v2/accounts/{account_id}` |
| One Scope and one scoped key per customer or tenant *(your backend, Service key)* | `POST /v2/scopes/` · `POST /v2/api-keys/` |
| Real-time new messages, emails and account events instead of polling *(your backend, Service key)* | `POST /v2/webhooks/endpoints/` |

## API version: v2 by default, v1 still available

The `branch` query parameter picks which Unipile API the server reads from and calls. **Use `branch=v2.0`**: every example in this README targets v2. If your integration still runs on the v1 API, switch to `branch=v1.0` and put your v1 access token in `X-API-KEY`; the rest of the client config stays the same.

v1 and v2 are **separate environments**. An account connected in one is not visible from the other, and a key from one does not work on the other. Use the branch that matches the environment your accounts live in.

|  | v2 (`?branch=v2.0`, recommended) | v1 (`?branch=v1.0`) |
|---|---|---|
| Dashboard | [dashboardv2.unipile.com](https://dashboardv2.unipile.com/) | [dashboard.unipile.com](https://dashboard.unipile.com/) |
| Credentials | An API key only | An access token **plus** your DSN (`https://apiX.unipile.com:XXXXX`) |
| Base URL | `https://api.unipile.com` | Your DSN |
| Routes | `/v2/...`, 179 operations | `/api/v1/...`, 94 operations |
| Accounts | Accounts connected in the v2 environment | Accounts connected in the v1 environment |
| API reference | [developer.unipile.com/v2.0/reference](https://developer.unipile.com/v2.0/reference) | [developer.unipile.com/v1.0/reference](https://developer.unipile.com/v1.0/reference) |

On v1, the agent reads your DSN from the `get-server-variables` tool and must be given it before calling `execute-request`.

## API keys

The key goes in the `X-API-KEY` header of the MCP connection. It is optional for reading the API reference: without a key, the agent can still search endpoints and read their schemas. It is required for `execute-request`.

v2 has three kinds of key. **Give an MCP client a scoped Account API key only:**

| Key | Reaches | With an MCP client |
|---|---|---|
| **Scoped Account API key** | Only the accounts assigned to one Scope | **Use this one.** Create a [Scope](https://developer.unipile.com/v2.0/docs/scopes), assign the test accounts the agent may use, then create a [scoped key](https://developer.unipile.com/v2.0/docs/api-keys) for it |
| **Global Account API key** | Every account in the application | Do not use: it reaches all your users' accounts |
| **Service API key** | Application management: Scopes, API keys, webhook endpoints | Do not use: keep it in your backend |

The agent can still read the schemas of the management routes (`/v2/scopes`, `/v2/api-keys`, `/v2/webhooks`) and write the backend code that calls them with your Service key. Never commit a key to a shared repository.

## Tools

On `branch=v2.0` the server exposes five tools:

| Tool | What it does |
|---|---|
| `search-endpoints` | Searches paths, operations and parameters, for example `sales-navigator`, `inmail` or `relation-requests` |
| `list-specs` | Lists the available OpenAPI specs; the others take the spec `title` as a parameter (`Unipile API`) |
| `list-endpoints` | Lists every path and method with its summary |
| `get-endpoint` | Returns one operation's full request/response schema, security and servers |
| `execute-request` | Runs the request for real (a HAR object) against your own accounts |

On `branch=v1.0`, `get-server-variables` replaces `list-specs` and the tools take no `title`.

## Setup

Every client below speaks Streamable HTTP and takes the key in an `X-API-KEY` header. For v1, replace `v2.0` with `v1.0` in the URL and use your v1 access token as the key.

<details>
<summary>Cursor: <code>~/.cursor/mcp.json</code> or <code>.cursor/mcp.json</code></summary>

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

Installed as a plugin from the Cursor Marketplace, the server reads the key from the `UNIPILE_API_KEY` environment variable instead.
</details>

<details>
<summary>VS Code: <code>.vscode/mcp.json</code></summary>

```json
{
  "inputs": [
    { "type": "promptString", "id": "unipile_api_key", "description": "Unipile scoped Account API key", "password": true }
  ],
  "servers": {
    "unipile": {
      "type": "http",
      "url": "https://developer.unipile.com/mcp?branch=v2.0",
      "headers": { "X-API-KEY": "${input:unipile_api_key}" }
    }
  }
}
```
</details>

<details>
<summary>Claude Code: <code>claude mcp add</code></summary>

```bash
claude mcp add --transport http unipile "https://developer.unipile.com/mcp?branch=v2.0" --header "X-API-KEY: your-scoped-api-key"
```
</details>

<details>
<summary>Codex: <code>~/.codex/config.toml</code> or <code>.codex/config.toml</code></summary>

```toml
[mcp_servers.unipile]
url = "https://developer.unipile.com/mcp?branch=v2.0"
http_headers = { "X-API-KEY" = "your-scoped-api-key" }
```
</details>

<details>
<summary>Gemini CLI: <code>~/.gemini/settings.json</code></summary>

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
<summary>Windsurf: <code>~/.codeium/windsurf/mcp_config.json</code>. Claude Desktop: <code>claude_desktop_config.json</code></summary>

```json
{
  "mcpServers": {
    "unipile": {
      "type": "http",
      "url": "https://developer.unipile.com/mcp?branch=v2.0",
      "headers": { "X-API-KEY": "your-scoped-api-key" }
    }
  }
}
```
</details>

Any other MCP client or agent framework (OpenAI Agents SDK, Claude Agent SDK, LangChain, LlamaIndex, CrewAI, a custom client) connects the same way: Streamable HTTP with header auth.

## From the editor to production

- **SDKs:** [Node.js/TypeScript](https://github.com/unipile/unipile-node-sdk) and [Python](https://github.com/unipile/unipile-python) wrap the same endpoints the agent discovers through MCP. Ask the agent to use them in the code it writes.
- **n8n:** [`@unipile/n8n-nodes-unipile`](https://github.com/unipile/n8n-nodes-unipile) is a community node that exposes the same channels as typed resources and operations, for workflows with no code and no agent in the loop.

## FAQ

**Is there a LinkedIn MCP server?**
LinkedIn does not publish an official one. The Unipile MCP server is a LinkedIn MCP server for coding agents, built on the Unipile LinkedIn API. It acts on the LinkedIn accounts your users connect, within each account's own limits.

**Is there a Sales Navigator MCP or a LinkedIn Recruiter MCP?**
Yes, in the same server. Sales Navigator has its own lead and account search, lead lists and InMail; Recruiter has its own candidate search, hiring projects, pipeline and InMail. See [Sales Navigator MCP](#sales-navigator-mcp-the-linkedin-sales-navigator-api) and [LinkedIn Recruiter MCP](#linkedin-recruiter-mcp-the-linkedin-recruiter-api).

**Is there a WhatsApp MCP, an Instagram MCP or a Telegram MCP?**
Yes. WhatsApp chats and groups, Instagram DMs and Telegram chats share the same messaging routes as LinkedIn messages. Instagram also has posts, stories, comments and location search, under [Posts and engagement](#posts-and-engagement-linkedin-and-instagram).

**Is there a Gmail MCP, an Outlook MCP or an IMAP MCP?**
Yes. One email schema covers Gmail, Outlook and any IMAP mailbox: search, read threads, send, reply, drafts, folders and attachments.

**Does my product need MCP in production?**
No. The agent uses MCP to discover and test the API while you build. Your product calls the Unipile REST API, or an SDK, directly.

**Which coding agents does it work with?**
Any client that supports remote MCP servers over Streamable HTTP with a custom header: Cursor, Claude Code, Codex, Gemini CLI, VS Code, Windsurf and Claude Desktop, plus agent frameworks.

**Should I use v1 or v2?**
v2, unless your accounts are in the v1 environment. See [API version](#api-version-v2-by-default-v1-still-available).

## Notes

- Only repositories under `github.com/unipile/*` are official. Other GitHub repositories built on the Unipile API are third-party projects that Unipile does not maintain.
- This repository is the distribution kit for the hosted server: registry manifest, directory listing copy and setup notes. It does not run a second server. The URL at the top, documented at [developer.unipile.com/docs/mcp](https://developer.unipile.com/docs/mcp), is the only one.

## Registry manifest

[`server.json`](./server.json) is the [MCP registry](https://github.com/modelcontextprotocol/registry) manifest for this server. It is used for the official registry submission and by directories that ingest it (Glama, PulseMCP, mcp.so...). It declares `branch` as a URL variable (`v2.0` by default, `v1.0` optional) and `X-API-KEY` as a required secret header.
