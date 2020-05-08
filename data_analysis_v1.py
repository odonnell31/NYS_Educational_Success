# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:49:30 2020

@author: ODsLaptop
"""

# import libraries
import numpy as np
import pandas as pd


# import data

# this is a dataset of grades 3-8 math and ELA scores at the school level
# the column SCHOOL_NAME shows the school name
# the column MEAN_SCALE_SCORE shows the mean score of the school for that grade level
nys_3through8_data = pd.read_excel("data/NYSED/ELA_AND_MATH_RESEARCHER_FILE_2019.xlsx")

