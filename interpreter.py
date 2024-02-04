import sys

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

class Errors:
    def __init__(self, num, num2):
        self.se = ("", "you forgot input", "incorrect Token", "incorrect function", "you forgot a token")
        self.ffe = "you forgot or you type incorrectly the function 'endtok;'"
        self.ve = "you write in the incorrect type"
        self.errors = ("", "Syntax_Error", "Final-Function_Error", "Val_Error")
        self.pos = num
        self.pos2 = num2
    def ErrorIndentificator(self):
        error = 0
        if self.pos == 1:
            print(f"_{self.pos}_: {self.errors[self.pos]}: {self.se[self.pos2]}")
            error += 1
        elif self.pos == 2:
            print(f"_{self.pos}_: {self.errors[self.pos]}: {self.ffe}")
            error += 1
        elif self.pos == 3:
            print(f"_{self.pos}_: {self.errors[self.pos]}: {self.ve}")
            error += 1
        print(error)
        sys.exit()


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
try:
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
        try:
            na = stack.ret()
            nb = stack.ret()
            stack.put(nb+na)
        except ValueError:
            Errors(3,1).ErrorIndentificator()
    elif a.lower() == "sub":
        na = stack.ret()
        nb = stack.ret()
        stack.put(nb-na)
    elif a.lower() == "imprint":
       try:
        stri = toks[pc]
        if stri.startswith('"') and stri.endswith('"'):
             pc += 1
             stri = stri[1:-1]
             print(stri)
        else:
            Errors(4, 1).ErrorIndentificator()
       except IndexError:
        Errors(1, 1).ErrorIndentificator()
    elif a.lower() == "intinput":
        try:
            num = int(input())
            stack.put(num)
        except ValueError:
            Errors(3,1).ErrorIndentificator()
        except IndexError:
            Errors(1,1).ErrorIndentificator()

    elif a.lower() == "goto-equ.0":
        num = stack.up()
        if num == 0:
            pc = label_tra[toks[pc]]
        else:
            pc += 1
    elif a.lower() == "strinput":
        try:
         stri = toks[pc]
         pc += 1
         input(stri)
        except IndexError:
            Errors(1,1).ErrorIndentificator()
        except ValueError:
            Errors(3,1).ErrorIndentificator()
    elif a.lower() == "goto-grth.0":
        num = stack.up()
        if num > 0:
            pc = label_tra[toks[pc]]
        else:
            pc += 1
    elif a.lower() == "escape;":
        sys.mexit()
    elif a.lower() == "break;":
            break
    elif a.lower() == "$":
        comment = " ".join(a[1:])
    elif a.lower() == "continue;":
        continue
    else:
        Errors(1,2).ErrorIndentificator()
except IndexError:
    Errors(2, 1).ErrorIndentificator()

finally:
    print("\nend_program")

