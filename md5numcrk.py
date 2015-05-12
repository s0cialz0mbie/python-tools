#!/usr/bin/env python
#
#    md5 number cracker (md5numcrk.py)


import sys, md5
b = int(sys.argv[1])
e = int(sys.argv[2])
l = int(sys.argv[3])
h = sys.argv[4]
n = b

print 'Range: %s to %s' % (str(b).zfill(l), str(e).zfill(l))
print 'Hash: %s' % h

while n != b:
  m1 = md5.new()
  m1.update(str(n))
  if h == m1.hexdigest():
    print 'Cracked! Plaintext = %d' % n
    break
  m2 = md5.new()
  m2.update(str(n).zfill(l))
  if h == m2.hexdigest():
    print 'Cracked! Plaintext = %s' % str(n).zfill(l)
    break
  p = ((n-b)*1.0)/(((e-b)/10)*0.1)
  # print 'b=%d e=%d n=%d p=%d p%%10=%d' % (b, e, n, p, p%10)
  if p%10 == 0:
#   print 'Current number = %s  m1 = %s   m2 = %s' % (str(n).zfill(l), m1.hexdigest(), m2.hexdigest())
   print '%d%% complete - Current number = %s' % (p, str(n).zfill(l))
  n += 1
    
    

