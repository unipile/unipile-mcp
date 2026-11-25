# Unipile Developer MCP: the LinkedIn API, WhatsApp, Facebook, email and calendar APIs inside Claude

Unipile is the API that SaaS teams use to add LinkedIn (Classic, Sales Navigator and Recruiter), WhatsApp, Instagram, Facebook, Telegram, email (Gmail, Outlook, IMAP) and calendar (Google, Outlook) features to their own product. Their users connect their own accounts, and the product acts on those accounts through one REST API.

This plugin connects Claude to the Unipile **Developer MCP**, the official MCP server for building with the API. While you build, Claude searches the Unipile API reference by intent, reads the exact parameters and response schema of the route it needs, writes the integration in your stack, and tests the call on your own connected test accounts. It works from the live API reference, not from memory, so it doesn't invent endpoints or fields.

To let Claude work with your own accounts day to day rather than build a product, use the [Unipile User MCP](https://developer.unipile.com/v2.0/docs/user-mcp) instead.

## What you can build with it

- **LinkedIn API:** people, company, post and job search, profile enrichment, invitations, messages and InMail, company pages, groups, events, job postings and applicants.
- **Sales Navigator API:** lead and account search with Sales Navigator filters, lead and account lists, Sales Navigator InMail.
- **LinkedIn Recruiter API:** candidate search, hiring projects, pipelines, applicants and Recruiter InMail.
- **Facebook:** Messenger conversations, including encrypted chats, Pages, posts, comments and reactions, groups, events and search.
- **Unified messaging:** WhatsApp, Instagram, Facebook Messenger, Telegram and LinkedIn chats through one set of routes: chats, messages, attachments, reactions, groups and blocked users.
- **Email API:** Gmail, Outlook and IMAP with one schema: search, threads, send and reply, drafts, folders, attachments and Outlook categories.
- **Calendar API:** Google and Outlook calendars, events and RSVPs.
- **Production plumbing:** the hosted "Connect your account" page, multi-tenant Scopes and keys, and webhooks for new messages, emails and account events.

## Try it

- "Add a 'Connect LinkedIn' button to my app with Unipile hosted auth, then list the connected accounts."
- "Write a function that sends a LinkedIn invitation with a note, and test it on my connected account."
- "Build a Sales Navigator lead search with seniority and headcount filters."
- "Build an inbox view that lists WhatsApp, Messenger and LinkedIn chats together, newest first."
- "Add Gmail and Outlook sending to our sequences, with replies threaded under the original email."

## Setup

Install it from the Claude plugin directory, or in Claude Code:

```
/plugin install unipile-developer --marketplace unipile/unipile-mcp
```

The plugin asks for one optional value when you enable it: an **Account API key**.

- **Without a key**, Claude can search and read the whole API reference. That is enough to design and write an integration.
- **With a key**, Claude can also run requests on the accounts that key can reach and check the real responses.

Use a scoped key. In the [Unipile dashboard](https://dashboardv2.unipile.com/), connect a test account (LinkedIn, WhatsApp, Gmail...), create a [Scope](https://developer.unipile.com/v2.0/docs/scopes) with only that account, then create a [scoped Account API key](https://developer.unipile.com/v2.0/docs/api-keys) for that Scope. The development key that the dashboard's **Connect my project** guide creates is global: it reaches every account in your application and expires after 90 days. Never use a Service key here. Claude Code stores the key in your system's secure credential store, not in a settings file.

## What the plugin contains and where data goes

- **One remote MCP server**, `https://developer.unipile.com/mcp?branch=v2.0`, operated by Unipile. Your key, if you set one, is sent to it in the `X-API-KEY` header.
- **One skill**, `unipile-api`, which tells Claude how to use the server: find the route, read its schema, write the code, then test it.

The server exposes five tools:

| Tool | What it does | Effect |
|---|---|---|
| `search-endpoints` | Finds the routes that match a keyword, such as `sales-navigator`, `inmail` or `emails` | Read-only |
| `list-specs` | Lists the available API specifications | Read-only |
| `list-endpoints` | Lists every route with its summary | Read-only |
| `get-endpoint` | Returns one route's parameters, request body, response schema and auth | Read-only |
| `execute-request` | Sends a real request to the Unipile API (`https://api.unipile.com`) with your key and returns the response | Acts on your connected accounts |

`execute-request` can send messages, invitations or emails and delete data on the accounts your key can reach. The skill tells Claude to ask you before any request that writes, sends or deletes. The plugin runs no local code, no hooks and no other network calls.

## API version

The plugin uses Unipile API v2. If your accounts are on the v1 API, add the server yourself with `branch=v1.0` and your v1 access token:

```bash
claude mcp add --transport http unipile-v1 "https://developer.unipile.com/mcp?branch=v1.0" --header "X-API-KEY: your-v1-access-token"
```

## Links

- Documentation: [Developer MCP](https://developer.unipile.com/v2.0/docs/developer-mcp)
- API reference: [developer.unipile.com/v2.0/reference](https://developer.unipile.com/v2.0/reference)
- Support: [unipile.com/contact-us](https://www.unipile.com/contact-us/) · Status: [status.unipile.com](https://status.unipile.com/)
- [Privacy policy](https://www.unipile.com/privacy-policy/) · [Terms of use](https://www.unipile.com/terms-of-use/)

Published by Unipile SAS (France). Unipile is not affiliated with or endorsed by LinkedIn, Meta, Telegram, Google or Microsoft.
