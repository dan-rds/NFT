
import sys
import os
import subprocess
import datetime
from subprocess import PIPE, Popen

def build_make(TEMPLATE, PATH, REPLACE_PAIRS):
	mf = open(PATH+"/Makefile", 'w')
	template = open(TEMPLATE, 'r')
	cont = template.read()

	for old, new in list(REPLACE_PAIRS.items()):
		cont = cont.replace(old, new)
	print (cont)
	mf.write(cont)

def find_dependancies(PATH, EXE, LANG):

	deps = ''
	subprocess.call("javac *.java", shell=True)
	p = Popen("ls *.class", stdout=PIPE, shell=True)
	output_p = p.communicate()[0]
	deps =str(output_p).replace("\\n", "\\\n")
	return (deps[2:-3])

def consruct_makefile(PATH, TEMPLATE_DIR):
	makefile_types = {"c":"C with flags, mostly error checking",
						"java":"simple Java ",
						"jar": "Creates a .jar executable", 
						"":"(return) other"}
	chosen_type = ""
	while True:
		print ("Specify Makefile type:")
		for k, v in list(makefile_types.items()):
			print('\t\'{}\' : {}'.format(k, v))
		chosen_type = input("Specify Makefile type:")
		if(chosen_type in makefile_types):
			break
		print("\nInvalid Makefile type, try again.")
	exe = input("Specify executable [optional]: ")
	main_class = input("Specify class that contains main(): ")
	ext = exe.split(".")[-1]


	template = TEMPLATE_DIR + "/Makefile-" + chosen_type
	pairs = {"<classes>":find_dependancies(PATH, exe, ext), "<executable>":exe, "<main-class>":main_class}

	build_make(template, PATH, pairs)
	
