from setuptools import setup, find_packages

setup(
    name="scrapingtool",
    version="1.0.0",
    author="Ji Wan Kang",
    author_email="jwkang3929@naver.com",
    description="Provides tools for web scraping",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/boringariel/scrapingtool",
    packages=find_packages(),
    install_requires=[
        "requests",
        "selenium",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License, Version 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
