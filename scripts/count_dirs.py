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

print("Num. samples/dirs: " + str(len(list_dirs)))

no_gesture = 0
doing_others = 0
stop = 0
thumb_up = 0
slide_two_down = 0
slide_two_up = 0
swip_right = 0
swip_left = 0
trun_hand = 0
tot_count = 0
useful_count = 0

for index, row in train_df.iterrows():
    if (row['action'] == 'No gesture'):
        no_gesture = no_gesture + 1
    if (row['action'] == 'Doing other things'):
        doing_others = doing_others + 1
    if (row['action'] == 'Stop Sign'):
        stop = stop + 1
    if (row['action'] == 'Thumb Up'):
        thumb_up = thumb_up + 1
    if (row['action'] == 'Sliding Two Fingers Down'):
        slide_two_down = slide_two_down + 1
    if (row['action'] == 'Sliding Two Fingers Up'):
        slide_two_up = slide_two_up + 1
    if (row['action'] == 'Swiping Right'):
        swip_right = swip_right + 1
    if (row['action'] == 'Swiping Left'):
        swip_left = swip_left + 1
    if (row['action'] == 'Turning Hand Clockwise'):
        trun_hand = trun_hand + 1
    if (row['action'] in keep_labels):
        useful_count = useful_count + 1
    tot_count = tot_count +1

print("Num. entries in train csv: " + str(tot_count))
print("Num. entries for useful labels in train csv: " + str(useful_count))
print("No gesture: " + str(no_gesture))
print("DOing others: " + str(doing_others))
print("Stop Sign: " + str(stop))
print("THumb Up: " + str(thumb_up))
print("Sliding Two Fingers Down: " + str(slide_two_down))
print("Sliding Two Fingers Up: " + str(slide_two_up))
print("Swiping Right: " + str(swip_right))
print("Swiping Left: " + str(swip_left))
print("Turning Hand Clockwise: " + str(trun_hand))


