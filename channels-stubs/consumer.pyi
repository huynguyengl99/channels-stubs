from collections.abc import Awaitable, Callable
from typing import Any, ClassVar, TypedDict, TypeVar

from asgiref.typing import (
    ASGIReceiveCallable,
    ASGISendCallable,
    ASGISendEvent,
    WebSocketScope,
)
from channels.auth import UserLazyObject
from django.contrib.sessions.backends.base import SessionBase
from django.utils.functional import LazyObject

T = TypeVar("T", bound="AsyncConsumer")

# ASGI specification-compliant type definitions
class ASGIVersions(TypedDict):
    """ASGI version information"""

    version: str
    spec_version: str

class LazySession(SessionBase, LazyObject):
    """A lazy loading session object as used in the scope."""

    _wrapped: SessionBase

# Base ASGI Scope definition
class ChannelScope(WebSocketScope, total=False):
    # Channel specific
    channel: str
    url_route: dict[str, Any]
    path_remaining: str

    # Auth specific
    cookies: dict[str, str]
    session: LazySession
    user: UserLazyObject | None

def get_handler_name(message: ASGISendEvent) -> str: ...

class AsyncConsumer:
    _sync: ClassVar[bool] = ...
    channel_layer_alias: ClassVar[str] = ...

    scope: ChannelScope
    channel_layer: Any
    channel_name: str
    channel_receive: ASGIReceiveCallable
    base_send: ASGISendCallable

    async def __call__(
        self,
        scope: ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> None: ...
    async def dispatch(self, message: ASGISendEvent) -> None: ...
    async def send(self, message: ASGISendEvent) -> None: ...
    @classmethod
    def as_asgi(cls: type[T], **initkwargs: Any) -> Callable[..., Awaitable[None]]: ...

class SyncConsumer(AsyncConsumer):
    _sync: ClassVar[bool] = ...

    def dispatch(self, message: ASGISendEvent) -> None: ...
    def send(self, message: ASGISendEvent) -> None: ...
