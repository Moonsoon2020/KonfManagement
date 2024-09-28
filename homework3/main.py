import re


def ui(inp: str):
    if inp[-1] != ";":
        raise Exception("err")
    inp = inp.split(' := ')
    inp[0] = inp[0].strip()
    if inp[1].strip()[0] == '$':
        return inp[0], inp[1][2:-1]
    if inp[1].strip() == "begin":
        return inp[0], {}
    if re.search("[0-9]+", inp[1].strip()):
        return inp[0], int(inp[1])


def main():
    all_ = {}
    root = all_
    while True:
        line = input()
        if line == '__stop__':
            break
        if line == 'end':
            root = all_
        else:
            try:
                key, var = ui(line)
                if var is None:
                    print(root[key])
                root[key] = var
                if var == {}:
                    root = root[key]
            except Exception as e:
                print(e)
    print(all_)


if __name__ == '__main__':
    main()
