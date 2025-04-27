from collections.abc import Awaitable, Callable
from typing import Any

from .consumer import ASGIMessage

def name_that_thing(thing: Any) -> str: ...
async def await_many_dispatch(
    consumer_callables: list[Callable[[], Awaitable[ASGIMessage]]],
    dispatch: Callable[[ASGIMessage], Awaitable[None]],
) -> None: ...
