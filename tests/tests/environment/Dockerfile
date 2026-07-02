FROM python:3.11-slim@sha256:8357da08af3a681cb2aa026b9117604a1b023f7c46ee0997193f41c4bc268d80

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log

# Note: Removed "COPY solution_hint.py /app/solution_hint.py" to prevent leakage to the agent.
