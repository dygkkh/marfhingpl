import sys
from time import *

filepath = sys.argv[1]

with open(filepath, "r") as file:
    program_lines = [
    line.strip()
    for line in file.readlines()]

vars = {"au":"149.597.870,66 km",
        "km":"1000m",
        "m":"100cm"}
toks = []
tok_count = 0
label_tra = {}
for line in program_lines:
    tok = line.split(" ")
    a = tok[0]

    if a == "":
        continue

    if a.endswith(":"):
        label_tra[a[:-1]] = tok_count
        continue

    toks.append(a)
    tok_count += 1
    if a.lower() == "put":
        num = int(tok[1])
        toks.append(num)
        tok_count += 1
    elif a.lower() == "res":
        eval(" ".join(tok[1:]))
    elif a.lower() == "imprint":
        stri = " ".join(tok[1:])
        if stri.startswith('"'):
            if stri.endswith('"'):
                stri = stri[1:-1]
                toks.append(stri)
            elif stri.endswith('";'):
                stri = stri[1:-2]
                toks.append(stri)
        tok_count += 1
    elif a.lower() == "strinput":
        stri = " ".join(tok[1:])[1:-1]
        toks.append(stri)
        tok_count += 1
    elif a.lower() == "goto-equ.0":
        label = tok[1]
        toks.append(label)
        tok_count += 1
    elif a.lower() == "goto-grth.0":
        label = tok[1]
        toks.append(label)
        tok_count += 1
    elif a.lower() == "v":
        name = toks[3]
        if tok[1] == "stri":
            stri = " ".join(tok[4])
            if tok[2] == "equ":
                if stri.startswith('"'):
                    if stri.endswith('"'):
                        stri = stri[1:-1]
                        vars[name] = stri
                    elif stri.endswith('";'):
                        stri = stri[1:-2]
                        vars[name]  = stri
        elif tok[1] == "int":
            inv = " ".join(tok[4])
            if tok[2] == "equ":
                toks[name] = int(inv)




class stack:
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1
    def put(self, num):
        self.sp += 1
        self.buf[self.sp] = num
    def ret(self):
        num = self.buf[self.sp]
        self.sp += 1
        return num
    def up(self):
        return self.buf[self.sp]

pc = 0
stack = stack(256)

while toks[pc] != "endtok;":
    a = toks[pc]
    pc += 1

    if a.lower() == "put":
        num = toks[pc]
        pc += 1

        stack.put(num)
    elif a.lower() == "ret":
        stack.ret()

    elif a.lower() == "sum":
        na = stack.ret()
        nb = stack.ret()
        stack.put(nb+na)
    elif a.lower() == "sub":
        na = stack.ret()
        nb = stack.ret()
        stack.put(nb-na)
    elif a.lower() == "imprint":
        stri = toks[pc]
        pc += 1
        print(stri)
    elif a.lower() == "intinput":
        num = int(input())
        stack.put(num)
    elif a.lower() == "goto-equ.0":
        num = stack.up()
        if num == 0:
            pc = label_tra[toks[pc]]
        else:
            pc += 1
    elif a.lower() == "strinput":
        stri = toks[pc]
        pc += 1
        input(stri)
    elif a.lower() == "goto-grth.0":
        num = stack.up()
        if num > 0:
            pc = label_tra[toks[pc]]
        else:
            pc += 1
    elif a.lower() == "escape;":
        exit()
    elif a.lower() == "break;":
            break
    elif a.lower() == "continue;":
        continue
