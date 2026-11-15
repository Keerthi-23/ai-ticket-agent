# AI Ticket Agent

An autonomous, LLM-powered background service that bridges chat platforms (like Nextcloud Talk or Slack) with REST-based ticketing systems. 

Instead of manual ticket management, users type natural language commands in chat. Claude parses the intent, extracts the payload, and executes the appropriate create, update, or query actions against the ticketing API.

## Workflow

```text
[ Chat Webhook ] ➔ [ Router / API ] ➔ [ Claude AI (Intent Parsing) ] ➔ [ Ticketing REST API ]
```

## Tech Stack
- **Language:** Python 3.10+
- **AI Engine:** Anthropic Claude API
- **Integration:** REST APIs & Webhooks
- **Deployment:** Docker, Docker Compose, GitHub Actions CI

---

## Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/Keerthi-23/ai-ticket-agent.git
cd ai-ticket-agent
```

### 2. Set Up Environment Variables
Copy the template file and fill in your API tokens and endpoints:
```bash
cp .env.example .env
```

### 3. Install Dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Application
You can run it natively or via Docker Compose:

* **Locally:**
  ```bash
  python src/agent.py
  ```
* **Via Docker:**
  ```bash
  docker-compose up --build
  ```

## Testing
Run the test suite using pytest:
```bash
pytest tests/
```

## License
MIT License. See `LICENSE` for details.