'''
this will saving the match code to create number

top: t
left: lt, lb
right: rt, rb
centre: c
bottom: b

'''


class matchNumber:

    # number match code
    matchPositionOrder = ["t", "c", "b", "lt", "lb", "rt", "rb"]
    matchNumberCode = {
        1: [0, 0, 0, 0, 0, 1, 1],
        2: [1, 1, 1, 0, 1, 1, 0],
        3: [1, 1, 1, 0, 0, 1, 1],
        4: [0, 1, 0, 1, 0, 1, 1],
        5: [1, 1, 1, 1, 0, 0, 1],
        6: [1, 1, 1, 1, 1, 0, 1],
        7: [1, 0, 0, 0, 0, 1, 1],
        8: [1, 1, 1, 1, 1, 1, 1],
        9: [1, 1, 1, 1, 0, 1, 1],
        0: [1, 0, 1, 1, 1, 1, 1]
    }

    def switchOn(self, val, ish=0):
        if ish:
            sym = "|"
            bsym = " "
        else:
            sym = " - "
            bsym = "   "
        if val:
            return sym
        else:
            return bsym

    def printNumber(self, code=[1, 1, 1, 1, 1, 1, 1]):
        line = [""] * 5
        line[0] = self.switchOn(code[0])
        line[2] = self.switchOn(code[1])
        line[4] = self.switchOn(code[2])

        # "|"
        line[1] = "{} {}".format(
            self.switchOn(code[3], ish=1), self.switchOn(code[5], ish=1))
        line[3] = "{} {}".format(
            self.switchOn(code[4], ish=1), self.switchOn(code[6], ish=1))

        return line

    def numbertoCode(self, num):
        return self.printNumber(self.matchNumberCode[num])

    def printNumberGroup(self, numbers, space="\t"):
        newline = [""] * 5
        for i in numbers:
            for l in range(len(i)):
                newline[l] += space
                newline[l] += i[l]
        return newline

    def display(self, lines):
        for l in lines:
            print(l)


if __name__ == "__main__":

    matchSet = matchNumber()
    numbers = []
    for i in range(10):
        numbers.append(matchSet.numbertoCode(i))
    matchSet.display(matchSet.printNumberGroup(numbers))
