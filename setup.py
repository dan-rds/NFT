from setuptools import setup
import io
__version__ = '2.0'
with io.open('requirements.txt') as requireFile:
    install_requirements = [str(r.strip()) for r in requireFile.readlines()]
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
                install_requires=install_requirements,
                zip_safe=False,
                scripts=['bin/nft'],
                keywords='automation, template',
                )
