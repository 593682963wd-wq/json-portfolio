from __future__ import annotations
from typing import Any
TOOLS=[]
def _load_registry():return TOOLS

def _registry_stats(tools: list[dict] | None = None) -> dict[str, Any]:
    tools = _load_registry() if tools is None else tools
    categories = sorted({str(tool.get("category", "未分类")) for tool in tools if tool.get("category")})
    web_tools = [tool for tool in tools if tool.get("kind") == "web"]
    public_tools = [tool for tool in tools if tool.get("access") == "public"]
    return {
        "tool_count": len(tools),
        "web_count": len(web_tools),
        "public_count": len(public_tools),
        "category_count": len(categories),
        "categories": categories,
    }
