from inspect import signature
from abc import ABC, ABCMeta, abstractmethod


class EnforceMethodSignatureMeta(ABCMeta):
    def __new__(cls, name, bases, class_dict):
        # Check that the class we're constructing derives from our abstract base
        if bases:
            base = bases[0]
            for name, member in class_dict.items():
                # If the base has the method, and it's not the one we're currently defining
                if hasattr(base, name) and callable(member):
                    base_signature = signature(getattr(base, name))
                    derived_signature = signature(member)

                    if base_signature != derived_signature:
                        raise TypeError(
                            f"Signature of {name} does not match the base class. "
                            f"Expected {base_signature}, but got {derived_signature}."
                        )

        return super().__new__(cls, name, bases, class_dict)


class Extension(ABC, metaclass=EnforceMethodSignatureMeta):
    @abstractmethod
    def setup(self, parser, actions, config, root):
        pass
