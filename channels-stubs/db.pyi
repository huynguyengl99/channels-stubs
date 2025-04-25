from collections.abc import Awaitable, Callable
from typing import Any, TypeVar

from asgiref.sync import SyncToAsync

T = TypeVar("T")

class DatabaseSyncToAsync(SyncToAsync):
    def thread_handler(self, loop: Any, *args: Any, **kwargs: Any) -> Any: ...

# This correctly types the database_sync_to_async decorator
database_sync_to_async: Callable[[Callable[..., T]], Callable[..., Awaitable[T]]]

async def aclose_old_connections() -> None: ...
