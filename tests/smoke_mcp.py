"""Read-only, credential-free hosted MCP smoke check (Python standard library + curl)."""
import json
import subprocess

URL = "https://developer.unipile.com/mcp?branch=v2.0"


def rpc(method, request_id, params):
    payload = {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params}
    # curl works with the hosted endpoint's edge protection in this environment.
    completed = subprocess.run([
        "curl", "--fail-with-body", "--silent", "--show-error", "--max-time", "30",
        URL, "-H", "Content-Type: application/json",
        "-H", "Accept: application/json, text/event-stream",
        "--data", json.dumps(payload),
    ], check=True, capture_output=True, text=True)
    body = completed.stdout
    if body.lstrip().startswith("{"):
        result = json.loads(body)
    else:
        messages = [json.loads(line[6:]) for line in body.splitlines()
                    if line.startswith("data: ")]
        result, = [message for message in messages if message.get("id") == request_id]
    if "error" in result:
        raise RuntimeError(result["error"])
    return result["result"]


if __name__ == "__main__":
    initialized = rpc("initialize", 1, {
        "protocolVersion": "2025-03-26", "capabilities": {},
        "clientInfo": {"name": "unipile-connector-check", "version": "1.0.0"},
    })
    assert initialized["protocolVersion"] == "2025-03-26", initialized
    listed = rpc("tools/list", 2, {})
    names = {tool["name"] for tool in listed["tools"]}
    expected = {"search-endpoints", "list-specs", "list-endpoints", "get-endpoint", "execute-request"}
    assert names == expected, names
    for tool in listed["tools"]:
        assert tool["inputSchema"]["type"] == "object", tool["name"]
    print("Hosted MCP initialized; five v2 tools and input schemas verified (no execution).")
