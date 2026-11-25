---
name: unipile-api
description: Use when building, extending or debugging a product integration with the Unipile API, for LinkedIn (Classic, Sales Navigator, Recruiter), WhatsApp, Instagram, Telegram, Gmail, Outlook or IMAP email, Google or Outlook calendar, hosted account connection, Scopes or webhooks. Look up the real route and schema with the Unipile MCP tools before writing any request.
---

# Build with the Unipile API

The `unipile` MCP server exposes the live Unipile API v2 reference. Use it instead of what you remember about the API: routes, field names and filters change, and the reference is always current.

## Workflow

1. **Find the route.** Call `search-endpoints` with a short keyword, such as `relation-requests`, `sales-navigator`, `inmail`, `emails`, `calendars` or `webhooks`. Use `list-endpoints` to browse a whole area.
2. **Pick the spec.** `get-endpoint` and `list-endpoints` take a spec `title`. Call `list-specs` once and use the title it returns. If it lists more than one v2 spec, use `Unipile API (reference)`, which is the complete one.
3. **Read the contract.** Call `get-endpoint` with the path, method and title before writing a request body. Take the base URL, auth scheme, required fields and enum values from its answer.
4. **Write the code** in the user's stack. If the project already uses the Unipile [Node.js](https://github.com/unipile/unipile-node-sdk) or [Python](https://github.com/unipile/unipile-python) SDK, use it. Read the API key from the project's configuration or environment, and never write a key into code or commit it.
5. **Test it** with `execute-request` when the user has set a key. Read requests (lists, searches, profiles) can run directly. Before any request that sends, posts, invites, reacts, edits or deletes, show the user the exact request and wait for their go-ahead: it acts on a real account.

If `execute-request` fails with an authentication error, the plugin has no key or the key is wrong. Tell the user to set a scoped Account API key in the plugin's configuration. Never ask them to paste a key into the chat.

## Things to get right

- **`{account_id}`** in a path is the `acc_...` ID of a connected account, from `GET /v2/accounts/`. Each request runs on behalf of that account.
- **LinkedIn products are separate.** Classic, Sales Navigator and Recruiter each have their own search routes, filter IDs and InMail options under `specifics`. Use the routes for the product the user's account has; don't fall back to Classic when they asked for Sales Navigator or Recruiter.
- **Search filters use IDs.** Locations, industries, companies and schools are IDs from the matching `search/parameters` route, not free text.
- **Messaging is unified.** WhatsApp, Instagram, Telegram and LinkedIn messages share the `chats` routes. Email has its own unified routes for Gmail, Outlook and IMAP.
- **Keys.** The MCP server and test calls take a scoped Account API key, which only reaches the accounts of one Scope. Scopes, API keys and webhook endpoints are managed with a Service key, from the user's backend only.
- **v1 and v2 are separate environments.** This plugin targets v2 (`/v2/...` on `https://api.unipile.com`). An account or key from v1 doesn't work on v2.

Documentation: https://developer.unipile.com/docs/mcp
