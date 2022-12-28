import sys

from argparse import ArgumentParser
from typing import NoReturn, TextIO

def main(argv: list[str], stream: TextIO) -> int:
    parser = ArgumentParser('python3 -m formulae')
    subparsers = parser.add_subparsers()
    parser.set_defaults(cmd=None)

    return cmd

def entrypoint() -> NoReturn:
    sys.exit(main(argv=sys.argv[1:], stream=sys.stdout))