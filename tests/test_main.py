import unittest
import json
import threading
import time
import urllib.request
from http.server import HTTPServer
from src.main import AgentHandler

class TestAgentServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(('127.0.0.1', 8001), AgentHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(0.1)  # Allow server to spin up

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_run_agent_success(self):
        url = "http://127.0.0.1:8001/run-agent"
        payload = json.dumps({"natural_language_query": "Create a high priority bug ticket for login failure"}).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
        
        try:
            with urllib.request.urlopen(req) as response:
                self.assertEqual(response.status, 200)
                data = json.loads(response.read().decode('utf-8'))
                self.assertEqual(data["status"], "success")
                self.assertEqual(data["parsed_intent"]["intent"], "create_ticket")
        except urllib.error.HTTPError as e:
            self.fail(f"HTTP Error: {e.code}")

    def test_run_agent_missing_field(self):
        url = "http://127.0.0.1:8001/run-agent"
        payload = json.dumps({}).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
        
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            urllib.request.urlopen(req)
        self.assertEqual(ctx.exception.code, 422)

if __name__ == '__main__':
    unittest.main()