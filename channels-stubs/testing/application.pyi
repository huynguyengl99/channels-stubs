from typing import Any

from asgiref.testing import ApplicationCommunicator as BaseApplicationCommunicator

def no_op() -> None: ...

class ApplicationCommunicator(BaseApplicationCommunicator):
    async def send_input(self, message: dict[str, Any]) -> None: ...
    async def receive_output(self, timeout: float = ...) -> dict[str, Any]: ...
    async def receive_nothing(self, timeout: float = ..., interval: float = ...) -> bool: ...
    async def wait(self, timeout: float = ...) -> None: ...
    def stop(self, exceptions: bool = ...) -> None: ...
