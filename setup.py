import os, pathlib
from setuptools.command.develop import develop
from setuptools.command.install import install
from setuptools.command.sdist import sdist
from setuptools import setup, find_packages
from subprocess import check_call

# Package 
HERE = pathlib.Path(__file__).parent
PACKAGE_NAME  = 'YolovPackage'
VERSION = '1.0'
AUTHOR = 'Diego De Quintal'
AUTHOR_EMAIL = 'diego.dequintal@newtoms.com'
URL = 'https://github.com/diegodequintal/Yolov5_DeepSort_Pytorch'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Yolov5'
LONG_DESCRIPTION = (HERE/"README.md").read_text()
LONG_DESC_TYPE = 'text/markdown'

def gitcmd_update_submodules():
	'''	Check if the package is being deployed as a git repository. If so, recursively
		update all dependencies.

		@returns True if the package is a git repository and the modules were updated.
			False otherwise.
	'''
	if os.path.exists(os.path.join(HERE, '.git')):
		check_call(['git', 'submodule', 'update', '--init', '--recursive'])
		return True

	return False


class gitcmd_develop(develop):
	'''	Specialized packaging class that runs git submodule update --init --recursive
		as part of the update/install procedure.
	'''
	def run(self):
		gitcmd_update_submodules()
		develop.run(self)


class gitcmd_install(install):
	'''	Specialized packaging class that runs git submodule update --init --recursive
		as part of the update/install procedure.
	'''
	def run(self):
		gitcmd_update_submodules()
		install.run(self)


class gitcmd_sdist(sdist):
	'''	Specialized packaging class that runs git submodule update --init --recursive
		as part of the update/install procedure;.
	'''
	def run(self):
		gitcmd_update_submodules()
		sdist.run(self)


setup(
    cmdclass={
		'develop': gitcmd_develop, 
		'install': gitcmd_install, 
		'sdist': gitcmd_sdist,
	}, 
	name=PACKAGE_NAME,
	version=VERSION,
	description=DESCRIPTION, 
	author=AUTHOR, license=LICENSE, 
	author_email=AUTHOR_EMAIL, 
	url=URL, 
	packages=find_packages())
