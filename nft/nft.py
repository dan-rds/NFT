from os import listdir
from os.path import isfile, join, exists
from plumbum.cmd import chmod
import os
import pickle
import yaml
import datetime


def absolute_filename(relative_filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if relative_filename is None:
        return dir_path
    return join(dir_path, relative_filename)


def test_file():

    onlyfiles = [
        f for f in listdir(
            absolute_filename("templates")) if isfile(
            absolute_filename(
                join(
                    "templates",
                    f)))]
    print(absolute_filename(None))
    print("Files : ", onlyfiles)
    f = open(absolute_filename("text.txt"), "r+")
    print("from pkg: ", f.readlines())
    return f.readlines()


def get_project_name(current_dir):
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


def edit_template_string(template_str, file_prefix, project_name):
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
    config_filename = absolute_filename("config.yaml")
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

    template_filenames = [
        absolute_filename(
            join(
                "templates",
                f)) for f in listdir(
            absolute_filename("templates")) if isfile(
                    absolute_filename(
                        join(
                            "templates",
                            f)))]
    print(template_filenames)

    templates_dict = {}
    for filename in template_filenames:
        template = open(filename, "rb")
        file_extention = filename.split('.')[-1]
        templates_dict[file_extention] = template.read().strip()

    filename = absolute_filename("templates.pickle")
    outfile = open(filename, 'wb')

    pickle.dump(templates_dict, outfile)
    outfile.close()

    print("Starting user configuration...")
    config_name = raw_input("Name: ")
    email = raw_input("Email address [or github URL]: ")

    configs = {"name": config_name, "email": email}
    config_filename = absolute_filename("config.yaml")
    config_file = open(config_filename, 'w')
    yaml.dump(configs, config_file, default_flow_style=False)


def main(args, executable_flag):
    """ Main function """
    filename = args[0]

    pickle_filename = absolute_filename("templates.pickle")

    if filename == "setup" or not exists(pickle_filename):
        config()
        if filename == "setup":
            return
    templates_pickle = open(pickle_filename, 'rb')
    file_extention = filename.split('.')[-1]
    curr_path = os.getcwd()

    templates_dict = pickle.load(templates_pickle)
    print(templates_dict.keys())
    template_string = templates_dict[file_extention].decode('UTF-8')

    project_name = get_project_name(curr_path)
    file_prefix = filename.split('.')[0]
    with open(filename, 'w+') as output:
        output.write(edit_template_string(template_string,
                                          file_prefix, project_name))
        output.close()
    if executable_flag:
        chmod["a+x", filename]()
