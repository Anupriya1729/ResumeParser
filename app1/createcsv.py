import csv
import os
from django.core.files.storage import FileSystemStorage

def data(path_to_file,n,e,p,l,t,tc):
    # field names
    fields = ['Name', 'Email', 'linkedIn', 'Phone', 'Total Lines', 'Total Characters']

    # data rows of csv file
    rows = [[n,e,p,l,t,tc]]

    # name of csv file
    FileTXT = 'C:/Users/admin/Desktop/Projects done/Resume Reader/Resume_Reader/media/csvfiles'
    base = os.path.basename(path_to_file)
    #fileNAME = os.path.splitext(base)[0]
    filename = FileTXT+'/'+'out'+'.csv'

    # writing to csv file
    with open(filename, 'w+') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

    return filename
