import re
import sys
import yaml


def trabsl(num: int, n: int):
    return "0" * (n - len(bin(num)[2:])) + bin(num)[2:]


def main(text_program: str, text_bin: str, text_pr: str):
    bibl = {}
    matr = []
    memory = 0
    if text_pr != "":
        with open(text_pr) as f:
            templates = yaml.safe_load(f)
        if templates is not None:
            for var, num in templates.items():
                bibl[var] = [memory, num]
                matr.append("00" + trabsl(memory, 6) + trabsl(num, 33))
                memory += 1
    file_program = open(text_program, 'r')
    for line in file_program:
        line = line.replace('\n', '').replace(" ", "")
        if re.match("[a-zA-Z]+=[a-zA-Z]+", line):
            var, num = map(str, line.split("="))
            if var not in bibl.keys():
                bibl[var] = [memory, bibl[num][1]]
                matr.append("01" + trabsl(memory, 6) + trabsl(bibl[num][1], 10))
                memory += 1
            else:
                bibl[var][1] = bibl[num][1]
                matr.append("01" + trabsl(bibl[var][0], 6) + trabsl(bibl[num][1], 10))
        elif re.match("[a-zA-Z]+=[0-9]+", line):
            var, num = map(str, line.split("="))
            if var not in bibl.keys():
                bibl[var] = memory, int(num)
                matr.append("00" + trabsl(memory, 6) + trabsl(int(num), 33))
                memory += 1
            else:
                bibl[var][1] = int(num)
                matr.append("00" + trabsl(bibl[var][0], 6) + trabsl(int(num), 33))
        elif re.match("[a-zA-Z]+/=[a-zA-Z]+", line):
            var, num = map(str, line.split("/="))
            if var not in bibl.keys():
                raise Exception("var not defined")
            else:
                bibl[var][1] = int(bibl[var][1] / bibl[num][1])
                matr.append("10" + trabsl(bibl[var][0], 6) + trabsl(bibl[var][1], 27))
    print(bibl, matr)


if __name__ == "__main__":
    home = ""
    # main(sys.argv[1], sys.argv[2], sys.argv[3])
    main(home + "prog.txt", home + "", home + "tap.yaml")
