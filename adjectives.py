import json

from nltk import word_tokenize, pos_tag

new_text = {"JJ": [], "JJS": []}
with open('adjective-dictionaries.json') as adj_json:
    data = json.load(adj_json)
    for word in data["adjs"]:
        print(word)
        new_word = word_tokenize(word)
        pos = pos_tag(new_word)
        new_pos = str(pos[0][1]).strip()
        print(new_pos)
        if new_pos == "JJ":
            new_text["JJ"].append(pos[0][0])
        if new_pos == "JJS":
            new_text["JJS"].append(pos[0][0])



with open('adjectives-tagged.json', 'w') as out_json:
    json.dump(new_text, out_json, indent=2, sort_keys=True)
