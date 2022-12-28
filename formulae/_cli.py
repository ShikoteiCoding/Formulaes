import sys

from argparse import ArgumentParser
from typing import NoReturn, TextIO

from ._commands import COMMANDS, run_wrapper


def main(argv: list[str]) -> int:
    parser = ArgumentParser("python3 -m formulae")
    subparsers = parser.add_subparsers()
    parser.set_defaults(cmd=None)

    for name, cmd_func in COMMANDS.items():
        subparser = subparsers.add_parser(
            name=name
        )  # Set function name as the first argument
        subparser.set_defaults(cmd=cmd_func)

    args = parser.parse_args(argv)

    cmd_func = args.cmd

    if cmd_func is None:
        return 1

    run_wrapper(cmd_func, args)


def entrypoint() -> NoReturn:
    sys.exit(main(argv=sys.argv[1:]))
