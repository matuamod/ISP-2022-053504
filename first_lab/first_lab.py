import argparse
import re
from statistics import mean, median

def get_parser() -> tuple:
	parser = argparse.ArgumentParser(description="Get some values for our lab :")
	parser.add_argument("text", type = str, help = "Text for some next operations")
	parser.add_argument("k", nargs = "?", default = 10, type = int, help = "Need some value of k, default = 10")
	parser.add_argument("n", nargs = "?", default = 4, type = int, help = "Need some value of n, default = 4")
	args = parser.parse_args()

	return (args.text, args.k, args.n)

def remove_chars(data : str) -> list:
    chars = "@#%&,;:'()"

    for char in chars:
        data = data.replace(char, "")

    return data

def split_str_to_arr(data : str) -> list:
    data = remove_chars(data)
    sentanses = []
    post_chars = "\\. |\\! |\\?"

    for sentanse in re.split(post_chars, data):
        if len(sentanse) > 0:
            words = sentanse.split(" ")

            while "" in words:
                words.remove("")
            sentanses.append(words)

    return sentanses

def get_repeating_words(sentanses : list) -> dict:
    cust_dict = dict()

    for sentanse in sentanses:

        for word in sentanse:
            if word in cust_dict:
                cust_dict[word] += 1

            else:
                cust_dict[word] = 1

    return cust_dict

def average_amount_words(sentanses : list) -> int:
    average_count = mean([len(sentanse) for sentanse in sentanses])

    return average_count

def median_amount_words(sentanses : list) -> int:
    median_count = median([len(sentanse) for sentanse in sentanses])

    return median_count

def get_top_grams(sentanses : list, n : int) -> dict:
    grams_dict = dict()
    buf_grams_dict = dict()

    for sentanse in sentanses:
        buf_gram = ""

        for i in range(len(sentanse)):
            if (i + n) <= len(sentanse):

                for j in range(n):
                    buf_gram += str(sentanse[j + i]  + " ").lower()
                buf_gram = buf_gram.strip()
                if buf_gram in grams_dict:
                    grams_dict[buf_gram] += 1
                    if grams_dict[buf_gram] >= n:
                        buf_grams_dict[buf_gram] = grams_dict[buf_gram]

                else:
                    grams_dict[buf_gram] = 1
                buf_gram = ""
    
    return buf_grams_dict   

def sorted_grams(grams_dict : dict) -> dict:
    sorted_grams_dict = dict(sorted(grams_dict.items(), key = lambda kv : kv[1], reverse = True))

    return sorted_grams_dict

def print_all_inf(data : str, sentanses : list, k : int, n : int):
    word_dict = get_repeating_words(sentanses)

    for word in word_dict:
        print("  |  {} = {}".format(word, word_dict[word]), end= "  |  \n")
    average_count = average_amount_words(sentanses)
    print("\nAverage count of words in text is : " + str(average_count))
    median_count = median_amount_words(sentanses)
    print("\nMedian count of words in text is : " + str(median_count))
    grams_dict = get_top_grams(sentanses, n)
    sorted_grams_dict = sorted_grams(grams_dict)
    print("\nTop k n-grams are :\n" + " ".join(str(sorted_grams_dict)))

    for i, (key, value) in enumerate(sorted_grams_dict.items()):
        if i == k:
            break
        
        else:
            print(" "+" {} = {}".format(key, value))

def main():	
	text, k, n = get_parser()
	sentanses = split_str_to_arr(text)
	print_all_inf(text, sentanses, k, n)

if __name__ == "__main__":
    main()