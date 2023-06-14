import numpy as np
import pandas as pd

def read_file(path):
    result = []
    with open(file=path, mode='r') as file:
        for line in file.readlines():
            result.append(line.strip().split('::'))
    return result

def read_dataset(folder_path=".\ml-1m"):
    movie_list = read_file(path=folder_path + "\movies.dat")
    return movie_list