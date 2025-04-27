import datetime
from collections.abc import Awaitable
from typing import Any

from asgiref.typing import (
    ASGIApplication,
    ASGIReceiveCallable,
    ASGISendCallable,
    ASGISendEvent,
)
from channels.consumer import _ChannelScope

class CookieMiddleware:
    inner: ASGIApplication

    def __init__(self, inner: ASGIApplication) -> None: ...
    async def __call__(
        self,
        scope: _ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> Any: ...
    @classmethod
    def set_cookie(
        cls,
        message: ASGISendEvent,
        key: str,
        value: str = "",
        max_age: int | None = ...,
        expires: str | datetime.datetime | None = ...,
        path: str = ...,
        domain: str | None = ...,
        secure: bool = ...,
        httponly: bool = ...,
        samesite: str = ...,
    ) -> None: ...
    @classmethod
    def delete_cookie(
        cls,
        message: ASGISendEvent,
        key: str,
        path: str = ...,
        domain: str | None = ...,
    ) -> None: ...

class InstanceSessionWrapper:
    save_message_types: list[str]
    cookie_response_message_types: list[str]
    cookie_name: str
    session_store: Any
    scope: _ChannelScope
    activated: bool
    real_send: ASGISendCallable

    def __init__(self, scope: _ChannelScope, send: ASGISendCallable) -> None: ...
    async def resolve_session(self) -> None: ...
    async def send(self, message: ASGISendEvent) -> Awaitable[None]: ...
    async def save_session(self) -> None: ...

class SessionMiddleware:
    inner: ASGIApplication

    def __init__(self, inner: ASGIApplication) -> None: ...
    async def __call__(
        self,
        scope: _ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> ASGIApplication: ...

def SessionMiddlewareStack(inner: ASGIApplication) -> ASGIApplication: ...
