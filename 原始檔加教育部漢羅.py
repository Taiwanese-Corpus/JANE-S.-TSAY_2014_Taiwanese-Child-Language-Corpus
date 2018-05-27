from os import walk
from os.path import join
import re

from bs4 import BeautifulSoup


def _main():
    for 所在, _資料夾陣列, 檔案陣列 in sorted(walk('Tsay')):
        for 檔案 in sorted(檔案陣列):
            if 檔案.endswith('.xml'):
                檔名 = join(所在, 檔案)
                處理(檔名)
                break


def 處理(檔名):
    with open(檔名) as 檔案:
        soup = BeautifulSoup(檔案.read(), 'lxml')
        for u in soup.find_all('u'):
            揣出漢羅詞性(u)


def 揣出漢羅詞性(u):
    han = []
    for com in u.find_all(
        re.compile(r'^(com|w)'),  # attrs={'type': 'blob'}
    ):
        try:
            if com.name == 'w' or (com.name == 'com' and com['type'] == 'blob'):
                han.append(com.string)
        except KeyError:
            pass
    im = u.find('flattier', attrs={'tiername': 'ort'})
    susing = u.find('flattier', attrs={'tiername': 'cod'})
    print(u)
    print(han, im.string.split(), susing.string.split())
    return han, im.string.split(), susing.string.split()


if __name__ == '__main__':
    _main()
