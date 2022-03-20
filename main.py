'''
main module of project. developed for site-scrapping
'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
from bs4 import BeautifulSoup
import requests


def los(link):
    '''

    :param link: http://example.com
    :return: nothing to return
    '''
    if link in result:
        return
    result.append(link)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    for page in soup.find_all('a', href=True):
        buf = page.get('href')
        #print(buf)
        if buf.startswith('http') and f'{shortpage}' in buf:
            ul.add(buf)
            los(buf)
        elif buf.startswith('/'):
            buf = f'{STARTPAGE}{buf}'
            ul.add(buf)
            los(buf)




if __name__ == '__main__':
    ul = set()
    result = []
    STARTPAGE = 'https://letsenhance.io'
    if STARTPAGE.startswith('https'):
        shortpage = re.sub(r'https://', '', f'{STARTPAGE}')
    else:
        shortpage = re.sub(r'http://', '', f'{STARTPAGE}')
    print(shortpage)
    los(STARTPAGE)
    print(result)
    with open('listfile.txt', 'w') as filehandle: # pylint: disable=unspecified-encoding
        for line in result:
            filehandle.write(line + '\n')
