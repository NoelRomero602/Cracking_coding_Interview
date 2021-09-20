import sys

def is_Unique(string: str):
    isunique = True
    map = [False] * 400
    for c in string:
        if(map[ord(c)]):
            isunique = False
            break
        else:
            map[ord(c)] = True
    return  isunique




def main():
    if len(sys.argv) < 2:
        print('Please enter a string to check')
    else:
        if is_Unique(sys.argv[1]):
            print(f'{sys.argv[1]} has all unique characters')
        else:
            print(f'{sys.argv[1]} does not have all unique characters')

if __name__ == '__main__':
    main()