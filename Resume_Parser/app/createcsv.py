import csv
import os
from django.core.files.storage import FileSystemStorage


def data(path_to_file, n, e, p, l, t, tc):
    # field names
    fields = ['Name', 'Email', 'Phone', 'linkedIn',
              'Total Lines', 'Total Characters']

    # data rows of csv file
    rows = [[n, e, p, l, t, tc]]

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parentdir = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    mediadir = os.path.join(BASE_DIR, "media")
    # name of csv file
    Filecsv = os.path.join(mediadir, "csvfiles")
    base = os.path.basename(path_to_file)
    #fileNAME = os.path.splitext(base)[0]
    csvfile = 'parsed.csv'
    filename = os.path.join(Filecsv, csvfile)

    # writing to csv file
    with open(filename, 'w+') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

    return filename
