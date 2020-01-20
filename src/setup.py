################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: Apache Software License",
	],
	description = "This python module contains support classes for loading and verifying configuratios. It is currently in alpha state as it is not yet clear how complete the implementation and how stable the API is. This modul might still undergo quite some rework.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-jsoncfghelper2/tarball/0.2019.10.29",
	include_package_data = False,
	install_requires = [
		"jk_xmlparser",
		"jk_simplexml",
	],
	keywords = [
		"configuration",
		"json",
	],
	license = "Apache 2.0",
	name = "jk_jsoncfghelper2",
	packages = [
		"jk_jsoncfghelper2",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-jsoncfghelper2",
	version = "0.2019.10.29",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
