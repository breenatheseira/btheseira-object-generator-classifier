# Answer for Challenge B
import re

def read_from_file(filepath):
    with open(filepath) as file:
        line = file.readline()
        objects = line.split(',')
        for object in objects:
            type = identify(object)
            string = 'Object: "' + object.strip() + '" Type: ' + type + '\n'
            print(string)
        file.close()
            
def identify(text):
    if is_alphanumeric(text):
        return 'ALPHANUMERIC'
    elif is_alphabetical(text):
        return 'ALPHABETICAL'
    elif is_integer(text):
        return 'INTEGER'
    elif is_real_number(text):
        return 'REAL NUMBER'
    else:
        return 'NOT IDENTIFIABLE'

def is_alphanumeric(text):
    return re.search(r'^\s+[A-Z0-9]+\s+$', text)

def is_alphabetical(text):
    return re.search(r'^[A-Z]+$', text)

def is_integer(text):
    return re.search(r'^-?[0-9]+$', text)

def is_real_number(text):
    return re.search(r'^[0-9]+[.][0-9e+]+$', text)

def main():
    print('Starting file reader')
    read_from_file('random-strings.txt')
    print('Done!')

if __name__ == '__main__':
    main()