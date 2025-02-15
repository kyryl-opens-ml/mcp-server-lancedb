# mcp-lance-db: A LanceDB MCP server

> The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need.

This repository is an example of how to create a MCP server for [LanceDB](https://lancedb.com/), an embedded vector database.

## Overview

A basic Model Context Protocol server for storing and retrieving memories in the LanceDB vector database.
It acts as a semantic memory layer that allows storing text with vector embeddings for later retrieval.

## Components

### Tools

The server implements two tools:
- add-memory: Adds a new memory to the vector database
  - Takes "content" as a required string argument
  - Stores the text with vector embeddings for later retrieval
  
- search-memories: Retrieves semantically similar memories
  - Takes "query" as a required string argument
  - Optional "limit" parameter to control number of results (default: 5)
  - Returns memories ranked by semantic similarity to the query
  - Updates server state and notifies clients of resource changes

## Configuration

The server uses the following configuration:
- Database path: "./lancedb"
- Collection name: "memories"
- Embedding provider: "sentence-transformers"
- Model: "BAAI/bge-small-en-v1.5"
- Device: "cpu"
- Similarity threshold: 0.7 (upper bound for distance range)

## Quickstart

#### Claude Desktop

On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```
{
  "lancedb": {
    "command": "uvx",
    "args": [
      "mcp-lance-db"
    ]
  }
}
```

## Development

### Building and Publishing

To prepare the package for distribution:

1. Sync dependencies and update lockfile:
```bash
uv sync
```

2. Build package distributions:
```bash
uv build
```

This will create source and wheel distributions in the `dist/` directory.

3. Publish to PyPI:
```bash
uv publish
```

Note: You'll need to set PyPI credentials via environment variables or command flags:
- Token: `--token` or `UV_PUBLISH_TOKEN`
- Or username/password: `--username`/`UV_PUBLISH_USERNAME` and `--password`/`UV_PUBLISH_PASSWORD`

### Debugging

Since MCP servers run over stdio, debugging can be challenging. For the best debugging
experience, we strongly recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector).


You can launch the MCP Inspector via [`npm`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) with this command:

```bash
npx @modelcontextprotocol/inspector uv --directory $(PWD) run mcp-lance-db
```

Upon launching, the Inspector will display a URL that you can access in your browser to begin debugging.