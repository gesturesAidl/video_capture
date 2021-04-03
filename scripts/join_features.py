import numpy as np
import os
from tqdm import tqdm
import pickle


def read_option():
    while True:
        print("\nWhich features do you want to join in a pickle file?")
        print("  1. RGB")
        print("  2. Optical Flow")
        type = input("\nEnter option (1|2): ")
        try:
            type = int(type)
            if not(type==1 or type==2):
                raise ValueError("Wrong value")
            else:
                return type
        except ValueError:
            print("Incorrect option: only '1' or '2' are allowed")

option = read_option()
type = {1 : 'RGB', 2 : 'flow'}
feat_type = type[option]

feat_dir = '/home/gestures_aidl/features'
feat_dir_type = os.path.join(feat_dir, feat_type)
feat_file = 'features_' + feat_type + '.pickle'

# feature filename example:
#   RGB --> 'i3d_resnet50_v1_kinetics400_1.mp4_feat.npy'
#   flow -> 'i3d_resnet50_v1_kinetics400_opfw_1.mp4_feat.npy'

if int(option) == 1:
    feat_model = 'i3d_resnet50_v1_kinetics400_'         # RGB features
else:
    feat_model = 'i3d_resnet50_v1_kinetics400_opfw_'    # Optical flow features
    
features_dict = {}
feat_num = 0

for dirName, subdirList, fileList in os.walk(feat_dir_type):         # go through the dir, subdir & folder's files 
    print('Features folder: %s' % dirName)
    for fname in tqdm(fileList, unit=" files"):                 # go only through the folder's files
        feat_num += 1
        fname_short = ''
                           
        if fname.find(feat_model) != -1:                 
            fname_short = fname [len(feat_model):]         # Deletes model name from filename
        else:
            fname_short = fname                            # filename already like '1.mp4_feat.npy'
        
        n_video = fname_short[:fname_short.find('.')]      # Extracts video number from feature filename  --> '1'   
        
        features = np.load(os.path.join(feat_dir_type, fname))  # Read single features file --> numpy array (1,2048) [[...]]
     
        features_dict[n_video] = features                  # Creates dict as {n_video:features, ...}

# Save features dict as pickle file       
with open(os.path.join(feat_dir, feat_file), 'wb') as handle:
    pickle.dump(features_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("\n")
print(feat_num, "features read from numpy files")
print("Packed", feat_type, "features (dict) saved in", os.path.join(feat_dir, feat_file))
print("\n")
