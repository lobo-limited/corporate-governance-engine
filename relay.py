#!/usr/bin/env python3
"""
Relay + static file server for corporate-governance-engine.

Routes:
  GET  /                → serves corporate-governance-engine.html
  GET  /static/<file>   → serves files from the same directory
  POST /api/chat        → proxies to: opencode run --agent corporate-governance-engine

Usage:
    python3 relay.py          # port 3456
    python3 relay.py 8080     # custom port
"""

import http.server
import json
import mimetypes
import os
import subprocess
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3456
AGENT = "corporate-governance-engine"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "corporate-governance-engine.html")


class RelayHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(f"[relay] {fmt % args}")

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?")[0]

        if path == "/" or path == "/index.html":
            self._serve_file(INDEX_FILE)
        elif path.startswith("/static/"):
            filename = path[len("/static/"):]
            self._serve_file(os.path.join(BASE_DIR, filename))
        else:
            self.send_response(404)
            self.end_headers()

    def _serve_file(self, filepath):
        if not os.path.isfile(filepath):
            self.send_response(404)
            self.end_headers()
            return
        mime, _ = mimetypes.guess_type(filepath)
        mime = mime or "application/octet-stream"
        with open(filepath, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", len(data))
        self._cors()
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        message = body.get("message", "").strip()

        if not message:
            self._json(400, {"error": "empty message"})
            return

        try:
            result = subprocess.run(
                ["opencode", "run", "--agent", AGENT, message],
                capture_output=True,
                text=True,
                timeout=120,
            )
            response_text = result.stdout.strip() or result.stderr.strip() or "(no output)"
            self._json(200, {"response": response_text})
        except subprocess.TimeoutExpired:
            self._json(504, {"error": "agent timed out after 120s"})
        except FileNotFoundError:
            self._json(503, {"error": "opencode not found in PATH"})
        except Exception as exc:
            self._json(500, {"error": str(exc)})

    def _json(self, status, payload):
        data = json.dumps(payload).encode()
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", PORT), RelayHandler)
    print(f"[relay] http://localhost:{PORT}")
    print(f"[relay] routing /api/chat → opencode run --agent {AGENT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[relay] stopped")
