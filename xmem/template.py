from pathlib import Path


class BaseTemplate:
    def save(self, data, path: Path):
        """
        write the given dictionary to :path:

        :param path: path to save to
        :param data: item to save
        """
        raise NotImplementedError

    def load(self, path: Path):
        """
        :param path: path to load from
        :return: content read from disk
        """
        raise NotImplementedError
