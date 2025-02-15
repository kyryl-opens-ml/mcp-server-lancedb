import pytest
from mcp_lance_db.db_client import LanceDBConnector
import tempfile


@pytest.fixture
def db_connector():
    # Create a temporary directory for the test database
    with tempfile.TemporaryDirectory() as temp_dir:
        connector = LanceDBConnector(
            db_path=temp_dir,
            collection_name="test_memories",
            embedding_provider="sentence-transformers",
            model_name="BAAI/bge-small-en-v1.5",
            device="cpu",
        )
        yield connector


def test_store_and_find_memories(db_connector):
    # Test storing a memory
    test_memory = "This is a test memory about Python programming"
    db_connector.store_memory(test_memory)

    # Test finding the stored memory
    found_memories = db_connector.find_memories("Python programming")
    assert len(found_memories) > 0
    assert test_memory in found_memories


def test_find_nonexistent_memories(db_connector):
    # Test searching for memories that don't exist
    found_memories = db_connector.find_memories("something that doesn't exist")
    assert len(found_memories) == 0
