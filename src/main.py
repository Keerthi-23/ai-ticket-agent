import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class AgentHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/run-agent':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            
            try:
                data = json.loads(body.decode('utf-8'))
                query = data.get("natural_language_query", "")
            except Exception:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Invalid JSON payload"}')
                return

            if not query:
                self.send_response(422)
                self.end_headers()
                self.wfile.write(b'{"error": "Missing natural_language_query"}')
                return

            # Native intent parsing logic
            query_lower = query.lower()
            if "bug" in query_lower or "create" in query_lower:
                parsed_intent = {
                    "intent": "create_ticket",
                    "project_id": "Alpha",
                    "subject": query,
                    "priority": "high",
                    "status": "open"
                }
            else:
                parsed_intent = {
                    "intent": "get_sprint_status",
                    "project_id": "Alpha",
                    "subject": query,
                    "priority": "medium",
                    "status": "in_progress"
                }

            response_data = {
                "status": "success",
                "mode": "100% Native Python Standard Library (Zero External Dependencies)",
                "parsed_intent": parsed_intent,
                "action_taken": "Successfully processed prompt and routed to mock ticketing layer.",
                "target_system": "Redmine API / Nextcloud Webhook Simulator",
                "api_response": {
                    "ticket_id": "TICKET-405",
                    "url": "https://mock-redmine-sandbox.local/issues/405",
                    "status": "Created successfully in mock sandbox"
                }
            }

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Suppress default server logs during tests
        return

def run(server_class=HTTPServer, handler_class=AgentHandler, port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server started on http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()