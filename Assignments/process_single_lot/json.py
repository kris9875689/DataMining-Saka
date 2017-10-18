# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:41:00 2017

Team members:
1.Krishna Saka
2.Lavanya Mengaraboina
3.Keerthi Reddy Gangidi
"""

from xmljson import parker, Parker
from xmljson import yahoo
from xml.etree.ElementTree import fromstring
from json import dumps,loads
import pprint as pp



def xmltojson(file_name,out_file=None):
    fp = open(file_name,'r')

    xmldata = fp.read()

    jsond = dumps(yahoo.data(fromstring(xmldata)))

    jsond = loads(jsond)

    spaces = jsond['parking']['space']

    if not out_file is None:
        f = open(out_file,'w')
        f.write(dumps(spaces,indent=4, separators=(',', ': ')))
        f.close()

    for space in spaces:
        print(space['contour'])
        for point in space['contour']['point']:
            print(point)

if __name__=='__main__':
    filename = 'C:\\Users\\keerthi\\.spyder-py3\\2012-12-07_17_12_25.xml'
    xmltojson(filename,'project1.json')
