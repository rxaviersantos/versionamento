import xml.dom.minidom

import os
file_path = os.path.join(os.getcwd(), "file.xml")
doc = xml.dom.minidom.parse(file_path)


def get_xml():
    
    doc = xml.dom.minidom.parse("file.xml")
    root = doc.documentElement

    tagName  = doc.getElementsByTagName('hello')

    print (doc.firstChild.tagName)
    for music in tagName:
        adele = music.getAttribute('adele')
        tags = music.getElementsByTagName('item')[0].childNodes[0].data
        print (adele)
        print (tags)

if __name__ == "__main__":
    get_xml();