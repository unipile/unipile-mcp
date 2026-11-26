# Unipile Developer: the Unipile API reference inside Claude Code

Unipile is a REST API that software teams use to add LinkedIn (Classic, Sales Navigator and Recruiter), WhatsApp, Instagram, Facebook, Telegram, email (Gmail, Outlook, IMAP) and calendar (Google, Outlook) features to their own product, for the accounts their own users connect.

This plugin gives Claude Code the Unipile API reference, through the read-only **Developer MCP**. While you code, Claude searches the reference by intent, reads the exact parameters and response schema of the route it needs, and writes the integration in your stack. It works from the live reference, not from memory, so it doesn't invent endpoints or fields.

The plugin is documentation only. It holds no API key and doesn't call the Unipile API or any account: you run the code Claude writes in your own environment, with your own keys.

## What the reference covers

- **LinkedIn API:** search for people, companies, posts and jobs, profiles, relations, messaging and InMail, company pages, job postings and applicants.
- **Sales Navigator API:** lead and account search with Sales Navigator filters, lead and account lists.
- **LinkedIn Recruiter API:** candidate search, hiring projects, pipelines and applicants.
- **Facebook:** Messenger conversations, Pages, posts, comments, groups and events.
- **Unified messaging:** WhatsApp, Instagram, Facebook Messenger, Telegram and LinkedIn chats through one set of routes.
- **Email API:** Gmail, Outlook and IMAP with one schema: search, threads, drafts, folders and attachments.
- **Calendar API:** Google and Outlook calendars and events.
- **Production plumbing:** the hosted "Connect your account" page, multi-tenant Scopes and API keys, and webhooks.

## Try it

- "Add a 'Connect LinkedIn' button to my app with Unipile hosted auth."
- "Which route returns a LinkedIn profile, and what does its response look like?"
- "Write a typed client for the Sales Navigator lead search, with seniority and headcount filters."
- "Build an inbox view that lists WhatsApp, Messenger and LinkedIn chats together, newest first."
- "Add a webhook handler for new emails, with the payload types from the reference."

## Setup

In Claude Code:

```
/plugin install unipile-developer --marketplace unipile/unipile-mcp
```

Nothing to configure: the plugin needs no account and no key.

## What the plugin contains and where data goes

- **One remote MCP server**, `https://developer.unipile.com/mcp?branch=v2.0`, the Unipile API documentation server. Claude sends it search terms and route names, nothing from your project.
- **One skill**, `unipile-api`, which tells Claude how to use it: find the route, read its schema, then write the code.

Claude uses four read-only tools from that server:

| Tool | What it does |
|---|---|
| `search-endpoints` | Finds the routes that match a keyword, such as `sales-navigator`, `inmail` or `emails` |
| `list-specs` | Lists the available API specifications |
| `list-endpoints` | Lists every route with its summary |
| `get-endpoint` | Returns one route's parameters, request body, response schema and auth |

The documentation server also lists an `execute-request` tool from its documentation platform. The plugin sends no key, so that tool can't reach any account, and the skill tells Claude not to use it. The plugin runs no local code, no hooks and no other network calls.

## API version

The plugin uses the Unipile API v2 reference (`/v2/...` routes).

## Links

- Documentation: [Developer MCP](https://developer.unipile.com/v2.0/docs/developer-mcp)
- API reference: [developer.unipile.com/v2.0/reference](https://developer.unipile.com/v2.0/reference)
- Support: [unipile.com/contact-us](https://www.unipile.com/contact-us/) · Status: [status.unipile.com](https://status.unipile.com/)
- [Privacy policy](https://www.unipile.com/privacy-policy/) · [Terms of use](https://www.unipile.com/terms-of-use/)

Published by Unipile SAS (France). Unipile is not affiliated with or endorsed by LinkedIn, Meta, Telegram, Google or Microsoft.
