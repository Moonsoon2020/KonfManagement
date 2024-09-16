import zipfile
from datetime import datetime
import json
import yaml

history = []
all_f = []
path = ['archive']
directory = []

def clear():
    global history, all_f, path, directory
    history = []
    all_f = []
    path = ['archive']
    directory = []


class Action:
    def __init__(self, user, command, param):
        self.user = user
        self.command = command
        self.param = param
        self.time = str(datetime.now())

    def json(self):
        return {"user": self.user, "command": self.command, "time": self.time, "param": self.param}


class Base:
    def __init__(self, title):
        self.title = title
        self.permission = [1, 1, 1, 1, 1, 0, 0, 0, 0]
        self.childs = []

    def add_child(self, el, a):
        if el == self:
            return
        if len(a) == 0:
            self.childs.append(el)
            return
        for child in self.childs:
            if child.title == a[0]:
                a.pop(0)
                child.add_child(el, a)
                return

    def get_child(self, title):
        for child in self.childs:
            if child.title == title:
                return child

    def set_permission(self, permission, user, status):
        users = {'q': 1, "a": 0, "b": 2}
        perm = {'w': 2, "r": 1, "x": 0}
        self.permission[users[user] * 3 + perm[permission]] = status


def check(elem1, elem2):
    for j in range(min(len(elem1), len(elem2))):
        if elem1[j] != elem2[j]:
            return False
    return True


def find_file(text):
    global path, directory
    if text[0] == '/':
        path_new = path + text[1:].split('/')
    else:
        path_new = text.split('/')
    flag = False
    for elem in directory[1:]:
        if check(elem, path_new):
            flag = True
    if not flag:
        return f"Path '{text}' does not exist."
    else:
        kon = all_f[0]
        while len(path_new) > 1:
            kon = kon.get_child(path_new[1])
            path_new.pop(1)
        return kon


def rep(x):
    if x[-1] == '/':
        return x.split('/')[:-1]
    return x.split('/')


def main_c():
    global path
    with open('konf.yaml') as f:
        templates = yaml.safe_load(f)

    files = templates['path_vm'] + "\\archive.zip"
    user = templates['user']
    with zipfile.ZipFile(files) as zf:
        for der in sorted(map(rep, zf.namelist()), key=lambda x: len(x)):
            directory.append(der)
        for base in directory:
            all_f.append(Base(base[-1]))
            all_f[0].add_child(all_f[-1], base[1:-1])
    kon = all_f[0]
    while True:
        try:
            print(f"[{user}] : {'/'.join(path)} :", end='')
            command, *param = input().split()
        except ValueError:
            continue
        history.append(Action(user, command, param).json())
        if command == "ls":
            length = []
            if len(kon.childs) == 0:
                print("0 files")
                continue
            for i in kon.childs:
                length.append(len(i.title))
            print(" " * (max(length) + 2) + 'a  q  b  ')
            print(" " * (max(length) + 2) + 'xrwxrwxrx')
            for i in kon.childs:
                print(i.title + " " * (max(length) - len(i.title) + 2) + ''.join(map(str, i.permission)))
        elif command == "cd":
            if len(param) == 0:
                print("You need to specify a directory")
                continue
            file = find_file(param[0])
            if isinstance(file, str):
                print(file)
                continue
            kon = file
            if param[0][0] == '/':
                path = path + param[0][1:].split('/')
            else:
                path = param[0].split('/')
        elif command == "exit":
            break
        elif command == "chmod":
            if len(param) != 2:
                print("You need to specify a permission")
                continue
            file = find_file(param[1])
            if isinstance(file, str):
                print(file)
                continue
            if param[0].count('+') == 1:
                users, perms = param[0].split('+')
                for user in users:
                    for perm in perms:
                        file.set_permission(perm, user, 1)
            elif param[0].count('-') == 1:
                users, perms = param[0].split('-')
                for user in users:
                    for perm in perms:
                        file.set_permission(perm, user, 0)
            else:
                print('error')
        elif command == "history":
            for action in history:
                print(action['time'], action['user'], action['command'], action['param'])
        elif command == "wc":
            input_text = ''
            s = 0
            while True:
                line = input()
                if line == 'stop':
                    break
                input_text += line
                s += 1
            print(s, len(input_text.split()) + s, len(input_text) + s)
        elif len(command) == 0:
            history.pop()
            continue
        else:
            print(f"The name '{command}' is not recognized as a command name")
    file = open(templates["path_log"] + '\\history.json', 'w')
    json.dump(history, file)
    file.close()
    clear()


if __name__ == '__main__':
    main_c()
