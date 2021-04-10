# -*- coding: utf-8 -*-
import os

split_tup=os.path.splitext('abc.py')
file_name=split_tup[0]
file_extension=split_tup[1]
print("the file extension is",file_extension)