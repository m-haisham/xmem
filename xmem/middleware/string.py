import json
from pathlib import Path

from .template import Middleware


class StringLayer(Middleware):
    def save(self, data: dict, path: Path):
        """
        Converts incoming dict to string and forwards it
        """
        self.template.save(
            json.dumps(data),
            path
        )

    def load(self, path: Path) -> dict:
        """
        :return: string data decrypted to dict
        """
        return json.loads(
            self.template.load(path),
        )
