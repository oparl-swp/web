# OParl Validator GUI

## Installation

```bash
python get-pip.py
pip install Flask
```

## Running

```bash
pip install Flask
python app.py
```

## Todo

- Implement things
- Replace Supervisord with something that supports Python 3
  (e.g., https://github.com/mozilla-services/circus)

## Bear in Mind

- To start all Python files with to facilitate the switch to Python 3:
```python
# -*- encoding: utf-8 -*-
from __future__ import (unicode_literals, absolute_import,
                        division, print_function)
```
- The `oparlgui/templates` directory should only contain base.html (and .keep)
- The `oparlgui/static` directory should only contain .keep
- All other files go into app subdirectories
