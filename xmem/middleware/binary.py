import json
from pathlib import Path

from .template import Middleware


class BinaryLayer(Middleware):
    def save(self, data: dict, path: Path):
        """
        Converts incoming dict to bytes and forwards it
        """
        self.template.save(
            json.dumps(data).encode('utf-8'),
            path
        )

    def load(self, path: Path) -> dict:
        """
        :return: byte data decrypted to dict
        """
        return json.loads(
            self.template.load(path).decode('utf-8')
        )
