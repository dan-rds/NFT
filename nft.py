#!/usr/bin/env python3
""" nft script. For more info, see https://pypi.org/project/nft/ """
from optparse import OptionParser
import pickle
import logging
import datetime
import os
from os import listdir
from os.path import isfile, join, exists
from plumbum.cmd import git, chmod
import yaml
import pkg_resources


verbose_flag = False
executable_flag = False
__version__ = '1.11'


def get_project_name(current_dir) -> str:
    """
    Grabs name of remote if it exists, otherwise, gets directory name

    Parameters:
    current_dit (str): The CWD

    Returns:
    str: project name

    """
    project_name = ''
    if exists(join(current_dir, ".git")):
        full_projectname = git["config", "--get", "remote.origin.url"]()
    else:
        full_projectname = current_dir

    project_name = full_projectname.split("/")[-1].replace(".git", "")

    return project_name


def edit_template_string(template_str, file_prefix, project_name) -> str:
    """
    A fancy find-and-replace that replaces all the necessary info in the template string.

    Parameters:
    template_str (str): The contents of the template file
    file_prefix (str): Filename without extention, e.g. test.py => test
    project_name (str): Name of the project

    Returns:
    str: edited template
    """

    replace_pairs = {}
    now = datetime.datetime.now()
    date = ("{}-{}-{}".format(now.month, now.day, now.year))
    config_filename = pkg_resources.resource_filename(__name__, "config.yaml")
    configs = yaml.load(open(config_filename, "r+"), Loader=yaml.SafeLoader)
    replace_pairs["<date>"] = date
    replace_pairs["<filename>"] = file_prefix
    replace_pairs["<project>"] = project_name
    replace_pairs["<email>"] = configs["email"]
    replace_pairs["<name>"] = configs["name"]

    for pattern, replacement in replace_pairs.items():
        template_str = template_str.replace(pattern, replacement)

    return template_str


def config():
    """
    Config step. Reads template files into pickle. Then prompts
    user for name and email and saves to config.yaml
    """
    template_filenames = [f for f in listdir(
        "templates") if isfile(join("templates", f))]

    templates_dict = {}
    for filename in template_filenames:
        template = open(join("templates", filename), "rb")
        file_extention = filename.split('.')[-1]
        templates_dict[file_extention] = template.read()

    filename = pkg_resources.resource_filename(__name__, "templates.pickle")
    outfile = open(filename, 'wb')

    pickle.dump(templates_dict, outfile)
    outfile.close()

    print("Starting user configuration...")
    name = input("Name:")
    email = input("Email address [or github URL] :")

    configs = {"name": name, "email": email}
    config_filename = pkg_resources.resource_filename(__name__, "config.yaml")
    config_file = open(config_filename, 'w')
    yaml.dump(configs, config_file, default_flow_style=False)


def main(args):
    """ Main function """
    filename = args[0]
    pickle_filename = pkg_resources.resource_filename(
        __name__, "templates.pickle")
    if filename == "setup" or not isfile(pickle_filename):
        config()
    templates_pickle = open(pickle_filename, 'rb')
    file_extention = filename.split('.')[-1]
    curr_path = os.getcwd()

    templates_dict = pickle.load(templates_pickle)
    template_string = templates_dict[file_extention].decode('UTF-8')

    project_name = get_project_name(curr_path)
    file_prefix = filename.split('.')[0]
    with open(filename, 'w+') as output:
        output.write(edit_template_string(template_string,
                                          file_prefix, project_name))
        output.close()
    if executable_flag:
        chmod["a+x", filename]()


def nft():
    """ nft entry point. Mostly command line parsing """
    parser = OptionParser(usage="usage: $./nft [options] <filename>",
                          version="%prog 0.1")
    parser.add_option("-x", "--eXecutable",
                      action="store_true",
                      dest="x_flag",
                      default=False,
                      help="Chmods the file so it is an executable")
    parser.add_option("-v", "--verbose",
                      action="store_true",
                      dest="v_flag",
                      default=False,
                      help="Verbose mode",)
    (options, args) = parser.parse_args()
    options_dict = vars(options)
    global executable_flag
    global verbose_flag
    executable_flag = options_dict['x_flag']
    verbose_flag = options_dict['v_flag']
    if len(args) != 1:
        msg = "Needed one file name but found " + str(len(args))
        logging.error(msg)
    main(args)
