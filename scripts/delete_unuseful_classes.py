import pandas as pd
import os
import shutil

validate_csv = 'jester-v1-validation.csv'
test_csv = 'jester-v1-test.csv'
train_csv= 'jester-v1-train.csv'
labels_csv = 'jester-v1-labels.csv'
csv_dir = '/mnt/disks/disk-1/jester_dataset/dataset/csvs/'
dataset_path = '/mnt/disks/disk-1/jester_dataset/dataset/20bn-jester-v1/'

tot_labels = pd.read_csv(csv_dir+labels_csv, header=None).iloc[:, 0].to_list() # List of labels in dataset
train_df = pd.read_csv(csv_dir+train_csv, header=None, names=["folder", "action"], sep=';')
validate_df = pd.read_csv(csv_dir+validate_csv, header=None, names=["folder", "action"], sep=';')


keep_labels = [
    'No gesture',
    'Doing other things',
    'Stop Sign',
    'Thumb Up',
    'Sliding Two Fingers Down',
    'Sliding Two Fingers Up',
    'Swiping Right',
    'Swiping Left',
    'Turning Hand Clockwise'
]


# Go through all directories in {@dataset_path}
for x in os.walk(dataset_path):
    list_dirs = x[1]
    break

#For each row in dataset (train)
for index, row in train_df.iterrows():
    if not (row['action'] in keep_labels):
        # Delete folder
        try:
            print("del dir: " + str(row['folder']))
            shutil.rmtree(dataset_path + str(row['folder']), ignore_errors=True)
        except:
            print("Unable deleting folder with name: " + str(ror['folder']) + ". cause: Doesn't exist")

#For each row in dataset (validation)
for index, row in validate_df.iterrows():
    if not (row['action'] in keep_labels):
        # Delete folder
        try:
            print("del dir: " + str(row['folder']))
            shutil.rmtree(dataset_path + str(row['folder']), ignore_errors=True)
        except:
            print("Unable deleting folder with name: " + str(ror['folder']) + ". cause: Doesn't exist")

