import os
import inspect
import argparse
import importlib
from common.extension import Extension
from utils.config_handler import ConfigHandler


class GatherValidInput:
    def __init__(self):
        self.root = f"{os.path.dirname(os.path.abspath(__file__))}{os.sep}"

        self.actions = {}
        self.parser = argparse.ArgumentParser(
            description="Gather, validate and store information."
        )

        self.config = ConfigHandler(self.parser, self.root).config
        self.load_extensions()

    def load_extensions(self):
        for directory, _, files in os.walk(self.root):
            for file in files:
                module = self.get_module(directory, file)
                extension = self.get_extension(module)
                if extension:
                    extension().setup(
                        parser=self.parser,
                        actions=self.actions,
                        config=self.config,
                        root=self.root,
                    )

    def get_module(self, directory, file):
        if file == "__init__.py" or file == __file__ or not file.endswith(".py"):
            return None

        module_root = directory.replace(self.root, "").replace(os.sep, ".")
        module_path = f"{module_root}.{file[:-3]}" if len(module_root) else file[:-3]
        return importlib.import_module(module_path)

    def get_extension(self, module):
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if issubclass(obj, Extension) and obj != Extension:
                    return getattr(module, name)
        return None

    def run(self):
        args = self.parser.parse_args()
        for action, func in self.actions.items():
            if getattr(args, action, None) is not None:
                func(args)


if __name__ == "__main__":
    app = GatherValidInput()
    app.run()
