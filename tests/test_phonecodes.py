import sys

import phondler.phondler as phondler
from sentences import sents
import pytest

sys.path.append('../')


def do_something():
    phonecode_test_cases = [('arpabet', 'ipa', phondler.arpabet2ipa, 'eng'),
                            ('ipa', 'arpabet', phondler.ipa2arpabet, 'eng'),
                            ('ipa', 'callhome', phondler.ipa2callhome, 'arz'),
                            ('ipa', 'callhome', phondler.ipa2callhome, 'cmn'),
                            ('ipa', 'callhome', phondler.ipa2callhome, 'spa'),
                            ('callhome', 'ipa', phondler.callhome2ipa, 'arz'),
                            ('callhome', 'ipa', phondler.callhome2ipa, 'cmn'),
                            ('callhome', 'ipa', phondler.callhome2ipa, 'spa'),
                            ('ipa', 'disc', phondler.ipa2disc, 'deu'),
                            ('ipa', 'disc', phondler.ipa2disc, 'eng'),
                            ('ipa', 'disc', phondler.ipa2disc, 'nld'),
                            ('disc', 'ipa', phondler.disc2ipa, 'deu'),
                            ('disc', 'ipa', phondler.disc2ipa, 'eng'),
                            ('disc', 'ipa', phondler.disc2ipa, 'nld'),
                            ('ipa', 'xsampa', phondler.ipa2xsampa, 'amh'),
                            ('ipa', 'xsampa', phondler.ipa2xsampa, 'ben'),
                            ('xsampa', 'ipa', phondler.xsampa2ipa, 'amh'),
                            ('xsampa', 'ipa', phondler.xsampa2ipa, 'ben')]

    for test_case in phonecode_test_cases:
        yield test_case


@pytest.mark.parametrize('case', do_something())
def test_phondler(case):
    print('##### %s2%s ############################' % (case[0], case[1]))
    res = case[2]
    print('%s %s ==> %s %s' % (case[0], sents[case[3]][case[0]], case[1], res))
    assert res == sents[case[3]][case[1]]
