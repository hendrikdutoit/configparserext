'''Testing configparserext__init__()'''

from pathlib import Path
from beetools.beearchiver import Archiver
import ConfigParserExt


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)


def project_desc():
    return _PROJ_DESC


b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)


class TestConfigParserExt:
    def test__init__(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_cpe = ConfigParserExt.ConfigParserExt()
        t_cpe.read(env_setup.ini_pth)

        assert t_cpe
        pass

    def test_get(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_cpe = ConfigParserExt.ConfigParserExt()
        t_cpe.read([env_setup.ini_pth])

        series_prefix = t_cpe.get('General', 'SeriesPrefix')
        assert (
            series_prefix == env_setup.raw_struct['General']['SeriesPrefix']
        )  # Series
        assert t_cpe.get('Series02', 'Cmd1') == 'You;can;split;the;option'
        assert t_cpe.get('Series02', 'Cmd2') == 'Some instruction 4'
        assert t_cpe.get('Series02', 'Cmd', p_prefix=True) == [
            ['cmd1', 'You;can;split;the;option'],
            ['cmd2', 'Some instruction 4'],
        ]
        assert t_cpe.get('Series02', 'Cmd', p_prefix=True, p_split=True) == [
            ['cmd1', ['You', 'can', 'split', 'the', 'option']],
            ['cmd2', ['Some instruction 4']],
        ]
        pass

    def test_sections(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_cpe = ConfigParserExt.ConfigParserExt()
        t_cpe.read([env_setup.ini_pth])

        sections_series = t_cpe.sections()
        assert sections_series == list(env_setup.raw_struct.keys())
        pass

    def test_options(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_cpe = ConfigParserExt.ConfigParserExt()
        t_cpe.read([env_setup.ini_pth])

        option_series = t_cpe.options('Series02')
        assert option_series == list(env_setup.raw_struct['Series02'].keys())
        option_prefix = t_cpe.get('General', 'OptionPrefix')
        option_series = t_cpe.options('Series02', option_prefix)
        assert option_series == ['cmd1', 'cmd2']
        pass

    def test_do_examples(self):
        ConfigParserExt.do_examples()


del b_tls
