#!/usr/bin/env python
"""
This client will send the content of solution.py as a solution to a given challenge.
In return it will display

Usage:
    client.py [options]
    client.py -h | --help

Options:
    --solution-file=S   Path to the solution file [default: solution.py]
    --host=H            Host address of the coding game plateforme (http://<ip>:<port>) [default: http://127.0.0.1:5000/challenge/1]
    -h, --help          Show help.
"""
import logging
import requests

import docopt

from defacto.init_logging import init_logging


LOGGER = logging.getLogger(__file__)


def run(solution_file: str, host: str):
    with open(solution_file, "r") as s_file:
        solution = s_file.read()
        response = requests.post(host, json={"solution": solution})
        data = response.json()
        print(f"{data}")


def main():
    """Main function of defacto coding game client."""
    args = docopt.docopt(__doc__)
    init_logging()
    run(
        solution_file=args["--solution-file"],
        host=args["--host"]
    )


if __name__ == "__main__":
    main()
