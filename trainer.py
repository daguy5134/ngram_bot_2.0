import user_input
import os
import shutil
import json
from nltk import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter, defaultdict

source_dir = 'data/books/new'
destination_dir = 'data/books/archived'
ngram_dict_four = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: Counter())))
trigram_dict = defaultdict(lambda: defaultdict(lambda: Counter()))
punctuation = """
"#$%&'()*+,-/:;<=>@[]^_{|}~`'
"""

books = os.listdir(source_dir)
if books:
	print("Do you want the program to start training on the new files added (options : y/n) ?")
	start = user_input.in_list(
		">>>",
		"You have to enter one of the two options (y or n)!",
		["y", "n", "dev_mode"]
	)
	if start == "dev_mode":
		print("Activating developer mode")
	if start in ["y", "dev_mode"]:
		print("The process has begun")
		for file in books:
			with open(os.path.join(source_dir, file), "r", encoding="utf-8") as book:
				text = book.read()
				clean_list = []
				for word in text.split():
					word.lower().strip(punctuation)
					clean_list.append(word)
				clean_text = " ".join(clean_list)
				words = word_tokenize(clean_text, language="english")
				trigrams = ngrams(words, 3)
				four_grams = ngrams(words, 4)
				for item in trigrams:
					trigram_dict[item[0]][item[1]][item[2]] += 1
				for item in four_grams:
					ngram_dict_four[item[0]][item[1]][item[2]][item[3]] += 1
		
		if start == "y":
			with open('data/ngrams/quadrigrams.json', 'w') as four_gram_file:
				json.dump(ngram_dict_four, four_gram_file)
			with open('data/ngrams/trigrams.json', 'w') as trigrams_file:
				json.dump(trigram_dict, trigrams_file)
			for filename in books:
				source_file = os.path.join(source_dir, filename)
				destination_file = os.path.join(destination_dir, filename)
				shutil.move(source_file, destination_file)
		elif start == "dev_mode":
			def commands():
				print("""
trigram_dict : Dictionary with trigrams and their frequency,
ngram_dict_four : Dictionary with four_grams and their frequency.
	                """)
			
			print("""You can now code to access data.
Type commands() to access the name of the variables.""")
			while True:
				user_command = input(">>>")
				try:
					exec(user_command)
				except Exception as e:
					print(f"An error occurred: {e}")
	else:
		exit()
else:
	print("Their are no new books to train on.")
	