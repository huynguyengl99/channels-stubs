from typing import Any, TypeVar

from asgiref.typing import ASGIApplication, ASGIReceiveCallable, ASGISendCallable
from channels.middleware import BaseMiddleware
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.utils.functional import LazyObject

from .consumer import _ChannelScope, _LazySession

_User = TypeVar("_User", bound=AbstractBaseUser)

def get_user(scope: _ChannelScope) -> _User | AnonymousUser: ...
def login(
    scope: _ChannelScope, user: _User, backend: BaseBackend | None = ...
) -> None: ...
def logout(scope: _ChannelScope) -> None: ...
def _get_user_session_key(session: _LazySession) -> Any: ...

class UserLazyObject(AbstractBaseUser, LazyObject):
    def _setup(self) -> None: ...

class AuthMiddleware(BaseMiddleware):
    def populate_scope(self, scope: _ChannelScope) -> None: ...
    async def resolve_scope(self, scope: _ChannelScope) -> None: ...
    async def __call__(
        self,
        scope: _ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> ASGIApplication: ...

def AuthMiddlewareStack(inner: ASGIApplication) -> ASGIApplication: ...
