from argparse import ArgumentParser

parser = ArgumentParser(
    description="A utility for checking files if it's outdated",
    epilog="It's important to thoroughly to keep testing until you're satisfied with the changes!"
)

parser.add_argument("config_file",
                    help="Required to have one, otherwise, it'll generate one automatically")

parser.add_argument("--local-only", action="store_true",
                    help="Scan for files from a folder, including non-git directories; will fallback to `--local-only` if no connection is detected")

parser.add_argument("--ci-mode", action="store_true",
                    help="A switch meant for running CI/CD pipelines")

args = parser.parse_args()


def main():
    # check for internet first, if none, fallback to local change
    # update schema for any changes
    # do some parsing, log for any errors
    pass


if __name__ == "__main__":
    main()
