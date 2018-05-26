from os import walk
from os.path import join

from bs4 import BeautifulSoup


def _main():
    for 所在, _資料夾陣列, 檔案陣列 in sorted(walk('Tsay')):
        for 檔案 in 檔案陣列:
            if 檔案.endswith('.xml'):
                檔名 = join(所在, 檔案)
                處理(檔名)
                break


def 處理(檔名):
    with open(檔名) as 檔案:
        soup = BeautifulSoup(檔案.read(), 'lxml')
        for u in soup.find_all('u'):
            han = [
                com.string
                for com in u.find_all('com', attrs={'type': 'blob'})
            ]
            im = u.find('flattier', attrs={'tiername': 'ort'})
            susing = u.find('flattier', attrs={'tiername': 'cod'})
            print(u)
            print(han, im.string.split(), susing.string.split())


if __name__ == '__main__':
    _main()
