"""Setup for nft"""

import pickle
from os import listdir
from os.path import isfile, join
import yaml
import io
import ast

from setuptools import setup


INSTALL_REQUIRES = (
    ['plumbum>=1.6.7', 'setuptools>=40.7.3', 'PyYAML>=5.1.1']
)


def version():
    """Return version string."""
    with io.open('autopep8.py') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


with io.open('README.md') as readme:
    setup(
        name='nft',
        version=version(),
        description='A tool for quickly ceating a New File form a Template',
        long_description=readme.read(),
        license='Expat License',
        author='Daniel Richards',
        author_email='ddrichar@ucsc.edu',
        url='https://github.com/dan-rds/NFT',
        classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Quality Assurance',
        ],
        keywords='automation, template',
        install_requires=INSTALL_REQUIRES,
        py_modules=['nft'],
        zip_safe=False,
        entry_points={'console_scripts': ['nft = main:main']},
    )

template_filenames = [f for f in listdir(
    "templates") if isfile(join("templates", f))]

templates_dict = {}
for filename in template_filenames:
    template = open(join("templates", filename), "rb")
    file_extention = filename.split('.')[-1]
    templates_dict[file_extention] = template.read()


filename = 'templates.pickle'
outfile = open(filename, 'wb')

pickle.dump(templates_dict, outfile)
outfile.close()

print("Starting user configuration...")
name = input("Name:")
email = input("Email address [or github URL] :")

configs = {"name": name, "email": email}
config_file = open("config.yaml", "w")
yaml.dump(configs, config_file, default_flow_style=False)
