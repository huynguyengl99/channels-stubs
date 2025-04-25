# management/commands/runworker.pyi
import logging
from argparse import ArgumentParser
from typing import Any

from channels import DEFAULT_CHANNEL_LAYER
from channels.worker import Worker
from django.core.management.base import BaseCommand

logger: logging.Logger

class Command(BaseCommand):
    leave_locale_alone: bool = True
    # This is the key fix - worker_class is a class reference, not a function
    worker_class: type[Worker] = Worker
    verbosity: int
    channel_layer: Any

    def add_arguments(self, parser: ArgumentParser) -> None: ...
    def handle(
        self,
        *args: Any,
        application_path: str | None = None,
        channels: list[str] | None = None,
        layer: str = DEFAULT_CHANNEL_LAYER,
        **options: Any,
    ) -> None: ...
