import pandas
import os
import glob
import time
import numpy

start_time = "start time: " + time.ctime()

##feed path of CSVs
csv_path = 'C:\\Users\\raheel\\Downloads\\'

##feed file prefix
files = glob.glob(csv_path + "\\vuln scan dumps*.csv")
files.sort(key=os.path.getctime)   #sort by create time
number_of_files = len(files) #count how many files

create_times = []
sevs_array = []
x=0

##Loop through each file
for file in files:
	#timestamp = time.ctime(os.path.getctime(file)))
	timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getctime(file)))
	create_times.insert(x, timestamp)
	df = pandas.read_csv(file)  #read csv
	df = df[df['Last Status'] != 'fixed']   #filter our fixed
	df['Severity'].value_counts()   #summarize Severities
	capture = df['Severity'].value_counts()
	sevs_array.append([create_times[x],"Critical",capture.critical])
	sevs_array.append([create_times[x],"High",capture.high])
	sevs_array.append([create_times[x],"Medium",capture.medium])
	sevs_array.append([create_times[x],"Low",capture.low])
	sevs_array.append([create_times[x],"Trivial",capture.trivial])
    
	x += 1

header = "date,severity,count"

##spit out file with summarized severities
numpy.savetxt(csv_path + "summarized_sevs.csv", sevs_array, delimiter=",", fmt='%s', header=header)

finish_time = "finish time: " + time.ctime()

print start_time
print finish_time

time.sleep(10)  #pause to display results
