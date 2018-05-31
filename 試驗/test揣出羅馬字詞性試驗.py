from unittest.case import TestCase

from bs4 import BeautifulSoup
from 原始檔加教育部漢羅 import 揣出漢羅詞性


class 揣出羅馬字詞性試驗(TestCase):
    資料 = '''
        <u speaker="INV" id="76274cb4-748b-462a-b532-1650b21854b5" excludeFromSearches="false">
            <orthography>
                <g>
                    <com type="blob">遐1</com>
                    <com type="blob">是</com>
                    <com type="blob">佗位?</com>
                    <com type="t">missing CA terminator</com>
                </g>
            </orthography>
            <ipaTier form="model">
                <pg>
                    <w></w>
                    <sb/>
                </pg>
            </ipaTier>
            <ipaTier form="actual">
                <pg>
                    <w></w>
                    <sb/>
                </pg>
            </ipaTier>
            <alignment type="segmental">
                <ag length="0"/>
            </alignment>
            <segment startTime="5940.0" duration="1137.0" unitType="ms"/>
            <flatTier tierName="ort">hia1 si7 to2ui7?</flatTier>
            <flatTier tierName="cod">Ncd SHI Ncd</flatTier>
        </u>'''

    def test_詞性(self):
        _漢, _羅, 詞性 = 揣出漢羅詞性(BeautifulSoup(self.資料, 'lxml'))
        self.assertEqual(詞性, ['Ncd', 'SHI', 'Ncd'])

    def test_羅馬字(self):
        _漢, 羅, _詞性 = 揣出漢羅詞性(BeautifulSoup(self.資料, 'lxml'))
        self.assertEqual(羅, ['hia1', 'si7', 'to2ui7?'])

    def test_愛deocde(self):
        資料 = '''
        <u speaker="INV" id="4962c440-ff46-45c3-abe0-8689f56f0793" excludeFromSearches="false">
            <orthography>
                <g>
                    <w>好</w>
                    <p type="COMMA">,</p>
                </g>
                <g>
                    <p type="OPEN_BRACE">{</p>
                    <w>換</w>
                    <w>爿</w>
                    <com>/</com>
                    <p type="CLOSE_BRACE">}</p>
                </g>
                <g>
                    <w>換</w>
                </g>
                <g>
                    <w>爿</w>
                    <p type="PERIOD">.</p>
                </g>
            </orthography>
            <ipaTier form="model">
                <pg>
                    <w></w>
                    <sb/>
                </pg>
                <pg>
                    <w></w>
                    <sb/>
                </pg>
                <pg>
                    <w></w>
                    <sb/>
                </pg>
                <pg>
                    <w></w>
                    <sb/>
                </pg>
            </ipaTier>
            <ipaTier form="actual">
                <pg>
                    <w></w>
                    <sb/>
                </pg>
                <pg>
                    <w></w>
                    <sb/>
                </pg>
                <pg>
                    <w></w>
                    <sb/>
                </pg>
                <pg>
                    <w></w>
                    <sb/>
                </pg>
            </ipaTier>
            <alignment type="segmental">
                <ag length="0"/>
                <ag length="0"/>
                <ag length="0"/>
                <ag length="0"/>
            </alignment>
            <segment startTime="459850.0" duration="1300.0" unitType="ms"/>
            <flatTier tierName="ort">ho2 &lt;uann7 ping5&gt; [/] uann7 ping5.</flatTier>
            <flatTier tierName="cod">VH VC Ncd VC Ncd</flatTier>
        </u>'''
        _漢, 羅, _詞性 = 揣出漢羅詞性(BeautifulSoup(資料, 'lxml'))
        self.assertEqual(羅, 'ho2 <uann7 ping5> [/] uann7 ping5.'.split())

    def test_無詞性(self):
        資料 = '''
        <u excludefromsearches="false" id="ef092fc0-5b46-4123-a6bd-147d62c8b1f1" speaker="GRM">
<orthography>
<g>
<com type="blob">&lt;你</com>
<com type="blob">e0</com>
<com type="blob">衫&gt;</com>
<com type="blob">[&lt;]</com>
<com type="blob">有</com>
<com type="blob">口袋@s</com>
<com type="blob">oo02.</com>
<com type="t">missing CA terminator</com>
</g>
</orthography>
<ipatier form="model">
<pg>
<w></w>
<sb></sb>
</pg>
</ipatier>
<ipatier form="actual">
<pg>
<w></w>
<sb></sb>
</pg>
</ipatier>
<alignment type="segmental">
<ag length="0"></ag>
</alignment>
<segment duration="1245.0" starttime="1122464.0" unittype="ms"></segment>
<flattier tiername="ort">&lt;li2 e0 sann1&gt; [&lt;] u7 kou3dai4@s oo0.</flattier>
</u>'''
        _漢, _羅, 詞性 = 揣出漢羅詞性(BeautifulSoup(資料, 'lxml'))
        self.assertEqual(詞性, None)
