# Reading an entire text file in Python
# tutorial from https://datagy.io/python-read-text-file/
#--------------------------------------------------------
import os
# get the list of pdf files from the docs directory into a list  format
xls_folder_path = './'
doc_list = [s for s in os.listdir(xls_folder_path) if s.startswith('Medium_4earn')]
num_of_docs = len(doc_list)
print(doc_list)
print(num_of_docs)