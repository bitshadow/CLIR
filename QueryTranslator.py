# -*- coding: utf-8 -*-
from translator import translator
import urllib2
from xml.dom.minidom import parseString
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

fp = open("FIRE-2011-G/gu.bn.g.topics.126-175.2011.txt", "r");
data = fp.read();
fp.close();

FromLang = "english"
ToLang = "gujarati"

dom = parseString(data);
tags = ["num","title","desc","narr"]

for i in xrange(50):
  print "<top>"
  for j in range(len(tags)-1):
      tag = dom.getElementsByTagName(tags[j])[i].toxml()
      data = tag.replace('<'+tags[j]+'>','').replace('</'+tags[j]+'>','')
      print '<'+tags[j]+'>',
      print translator().fromHtml(data, FromLang, ToLang),
      print "</"+tags[j]+">"
  print "</top>"
  print

