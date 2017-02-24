#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-02-12

from retriever import GoogleImageRetriever
import sys

if __name__ == '__main__':
  retriever = GoogleImageRetriever()
  num = 10
  start = 1
  if len(sys.argv) < 2:
    retriever.usage()
    sys.exit(-1)

  base_file_path = sys.argv[1]

  if len(sys.argv) == 3:
    start = sys.argv[2]

  for n_epoch in range(start):
    retriever.run("%s_%02d" % (base_file_path, n_epoch), num, n_epoch)
