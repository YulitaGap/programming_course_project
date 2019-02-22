import json

def file_read(file_name):
    """
    (str)->(list(dict))
    Reads file given and converts it to python dictionaries list
    """
    f = open(file_name, encoding='utf-8')
    ff = json.load(f)
    return ff



if __name__ == '__main__':
    ff = file_read('package.json')
    print(ff)



