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
        soup = BeautifulSoup(檔案.read())
        for a in soup.findAll('u'):
            print(a)


if __name__ == '__main__':
    _main()
