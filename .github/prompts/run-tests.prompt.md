---
description: "Run all project tests with pytest and report results."
agent: "agent"
tools: [execute]
---
Run the full test suite:

1. Install test dependencies if needed: `pip install pytest pytest-asyncio httpx aiosqlite`
2. Run: `pytest tests/ -v --tb=short`
3. Report:
   - Total tests passed/failed
   - Any failures with the test name and error summary
   - Suggestions to fix failures if any
