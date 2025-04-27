from typing import Any

from asgiref.typing import ASGIApplication, ASGIReceiveCallable, ASGISendCallable
from django.urls.resolvers import URLPattern, URLResolver

from .consumer import ChannelScope

def get_default_application() -> ProtocolTypeRouter: ...

class ProtocolTypeRouter:
    application_mapping: dict[str, ASGIApplication]

    def __init__(self, application_mapping: dict[str, Any]) -> None: ...
    async def __call__(
        self,
        scope: ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> None: ...

class URLRouter:
    _path_routing: bool = ...
    routes: list[URLPattern | URLResolver]

    def __init__(self, routes: list[URLPattern | URLResolver]) -> None: ...
    async def __call__(
        self,
        scope: ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> None: ...

class ChannelNameRouter:
    application_mapping: dict[str, ASGIApplication]

    def __init__(self, application_mapping: dict[str, ASGIApplication]) -> None: ...
    async def __call__(
        self,
        scope: ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> None: ...
