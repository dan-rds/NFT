#!/usr/bin/env python3
from optparse import OptionParser
import pickle
import logging
import datetime
import os
import yaml
from os.path import isfile, join, exists
from plumbum.cmd import git, basename
from plumbum import local


verbose_flag = False
executable_flag = False
__version__ = '1.1'


def get_project_name(current_dir, script_path) -> str:
    project_name = ''
    if exists(join(current_dir, ".git")):
        full_projectname = git["config", "--get", "remote.origin.url"]()
    else:
        full_projectname = current_dir

    project_name = full_projectname.split("/")[-1].replace(".git", "")

    return project_name


def edit_template_string(TEMPLATE_STR, FILE_PREFIX, PROJECT, CONFIG_PATH) -> str:

    replace_pairs = {}
    now = datetime.datetime.now()
    date = ("{}-{}-{}".format(now.month, now.day, now.year))
    configs = yaml.load(open(CONFIG_PATH, "r+"))
    replace_pairs["<date>"] = date
    replace_pairs["<filename>"] = FILE_PREFIX
    replace_pairs["<project>"] = PROJECT
    replace_pairs["<email>"] = configs["email"]
    replace_pairs["<name>"] = configs["name"]

    for f, r in replace_pairs.items():
        TEMPLATE_STR = TEMPLATE_STR.replace(f, r)

    return TEMPLATE_STR


def main(args):
    filename = args[0]
    file_extention = filename.split('.')[-1]
    curr_path = os.getcwd()

    script_path = os.path.dirname(os.path.realpath(__file__))

    templates_pickle = open(join(script_path, "templates.pickle"), 'rb')
    templates_dict = pickle.load(templates_pickle)

    template_string = templates_dict[file_extention].decode('UTF-8')
    config_path = join(script_path, "config.yaml")
    project_name = get_project_name(curr_path, script_path)
    file_prefix = filename.split('.')[0]
    print(edit_template_string(template_string,
                               file_prefix, project_name, config_path))


if __name__ == '__main__':
    parser = OptionParser(usage="usage: $./check_pos [options] <input_img> <template_img>",
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
    executable_flag = options_dict['x_flag']
    verbose_flag = options_dict['v_flag']
    if len(args) != 1:
        logging.error("Needed one file name but found " + str(len(args)))
    main(args)
