from collections.abc import Callable
from typing import Any, ClassVar

from daphne.testing import DaphneProcess  # type: ignore[import-untyped]
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
from django.test.testcases import TransactionTestCase

def make_application(*, static_wrapper: Callable[[Any], Any] | None) -> Any: ...

class ChannelsLiveServerTestCase(TransactionTestCase):
    host: ClassVar[str] = "localhost"
    ProtocolServerProcess: ClassVar[type[DaphneProcess]] = DaphneProcess
    static_wrapper: ClassVar[type[ASGIStaticFilesHandler]] = ASGIStaticFilesHandler
    serve_static: ClassVar[bool] = True

    _port: int
    _server_process: DaphneProcess
    _live_server_modified_settings: Any

    @property
    def live_server_url(self) -> str: ...
    @property
    def live_server_ws_url(self) -> str: ...
    def _pre_setup(self) -> None: ...
    def _post_teardown(self) -> None: ...
    def _is_in_memory_db(self, connection: Any) -> bool: ...
