# Import modules and packages
import os
import pandas as pd
import argparse
from utils import *


# Initialize the given arguments
parser = argparse.ArgumentParser()
# Add long and short arguments
parser.add_argument("--myimages", "-mi", help="Wheere are my images? Please provide a folder name.")
# Read the arguments from the command line (Terminal)
args = parser.parse_args()


# Constants
EXTENSIONS = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']
ROOT_DIR = f'{args.myimages}'


# Run search
if __name__ == '__main__':
	data = get_images_data(ROOT_DIR, EXTENSIONS)
	if len(data) > 0:
		create_folders(data['Timestamp'].unique())
		move_files(data)
		delete_original_folder(ROOT_DIR)
		save_summary(data)