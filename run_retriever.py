#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-02-12

from retriever import GoogleImageRetriever
import sys

if __name__ == '__main__':
  retriever = GoogleImageRetriever()

  MAX_PAGE = 1
  START    = 1
  NUM      = 10

  if len(sys.argv) < 2:
    retriever.usage()
    sys.exit(-1)

  base_file_path = sys.argv[1]

  if len(sys.argv) >= 3:
    MAX_PAGE = int(sys.argv[2])

  if len(sys.argv) >= 4:
    START    = int(sys.argv[3])

  if len(sys.argv) >= 5:
    NUM      = int(sys.argv[4])

  if MAX_PAGE <= START:
    print("MAX_PAGE(%d) can't be smaller than START(%d)" % (MAX_PAGE, START))

  for n_epoch in range(START, MAX_PAGE + 1):
    # print(START, MAX_PAGE, NUM, n_epoch)
    retriever.run(base_file_path="%s_%02d" % (base_file_path, n_epoch),\
                  num=NUM,\
                  start=n_epoch)
