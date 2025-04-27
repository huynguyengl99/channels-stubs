from typing import Any, TypeVar

from asgiref.typing import ASGIApplication, ASGIReceiveCallable, ASGISendCallable
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.utils.functional import LazyObject

from .consumer import ChannelScope, LazySession

User = TypeVar("User", bound=AbstractBaseUser)

@database_sync_to_async
def get_user(scope: ChannelScope) -> User | AnonymousUser: ...
@database_sync_to_async
def login(
    scope: ChannelScope, user: User, backend: BaseBackend | None = ...
) -> None: ...
@database_sync_to_async
def logout(scope: ChannelScope) -> None: ...
def _get_user_session_key(session: LazySession) -> Any: ...

class UserLazyObject(AbstractBaseUser, LazyObject):
    def _setup(self) -> None: ...

class AuthMiddleware(BaseMiddleware):
    def populate_scope(self, scope: ChannelScope) -> None: ...
    async def resolve_scope(self, scope: ChannelScope) -> None: ...
    async def __call__(
        self,
        scope: ChannelScope,
        receive: ASGIReceiveCallable,
        send: ASGISendCallable,
    ) -> ASGIApplication: ...

def AuthMiddlewareStack(inner: ASGIApplication) -> ASGIApplication: ...
