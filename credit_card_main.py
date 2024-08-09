import pandas as pd  #Importing of libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import sklearn
import sys
from simple_colors import *
import string


class read():

	# def __init__(self,data):
	#  	self.data = data

	def reading(self):
		data = pd.read_csv('creditcard.csv') #reading & importing CSV file using pandas
		return data


class extract():

	def __init__(self,data):
		self.data=data

	def extracting(self):
		print(self.data.columns) #dataset methods to extract values
		print(self.data.shape) #Data Exploration 
		print(self.data.head)


class PreProcessing():

	# def processing(self,data):
	# 	self.data=data
    
    def processing(self):
        print("Reading & importing CSV file using pandas")
        d1 = read()
        data = d1.reading()
        d2 = extract(data)
        d2.extracting()

        print(data)
        return data

# class sampling():

# 	def samp():
# 		data = data.sample(frac = 0.2, random_state = 2) #Sampling
# 		# random_state helps assure that you always get the same output when you split the data
# 		# this helps create reproducible results and it does not actually matter what the number is
# 		# frac is percentage of the data that will be returned
# 		print(data.shape)


class plotting():
    
    @staticmethod
	
	def plot():
		# plot the histogram of each parameter in csv file
		data.hist(figsize = (20, 20)) #histogram of all columns
		plt.show()

		# boxplot of each parameter in csv file	
		boxplot = data.boxplot(grid=True,figsize=(20,20))  #boxplot of all values
		plt.show()


	