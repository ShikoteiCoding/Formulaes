from argparse import ArgumentParser
from typing import Type, Callable, TypeVar, Any

import inspect


# Store all commands
COMMANDS: dict[str, Callable] = dict()
# Type the commands as func
T = TypeVar("T", bound=Callable)


def register(cmd: T) -> T:
    """
    Decorator to register a command in CLI.
    """
    COMMANDS[cmd.__name__] = cmd
    return cmd


def run_wrapper(cmd: T, args: dict) -> int:
    """
    Wrapper to execute functions as command lines by passing args.
    """
    return cmd(**args)


def parse_arguments_from_func(parser: ArgumentParser, func: Callable):
    """
    From a function signature, create dynamic arguments parser.
    """
    for arg in inspect.signature(func).parameters:
        parser.add_argument(f'--{str(arg)}', required=True)