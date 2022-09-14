This is an example plugin project which works with the myproject-core available [here](https://github.com/jpoullet2000/myproject-core).


One needs first to install myproject-core, then install myproject-plugin1.

Open some python interpreter and test it

```python
from myproject.plugin_manager import (
    features_modules,
    integrate_feature_plugins
)

integrate_feature_plugins()

from myproject.features.myplugin import MyFeature
```
