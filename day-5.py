#!/usr/bin/env/python

import hashlib

def main():
    input_data = 'wtnhxymk'
    i = 0
    code = ''
    while True:
        md5 = hashlib.md5()
        md5.update('%s%s' % (input_data, i))
        digest = md5.hexdigest()
        i += 1
        if digest[:5] == '00000':
            code += digest[6]
            print digest
        if len(code) == 9:
            break
    print code

if __name__ == '__main__':
    main()
