#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :  2018/4/4 13:55
# @Author   :  Zhu Mengyan
# @File     :  sra_to_fastq.py
# @Software :  PyCharm

import fire
#from pyfancy import pyfancy as w
import os.path
import click
import sys
import os

def check_dir(directory):
    """
    judge if your directory is valid!!!
    :param dirs: input directory, containg .sra data
    :return:
    """
    srafiles = []
    if os.path.exists(directory):
        pathlist = os.listdir(directory)

        for filename in pathlist:
            if filename.endswith("sra"):
                print(filename)
                srafiles.append(filename)

        if srafiles:
            print("Obviously, you have .sra file(s) in the directory...")
        else:
            raise FileNotFoundError("SRA file not found!!!!")
    else:
        raise FileNotFoundError("Invalid directory")

    return srafiles



#def check_end(endtype):
    #"""
    #end type: paired end or single end
    #:param endtype:
    #:return:
    #"""
    #if endtype not in ["single", "paired"]:
        #raise ValueError("you should specify end type, single or paired...")
    #print("Your sra files are %s", endtype)

def run(dirs, gz = True):
    filenames = check_dir(dirs)

    command = ""
    for filename in filenames:
        abspath = os.path.join(dirs, filename)
        if gz:
            command = "fastq-dump --gzip --split-3 {name}".format(name = abspath)
        else:
            command = "fastq-dump --split-3 {name}".format(name = abspath)

        os.system(command)




if __name__ == "__main__":
    fire.Fire(run)

