from typing import Union

try:
    import winreg
except ImportError:
    pass

from ..template import BaseTemplate
from ..exceptions import NotFoundError


class RegistryTemplate(BaseTemplate):
    root = winreg.HKEY_CURRENT_USER

    def __init__(self, name='xmem'):
        """
        :param name: name of your application, will be created in registry
        """
        super(RegistryTemplate, self).__init__()

        # check if os is supported [Windows]
        import platform
        if platform.system() != 'Windows':
            raise OSError('Unsupported operating system, this template only works on windows')

        self.registry_path = f'SOFTWARE\\{name}\\Settings'

    def save(self, data: Union[str, bytes], path):
        try:
            winreg.CreateKey(self.root, self.registry_path)

            with winreg.OpenKey(self.root, self.registry_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, str(path), 0, winreg.REG_SZ, data)

            return True
        except WindowsError:
            return False

    def load(self, path) -> Union[str, bytes]:
        try:
            with winreg.OpenKey(self.root, self.registry_path, 0, winreg.KEY_READ) as key:
                data, type = winreg.QueryValueEx(key, str(path))

            return data
        except WindowsError:
            path = self.registry_path + f"\\{path}"

            raise NotFoundError(f'registry path, {path} does not exist')
