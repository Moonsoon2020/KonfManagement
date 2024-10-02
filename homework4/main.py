import re
import sys
from fileinput import close

import yaml


def trabsl(num: int, n: int):
    return "0" * (n - len(bin(num)[2:])) + bin(num)[2:]


def interpretation(text_program: str, text_bin: str, text_pr: str):
    bibl = {}
    matr = []
    memory = 0
    if text_pr != "":
        with open(text_pr) as f:
            templates = yaml.safe_load(f)
        if templates is not None:
            for var, num in templates.items():
                bibl[var] = memory
                matr.append("100" + trabsl(memory, 4) + trabsl(num, 27))
                memory += 1
    file_program = open(text_program, 'r')
    for line in file_program:
        line = line.replace('\n', '').replace(" ", "")
        if re.match("[a-zA-Z]+=[a-zA-Z]+", line):
            var, num = map(str, line.split("="))
            if var not in bibl.keys():
                bibl[var] = memory
                matr.append("101" + trabsl(memory, 4) + trabsl(bibl[num], 4))
                memory += 1
            else:
                matr.append("101" + trabsl(bibl[var], 4) + trabsl(bibl[num], 4))
        elif re.match("[a-zA-Z]+=[0-9]+", line):
            var, num = map(str, line.split("="))
            if var not in bibl.keys():
                bibl[var] = memory
                matr.append("100" + trabsl(memory, 4) + trabsl(int(num), 27))
                memory += 1
            else:
                matr.append("100" + trabsl(bibl[var], 4) + trabsl(int(num), 27))
        elif re.match("[a-zA-Z]+/=[a-zA-Z]+", line):
            var, num = map(str, line.split("/="))
            if var not in bibl.keys():
                raise Exception("var not defined")
            else:
                matr.append("110" + trabsl(bibl[var], 4) + trabsl(bibl[num], 20))
    file_bin = open(text_bin, 'w')
    print(*matr, file=file_bin, sep="", end="")
    file_bin.close()

def translator(bin_file: str, log_file: str):
    with open(bin_file, 'r') as f:
        prog = f.readline()
        f.close()
    memory = [0 for _ in range(16)]
    while len(prog) != 0:
        print(prog)
        if prog[:3] == "100":
            memory[int(prog[3:7], 2)] = int(prog[7:34], 2)
            prog = prog[34:]
        elif prog[:3] == "101":
            memory[int(prog[3:7], 2)] = memory[int(prog[7:11], 2)]
            prog = prog[11:]
        elif prog[:3] == "110":
            memory[int(prog[3:7], 2)] = int(memory[int(prog[3:7], 2)] / memory[int(prog[7:28], 2)])
            prog = prog[27:]
    log_file = open(log_file, 'w')
    for num in memory:
        print(num, end=", ", file=log_file)
    log_file.close()
    print(memory)


if __name__ == "__main__":
    home = ""
    # main(sys.argv[1], sys.argv[2], sys.argv[3])
    interpretation(home + "prog.txt", home + "bin.txt", home + "tap.yaml")
    translator(home + "bin.txt", home + "log.json")
