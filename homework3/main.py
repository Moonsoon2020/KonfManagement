import re
import json


def parser(inp: str):
    if inp[-1] != ";" or inp.count(";") != 1 or inp.count(' := ') != 1:
        raise Exception("error")
    inp = inp[:-1]
    inp = inp.split(' := ')
    inp[0] = inp[0].strip()
    if re.match(r'\$"[a-z_0-9A-Z`!#%^&*()]*"', inp[1].strip()):
        return inp[0], inp[1][2:-1]
    if inp[1].strip() == "begin":
        return inp[0], {}
    if re.search("[0-9]+", inp[1].strip()):
        return inp[0], int(inp[1])
    raise Exception("error")


def main():
    all_ = {}
    root = all_
    while True:
        line = input()
        match = re.match(r"\[[_a-zA-Z]+\]", line)
        if line == '__stop__':
            break
        elif line == 'end':
            root = all_
        elif match and match.endpos == len(line):
            if line[1:-1] in root.keys():
                print(root[line[1:-1]])
            else:
                print("error not in memory")
        else:
            try:
                key, var = parser(line)
                root[key] = var
                if var == {}:
                    root = root[key]
            except Exception as e:
                print(e)
    print(json.dumps(root))


if __name__ == '__main__':
    main()
