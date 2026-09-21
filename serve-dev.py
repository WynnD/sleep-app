#!/usr/bin/env python3
"""Dev server for sleep-app: serves public/ with Cache-Control: no-store."""
import http.server, socketserver, functools, sys

PORT = 8777
DIRECTORY = "/home/wynn/projects/sleep-app/public"

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

class ThreadingTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

with ThreadingTCPServer(("0.0.0.0", PORT), NoCacheHandler) as httpd:
    print(f"serving {DIRECTORY} at :{PORT}, no-cache", flush=True)
    httpd.serve_forever()
