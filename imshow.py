#!/usr/bin/python3

import csv
from PIL import Image
from pylab import *

import numpy
import cv2

my_matrix = numpy.loadtxt(open("./Bmode.csv","rb"),delimiter=",",skiprows=0) 

print(my_matrix)

imshow(my_matrix)

res = cv2.resize(my_matrix, dsize=(3118, 3118), interpolation=cv2.INTER_CUBIC)

imshow(res)