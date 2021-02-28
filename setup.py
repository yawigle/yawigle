import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yawigle", # Replace with your own username
    version="0.0.4",
    author="yawigle",
    author_email="danilonc@users.noreply.github.com",
    description="Yet another Wigle.net client API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yawigle/yawigle",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Topic :: Communications :: Ham Radio"
    ],
    python_requires='>=3.5.1',
)
