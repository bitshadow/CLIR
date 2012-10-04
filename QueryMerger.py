# -*- coding: utf-8 -*-
from parser import parser
import urllib2
from xml.dom.minidom import parseString
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

"""
Merge translated queries to compare different translation system
with human translation.
"""
size = 5
fp = [None]*size
dom = [None]*size
tag = [None]*size

fp[0] = open("FIRE-2011/hi.topics.126-175.2011.txt", "r");
fp[1] = open("FIRE-2011-G/hi.en.g.topics.126-175.2011.txt", "r");
fp[2] = open("FIRE-2011-G/hi.bn.g.topics.126-175.2011.txt", "r");
fp[3] = open("FIRE-2011-G/hi.gu.g.topics.126-175.2011.txt", "r");
fp[4] = open("FIRE-2011-G/hi.en.m.topics.126-175.2011.txt", "r");

for i in xrange(size):
   data = fp[i].read();
   dom[i] = parseString(data);
   fp[i].close();

tags = ["num","title","desc","narr"]
qrys = {"hi": 0, "hi.en" : 1, "hi.bn" : 2, "hi.gu" : 3}

for i in xrange(50):

  tg = dom[0].getElementsByTagName(tags[0])[i].toxml()
  print tg.replace('<'+tags[1]+'>','').replace('</'+tags[1]+'>','')

  for j in range(size):
    tag = dom[j].getElementsByTagName(tags[1])[i].toxml()

    if j == qrys["hi"]:
      print "<HI>",
      print tag.replace('<'+tags[1]+'>','').replace('</'+tags[1]+'>',''),
      print "</HI>"

    elif j == qrys["hi.en"]:
      print "<HI_E_G>",
      print tag.replace('<'+tags[1]+'>','').replace('</'+tags[1]+'>',''),
      print "</HI_E_G>"

    elif j == qrys["hi.bn"]:
      print "<HI_B_G>",
      print tag.replace('<'+tags[1]+'>','').replace('</'+tags[1]+'>',''),
      print "</HI_B_G>"

    elif j == qrys["hi.gu"] :
      print "<HI_GU_G>",
      print tag.replace('<'+tags[1]+'>','').replace('</'+tags[1]+'>',''),
      print "</Hi_GU_G>"

    else:
      print "<HI_E_BING>",
      print tag.replace('<'+tags[1]+'>','').replace('</'+tags[1]+'>',''),
      print "</Hi_E_BING>"

  print


