import os
import runpy
import sys
from importlib.abc import MetaPathFinder
from importlib.util import spec_from_file_location
from json import JSONDecodeError

import click
import requests

SPACESNAKE_PATH = os.environ.get(
    "SPACESNAKE_PATH", os.path.join(os.path.expanduser("~"), ".spacesnake")
)

try:
    os.makedirs(SPACESNAKE_PATH, exist_ok=True)
except:
    pass


class IPFSInterface:
    def __init__(self, url=None):
        """Initialize IPFS interface which communicates with an IPFS node

        :parameter url: URL to IPFS
        :type url: str

        """
        self.url = url or os.environ.get(
            "SPACESNAKE_IPFS_NODE_URL", "http://localhost:5001"
        )

    def cat(self, ipfs_path, output_path=None):
        """Retrieve object from IPFS

        :parameter ipfs_path: Path to the IPFS object to be outputted
        :type ipfs_path: Path
        :parameter output_path: Path where the output should be stored
        :type output_path: Path

        :return: Output path
        """
        if not output_path:
            output_path = os.path.join(
                os.path.expanduser("~"), ".spacesnake", ipfs_path + ".py"
            )

        response = requests.post(
            self.url + "/api/v0/cat",
            params={
                "arg": ipfs_path,
            },
        )

        with open(output_path, "wb") as f:
            f.write(response.content)

        return output_path

    def add(self, input_path):
        """Add object to IPFS

        :parameter input_path: Path to the input file
        :type input_path: Path

        :return: IPFS object path hash (CID)
        """
        response = requests.post(
            self.url + "/api/v0/add", files={"file": open(input_path, "rb")}
        )

        try:
            data = response.json()
        except JSONDecodeError as exception:
            logging.exception(f"Could not add file from {input_path}")
            raise exception

        return data["Hash"]


ipfs_interface = IPFSInterface()


class IPFSFinder(MetaPathFinder):
    """Implements IPFS import mechanism
    https://docs.python.org/3/reference/import.html#the-meta-path
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find_spec(fullname, path, target=None):
        output_path = ipfs_interface.cat(fullname)

        return spec_from_file_location(fullname, output_path)


sys.meta_path = sys.meta_path + [IPFSFinder]  # Register the Meta Path Finder for IPFS


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Default command line interface group"""
    if ctx.invoked_subcommand is None:
        ctx.invoke(run)


@cli.command("push")
@click.argument("input_path")
@click.option("-y", "--no-confirm", is_flag=True)
def push(input_path, no_confirm=False):
    """Push command"""
    if not no_confirm:
        answer = input(
            f'Are you sure you want to add "{input_path}" to IPFS? This is irreversible. [y/n]: '
        )
        if answer != "y":
            return

    ipfs_path = ipfs_interface.add(input_path)

    print(ipfs_path)


@cli.command("script")
@click.argument("ipfs_path")
@click.option("-i", "--inspect", is_flag=True)
def script(ipfs_path, inspect=False):
    """Script command"""
    output_path = ipfs_interface.cat(ipfs_path)

    if inspect:
        with open(output_path, "r", encoding="utf-8") as f:
            print(f.read())

    else:
        runpy.run_path(output_path)
