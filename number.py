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
        try:
            if num > 9:
                numString = str(num)
                numberlist = []
                for d in numString:
                    numberlist.append(
                        self.printNumber(self.matchNumberCode[int(d)]))
                return self.printNumberGroup(
                    numberlist, space=" ", breakline=0)
            else:
                return self.printNumber(self.matchNumberCode[num])

        except Exception as e:
            print(f"##err input #{num} not in list.\n{e}")

    def printNumberGroup(self, numbers, space="\t", breakline=1, noOfDigit=5, diplaylines=5):
        newlines = [""] * diplaylines
        counter = 0
        newlineNum = 0
        for i in numbers:
            for l in range(len(i)):
                row = noOfDigit * newlineNum + l
                print(row, counter)
                newlines[row] += i[l]
                newlines[row] += space
            counter += 1

            if counter % noOfDigit == 0 and counter > 0 and breakline == 1:
                newlineNum += 1
                # print(newlineNum)
                for i in range(diplaylines):
                    newlines.append("")

        return newlines

    def display(self, lines):
        for l in lines:
            print(l)


if __name__ == "__main__":
    print("Testing...")
    matchSet = matchNumber()
    numbers = []

    for i in range(0, 20):
        numbers.append(matchSet.numbertoCode(i))
    matchSet.display(matchSet.printNumberGroup(numbers))
