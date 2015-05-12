#!/usr/bin/env python
#
#    wvss

__version__ = '0.0.1'
__author__ = 'TD'

__doc__ = """
Nothing to see here
"""

for av in  ["L", "A", "R"]:
  for ec in ["L", "M", "H"]: 
    for au in ["N", "S", "C"]:
      for c in ["N", "P", "C"]: 
        for i in ["N", "P", "C"]: 
          for a in ["N", "P", "C"]: 
            print "AV:%s/EC:%s/Au:%s/C:%s/I:%s/A:%s %s %s %s %s %s %s" % (av,ec,au,c,i,a,av,ec,au,c,i,a)

            