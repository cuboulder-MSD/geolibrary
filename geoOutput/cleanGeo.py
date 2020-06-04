# -*- coding: utf-8 -*-
import sys, re, uuid, glob
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import copy
from datetime import datetime
from pathlib import Path



# def removeColons(root):
#
#     return root

def updateForm(root):
    ns = {'mods':'http://www.loc.gov/mods/v3'}
    # header=root.find('mods:mods',ns)
    form = root.find('mods:physicalDescription/mods:form',ns)
    # print(form.text)
    if form.text == 'Vector data':
        form.set('authority','LCGFT')
        form.set('authorityURI','http://id.loc.gov/authorities/genreForms/gf2011026297')
        form.text = 'Geospatial data'
        # print(form.attrib)


    return root

def addPublisher(root):
    # print(root)
    ns = {'mods':'http://www.loc.gov/mods/v3'}
    for name in root.findall('mods:name',ns):
        for rt in name.findall('mods:role/mods:roleTerm',ns):
            if rt.text == 'publisher':
                root.remove(name)


        # print(x)


        # if roleTerm.text == 'publisher':
        #     roleTerm.text = 'motherfucker'
        #
        #     root.remove(roleTerm)
            # print(roleTerm.text)



    return root




# def updateAttributes(root):
#
#     return root



def main():
    parser = ET.XMLParser(encoding="utf-8")

    p = Path("/Users/erra1244/Desktop/geoTest/")

    # file_list = [f for f in p.iterdir() if f.is_file()]
    for file in p.glob('*.xml'):
        # print(file)
        ns = {'mods':'http://www.loc.gov/mods/v3'}
        ET.register_namespace('mods',"http://www.loc.gov/mods/v3")
        tree=ET.parse(file,ET.XMLParser(encoding='utf-8'))
        root=tree.getroot()
        updateForm(root)
        addPublisher(root)
        strfile=str(file)
        filename= strfile.strip('/Users/erra1244/Desktop/geoTest/')
    # print(tree)
        tree.write(filename, xml_declaration=True,encoding='utf-8',method='xml')

# make this a safe-ish cli script
if __name__ == '__main__':
    # print(tree)

    main()
