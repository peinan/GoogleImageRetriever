#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-02-12

from retriever import GoogleImageRetriever
import sys

if __name__ == '__main__':
  retriever = GoogleImageRetriever()
  if len(sys.argv) < 2:
    retriever.usage()
    sys.exit(-1)

  retriever.run(sys.argv[1])

