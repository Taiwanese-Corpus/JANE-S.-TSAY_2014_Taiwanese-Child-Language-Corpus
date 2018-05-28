from unittest.case import TestCase

from bs4 import BeautifulSoup


from 原始檔加教育部漢羅 import 揣出漢羅詞性


class 揣出漢字試驗(TestCase):
    def tearDown(self):
        漢, _羅, _詞性 = 揣出漢羅詞性(BeautifulSoup(self.資料, 'lxml'))
        self.assertEqual(漢, self.漢)

    def test_漢字_com(self):
        self.漢 = ['遐1', '是', '佗位?']
        self.資料 = '''
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

    def test_漢字_w(self):
        self.漢 = ['你','彼1','未使','揤2','oo02','<p type="PERIOD">.</p>']
        self.資料 = '''
        <u speaker="INV" id="3492e6a6-2c17-4318-8698-5aa30230092e" excludeFromSearches="false">
            <orthography>
                <g>
                    <w>你</w>
                </g>
                <g>
                    <w>彼1</w>
                </g>
                <g>
                    <w>未使</w>
                </g>
                <g>
                    <w>揤2</w>
                </g>
                <g>
                    <w>oo02</w>
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
                <ag length="0"/>
            </alignment>
            <segment startTime="0.0" duration="0.0" unitType="ms"/>
            <notes tierName="Notes">referring to the keystroke on the recording machine</notes>
            <flatTier tierName="ort">li2 he1 be7sai2 chih8 oo0.</flatTier>
            <flatTier tierName="cod">Nh Nep D VC T</flatTier>
        </u>'''

    def test_漢字_空的w(self):
        self.fail()
        self.漢 = 'xx'
        self.資料 = '''
        <u speaker="INV" id="1b7214eb-5b56-4cbf-acaf-39f4563191a7" excludeFromSearches="false">
            <orthography>
                <g>
                    <w>畫</w>
                </g>
                <g>
                    <w>一1</w>
                </g>
                <g>
                    <w>个</w>
                </g>
                <g>
                    <w>門</w>
                </g>
                <g>
                    <w>a02</w>
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
                <ag length="0"/>
            </alignment>
            <segment startTime="269260.0" duration="1719.0" unitType="ms"/>
            <flatTier tierName="ort">ue7 cit8 e5 mng5 a0.</flatTier>
            <flatTier tierName="cod">VC Neu Nf Na T</flatTier>
        </u>'''

    def test_漢字_w有com(self):
        self.fail()
        self.漢 = 'xx'
        self.資料 = '''
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
    def test_漢字_w同齊com(self):
        self.fail()
        self.漢 = 'xx'
        self.資料 = '''
        <u speaker="INV" id="342fbdbf-ce69-4a94-899f-6a1c9c094070" excludeFromSearches="false">
            <orthography>
                <g>
                    <p type="OPEN_BRACE">{</p>
                    <w>這1</w>
                    <com>/</com>
                    <p type="CLOSE_BRACE">}</p>
                </g>
                <g>
                    <w>這1</w>
                </g>
                <g>
                    <w>啥物</w>
                    <p type="QUESTION">?</p>
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
            </ipaTier>
            <alignment type="segmental">
                <ag length="0"/>
                <ag length="0"/>
                <ag length="0"/>
            </alignment>
            <segment startTime="5283.0" duration="801.0" unitType="ms"/>
            <flatTier tierName="ort">ce1 [/] ce1 sann2mih8?</flatTier>
            <flatTier tierName="cod">Nep Nep Nep</flatTier>
        </u>'''
    def test_華語(self):
        self.fail()
        '''
        <u speaker="INV" id="78577262-aa4a-4db3-aabd-754ef3f07d95" excludeFromSearches="false">
            <orthography>
                <g>
                    <com type="langs">single,zho</com>
                    <w>垃圾桶</w>
                </g>
                <g>
                    <w>oo02</w>
                    <p type="QUESTION">?</p>
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
            </ipaTier>
            <alignment type="segmental">
                <ag length="0"/>
                <ag length="0"/>
            </alignment>
            <segment startTime="470171.0" duration="1336.0" unitType="ms"/>
            <flatTier tierName="ort">le4se4tong3@s oo0?</flatTier>
            <flatTier tierName="cod">Na T</flatTier>
        </u>'''