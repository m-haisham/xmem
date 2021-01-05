from pathlib import Path

try:
    from cryptography.fernet import Fernet
except ImportError:
    pass

from .template import Middleware


class EncryptionLayer(Middleware):
    def __init__(self, template, key: bytes):
        super(EncryptionLayer, self).__init__(template)
        self.fernet = Fernet(key)

    def save(self, data: bytes, path: Path):
        """
        encrypts the byte data and forwards it
        """
        self.template.save(
            self.fernet.encrypt(data),
            path
        )

    def load(self, path: Path) -> bytes:
        """
        :return: decrypted byte data
        """
        return self.fernet.decrypt(
            self.template.load(path)
        )
