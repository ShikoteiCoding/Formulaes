from argparse import ArgumentParser
from typing import Callable

import inspect


# Store all commands
COMMANDS: dict[str, Callable] = dict()


def register(cmd: Callable) -> Callable:
    """
    Decorator to register a command in CLI.
    """
    COMMANDS[cmd.__name__] = cmd
    return cmd


def run_wrapper(cmd: Callable, **kwargs: dict) -> int:
    """
    Wrapper to execute functions as command lines by passing args.
    """
    return cmd(**kwargs)


def parse_arguments_from_func(parser: ArgumentParser, func: Callable):
    """
    From a function signature, create dynamic arguments parser.
    """
    signature = inspect.signature(func)
    for k,v in signature.parameters.items():
        if v is not inspect.Parameter.empty:
            parser.add_argument(f"--{str(k)}", required=False, default=v.default, help=f"argument '{k}' default value is '{v}")
        else:
            parser.add_argument(f"--{str(k)}", required=True, default=v.default, help=f"argument '{k}' does not have default value. please provide.")