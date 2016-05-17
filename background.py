#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: background.py
Author: wangtao(wangtao@baidu.com)
Date: 2016/05/16 15:26:48
"""

import os
import urllib
import json
import time
import argparse


def main():
    """
    Main Entry
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--images", help="folder to save images")
    args = arg_parser.parse_args()

    try:
        os.makedirs(args.images)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

    res_handler = urllib.urlopen("http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1")
    res = res_handler.read() 
    try:
        bing_images = json.loads(res)
        image_spec = bing_images["images"][0]
        image_url = image_spec["url"]
        image_name = time.strftime("%Y%m%H") + ".jpg"
        urllib.urlretrieve(image_url, os.path.join(args.images, image_name))
    except Exception as err:
        exit(0)


if __name__ == "__main__":
    main()

