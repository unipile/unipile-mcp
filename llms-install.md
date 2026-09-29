# Installing the Unipile MCP server

The Unipile MCP server is hosted. There is nothing to clone, build or run locally: add one remote server entry to the client configuration.

- Transport: Streamable HTTP
- URL: `https://developer.unipile.com/mcp?branch=v2.0`
- Header: `X-API-KEY: <scoped Account API key>`

## 1. Get a key from the user

Ask the user for a **scoped Account API key** from the [Unipile dashboard](https://dashboardv2.unipile.com/). If they do not have one yet, they need to:

1. Connect a test account (LinkedIn, WhatsApp, Gmail...) in the dashboard.
2. Create a [Scope](https://developer.unipile.com/v2.0/docs/scopes) and assign that account to it.
3. Create a [scoped key](https://developer.unipile.com/v2.0/docs/api-keys) for the Scope.

Do not accept a Global Account API key or a Service API key: they reach every account of the application. Never write the key anywhere other than the MCP configuration.

The key is optional for reading the API reference (`list-endpoints`, `get-endpoint`, `search-endpoints`, `list-specs`) and required for `execute-request`. If the user has no key yet, install the server without the header and add it later.

## 2. Add the server

In Cline, add this entry to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "unipile": {
      "type": "streamableHttp",
      "url": "https://developer.unipile.com/mcp?branch=v2.0",
      "headers": { "X-API-KEY": "<scoped Account API key>" }
    }
  }
}
```

If the user's integration still runs on the v1 API, use `branch=v1.0` in the URL and their v1 access token as `X-API-KEY`.

## 3. Check it works

List the tools. The server exposes five: `list-endpoints`, `get-endpoint`, `search-endpoints`, `list-specs` and `execute-request`. Then call `search-endpoints` with a query such as `send linkedin invitation` to confirm the connection.
