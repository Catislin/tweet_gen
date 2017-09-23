import histogram
import random
import operator
import datetime

# takes in a histogram and returns a random word from it
def random_word(hist):
    return random.choice(list(hist.keys()))

def create_probs_list(prob_dict):
    return_list = []
    current = 0
    for item in prob_dict:
        range_list = []
        range_list.append(current)
        current += prob_dict[item]
        range_list.append(current)
        return_list.append([item, range_list])
    return return_list

def random_weighted(probs_list):
    random_probability = random.random() # [0, 1)
    for pair in probs_list:
        if random_probability >= pair[1][0] and random_probability < pair[1][1]:
            return pair[0]

# takes in a histogram dictionary and returns a dictionary in which
# the key is the word and the value is its probability in the text
def probability_dictionary(hist):
    # total words in source text (add up all frequencies)
    total = 0
    return_dict = dict()
    for freq in hist.values():
        total += freq
    for word in hist.keys():
        return_dict[word] = hist[word] / total
    return return_dict

# run random_weighted many times and keep track of which word is returned
def testing(hist):
    reps = 1000
    start = datetime.now()
    probs = probability_dictionary(hist)
    print("Probabilities")
    print(probs)
    probs_list = create_probs_list(probs)

    #testing method two
    output = []
    for i in range (reps):
        output.append(random_weighted(probs_list))
    new_hist = histogram.create_dict(" ".join(output))
    generated_probs = probability_dictionary(new_hist)
    print(generated_probs)

    print("Time: " + str(datetime.now() - start))


if __name__ == '__main__':
    normalized_string = (histogram.normalize(histogram.read_in_file('fish.txt')))
    fish_words = histogram.create_dict(normalized_string)
    testing(fish_words)
