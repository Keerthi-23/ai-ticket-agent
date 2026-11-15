from locust import HttpUser, task, between
import json

class AgentWebhookUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def simulate_chat_webhook(self):
        """Simulates high-throughput concurrent chat webhook arrivals."""
        headers = {"Content-Type": "application/json", "X-Webhook-Signature": "test_token_123"}
        payload = {
            "event": "message_created",
            "user": "qa_engineer_bot",
            "message": "Create a task to update SSL certificates before Friday."
        }
        self.client.post("/api/v1/webhook", data=json.dumps(payload), headers=headers)

    @task(1)
    def health_check(self):
        """Monitors system responsiveness under load."""
        self.client.get("/health")