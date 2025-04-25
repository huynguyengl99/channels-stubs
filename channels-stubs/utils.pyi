from collections.abc import Awaitable, Callable
from typing import Any

def name_that_thing(thing: Any) -> str: ...
async def await_many_dispatch(
    consumer_callables: list[Callable[[], Awaitable[dict[str, Any]]]],
    dispatch: Callable[[dict[str, Any]], Awaitable[None]],
) -> None: ...
