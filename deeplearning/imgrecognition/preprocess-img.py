#!/usr/bin/env python

"""
	This script is responsible for preprocessing our images 
"""

# Imports
import numpy as np
import argparse
import os

from PIL import Image

# Docs
__author__ = 'Vaux Gomes and Wally Jam'
__version__ = '1.0.0'

#
def parse_arguments():
	"""
		Parsing of arguments
	"""
	parser = argparse.ArgumentParser()

	parser.add_argument('-s', help='Source folder', required=True)
	parser.add_argument('-t', help='Target folder')
	parser.add_argument('-e', help='File extension', default='jpg')
	parser.add_argument('-v', help='Verbosity', action='store_true')

	return parser.parse_args()

# Main
def main():
	# Parsing arguments
	args = parse_arguments()
	
	# Parameters
	source_path = args.s
	target_path = source_path + '_output'
	ext = args.e

	if args.t is not None: target_path = args.t

	# Creating target directory if necessary
	if not os.path.isdir(target_path):
		os.mkdir(target_path)
		
		# Verbosity
		if args.v: print('Created', target_path)

	# Verbosity
	if args.v:
		print(source_path)
		print(target_path)
		print('*.%s' % (ext))

	for i in os.listdir(source_path):
		if i.endswith(ext):
			print('Processed:', process_img(source_path + os.sep + i, target_path))

# Preprocessing
def process_img(img_path, target_path):
	img = Image.open(img_path).convert('L')
	img_arr = np.array(img)[24:212, 3:246]

	output_path = target_path + os.sep + os.path.basename(img_path)

	result = Image.fromarray(img_arr.astype(np.uint8))
	result.save(output_path)

	return output_path

# Main: Calling
if __name__ == "__main__":
	main()
