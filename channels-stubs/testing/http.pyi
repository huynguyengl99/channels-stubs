from typing import Iterable, Literal, Optional, Tuple, TypedDict

from asgiref.typing import ASGIApplication
from channels.testing.application import ApplicationCommunicator

# HTTP test-specific response type
class HTTPTestResponse(TypedDict, total=False):
    """HTTP response data structure for test cases"""

    status: int
    headers: Iterable[Tuple[bytes, bytes]]
    body: bytes

class HTTPTestScope(TypedDict, total=False):
    type: Literal["http"]
    http_version: str
    method: str
    scheme: str
    path: str
    raw_path: bytes
    query_string: bytes
    root_path: str
    headers: Iterable[Tuple[bytes, bytes]] | None
    client: Optional[Tuple[str, int]]
    server: Optional[Tuple[str, Optional[int]]]

class HttpCommunicator(ApplicationCommunicator):
    scope: HTTPTestScope
    body: bytes
    sent_request: bool

    def __init__(
        self,
        application: ASGIApplication,
        method: str,
        path: str,
        body: bytes = ...,
        headers: Iterable[Tuple[bytes, bytes]] | None = ...,
    ) -> None: ...
    async def get_response(self, timeout: float = ...) -> HTTPTestResponse: ...
