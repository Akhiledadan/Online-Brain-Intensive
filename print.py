#!/usr/bin/python2.7 -tt

import sys

def Cat(filename):
  f = open(filename,'rU')
  print f
  for line in f:
   print line,
  f.close()

def main():
  Cat(sys.argv[1])

if __name__ == '__main__':
  main()



