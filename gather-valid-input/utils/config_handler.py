import os
import yaml


class ConfigHandler:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.validate_config(self.config)

    def load_config(self, config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f'"{config_path}" does not exist.')
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        return config

    def validate_config(self, config):
        expected_keys = {"variables"}
        actual_keys = set(config.keys())
        if actual_keys - expected_keys:
            unexpected = ", ".join(actual_keys - expected_keys)
            raise ValueError(f"Unexpected keys in configuration: {unexpected}")

        for idx, variable in enumerate(config["variables"], 1):
            expected_variable_keys = {"name", "description", "aliases"}
            actual_variable_keys = set(variable.keys())
            diff = actual_variable_keys - expected_variable_keys
            if diff:
                unexpected = ", ".join(diff)
                raise ValueError(f"Unexpected keys in variable #{idx}: {unexpected}")

            if "name" not in variable:
                raise ValueError(f"Variable #{idx} missing 'name' field.")
            if "description" not in variable:
                raise ValueError(f"Variable '{variable['name']}' missing 'type' field.")
            if "aliases" in variable:
                if not isinstance(variable["aliases"], list):
                    raise ValueError(
                        f"'aliases' for variable '{variable['name']}' should be a list."
                    )
