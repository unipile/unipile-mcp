"""Distribution contract checks. Run: python3 -m unittest discover -s tests -v."""
import json
from pathlib import Path
import re
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
URL = "https://developer.unipile.com/mcp?branch=v2.0"


class ConnectorTests(unittest.TestCase):
    def test_gemini_extension_contract(self):
        manifest = json.loads((ROOT / "gemini-extension.json").read_text())
        self.assertRegex(manifest["name"], r"^[a-z0-9-]+$")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertIsInstance(manifest["description"], str)
        server = manifest["mcpServers"]["unipile"]
        self.assertEqual(server["httpUrl"], URL)
        self.assertNotIn("url", server)  # url means SSE in Gemini CLI
        self.assertNotIn("trust", server)
        self.assertEqual(server["headers"], {"X-API-KEY": "${UNIPILE_API_KEY}"})
        setting, = manifest["settings"]
        self.assertEqual(setting["envVar"], "UNIPILE_API_KEY")
        self.assertIs(setting["sensitive"], True)
        for field in ("name", "description"):
            self.assertIsInstance(setting[field], str)

    def test_grok_native_contract(self):
        config = tomllib.loads((ROOT / "connectors/grok.toml").read_text())
        server = config["mcp_servers"]["unipile"]
        self.assertEqual(server["url"], URL)
        self.assertEqual(server["headers"], {"X-API-KEY": "${UNIPILE_API_KEY:-}"})
        self.assertNotIn("command", server)

    def test_existing_distribution_stays_on_v2(self):
        for filename in (".mcp.json", "mcp.json"):
            server = json.loads((ROOT / filename).read_text())["mcpServers"]["unipile"]
            self.assertEqual(server["url"], URL)
            self.assertEqual(server.get("type", "http"), "http")
            self.assertIn("X-API-KEY", server["headers"])

    def test_all_distribution_json_parses(self):
        for path in ROOT.rglob("*.json"):
            if ".git" not in path.parts:
                with self.subTest(path=str(path.relative_to(ROOT))):
                    self.assertIsInstance(json.loads(path.read_text()), dict)

    def test_documented_gemini_settings_use_http(self):
        readme = (ROOT / "README.md").read_text()
        section = readme.split("<summary>Gemini CLI: <code>", 1)[1].split("</details>", 1)[0]
        snippet, = re.findall(r"```json\n(.*?)\n```", section, re.S)
        server = json.loads(snippet)["mcpServers"]["unipile"]
        self.assertEqual(server["httpUrl"], URL)
        self.assertEqual(set(server["headers"]), {"X-API-KEY"})


if __name__ == "__main__":
    unittest.main()
