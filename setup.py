try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': "Checks the strength of the password you enter to see if it meets today's standards.",
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/strong_pass_020918_1',
	'download_url': 'https://github.com/sunnylam13/strong_pass_020918_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['re'],
	'scripts': [],
	'name': 'Strong Password Checker'
}

setup(**config)