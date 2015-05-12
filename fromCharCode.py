#!/usr/bin/env python
#
#    fromCharCode

#convert pass string into String.fromCharCode(##,##,##,##,##)
import sys
inpstr = str(sys.argv[1])
print 'Converting %s...' % inpstr
outstr = 'String.fromCharCode(' + str(ord(inpstr[0]))
for i in range(1, len(inpstr)):
  outstr += ',' + str(ord(inpstr[i]))
outstr += ');'
print outstr

