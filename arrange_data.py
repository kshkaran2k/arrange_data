# purpose: read a csv file and then arrange the data into proper columnar format
# author: kaushik karan <kshkaran2k>

import csv
import os


file_full = os.path.realpath(__file__)
file_dir = os.path.dirname(file_full)
os.chdir(file_dir)

# initial configurations
csv_file = 'sample.csv'    #input file which is to be manipulated
num_col = 3             #number of columns present in the dataset
data_row = []

csv_out = csv_file.split('.')[0]+'_out.'+csv_file.split('.')[1]
csv_open = open(csv_file)
csv_reader = csv.reader(csv_open, delimiter=',')
csv_out_open = open(csv_out,'a',newline='', encoding='utf-8')
csv_writer = csv.writer(csv_out_open)


i = 0
for row in csv_reader:
    i = i + 1
    data_row.append(row[0])
    if(i==num_col):
        i = 0
        csv_writer.writerow(data_row)
        data_row = []
