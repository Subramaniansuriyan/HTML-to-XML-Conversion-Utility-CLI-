from bs4 import BeautifulSoup
import os
import sys
from pathlib import Path
import xml.etree.ElementTree as ET


def parse_htmlfile(filepath):
    file_descriptor = open(filepath,"r")
    html_file(file_descriptor)

def html_file(f):
    soup = BeautifulSoup(f.read(), "html.parser")
    print(soup)
    f.close()

    with open('a.xml', 'w') as q:
        q.write(soup.prettify())

    tree = ET.parse('a.xml').getroot()
    for elem in tree.findall('body/p'):
        elem.tag = 'para'



if __name__ == '__main__':
    try:
        arg = sys.argv[1]
        if not os.path.isfile(arg):
            print("file not found")        
        else:
            parse_htmlfile(arg)
    except Exception as e:
        print ("usage: python xml_conv.py directory_path|file_path")