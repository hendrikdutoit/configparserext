"""Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
"""

from pathlib import Path
from tempfile import mkdtemp

import pytest
from beetools import rm_tree

import configparserext

_DESC = __doc__.split("\n")[0]
_PATH = Path(__file__)


class WorkingDir:
    def __init__(self):
        self.dir = Path(mkdtemp(prefix="packageit_"))


class EnvSetUp:
    def __init__(self):
        self.dir = WorkingDir().dir
        self.ini_pth = self.dir / "test.ini"
        self.raw_struct = {
            "General": {"SeriesPrefix": "Series", "OptionPrefix": "Cmd"},
            "Series01": {
                "cmd1": "Some instruction 1",
                "cmd2": "Some instruction 2",
                "val1": 1,
                "val2": 2,
            },
            "Series02": {
                "cmd1": "You;can;split;the;option",
                "cmd2": "Some instruction 4",
                "str1": "c",
                "str2": "d",
            },
            "Series03": {"cmd1": 5, "cmd2": 6, "str1": "e", "str2": "f"},
        }
        self.ini = configparserext.ConfigParserExt()
        for item in self.raw_struct:
            self.ini[item] = self.raw_struct[item]
        with open(self.ini_pth, "w") as fp:
            self.ini.write(fp)
        # self.ini.read([self.ini_pth])
        pass


@pytest.fixture
def env_setup_self_destruct():
    """Set up the environment base structure"""
    setup_env = EnvSetUp()
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)


@pytest.fixture
def working_dir_self_destruct():
    """Set up the environment base structure"""
    working_dir = WorkingDir()
    yield working_dir
    rm_tree(working_dir.dir, p_crash=False)
