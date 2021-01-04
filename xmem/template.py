from pathlib import Path


class MemoryTemplate:
    def save(self, data: dict, path: Path):
        """
        write the given dictionary to :path:

        :param path: path to save to
        :param data: item to save
        """
        raise NotImplementedError

    def load(self, path: Path) -> dict:
        """
        :param path: path to load from
        :return: content read from disk
        """
        raise NotImplementedError
