from argparse import ArgumentParser
from typing import Type, Callable, TypeVar

commands: dict[str, Callable] = dict()
T = TypeVar('T', bound=Callable)

def register(cmd: T) -> T:
    """
    Decorator to register a command in CLI.
    """
    commands[cmd.__name__] = cmd
    return cmd