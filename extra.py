import json #for json file reading
import os
import sys

isFileFound = False
def open_file(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		path = sys._MEIPASS
		with open(os.path.join(path, relative_path), 'r') as f:
			data = json.load(f)
		isFileFound = True
	except Exception:
		try:
			path, filename = os.path.split(os.path.realpath(__file__))
			with open(os.path.join(path, relative_path), 'r') as f:
				data = json.load(f)
			isFileFound = True
		except FileNotFoundError:
			print("Dictionary file not found. Press anykey to exit...")
			os.system('pause')
			sys.exit()
		except Exception:
			print("Program not working correctly. Press anykey to exit.")
			os.system('pause')
			sys.exit()
	return data

def result_search():
    input_sample = input("Enter list of available character(s) for building word(s): ")
    output_result = []
    i = len(input_sample)
    while not(i==0):
        for word in words_with_len[i-1]:
            counter = 0
            checked_char = ""
            for char in word:
                if char in input_sample and input_sample.count(char)>=word.count(char) and not(char in checked_char):
                    counter += word.count(char)
                checked_char += char
            if len(word) == counter:
                output_result.append(word)
        i -= 1
        
    print("match word(s): " + str(len(output_result)))
    print(output_result)
	
word_dict = []
relative_file_path = "data\words_with_len.json"
words_with_len = open_file(relative_file_path)

repeat_list = ["Y", "y", "Yes", "yes"]
repeat_input = "y"
while repeat_input in repeat_list:
    result_search()
    repeat_input = input("Do Again? (Y/N) : ")