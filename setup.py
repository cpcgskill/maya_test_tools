#!/usr/bin/python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import setuptools

with open("README.md", "rb") as f:
    long_description = f.read().decode(encoding="utf-8")

setuptools.setup(
    name="maya_test_tools",
    version="0.1.0",
    author="cpcgskill",
    author_email="cpcgskill@outlook.com",
    description="maya 工具包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cpcgskill/maya_test_tools",
    project_urls={
        "Bug Tracker": "https://github.com/cpcgskill/maya_test_tools/issues",
    },
    license="Apache Software License (Apache 2.0)",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    package_dir={"": "src"},
    # 不使用自动搜索
    # packages=setuptools.find_packages(where="src"),
    # packages=["maya_test_tools"],
    py_modules=["maya_test_tools"],  # 单文件模块名称
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    # 指定依赖
    # install_requires=[
    #     'requests',
    #     'flask>=1.0'
    #     'setuptools==38.2.4',
    #     'django>=1.11, !=1.11.1, <=2',
    #     'requests[security, socks]>=2.18.4',
    # ]
)
