import user_input
import os
import shutil
import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize

source_dir = 'data/books/new'
destination_dir = 'data/books/archived'
ngram_dict_four = {}

books = os.listdir(source_dir)
if books:
	print("Do you want the program to start training on the new files added (options : y/n) ?")
	start = user_input.in_list(
		">>>",
		"You have to enter one of the two options (y or n)!",
		["y", "n"]
	)
	if start == "y":
		print("The process has begun")
		for file in books:
			with open(file, "r", encoding="utf-8") as book:
				text = book.read()
				words = word_tokenize(text, language="english")
				four_grams = ngrams(words, 4)
				for item in four_grams:
					if item[0] not in ngram_dict_four:
						ngram_dict_four[item[0]] = None
					if item[1] not in ngram_dict_four[item[0]]:
						ngram_dict_four[item[0]]
	else:
		exit()
else:
	print("Their are no new books to train on.")