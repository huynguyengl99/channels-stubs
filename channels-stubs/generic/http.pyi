from collections.abc import Iterable
from typing import Any, Union

from asgiref.typing import (
    HTTPDisconnectEvent,
    HTTPRequestEvent,
    HTTPResponseBodyEvent,
    HTTPResponseStartEvent,
    HTTPResponseTrailersEvent,
    HTTPScope,
    HTTPServerPushEvent,
)
from channels.consumer import AsyncConsumer

HTTPSendEvent = Union[
    HTTPResponseStartEvent,
    HTTPResponseBodyEvent,
    HTTPResponseTrailersEvent,
    HTTPServerPushEvent,
    HTTPDisconnectEvent,
]

class AsyncHttpConsumer(AsyncConsumer):
    body: list[bytes]
    scope: HTTPScope

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def send_headers(
        self,
        *,
        status: int = ...,
        headers: Iterable[tuple[bytes, bytes]] | None = ...,
    ) -> None: ...
    async def send_body(self, body: bytes, *, more_body: bool = ...) -> None: ...
    async def send_response(self, status: int, body: bytes, **kwargs: Any) -> None: ...
    async def handle(self, body: bytes) -> None: ...
    async def disconnect(self) -> None: ...
    async def http_request(self, message: HTTPRequestEvent) -> None: ...
    async def http_disconnect(self, message: HTTPDisconnectEvent) -> None: ...
    async def send(
        self,
        message: HTTPSendEvent,
    ) -> None: ...
