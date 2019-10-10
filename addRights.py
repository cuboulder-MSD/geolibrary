import sys, re, uuid, os, glob
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import copy, time, datetime
import datetime, requests, json


ns = {'mods':'http://www.loc.gov/mods/v3'}
ET.register_namespace('mods', "http://www.loc.gov/mods/v3")

    # do your stuff

for filename in glob.glob('*.xml'):


    tree=ET.parse(filename)
    root=tree.getroot()

    # for elem in root.findall('mods:name/mods:namePart',ns):
    for name in root.findall('mods:name',ns):
        for namePart in name.findall('mods:namePart',ns):
            if namePart.get('valueURI') == 'http://id.worldcat.org/fast/1978978':
                del namePart.attrib["valueURI"]
                name.set('valueURI', 'http://id.worldcat.org/fast/1978978')
                # print(namePart.get('valueURI'))
                # print(namePart.get('valueURI'))

    for rights in root.findall('mods:accessCondition',ns):
        if rights.get('xlink'):
            del rights.attrib['xlink']
        rights.set('xmlns:xlink','https://rightsstatements.org/page/NoC-US/1.0/?language=en')
        if rights.text == None:
            rights.set('type', 'use and reproduction')
            rights.text = 'The organization that has made the Item available believes that the Item is in the Public Domain under the laws of the United States.'

    newtree = ET.ElementTree(root)
    randomNumber = uuid.uuid4()
    # print(randomNumber)
    outfile_path = filename

    newtree.write(outfile_path, encoding="utf8")
