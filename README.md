# Settings Loader

Load your settings from toml, yml files.

### Usage

* Import lib:
```python
from settings_loader import SettingsLoader
```

* Pass settings type class and path to settings file:
```python
loader = SettingsLoader(file_name=PATH_SETTINGS_FILE, klass=Settings)
settings: Settings = loader.get_settingss()
```

