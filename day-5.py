#!/usr/bin/env/python

import hashlib

def main():
    input_data = 'wtnhxymk'
    i = 0
    code = {'0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None}
    while True:
        md5 = hashlib.md5()
        md5.update('%s%s' % (input_data, i))
        digest = md5.hexdigest()
        i += 1
        if digest[:5] == '00000':
            print((digest, code))
            if digest[5] in code.keys():
                if code[digest[5]] is None:
                    code[digest[5]] = digest[6]
        if None not in code.values():
            break
    print(''.join([x[1] for x in sorted(code.items(), key=lambda x: x[0], reverse=False)]))

if __name__ == '__main__':
    main()
