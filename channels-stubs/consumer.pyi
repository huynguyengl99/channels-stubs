from collections.abc import Awaitable, Callable
from typing import Any, ClassVar, TypeVar

from . import DEFAULT_CHANNEL_LAYER

T = TypeVar("T", bound="AsyncConsumer")

def get_handler_name(message: dict[str, Any]) -> str: ...

class AsyncConsumer:
    _sync: ClassVar[bool] = False
    channel_layer_alias: ClassVar[str] = DEFAULT_CHANNEL_LAYER

    scope: dict[str, Any]
    channel_layer: Any
    channel_name: str
    channel_receive: Callable[[], Awaitable[dict[str, Any]]]
    base_send: Callable[[dict[str, Any]], Awaitable[None]]

    async def __call__(
        self,
        scope: dict[str, Any],
        receive: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> None: ...
    async def dispatch(self, message: dict[str, Any]) -> None: ...
    async def send(self, message: dict[str, Any]) -> None: ...
    @classmethod
    def as_asgi(cls: type[T], **initkwargs: Any) -> Callable[..., Awaitable[None]]: ...

class SyncConsumer(AsyncConsumer):
    _sync: ClassVar[bool] = True

    def dispatch(self, message: dict[str, Any]) -> None: ...
    def send(self, message: dict[str, Any]) -> None: ...
