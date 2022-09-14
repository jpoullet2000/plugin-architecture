from typing import List
from myproject.plugin_manager import MyProjectPlugin
from myproject.features import BaseFeature


class MyFeature(BaseFeature):
    def print_hello(self):
        print('hello')

class MyPlugin(MyProjectPlugin):
    name: str = 'MyPlugin'
    features: List[BaseFeature] = [MyFeature]
