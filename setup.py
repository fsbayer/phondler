from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='phondler',
    version='0.0.3',
    license='MIT License',
    author='Frederic Bayer',
    author_email='frederic.s.bayer@gmail.com',
    description='Python phonetic handler',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fsbayer/phondler',
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    # package_dir={"": ""},
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Artistic Software",
        "Topic :: Education",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    python_requires=">=3.9"
)
