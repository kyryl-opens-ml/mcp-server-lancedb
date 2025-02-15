import pytest
from mcp_lance_db.server import add_memory, search_memories


@pytest.mark.asyncio
async def test_add_memory():
    result = await add_memory("Test memory content")
    assert "Added memory: Test memory content" in result


@pytest.mark.asyncio
async def test_search_memories():
    # First add a memory
    await add_memory("Python is a great programming language")

    # Then search for it
    result = await search_memories("Python programming")
    assert "Python is a great programming language" in result


@pytest.mark.asyncio
async def test_search_memories_no_results():
    result = await search_memories("something that definitely doesn't exist")
    assert "No relevant memories found." in result
