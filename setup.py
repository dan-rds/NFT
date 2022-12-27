from setuptools import setup
import io
def version():
    """Return version string."""
    with io.open('nft/nft.py') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s

with io.open('README.rst') as readme:
    setup(name='nft',
            version=version(),
            description='A tool for quickly creating a New File form a Template',
            long_description=readme.read(),
            license='Expat License',
            author='Daniel Richards',
            author_email='ddrichar@ucsc.edu',
            url='https://github.com/dan-rds/NFT',
            packages=['nft'],
            package_data={'nft': ['*.txt', 'templates/*']},
            classifiers=[
                "Programming Language :: Python :: 3"
            ],
            install_requires=['setuptools==65.5.1', 'plumbum==1.6.7', 'PyYAML==5.1.1'],
            zip_safe=False,
            scripts=['bin/nft'],
            keywords='automation, template',
            )
