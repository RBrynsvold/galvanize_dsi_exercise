def main():
    """
    Prompts user for filepath.
    Runs all subfunctions to perform the file operations, text analysis, and calculations.
    Prints the calculated stats for the file analyzed.
    """

    filepath = get_filepath()
    txt_str = get_txt(filepath)
    sentence_count, words_dict = make_counts(txt_str)
    total_words, unique_words, avg_sent_length, sorted_words_usage = calc_stats(sentence_count, words_dict)

    print "Total word count: %d" % total_words
    print "Unique words: %d" % unique_words
    print "Sentences: %d" % sentence_count
    print "Average sentence length (words): %.2f" % avg_sent_length
    print "List of words used, in order of descending frequency: "
    for item in sorted_words_usage:
        print item[1], ":", item[0]
    #add back in to make function return the stats (vs just print them)
    #return total_words, unique_words, words_dict, sentence_count, avg_sent_length


def get_filepath():
    """
    Prompts user to enter filepath.
    Validates filepath, and repeats prompt if valid filepath is not provided.

    Args: (none)

    Returns:
        filepath - str containing validated filepath
    """

    filepath = str(raw_input("Please enter filepath for file containing text to analyze: "))

    import os.path
    if os.path.isfile(filepath) == True:
        return filepath
    elif os.path.isfile(filepath) == False:
        print "Filepath entered not valid."
        return get_filepath()


def get_txt(filepath):
    """
    Performs all necessary file operations (opening, closing).
    Reads the text of the file and stores it in a string; formats string.

    Args:
        filepath - str containing filepath

    Returns:
        txt_str - str containing full text of the file (formatted)
    """

    import string

    txt_file = open(filepath, "r")
    txt_str_init = ""
    for line in txt_file:
        raw_line = line.rstrip(string.whitespace)
        txt_str_init += raw_line + " "
    txt_file.close()

    txt_str = txt_str_init.rstrip()
    return txt_str


def make_counts(txt_str):
    """
    Splits full file text string into list of strings of individual words.
    Iterates through split text and creates the counts needed to calculate all the stats in the next step.

    Args:
        txt_str - str containing full text of file (formatted)

    Returns:
        sentence_count - int containing number of sentences
        words_dict - dict containing each unique word and count of their incidence
    """

    import string

    split_str = txt_str.split()

    sentence_count = 0
    #first iteration pass - sentence counter
    for item in split_str:
        if "." in item or "?" in item or "!" in item:
            sentence_count += 1

    words_dict = dict()
    #second iteration pass - word counter
    for item in split_str:
        strp_item = item.rstrip(string.punctuation).lower()
        if (strp_item in words_dict) == False:
            words_dict[strp_item] = 1
        elif (strp_item in words_dict) == True:
            words_dict[strp_item] += 1

    return sentence_count, words_dict


def calc_stats(sentence_count, words_dict):
    """
    Calculates the requested file statistics using the counts created in the previous step.

    Args:
        sentence_count - int containing number of sentences
        words_dict - dict containing each unique word and count of their incidence

    Returns:
        total_words - int containing total number of words in text file
        unique_words - int containing number of unique words in text file
        avg_sent_length - float containing average length of the sentences in the text file, in words
        sorted_words_usage - list containing tuples of the key-value pairs, sorted descending by the values
    """
    total_words = 0
    for value in words_dict.values():
        total_words += value

    unique_words = len(words_dict)

    avg_sent_length =  float(total_words) / float(sentence_count)

    sorted_words_usage = []
    for key, value in sorted(words_dict.items(), key=lambda word: word[1], reverse=True):
        sorted_words_usage.append((key, value))

    return total_words, unique_words, avg_sent_length, sorted_words_usage


main()
