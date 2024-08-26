# Answer for Challenge A
import random
import string
import sys
import os

ALPHABETICAL = string.ascii_letters
NUMERIC = string.digits
RESULT_LENGTH = 10240 # 10240 ( 1024 * 10 ) was chosen to shorten the time taken to get 10 MB (1024 * 1024 * 10)
MAX_WHITESPACES = 10
MAX_FILE_SIZE = 10485760

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

def get_file_size(filename):
    return os.stat(filename).st_size

def bytes_to_megabytes(bytes):
    return bytes / (1024 * 1024)

def main():
    filename = './results/random-objects.txt'
    print(f'Writing to {filename}')
    print(f'This process may take about 3 - 5 minutes...')

    str_to_write = gen_object()
    loop = 1
    while(len(str_to_write.encode()) < MAX_FILE_SIZE): # 10MB
        str_to_write = str_to_write + ',' + gen_object()
        loop += 1

    write_to_file(filename, str_to_write)

    file_size = get_file_size(filename)
    
    print(f'\n')
    print(f'Done. {loop} items generated')
    print(f'File size: {file_size} bytes')
    print(f'File size: {bytes_to_megabytes(file_size)} MB')
    

if __name__ == '__main__':
    main()
