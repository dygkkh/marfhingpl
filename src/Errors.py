import sys
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
