#!/usr/bin/env python3
import csv, sys
import os
import subprocess
import datetime
from subprocess import PIPE, Popen

def file_replace(old, new, file_path, file_name):
	cmd = []
	cmd.append("ex -sc \'%s/" + old + "/" + new + "/g|x\' " + file_path +"/" + file_name)
	p = Popen(cmd, shell=True)
	print (cmd)

def modify_template(file_path, file_name):
	now = datetime.datetime.now()
	date = ("{}-{}-{}".format(now.month, now.day, now.year))

	file_replace("<date>", date, file_path, file_name)
	file_replace("<filename>", new_file.split(".")[0], file_path, file_name)


path = os.getcwd()
print (path)
print((len(sys.argv)))

file_types = {"py":"python", "c":"C", "java":"Java", "csh":"csh", "sh":"bash", "html":"HTML" }


if ('-h' in sys.argv or len(sys.argv) < 2):
	print("NFT e.g. New From Template \n   A helper script to quickly create files from a standard template. \n   Takes any file with one of the following extentions:")
	for k, v in list(file_types.items()):
		print('\t\'<filename>.{}\'\t {}'.format(k, v))

		filename = []
		filename.append(v)
		filename.append(k)
		print((".".join(filename)))
	print('\t<filename>.ch \t Source and header for C.')
	exit()

cmd = []
new_file = sys.argv[-1]
ext = new_file.split(".")[-1]
prefix = new_file.split(".")[0]
template_name = []

if(ext in file_types):
	template_name.append(file_types[ext])
	template_name.append(ext)
	template_name = (".".join(template_name))

	cmd.append("cat "+ "./" + template_name + " > " + path + "/" + new_file)
	p = Popen(cmd, cwd="/Users/daniel/scripts/new_from_template", shell=True)

	modify_template(path, new_file)

elif(ext == "hc" or ext == "ch"):
	header = prefix + ".h"
	print ("header = ", header)
	cmd.append("cat header.h > " + path + "/" + header)
	p = Popen(cmd, cwd="/Users/daniel/scripts/new_from_template", shell=True)
	
	cmd = []
	source = prefix + ".c"
	cmd.append("cat source.c > " + path + "/" + source)
	p = Popen(cmd, cwd="/Users/daniel/scripts/new_from_template", shell=True)
	
	modify_template(path, source)
	file_replace("!!!!", header, path, source)

	modify_template(path, header)

	




