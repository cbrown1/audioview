from setuptools import setup

setup(name='audioview',
    version='0.1',
    description='Simple script to view soundfiles in the terminal',
    url='http://github.com/cbrown1/audioview',
    author='Christopher Brown',
    author_email='cbrown1@pitt.edu',
    license='GPL3',
    packages=['audioview'],
    zip_safe=False,
    install_requires=[
        'pysndfile',
        'plotext',
    ],
    entry_points = {
        'console_scripts': ['audioview=audioview.audioview:main']
    },
      classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Natural Language :: English",
        ],
)

