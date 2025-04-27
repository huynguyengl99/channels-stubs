from asgiref.typing import ASGIApplication, ASGIReceiveCallable, ASGISendCallable

from .consumer import ChannelScope

class BaseMiddleware:
    inner: ASGIApplication | BaseMiddleware

    def __init__(self, inner: ASGIApplication | BaseMiddleware) -> None: ...
    async def __call__(
        self,
        scope: ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> ASGIApplication: ...
