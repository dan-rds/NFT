#!/usr/bin/env python3
import sys
import os
import subprocess
import datetime

import make_makefile 
from subprocess import PIPE, Popen

def edit_template(TEMPLATE_STR, FILE_PREFIX):

	now = datetime.datetime.now()
	date = ("{}-{}-{}".format(now.month, now.day, now.year))

	TEMPLATE_STR = TEMPLATE_STR.replace("<date>", date)
	TEMPLATE_STR = TEMPLATE_STR.replace("<filename>", FILE_PREFIX)
	return TEMPLATE_STR


path = os.getcwd()
running_dir = os.path.dirname(os.path.abspath(__file__))
file_types = {"py":"python", "c":"C", "java":"Java", "csh":"csh", "sh":"bash", "html":"HTML" }


if ('-h' in sys.argv ):#or len(sys.argv) < 2):
	print("NFT e.g. New From Template \n   A helper script to quickly create files from a standard template. \n   Takes any file with one of the following extentions:")
	for k, v in list(file_types.items()):
		print('\t\'<filename>.{}\'\t {}'.format(k, v))

		filename = []
		filename.append(v)
		filename.append(k)
		print((".".join(filename)))
	exit()


new_file = sys.argv[-1]
ext = new_file.split(".")[-1]
prefix = new_file.split(".")[0]


if(ext in file_types):
	template_name= running_dir + "/" + file_types[ext]+ "." + ext
	print("template_name  [" ,type(template_name).__name__, "]   :", template_name)
else:
	print ("Oops, invalid input {}".format(new_file))
	exit()

template_file = open(template_name, 'r')
template = template_file.read()

template = edit_template(template, prefix)
output_file = open("./"+new_file, 'w')
output_file.write(template)
output_file.close()




