import os
import os.path
from typing import Union, Iterable
import numpy as np
import scipy.io as mat
from numpy.core._multiarray_umath import ndarray
import random
import csv
import matplotlib.pyplot as plt

path = r"C:\Users\kp826252\Documents\Data\Test 1\ECG signals (1000 fragments)\MLII\1 NSR\\"
dir_path = r"C:\Users\kp826252\PycharmProjects\trial_project\datasets"
data: list = [None] * len(os.listdir(path))


def make_one(way):
    filename: Union[bytes, str]  # initialize filename as a str
    way3: Union[bytes, str] = way  # make a copy of the path to reset the directory
    a: int = 0  # this is an indicator for the number of files in a directory

    for filename in os.listdir(way):  # finding each file in the directory
        way += filename  # concat the finale directory and name
        data[a] = mat.loadmat(way)  # in a variable data, load the file data in columns
        a += 1  # just to keep iterating the column count for the next file
        way = way3  # reset the file name to just the directory

    return data  # return the variable data with columns filled with the file data


def dict2list(way):
    r = make_one(way)  # call the function which creates the data dictionary
    data_tr: ndarray = np.transpose(r)  # transpose to get all files in row by (optional)
    data_hold: Union[Iterable, tuple[int]] = np.shape(data_tr)  # to get a shape of the data
    data_values: list = [None] * data_hold[0]  # create an empty list with the same size of the data
    # this is to then later fill with individual data arrays

    for i in range(data_hold[0]):
        data_values[i] = [v for v in data_tr[i].values()]  # unpack the dictionary and store in new list
        data_values[i] = data_values[i][0][0]  # unpacking the lists in the dict

    return data_values


def time_stmp(dats_list, files_no):
    no_of_heads: int = 4
    timestmp = np.empty(len(dats_list[0]), dtype=bytearray)  # create an empty times stamp list
    fin_arr = [[[1 for z in range(0, no_of_heads)] for y in range(0, len(dats_list[x]))] for x in range(0, files_no)]
    # create an empty list for the final array
    i: int  # this signifies a millisecond iteration
    filename: {str, bytes} = 'sample_trainset'  # this is for later labeling function
    label: {int, bytes} = 0  # again for later labeling function

    minutes: {int, bytes} = 0  # for the variable minutes in timestamp
    minutes2: {str, bytes} = str(minutes)  # this is used for formatting later
    ii_sec: int = 0

    for i in range(0, len(timestmp)):  # the range(timestamp) is also the number of data values, 3600
        ii: {str, bytes} = str(ii_sec)  # converting the iterable variable to string

        if ii_sec == 0:
            if 9 >= minutes:  # if there are 60 seconds, we have a minute (total data set)
                minutes2 = "0" + str(minutes)
            elif 60 <= minutes:  # same process seconds above with minutes variable this time
                minutes = 0
                minutes2 = str(minutes)
            else:
                minutes2 = str(minutes)

        if 59 == ii_sec:  # if the iterable variable becomes 60 it signifies 1 second
            ii_sec = 0
            minutes += 1
        elif 9 >= ii_sec:  # this is to ensure there are no single integers, ie. 01,02,03...
            ii = "0" + str(ii_sec)  # process of introducing the 0
            ii_sec += 1
        else:
            ii_sec += 1

        timestmp[i] = "2020-01-01T" + minutes2 + ":" + ii + ":37Z"  # this is to format the final timestamp variable

    cnt: int = 0  # this is a variable to index the timestmp and data_list arrays

    for x in range(len(fin_arr)):  # iterate through the number of files, 283
        for y in range(len(fin_arr[x])):  # iterate through number of data points, 3600
            for z in range(len(fin_arr[x][y])):  # iterate through the number of variables in the file, 4
                if z == 0:
                    fin_arr[x][y][z] = filename
                elif z == 1:  # for the second column in the data file
                    fin_arr[x][y][z] = timestmp[cnt]  # inter the corresponding timestmp
                elif z == 2:  # for the third column in the data file
                    fin_arr[x][y][z] = dats_list[x][cnt]  # enter the corresponding data point
                else:
                    fin_arr[x][y][z] = label

            cnt += 1  # iterate the internal count for timestmp and data_list
            if cnt >= len(fin_arr[x]):
                cnt = 0

    return fin_arr


def organising_datasets(path1, path2, path3):
    new_list: list = list(range(no_of_files))

    for indexes in new_list:
        new_list[indexes] = random.uniform(0, 1)


data_list = dict2list(path)
no_of_files: int = len(data_list)

final_arr = time_stmp(data_list, no_of_files)

trial_path: str = dir_path + "\\Trail_datasets"
test_path: str = dir_path + "\\Test_datasets"
validation_path: str = dir_path + "\\Validation_datasets"

# organising_datasets(trial_path, test_path, validation_path)

# with open("NSR_datasets.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(final_arr[0])


# x_vals: range = range(0, len(data_list[0]), 1)
# print(type(data_list[0]))
# plt.plot(x_vals, data_list[0][2])
# plt.show()
