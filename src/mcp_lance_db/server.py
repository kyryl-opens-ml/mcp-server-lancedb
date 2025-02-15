from mcp.server.fastmcp import FastMCP
from mcp_lance_db.db_client import LanceDBConnector

mcp = FastMCP("mcp-lance-db")

db_connector = LanceDBConnector(
    db_path="/tmp/lancedb",
    collection_name="memories",
    embedding_provider="sentence-transformers",
    model_name="BAAI/bge-small-en-v1.5",
    device="cpu",
)


@mcp.tool()
async def add_memory(content: str) -> str:
    """
    Add a new memory to the vector database
    Args:
        content: Content of the memory
    """
    db_connector.store_memory(content)
    return f"Added memory: {content}"


@mcp.tool()
async def search_memories(query: str, limit: int = 5) -> str:
    """
    Search memories using semantic similarity
    Args:
        query: The search query
        limit: Maximum number of results to return
    """
    memories = db_connector.find_memories(query, limit=limit)
    if not memories:
        return "No relevant memories found."

    return "Found these relevant memories:\n\n" + "\n\n".join(memories)
