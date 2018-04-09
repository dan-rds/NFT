#!/usr/bin/env python3
import sys
import os
import subprocess
from subprocess import PIPE, Popen
import datetime

import create_make

def help_msg(file_types):
	file_types["README"] = "README"
	file_types["Makefile"] = "Makefile"
	print("NFT e.g. New From Template \n   A helper script to quickly create files from a standard template. \n   Takes any file with one of the following suffixentions:")
	for k, v in list(file_types.items()):
		print("\t{:<25}{:<25}".format("<filename>.{}".format(k), " creates " + v + " file"))
	print("\t{:<25}{:<25}".format("README", "creates README"))
	print("\t{:<25}{:<25}".format("Makefile", "creates Makefile"))
	print("Use nft with '-x' option to make the file executable.")
	print("\tCreated by Daniel Richards \n\tMore at github.com/danieldrichards")
	exit()

# Advanced find and replace, performed on str of template file
def edit_template(TEMPLATE_STR, FILE_PREFIX, PROJECT):

	now = datetime.datetime.now()
	date = ("{}-{}-{}".format(now.month, now.day, now.year))

	TEMPLATE_STR = TEMPLATE_STR.replace("<date>", date)
	TEMPLATE_STR = TEMPLATE_STR.replace("<filename>", FILE_PREFIX)
	TEMPLATE_STR = TEMPLATE_STR.replace("<project>", PROJECT)
	return TEMPLATE_STR

curr_path = os.getcwd()
template_dir = os.path.dirname(os.path.abspath(__file__)) + '/templates'
project = curr_path.split("/")[-1]
new_file = sys.argv[-1]
suffix = new_file.split(".")[-1]
prefix = new_file.split(".")[0]
file_types = {"py":"python", "c":"C", "java":"Java", "csh":"csh", "sh":"bash" }

if('-h' in sys.argv[-1] or len(sys.argv) <= 1 ):
	help_msg(file_types)

if(suffix in file_types):
	template_name = template_dir + "/"+ file_types[suffix] + '.' + suffix
elif(new_file == "README"):
	template_name = template_dir + "/README"
elif(new_file == "Makefile"):
	create_make.construct(curr_path, template_dir)
	exit()
else:
	print ("Oops, invalid input \'{}\'. \nTry one of the following:".format(new_file))
	for k in list(file_types.keys()):
		print("\t<filename>.{}".format(k))
	print("\tREADME\n\tMakefile")
	exit()

template = open(template_name, 'r').read()	# Contents of template file as str
template = edit_template(template, prefix, project)
output_file = open("./" + new_file, 'w')
output_file.write(template)
output_file.close()

# Changes file mode to executable.
if('-x' in sys.argv):
	Popen("chmod a+x " + new_file, shell=True)



