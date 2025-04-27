from collections.abc import Awaitable, Callable
from typing import Any

from asgiref.typing import ASGIReceiveCallable, ASGISendEvent

def name_that_thing(thing: Any) -> str: ...
async def await_many_dispatch(
    consumer_callables: list[Callable[[], Awaitable[ASGIReceiveCallable]]],
    dispatch: Callable[[ASGISendEvent], Awaitable[None]],
) -> None: ...
