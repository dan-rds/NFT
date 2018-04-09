import sys
import os
import subprocess
import datetime
from subprocess import PIPE, Popen


# find_dependancies; for java/jar projects
# nessesary if nested classes are used 
def find_dependancies(PATH, EXE, LANG):
	deps = ''
	subprocess.call("javac *.java", shell=True)
	p = Popen("ls *.class", stdout=PIPE, shell=True)
	output_p = p.communicate()[0]
	deps =str(output_p).replace("\\n", "\\\n")	#process ugly stdout 
	return (deps[2:-3]) 

def construct(PATH, TEMPLATE_DIR):
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
	main_class = input("Specify class that contains main() [optional]: ")
	ext = exe.split(".")[-1]
	template_path = TEMPLATE_DIR + "/Makefile-" + chosen_type

	new_file = open(PATH+"/Makefile", 'w')
	template = open(template_path, 'r').read()

	template = template.replace("<classes>", find_dependancies(PATH, exe, ext))
	template = template.replace("<executable>", exe)
	template = template.replace("<main-class>", main_class)

	new_file.write(template)
	new_file.close()

	
