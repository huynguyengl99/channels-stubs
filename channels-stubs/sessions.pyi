import datetime
from collections.abc import Awaitable, Callable
from typing import Any

class CookieMiddleware:
    inner: Any

    def __init__(self, inner: Any) -> None: ...
    async def __call__(
        self,
        scope: dict[str, Any],
        receive: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> Any: ...
    @classmethod
    def set_cookie(
        cls,
        message: dict[str, Any],
        key: str,
        value: str = "",
        max_age: int | None = None,
        expires: str | datetime.datetime | None = None,
        path: str = "/",
        domain: str | None = None,
        secure: bool = False,
        httponly: bool = False,
        samesite: str = "lax",
    ) -> None: ...
    @classmethod
    def delete_cookie(
        cls,
        message: dict[str, Any],
        key: str,
        path: str = "/",
        domain: str | None = None,
    ) -> None: ...

class InstanceSessionWrapper:
    save_message_types: list[str]
    cookie_response_message_types: list[str]
    cookie_name: str
    session_store: Any
    scope: dict[str, Any]
    activated: bool
    real_send: Callable[[dict[str, Any]], Awaitable[None]]

    def __init__(
        self, scope: dict[str, Any], send: Callable[[dict[str, Any]], Awaitable[None]]
    ) -> None: ...
    async def resolve_session(self) -> None: ...
    async def send(self, message: dict[str, Any]) -> Awaitable[None]: ...
    async def save_session(self) -> None: ...

class SessionMiddleware:
    inner: Any

    def __init__(self, inner: Any) -> None: ...
    async def __call__(
        self,
        scope: dict[str, Any],
        receive: Callable[[], Awaitable[dict[str, Any]]],
        send: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> Any: ...

def SessionMiddlewareStack(inner: Any) -> Any: ...
