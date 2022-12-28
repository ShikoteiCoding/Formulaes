import sys

from argparse import ArgumentParser
from typing import NoReturn, TextIO

from ._commands import COMMANDS


def main(argv: list[str], stream: TextIO) -> int:
    parser = ArgumentParser("python3 -m formulae")
    subparsers = parser.add_subparsers()
    parser.set_defaults(cmd=None)

    for name, cmd_func in COMMANDS.items():
        print(name, cmd_func)

    return 0


def entrypoint() -> NoReturn:
    sys.exit(main(argv=sys.argv[1:], stream=sys.stdout))
