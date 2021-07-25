import sys

import pytest

sys.path.append('../')
import phodic.phond as phonecodes
from sentences import sents


def do_something():
    phonecode_test_cases = [('arpabet', 'ipa', phonecodes.arpabet2ipa, 'eng'),
                            ('ipa', 'arpabet', phonecodes.ipa2arpabet, 'eng'),
                            ('ipa', 'callhome', phonecodes.ipa2callhome, 'arz'),
                            ('ipa', 'callhome', phonecodes.ipa2callhome, 'cmn'),
                            ('ipa', 'callhome', phonecodes.ipa2callhome, 'spa'),
                            ('callhome', 'ipa', phonecodes.callhome2ipa, 'arz'),
                            ('callhome', 'ipa', phonecodes.callhome2ipa, 'cmn'),
                            ('callhome', 'ipa', phonecodes.callhome2ipa, 'spa'),
                            ('ipa', 'disc', phonecodes.ipa2disc, 'deu'),
                            ('ipa', 'disc', phonecodes.ipa2disc, 'eng'),
                            ('ipa', 'disc', phonecodes.ipa2disc, 'nld'),
                            ('disc', 'ipa', phonecodes.disc2ipa, 'deu'),
                            ('disc', 'ipa', phonecodes.disc2ipa, 'eng'),
                            ('disc', 'ipa', phonecodes.disc2ipa, 'nld'),
                            ('ipa', 'xsampa', phonecodes.ipa2xsampa, 'amh'),
                            ('ipa', 'xsampa', phonecodes.ipa2xsampa, 'ben'),
                            ('xsampa', 'ipa', phonecodes.xsampa2ipa, 'amh'),
                            ('xsampa', 'ipa', phonecodes.xsampa2ipa, 'ben')]

    for test_case in phonecode_test_cases:
        yield test_case


@pytest.mark.parametrize('case', do_something())
def test_phonecodes(case):
    print('##### %s2%s ############################' % (case[0], case[1]))
    res = case[2](sents[case[3]][case[0]], case[3])
    print('%s %s ==> %s %s' % (case[0], sents[case[3]][case[0]], case[1], res))
    assert res == sents[case[3]][case[1]]
