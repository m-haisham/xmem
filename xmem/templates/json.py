import json

from ..template import MemoryTemplate
from ..exceptions import NotFoundError


class JsonTemplate(MemoryTemplate):
    """
    Memory template using json storage
    """

    def save(self, data: dict, path):
        with path.open('w') as f:
            json.dump(data, f)

    def load(self, path) -> dict:
        try:
            with path.open('r') as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise NotFoundError(e)
