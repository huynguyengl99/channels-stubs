from typing import Any

from asgiref.server import StatelessServer

class Worker(StatelessServer):
    channels: list[str]
    channel_layer: Any

    def __init__(
        self,
        application: Any,
        channels: list[str],
        channel_layer: Any,
        max_applications: int = 1000,
    ) -> None: ...
    async def handle(self) -> None: ...
    async def listener(self, channel: str) -> None: ...
