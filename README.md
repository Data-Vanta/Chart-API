# Chart-API — README

FastAPI service that suggests charts, builds queries with an LLM, and executes them on a data-lakehouse.

This README includes full commands for macOS, Linux, and Windows (PowerShell / CMD).

---

## Prerequisites

- Python 3.11+
- Docker & Docker Compose v2
- Git / GitHub account
- (Optional) gh CLI for GitHub

---

## Environment

Copy .env.example or create `.env` in project root and set:

```
OPENROUTER_API_KEY=...
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=anthropic/claude-3.5
DATALAKE_BASE_URL=http://localhost:8080/api/v1
```

Set OS-specific environment examples below when necessary.

---

## Install & Run (Python API)

macOS / Linux (bash/zsh):

```bash
cd /Users/mahmoudibrahim/Documents/Data-Vanta/Chart-API
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Windows PowerShell:

```powershell
cd C:\Users\mahmoudibrahim\Documents\Data-Vanta\Chart-API
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Windows CMD:

```cmd
cd C:\Users\mahmoudibrahim\Documents\Data-Vanta\Chart-API
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Docs: http://127.0.0.1:8000/docs

---

## Run Data-Lakehouse (Docker Compose)

Navigate to your data-lakehouse folder:

macOS / Linux:

```bash
cd /Users/mahmoudibrahim/Documents/Data-Vanta/data-lakehouse
# optionally edit .env and docker-compose.yml first
docker compose build --pull
docker compose up -d
docker compose ps
docker compose logs -f
```

Windows PowerShell / CMD:

```powershell
cd C:\Users\mahmoudibrahim\Documents\Data-Vanta\data-lakehouse
docker compose build --pull
docker compose up -d
docker compose ps
docker compose logs -f
```

If some images cannot be pulled, build locally:

```bash
docker compose build api-service spark-worker
docker compose up -d
```

---

## Change Host Ports

Edit `docker-compose.yml` ports mappings (host:container). Example change:

```yaml
services:
  api-service:
    ports:
      - "8088:8080"
  minio:
    ports:
      - "9100:9000"
      - "9101:9001"
  postgres:
    ports:
      - "5433:5432"
  rabbitmq:
    ports:
      - "5673:5672"
      - "15673:15672"
  redis:
    ports:
      - "6382:6379"
```

After edit:

```bash
docker compose down
docker compose up -d --build
```

Update `.env` and Chart-API `DATALAKE_BASE_URL` accordingly.

---

## Common Tasks & Debugging

Check containers:

```bash
docker compose ps
docker ps -a
```

Tail logs:

```bash
docker compose logs -f api-service
docker compose logs -f spark-worker
```

Check RabbitMQ queues (management API):

```bash
curl -s -u admin:Data_lakehouse2025! http://localhost:15672/api/queues | jq .
# if port changed, update host port
```

List Redis job keys:

```bash
docker exec -it redis redis-cli -p 6379 KEYS "query:*"
docker exec -it redis redis-cli -p 6379 HGETALL "query:<jobid>"
```

MinIO (mc) setup & list:

```bash
# set alias (inside host terminal)
docker exec -it minio mc alias set local http://minio:9000 admin Data_lakehouse2025!
docker exec -it minio mc ls local/warehouse/wh/elm4r7a/sales/
```

If CLI mc cannot access host MinIO from host machine, use:

```bash
mc alias set local http://localhost:9000 admin Data_lakehouse2025!
mc ls local/warehouse/wh/elm4r7a/sales/
```

---

## Fetch Schema (example)

Get schema job queued then poll result (data-lakehouse service):

```bash
curl -s http://localhost:8080/api/v1/schema/elm4r7a/sales | jq .
# if response contains jobId, poll:
curl -s http://localhost:8080/api/v1/query/<jobId> | jq .
```

Chart-API convenience endpoint (when running Chart-API):

```bash
curl http://127.0.0.1:8000/schema/elm4r7a/sales/columns | jq .
```

---

## Read Parquet Results & Convert to JSON

Install tooling:

```bash
# macOS / Linux / Windows (inside venv)
pip install pandas pyarrow duckdb
```

Download parquet from MinIO (example):

```bash
docker exec minio mc cp local/warehouse/wh/testproj/queries/<jobid>/data.parquet /tmp/result.parquet
python - <<'PY'
import pandas as pd, json
df = pd.read_parquet('/tmp/result.parquet')
print(json.dumps({"rowCount": len(df), "columns": df.columns.tolist(), "data": df.to_dict("records")}, indent=2))
PY
```

Or query parquet with duckdb:

```bash
python - <<'PY'
import duckdb, json
df = duckdb.query("SELECT * FROM '/tmp/result.parquet'").to_df()
print(df.to_dict('records'))
PY
```

---

## Handling LLM JSON Output Issues

- Ensure LLM returns "select" as list of objects, not SQL strings.
- Chart-API includes prompt constraints and validation. If LLM returns invalid format, add stricter system prompt or post-process before sending to data-lakehouse.

---

## Git / PR from VS Code (Source Control)

1. Fork repo on GitHub (web).
2. Open project in VS Code.
3. Create new branch: click branch name in status bar → Create branch.
4. Make changes → Source Control view → Stage → Commit.
5. Add fork remote if push denied:

```bash
git remote add fork git@github.com:<your-username>/Chart-API.git
git push -u fork <branch-name>
```

6. Use VS Code GitHub Pull Requests extension:
   - Open GitHub pane → Create Pull Request → fill title/body → Create.

---

## Troubleshooting Tips

- 500 / connection reset: tail api-service logs immediately while making the request to capture stack trace.
- Missing S3 objects: ensure MinIO buckets exist and services have AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY and s3 path settings.
- If API images fail to pull, build from source or fix image names in `docker-compose.yml`.

---

## Quick Example Workflows

Upload CSV to data-lakehouse (example API):

```bash
curl -s -X POST "http://localhost:8080/api/v1/upload" \
  -F "file=@/path/to/test_data.csv" \
  -F "userId=testuser" \
  -F "projectId=elm4r7a" \
  -F "tableName=sales" | jq .
```

Suggest charts (Chart-API):

```bash
curl -s -X POST http://127.0.0.1:8000/suggest-charts \
  -H "Content-Type: application/json" \
  -d '{"user_prompts":["Show revenue by region"]}' | jq .
```

Execute prompt end-to-end:

```bash
curl -s -X POST http://127.0.0.1:8000/execute-prompt \
  -H "Content-Type: application/json" \
  -d '{"user_prompts":["Show revenue by region"], "project_id":"elm4r7a", "table_name":"sales"}' | jq .
```

---

If you want, I can:

- produce a minimal quickstart README for just macOS or just Windows, or
- open a PR with this updated README (provide your GitHub username or let me walk you through VS Code steps).
