# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:43:07 2023

@author: GelzoneCC
"""

from setuptools import setup
from Cython.Build import cythonize

setup(
      name = 'pyxtopyd', 
      ext_modules=cythonize("CommonFunction.pyx"),
      compiler_directives={'language_level' : "3"}
      )
