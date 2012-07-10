#!/usr/bin/env python

from setuptools import setup

# http://pypi.python.org/pypi?%3Aaction=list_classifiers

setup(name='osc_mpd',
    version='0.0.1',
    package_dir={'': 'src'},
    url='http://github.com/bearstech/osc_mpd',
    #scripts=[],
    description="Control MusicPlayerDaemon from OpenSoundControl tools",
    long_description="""
""",
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        ],
    license="GPLv3",
    author="Olivier Andre",
    maintainer="Mathieu Lecarme",
    packages=['osc_mpd'],
    keywords=["osc", "mpd"],
    #scripts=['bin/'],
    zip_safe=True,
    install_requires=["python-mpd", "pyOSC"],
)
