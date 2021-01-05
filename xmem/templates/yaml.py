from pathlib import Path

try:
    import yaml
except:
    pass

from ..template import BaseTemplate
from ..exceptions import NotFoundError


class YamlTemplate(BaseTemplate):
    def save(self, data: dict, path: Path):
        with path.open('w') as f:
            yaml.dump(data, f)

    def load(self, path: Path) -> dict:
        try:
            with path.open('rb') as f:
                return yaml.load(f)
        except FileNotFoundError as e:
            raise NotFoundError(e)
