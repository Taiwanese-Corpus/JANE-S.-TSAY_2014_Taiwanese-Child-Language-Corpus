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
