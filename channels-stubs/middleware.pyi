from collections.abc import Awaitable, Callable
from typing import Any

class BaseMiddleware:
    inner: Any
    def __init__(self, inner: Any) -> None: ...
    async def __call__(
        self,
        scope: dict[str, Any],
        receive: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> Any: ...
