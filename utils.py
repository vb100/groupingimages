'''
This submodule works with our application.
Prepared by Vytautas Bielinskas. 2021.
'''


# Import modules and packages
import os
import argparse
import pandas as pd


# Pre-defined constants
TEMP_PATH = './temp/'


# Procedure for extracting date values from timestamp
def get_timestamp_values(timestamp):
	return timestamp[:4], timestamp[4:6], timestamp[6:8]


# Procedure for parsing filenames
def image_timestamp(filename):
	'''
		- filename example: IMG_20201217_220927.jpg (IMG_yyyymmdd_???)
	'''

	return f'{filename.split("_")[1].split("_")[0]}'


# Procedure to find files with specified extensions
def get_images_data(root_dir, E):

	raw_data = []

	for root, directories, filenames in os.walk(root_dir):
		for filename in filenames:

			if any(ext in filename for ext in E):

				d = {}
				d['Year'], d['Month'], d['Day'] = get_timestamp_values(image_timestamp(filename))
				d['Filename'] = filename
				d['Timestamp'] = image_timestamp(filename)
				d['Path'] = os.path.join(root, filename)
				raw_data.append(dict(d))

	return pd.DataFrame(raw_data)


def delete_original_folder(ROOT_DIR):

	try:
		os.rmdir(ROOT_DIR)
		print('\nThe Root Directory Removed Sucessfuly.')

	except:
		print('\nError on Removing The Root Directory.')


def move_files(data):
	for i, (this_original_file, filename, this_folder) in enumerate(zip(data['Path'], data['Filename'], data['Timestamp'])):
		print(f'| ({i:>{2}}) ::: Moving image {this_original_file} to folder --> {TEMP_PATH}{this_folder}')

		os.replace(
			this_original_file,
			f'{TEMP_PATH}{this_folder}/{filename}'
			)


def create_folders(timestamps):

	if len(timestamps) > 0:

		if not os.path.isdir(TEMP_PATH):
			os.mkdir(TEMP_PATH)
			print('| Temporary directory is created.')

		for this_timestamp in timestamps:
			os.mkdir(f'{TEMP_PATH}{this_timestamp}')
			print(f'| Directory for {this_timestamp} is being created.')


def save_summary(data):
	data.to_excel('Summary.xlsx', encoding='utf-8')
	print('The summary has been saved.')