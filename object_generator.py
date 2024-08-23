# Answer for Challenge A
import random
import string
import sys

ALPHABETICAL = string.ascii_letters
NUMERIC = string.digits
RESULT_LENGTH = 10240 # 10240 ( 1024 * 10 ) was chosen so roughly 1024 iterations is needed to get 10 MB
MAX_WHITESPACES = 10

def gen_object():
    value_list = [gen_alphabetical_str(), gen_alphanumerical_str(), gen_integer_str(), gen_real_num_str()]
    return random.choice(value_list)

def gen_alphabetical_str():
    generated_string = ''.join(random.choices(ALPHABETICAL, k = RESULT_LENGTH))
    return generated_string

def gen_alphanumerical_str():
    allowed_char = ''.join([ALPHABETICAL, NUMERIC])
    whitespace_before = random.randint(1, MAX_WHITESPACES - 1) # anywhere from 1 to 9
    whitespace_after = random.randint(1, MAX_WHITESPACES - whitespace_before) # anywhere from 1 to 10 - whitespace_before
    generated_string = ''.join(random.choices(allowed_char, k = RESULT_LENGTH - 10))
    return (' ' * whitespace_before) + generated_string + (' ' * whitespace_after)

def gen_integer_str():
    return str(random.randrange(-sys.maxsize, sys.maxsize))

def gen_real_num_str():
    return str(random.uniform(0, sys.maxsize))

def write_to_file(filename, str):
    f = open(filename, 'w')
    f.write(str)
    f.close()

def main():
    filename = 'strings.txt'
    print('Writing to ' + filename)

    str_to_write = gen_object()
    loop = 1
    while(len(str_to_write.encode()) < 10485760): # 10MB
        print(len(str_to_write.encode()))
        str_to_write = str_to_write + ',' + gen_object()
        loop += 1

    write_to_file(filename, str_to_write)
    print(loop + ' items written')    

if __name__ == '__main__':
    main()