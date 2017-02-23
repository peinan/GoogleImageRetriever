#!/usr/bin/env python
# coding: utf-8
#
# Author: Peinan ZHANG
# Created at: 2017-02-10

import requests
from PIL import Image
import json, time, os

class GoogleImageRetriever:
  def build_payload(self,
                    google_api_fp='google_api.token',
                    google_custom_search_engine_id_fp='google_custom_search_engine_id.token',
                    queries_fp='queries.txt',
                    num=10,
                    start=1):

    APIKEY  = open(google_api_fp).readline().rstrip()
    CXID    = open(google_custom_search_engine_id_fp).readline().rstrip()
    QUERIES = ' '.join([ line.rstrip() for line in open(queries_fp).readlines() ])
    TYPE    = 'image'
    NUM     = num
    START   = start

    payload = {
        'key': APIKEY,
        'cx':  CXID,
        'q':   QUERIES,
        'searchType': TYPE,
        'num': NUM,
        'start': START
    }

    return payload


  def extract_image_url(self, result):
    result_json = result.json()
    image_urls = []
    try:
      for i, item in enumerate(result_json['items']):
        if not self.is_image(item):
          continue
        image_url = item['link']
        image_urls.append(image_url)
    except:
      print(result.url)
      print(json.dumps(result_json, indent=2))

    return image_urls


  def is_image(self, item):
    if not 'image' in item['mime']:
      return False

    return True


  def is_valid(self, item):
    return True


  def download_images(self, urls, base_file_path=None, interval=5):
    count = 0
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for url in urls:
      image_name = os.path.split(url)[-1]
      file_path  = current_dir + '/' + image_name
      if base_file_path:
        base_dir = os.path.dirname(base_file_path)
        if not os.path.exists(base_dir):
          print(base_dir)
          os.makedirs(base_dir)
        file_path = "%s_%03d_%s" % (base_file_path, count, image_name)
      self.download(url, file_path)
      time.sleep(interval)


  def download(self, url, file_path):
    response = requests.get(url, stream=True)
    print("[INFO] downloading '{}'".format(url))
    if response.status_code != 200:
      print("[FAIL] failed to download '{}'".format(url))
      return False

    try:
      with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=2048):
          f.write(chunk)
      print("[INFO] ---> downloaded to '{}'".format(file_path))
    except:
      print("[FAIL] ---> download failed".format(url))
      return False

    return True


  def run(self, base_file_path=None, start=1, verbose=True):
    URL     = 'https://www.googleapis.com/customsearch/v1'
    payload = self.build_payload(start=start)
    print('QUERIES:', payload['q'])

    result = requests.get(URL, params=payload)

    image_urls = self.extract_image_url(result)
    self.download_images(image_urls, base_file_path)


  def usage(self):
    print("\n",
    "Usage: run_retriever.py [output_basepath]\n",
    "\n",
    "output_basepath:\n",
    "  /aaa/bbb/ccc will be /aaa/bbb/ccc_000_ddd.jpg\n",
    "\n")


if __name__ == '__main__':
  retriever = GoogleImageRetriever()
  retriever.run()

