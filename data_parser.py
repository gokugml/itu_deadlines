import json
import os

class DataParser(object):
    def __init__(self):
        return

    def json_to_dict(self, file):
        if os.path.isfile(file):
            with open(file, 'r') as f:
                dict = json.load(f)
                return dict


if __name__ == "__main__":
    test = DataParser()
    path = os.path.dirname(__file__)+"/data.json"
    print test.json_to_dict(path)

