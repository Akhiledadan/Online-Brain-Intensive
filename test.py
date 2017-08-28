#!/usr/bin/python2.7 -tt

import sys

def hello(name):
  if name == 'akhil' or name == 'Akhil':
   print name, 'edadan'
  else:
   print 'unknown'

def main():
  hello(sys.argv[1])

if __name__ == '__main__':
  main()



