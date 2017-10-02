import pandas
import os
import glob
import time
import numpy

start_time = "start time: " + time.ctime()

##feed path of file
csv_path = 'C:\\Users\\raheel\\Downloads'

#feed in prefix of file/s
files = glob.glob(csv_path + "\\vuln scan dump*.csv")
files.sort(key=os.path.getctime)   #sort by create time
number_of_files = len(files) #count how many files

create_times = []
sevs_array = []
x=0

df = pandas.read_csv(files[-1])  #read last csv
df = df[df['Last Status'] != 'fixed']   #filter out fixed
df['Severity'].value_counts()   #summarize Severities
capture = df['Severity'].value_counts()  

##use capture variable to get counts
