import os
import argparse
import importlib
from utils.config_handler import ConfigHandler


class GatherValidInput:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Gather input from given source, validate then store."
        )
        self.root = f"{os.path.dirname(os.path.abspath(__file__))}{os.sep}"
        self.actions = {}
        self.load("gatherers")
        self.load("validators")

    def load(self, name):
        path = os.path.join(self.root, name)
        for dir, _, files in os.walk(path):
            for file in files:
                if not file.endswith(".py".capitalize()):
                    continue
                module_root = dir.replace(self.root, "").replace(os.sep, ".")
                module_path = f"{module_root}.{file[:-3]}"
                module = importlib.import_module(module_path)
                plugin_name = name[:-1].capitalize()
                if hasattr(module, plugin_name):
                    plugin = getattr(module, plugin_name)
                    plugin().setup(self.parser, self.actions)

    def run(self, args=None):
        parsed_args = self.parser.parse_args(args)
        for action, func in self.actions.items():
            if getattr(parsed_args, action, None) is not None:
                func(parsed_args)


if __name__ == "__main__":
    app = GatherValidInput()
    config = ConfigHandler(f"{app.root}config.yaml").config

    app.run()
