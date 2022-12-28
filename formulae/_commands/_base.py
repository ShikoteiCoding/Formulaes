from argparse import ArgumentParser
from typing import Type, Callable, TypeVar, Any


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


def run_wrapper(cmd: T, args: Any) -> int:
    """
    Wrapper to execute functions as command lines by passing args.
    """
    return cmd(args)
