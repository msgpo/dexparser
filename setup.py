from setuptools import setup

with open("README.md") as f:
	long_description = f.read() 

setup(
	name = 'dexparser',
	version = '1.0.1',
	py_modules = ['dexparser'],
	author = 'austinkim',
	author_email = 'bunseokbot@gmail.com',
	url = 'https://github.com/bunseokbot/dexparser',
	description = 'Powerful DEX file format parser for Pythonist',
	long_description = long_description,
    long_description_content_type = 'text/markdown',
	classifiers = [
		'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	python_requires='>=3.5',
)
