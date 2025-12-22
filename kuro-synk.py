import sys
from argparse import ArgumentParser
from typing import TypedDict, NotRequired
from dataclasses import dataclass, asdict


# sometimes, I might need to have some exceptions
@dataclass
class KsynkFileRules:
    lines: int | list[int]


@dataclass
class KsynkFiles:
    source_file: str
    destinations: list[str | tuple[str, KsynkFileRules]]


@dataclass
class KysnkSchema:
    git_url: str
    local_path: str
    files: list[KsynkFiles]


###########################################################################

parser = ArgumentParser(
    description="A utility for checking files if it's outdated",
    epilog="It's important to thoroughly to keep testing until you're satisfied lol"
)

parser.add_argument("config_file",
                    help="Required to have one, otherwise, it'll generate one for you :3")

parser.add_argument("--local-only", action="store_true",
                    help="Scan for files from a folder, including non-git directories; will fallback to `--local-only` if no connection is detected.")

parser.add_argument("--ci-mode", action="store_true",
                    help="A switch meant for running CI/CD pipelines")

args = parser.parse_args()


def main():
    # check for internet first, if none, fallback to local change
    # update schema for any changes
    # do some parsing, log for any errors
    pass


if __name__ == "__main__":
    if (len(sys.argv) == 0):
        raise Exception("What the fuck bro")
        exit(2)

    main()
