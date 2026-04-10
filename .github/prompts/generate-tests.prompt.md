---
description: "Generate pytest tests for an existing module following project test conventions."
agent: "agent"
argument-hint: "Module name to test (e.g. 'users', 'products')"
---
Generate comprehensive pytest tests for the specified module.

## Requirements

Create `tests/test_<module>.py` with these tests:

1. `test_create_<entity>` — POST, assert 201
2. `test_list_<entity>s` — GET list, assert 200
3. `test_get_<entity>` — GET by ID, assert 200
4. `test_get_<entity>_not_found` — GET invalid ID, assert 404
5. `test_update_<entity>` — PUT, assert 200 and updated values
6. `test_delete_<entity>` — DELETE, assert 200

## Patterns

- Use `@pytest.mark.asyncio` on all tests
- Use the `client` fixture from [conftest.py](tests/conftest.py)
- Type hint: `client: AsyncClient`
- Create dependent entities in the test if needed (e.g., create user before order)

## Reference

Follow patterns from [test_users.py](tests/test_users.py).
