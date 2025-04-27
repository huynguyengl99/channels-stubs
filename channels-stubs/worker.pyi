from typing import TypedDict

from asgiref.server import StatelessServer
from asgiref.typing import ASGIApplication
from channels.layers import BaseChannelLayer

# Define channel scope for worker
class ChannelWorkerScope(TypedDict):
    """Scope for channel worker connections"""

    type: str
    channel: str

class Worker(StatelessServer):
    channels: list[str]
    channel_layer: BaseChannelLayer

    def __init__(
        self,
        application: ASGIApplication,
        channels: list[str],
        channel_layer: BaseChannelLayer,
        max_applications: int = ...,
    ) -> None: ...
    async def handle(self) -> None: ...
    async def listener(self, channel: str) -> None: ...
