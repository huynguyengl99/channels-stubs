from typing import Any

from channels.testing.application import ApplicationCommunicator

class WebsocketCommunicator(ApplicationCommunicator):
    scope: dict[str, Any]
    response_headers: list[tuple[bytes, bytes]] | None

    def __init__(
        self,
        application: Any,
        path: str,
        headers: list[tuple[bytes, bytes]] | None = None,
        subprotocols: list[str] | None = None,
        spec_version: int | None = None,
    ) -> None: ...
    async def connect(self, timeout: float = 1) -> tuple[bool, str | int | None]: ...
    async def send_to(
        self, text_data: str | None = None, bytes_data: bytes | None = None
    ) -> None: ...
    async def send_json_to(self, data: Any) -> None: ...
    async def receive_from(self, timeout: float = 1) -> str | bytes: ...
    async def receive_json_from(self, timeout: float = 1) -> Any: ...
    async def disconnect(self, code: int = 1000, timeout: float = 1) -> None: ...
