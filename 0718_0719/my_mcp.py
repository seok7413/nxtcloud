# my_mcp.py — 내 첫 MCP 서버
from fastmcp import FastMCP

mcp = FastMCP("my-first-mcp")


@mcp.tool()
def course_secret() -> str:
    """이 수업의 비밀 코드를 반환한다. 모델은 이 값을 추측할 수 없다."""
    return "NXT-MCP-2026"


@mcp.tool()
def add(a: int, b: int) -> int:
    """두 정수를 더한다."""
    return a + b


if __name__ == "__main__":
    mcp.run()  # 기본 stdio 전송 (Lab 05 의 그 stdio)
