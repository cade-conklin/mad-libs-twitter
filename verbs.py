import json

from nltk import word_tokenize, pos_tag

new_text = {"VB": [], "VBG": [], "VBN": []}

with open('verbs-dictionaries.json') as verb_json:
    data = json.load(verb_json)
    for i in range(0, len(data)):
        new_text["VB"].append(data[i][0])
        for j in range(1, len(data[i])):
            word = word_tokenize(data[i][j])
            pos = pos_tag(word)
            print(pos[0][1])
            new_pos = str(pos[0][1]).strip()
            if new_pos == "VBN":
                if not pos[0][0] in new_text["VBN"]:
                    new_text["VBN"].append(pos[0][0])
            if new_pos == "VBG":
                new_text["VBG"].append(pos[0][0])


with open('verbs-tagged.json', 'w') as out_json:
    json.dump(new_text, out_json, indent=2, sort_keys=True)
