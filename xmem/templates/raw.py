from ..template import BaseTemplate
from ..exceptions import NotFoundError


class RawTemplate(BaseTemplate):
    """
    Memory template using json storage
    """
    def save(self, data: bytes, path):
        with path.open('wb') as f:
            f.write(data)

    def load(self, path) -> bytes:
        try:
            with path.open('rb') as f:
                return f.read()
        except FileNotFoundError as e:
            raise NotFoundError(e)
