#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-02-12

from retriever import GoogleImageRetriever
import sys

if __name__ == '__main__':
  retriever = GoogleImageRetriever()
  NUM = 10
  MAX_PAGE = 1

  if len(sys.argv) < 2:
    retriever.usage()
    sys.exit(-1)

  base_file_path = sys.argv[1]

  if len(sys.argv) == 3:
    MAX_PAGE = int(sys.argv[2])

  if len(sys.argv) == 4:
    NUM = int(sys.argv[3])

  for n_epoch in range(1, MAX_PAGE + 1):
    retriever.run(base_file_path="%s_%02d" % (base_file_path, n_epoch),\
                  num=NUM,\
                  start=n_epoch)
