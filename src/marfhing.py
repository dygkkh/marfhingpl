import sys
from Errors import *
from stack import *
try:
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
    elif a.lower() == "if_addtok_equ.0":
        label = tok[1]
        toks.append(label)
        tok_count += 1
    elif a.lower() == "if_addtok_grth.0":
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


 val = []
 pc = 0
 stack = stack(256)
 print("&: program_started\n")
# python marfhing.py "C:\Users\Usuario\build\Desktop\Nueva carpeta (9)\Lean\codigo\programming languages\python\marfhinh\marfhingpl\marfhing\marfhingin\examples\probe.mrfng"
 try:
  while toks[pc] != "endtok;":
    a = toks[pc]
    pc += 1

    if a.lower() == "put":
        num = toks[pc]
        pc += 1
        stack.put(num)
        val.append(num)
    elif a.lower() == "ret":
        stack.ret()

    elif a.lower() == "sum":
        try:
            na = stack.ret()
            nb = stack.ret()
            stack.put(nb+na)
            val = sum(val)
        except ValueError:
            Errors(3,1).ErrorIndentificator()
    elif a.lower() == "sub":
        na = stack.ret()
        nb = stack.ret()
        stack.put(nb-na)
    elif a.lower() == "val.show;":
        print(val)
    elif a.lower() == "val.empy;":
        val = []
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
    elif a.lower() == "addtok_intinput":
        try:
            num = int(input())
            stack.put(num)
            val.append(num)
        except ValueError:
            Errors(3,1).ErrorIndentificator()
        except IndexError:
            Errors(1,1).ErrorIndentificator()

    elif a.lower() == "if_addtok_equ.0":
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
    elif a.lower() == "if_addtok_grth.0":
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
    print("\n&: end_program")
except IndexError:
    print("end")
