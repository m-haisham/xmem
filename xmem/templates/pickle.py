import pickle

from ..template import MemoryTemplate
from ..exceptions import NotFoundError


class PickleTemplate(MemoryTemplate):
    """
    Memory template using pickle storage
    """

    def save(self, data: dict, path):
        with path.open('wb') as f:
            pickle.dump(data, f)

    def load(self, path) -> dict:
        try:
            with path.open('rb') as f:
                return pickle.load(f)
        except FileNotFoundError as e:
            raise NotFoundError(e)
