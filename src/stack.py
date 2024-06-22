class stack:
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1
    def put(self, num):
        self.sp += 1
        self.buf[self.sp] = num
    def ret(self):
        num = self.buf[self.sp]
        self.sp -= 1
        return num
    def up(self):
        return self.buf[self.sp]
