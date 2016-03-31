#READING MATLAB- MAT.file


from path import Path
import argparse
import logging
import random
import scipy.io
import numpy as np


def read(files):
 
    for fname in files:
	raw = scipy.io.loadmat(fname)
	raw = raw[raw.keys()[0]].astype(np.uint8)
	pro = np.zeros((32,)*3, dtype=np.uint8)
	pro[1:-1, 1:-1, 1:-1] = raw


parser = argparse.ArgumentParser()
parser.add_argument('data_dir', type=Path)
parser.add_argument('fold_num', type=Path)
args = parser.parse_args()

base_dir = (args.data_dir/args.fold_num).expand()
records = {'train': [], 'test': []}

logging.info('Loading .mat files')
iter = 0
for fname in sorted(base_dir.walkfiles('*.mat')):
    elts = fname.splitall()
    split = elts[-2]
    #split the file name
    records[split].append(fname)


logging.info('Reading train npy file')
train_files = records['train']
random.shuffle(train_files)
read(train_files)

logging.info('Reading test npy file')
test_files = records['test']
random.shuffle(test_files)
read(test_files)








