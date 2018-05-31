import json
from os import walk
from os.path import join
import re

from bs4 import BeautifulSoup


def _main():
    with open('hàn-lô.json', 'wt', encoding='utf-8') as tóngàn:
        json.dump(
            list(tsuântsáu()), tóngàn,
            ensure_ascii=False, sort_keys=False, indent=2
        )


def tsuântsáu():
    for 所在, _資料夾陣列, 檔案陣列 in sorted(walk('Tsay')):
        for 檔案 in sorted(檔案陣列):
            if 檔案.endswith('.xml'):
                檔名 = join(所在, 檔案)
                yield from 處理(檔名)


def 處理(檔名):
    with open(檔名, encoding='utf-8') as 檔案:
        soup = BeautifulSoup(檔案.read(), 'lxml')
        for u in soup.find_all('u'):
            yield (檔名, *揣出漢羅詞性(u))


def 揣出漢羅詞性(u):
    han = []
    for com in u.find('orthography').find_all(
        re.compile(r'^((com)|w|p)'),
    ):
        try:
            if com.name == 'w' or (com.name == 'com' and com['type'] == 'blob'):
                han.append(com.string)
            elif com.name == 'p' or (com.name == 'com' and com['type'] == 'langs'):
                han.append(str(com))
        except KeyError:
            pass
    try:
        im = u.find('flattier', attrs={'tiername': 'ort'}).string.split()
    except AttributeError:
        print(u)
        raise
    try:
        susing = u.find('flattier', attrs={'tiername': 'cod'}).string.split()
    except AttributeError:
        susing = None

    return han, im, susing


if __name__ == '__main__':
    _main()
