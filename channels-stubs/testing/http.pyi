from typing import Any

from channels.testing.application import ApplicationCommunicator

class HttpCommunicator(ApplicationCommunicator):
    scope: dict[str, Any]
    body: bytes
    sent_request: bool

    def __init__(
        self,
        application: Any,
        method: str,
        path: str,
        body: bytes = b"",
        headers: list[tuple[bytes, bytes]] | None = None,
    ) -> None: ...
    async def get_response(self, timeout: float = 1) -> dict[str, Any]: ...
