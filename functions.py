import json
import pprint


def data_load(link):
    with open(link, "r", encoding='utf-8') as fp:
        data = json.load(fp)
    return data


def get_tags(data):
    results = set()

    for record in data:
        content = record['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                results.add(word[1:])
    return results
