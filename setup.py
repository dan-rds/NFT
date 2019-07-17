from setuptools import setup
import io
__version__ = '2.3'

with io.open('README.rst') as readme:
    setup(name='nft',
            version=__version__,
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
            install_requires=['setuptools==40.7.3', 'plumbum==1.6.7', 'PyYAML==5.1.1'],
            zip_safe=False,
            scripts=['bin/nft'],
            keywords='automation, template',
            )
