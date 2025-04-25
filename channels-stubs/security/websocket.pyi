from collections.abc import Awaitable, Callable
from re import Pattern
from typing import Any

from channels.generic.websocket import AsyncWebsocketConsumer

class OriginValidator:
    application: Any
    allowed_origins: list[str | Pattern[str]]

    def __init__(
        self, application: Any, allowed_origins: list[str | Pattern[str]]
    ) -> None: ...
    async def __call__(
        self,
        scope: dict[str, Any],
        receive: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> Any: ...
    def valid_origin(self, parsed_origin: Any) -> bool: ...
    def validate_origin(self, parsed_origin: Any) -> bool: ...
    def match_allowed_origin(
        self, parsed_origin: Any, pattern: str | Pattern[str]
    ) -> bool: ...
    def get_origin_port(self, origin: Any) -> str | None: ...

def AllowedHostsOriginValidator(application: Any) -> OriginValidator: ...

class WebsocketDenier(AsyncWebsocketConsumer):
    async def connect(self) -> None: ...
