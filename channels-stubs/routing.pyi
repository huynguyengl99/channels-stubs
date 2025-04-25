# routing.pyi
from collections.abc import Awaitable, Callable
from typing import Any

def get_default_application() -> Any: ...

class ProtocolTypeRouter:
    application_mapping: dict[str, Any]

    def __init__(self, application_mapping: dict[str, Any]) -> None: ...
    async def __call__(
        self,
        scope: dict[str, Any],
        receive: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> Any: ...

class URLRouter:
    _path_routing: bool = True
    routes: list[Any]

    def __init__(self, routes: list[Any]) -> None: ...
    async def __call__(
        self,
        scope: dict[str, Any],
        receive: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> Any: ...

class ChannelNameRouter:
    application_mapping: dict[str, Any]

    def __init__(self, application_mapping: dict[str, Any]) -> None: ...
    async def __call__(
        self,
        scope: dict[str, Any],
        receive: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> Any: ...
