from asyncio import EventLoop
from collections.abc import Callable, Coroutine
from typing import Any, TypeVar

from asgiref.sync import SyncToAsync
from typing_extensions import ParamSpec

T = TypeVar("T")

_P = ParamSpec("_P")
_R = TypeVar("_R")

class DatabaseSyncToAsync(SyncToAsync):
    def thread_handler(self, loop: EventLoop, *args: Any, **kwargs: Any) -> Any: ...

def database_sync_to_async(
    func: Callable[_P, _R],
) -> Callable[_P, Coroutine[Any, Any, _R]]: ...
async def aclose_old_connections() -> None: ...
