import sys
import math


class Save():
    def new(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def ret(self):
        return [self.a, self.b, self.c]


def solve(a, b, c):
    d = b**2 - 4*a*c
    state = (False, True)[d > 0]
    if state:
        print("x1 = ", (-1*b + math.sqrt(d)))
        print("x2 = ", (-1*b - math.sqrt(d)))
        print("0")
    else:
        print("дискриминант < 0")
        print("0")


if __name__ == "__main__":
    cli = Save()
    tester = [str(i) for i in range(1000)]

    login = input().split(" ")

    date = ["my", "name"]
    if(login[1] == date[0] and login[2] == date[1]):
        while True:
            solver = input().split(" ")
            if (solver[0] == "SOLVE" and len(solver) > 1):
                try:
                    state = True if solver[1] in tester and solver[2] in tester and solver[3] in tester else False
                    if(state):
                        solve(int(solver[1]), int(solver[2]), int(solver[3]))
                    else:
                        print("3")
                except:
                    print("2")

            elif(solver[0] == "STORE"):
                try:
                    cli.new(int(solver[1]), int(solver[2]), int(solver[3]))
                except:
                    print("3")
            elif (solver[0] == "SOLVE"):
                try:
                    big = cli.ret()
                    solve(big[0], big[1], big[2])
                except:
                    print("3")
                    print(big)
            else:
                pass
    else:
        print("1")
