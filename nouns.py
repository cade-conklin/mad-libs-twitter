import json

from nltk import word_tokenize, pos_tag

new_text = {"NN": [], "NNP": [], "NNS": []}
with open('nouns-dictionaries.json') as noun_json:
    data = json.load(noun_json)
    for word in data["nouns"]:
        new_word = word_tokenize(word)
        pos = pos_tag(new_word)
        new_pos = str(pos[0][1]).strip()
        if new_pos == "NN":
            new_text["NN"].append(pos[0][0])
        if new_pos == "NNP":
            new_text["NNP"].append(pos[0][0])
        if new_pos == "NNS":
            new_text["NNS"].append(pos[0][0])

        print(word)
    # for i in range(0, len(data)):
    #     new_text["VB"].append(data[i][0])
    #     for j in range(1, len(data[i])):
    #         word = word_tokenize(data[i][j])
    #         pos = pos_tag(word)
    #         print(pos[0][1])
    #         new_pos = str(pos[0][1]).strip()
    #         if new_pos == "VBN":
    #             if not pos[0][0] in new_text["VBN"]:
    #                 new_text["VBN"].append(pos[0][0])
    #         if new_pos == "VBG":
    #             new_text["VBG"].append(pos[0][0])


with open('nouns-tagged.json', 'w') as out_json:
    json.dump(new_text, out_json, indent=2, sort_keys=True)
