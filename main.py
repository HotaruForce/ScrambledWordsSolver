import json #for json file reading

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

	return os.path.join(base_path, relative_path)
	
word_dict = []
with open(("words_with_len.json"), 'r') as f:
	words_with_len = json.load(f)

def result_search():
	input_sample = input("Enter the scrambled word: ")
	output_result = []
	for word in words_with_len[len(input_sample)-1]:
		counter = 0
		checked_char = ""
		for char in input_sample:
			if char in word and input_sample.count(char)==word.count(char) and not(char in checked_char):
				counter += input_sample.count(char)
			checked_char += char
		if len(input_sample) == counter:
			output_result.append(word)
	print("match word(s): " + str(len(output_result)))
	print(output_result)

repeat_list = ["Y", "y", "Yes", "yes"]
repeat_input = "y"
while repeat_input in repeat_list:
	result_search()
	repeat_input = input("Do Again? (Y/N) : ")
