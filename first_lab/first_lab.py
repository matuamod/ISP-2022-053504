import argparse
import re
from statistics import mean, median

def Get_Parser():
	parser = argparse.ArgumentParser(description="Get some values for our lab :")
	parser.add_argument("text", type = str, help = "Text for some next operations")
	parser.add_argument("k", nargs = "?", default = 10, type = int, help = "Need some value of k, default = 10")
	parser.add_argument("n", nargs = "?", default = 4, type = int, help = "Need some value of n, default = 4")
	args = parser.parse_args()
	return args.text, args.k, args.n

def Remove_Chars(_data):
    chars = "@#%&,;:'()"
    for char in chars:
        _data = _data.replace(char, "")
    return _data

def Split_Str_To_Arr(_data : str) -> list:
    _data = Remove_Chars(_data)
    sentanses = []
    post_chars = "\\. |\\! |\\?"
    for sentanse in re.split(post_chars, _data):
        if len(sentanse) > 0:
            words = sentanse.split(" ")
            while "" in words:
                words.remove("")
            sentanses.append(words)
    return sentanses

def Get_Repeating_Words(_sentanses : list) -> dict:
    cust_dict = dict()
    for sentanse in _sentanses:
        for word in sentanse:
            if word in cust_dict:
                cust_dict[word] += 1
            else:
                cust_dict[word] = 1
    return cust_dict

def Average_Amount_Words(_sentanses : list) -> int:
    average_count = mean([len(sentanse) for sentanse in _sentanses])
    return average_count

def Median_Amount_Words(_sentanses : list) -> int:
    median_count = median([len(sentanse) for sentanse in _sentanses])
    return median_count

def Get_Top_Grams(_sentanses : list, _n : int) -> dict:
    grams_dict = dict()
    buf_grams_dict = dict()
    for sentanse in _sentanses:
        buf_gram = ""
        for i in range(len(sentanse)):
            if (i + _n) <= len(sentanse):
                for j in range(_n):
                    buf_gram += str(sentanse[j + i]  + " ").lower()
                buf_gram = buf_gram.strip()

                if buf_gram in grams_dict:
                    grams_dict[buf_gram] += 1
                    if grams_dict[buf_gram] >= _n:
                        buf_grams_dict[buf_gram] = grams_dict[buf_gram]
                else:
                    grams_dict[buf_gram] = 1
                buf_gram = ""
    
    return buf_grams_dict   

def Sorted_Grams(_grams_dict : dict) -> dict:
    sorted_grams_dict = dict(sorted(_grams_dict.items(), key = lambda kv : kv[1], reverse = True))
    return sorted_grams_dict

def Print_All_Inf(_data : str, _sentanses : list, _k : int, _n : int):
    word_dict = Get_Repeating_Words(_sentanses)
    for word in word_dict:
        print("  |  {} = {}".format(word, word_dict[word]), end= "  |  \n")
    average_count = Average_Amount_Words(_sentanses)
    print("\nAverage count of words in text is : " + str(average_count))
    median_count = Median_Amount_Words(_sentanses)
    print("\nMedian count of words in text is : " + str(median_count))
    grams_dict = Get_Top_Grams(_sentanses, _n)
    sorted_grams_dict = Sorted_Grams(grams_dict)
    print("\nTop k n-grams are :\n" + " ".join(str(sorted_grams_dict)))
    for i, (key, value) in enumerate(sorted_grams_dict.items()):
        if i == _k:
            break
        else:
            print(" "+" {} = {}".format(key, value))

def main():	
	text, k, n = Get_Parser()
	sentanses = Split_Str_To_Arr(text)
	Print_All_Inf(text, sentanses, k, n)

if __name__ == "__main__":
    main()