import sys
from random import randint


RIGHT = '0+'
LEFT = '0-'
UP = '-0'
DOWN = '+0'

if __name__ == '__main__':
    infile, outfile = sys.argv[1:3]
    fin = open(infile, "r")
    fout = open(outfile, "w")
    lines = [line.strip() for line in fin]

    s = [RIGHT, LEFT, DOWN, UP]
    reverse = {DOWN: UP, RIGHT: LEFT, UP: DOWN, LEFT: RIGHT, '00': '00'}
    wfield = int(lines[0])
    hod = int(lines[1])
    (x, y) = map(int, lines[2].split())
    kudahod = lines[3]

    memsize = int(lines[5])

    mem = ""
    if memsize != 0:
        mem = lines[6]

    waller = lines[4]

    prev_steps = mem.split()[:3]

    print(hod, lines)
    print(f"Prev 3: {prev_steps}")

    b = "00"
    c = "00"
    d = "00"
    if hod > 2:
        b = prev_steps[0]
        c = prev_steps[1]
        d = prev_steps[2]
        print(b, c, d, sep=' ')

    if hod == 0:
        new_step = s[randint(0, 3)]
    else:
        old_step = kudahod
        new_step = s[randint(0, 3)]
        while new_step==reverse[old_step]:
            new_step = s[randint(0, 3)]
        if x == 1:
            print("9*")
            new_step = s[randint(0, 3)]
            while new_step == UP or new_step == reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif y == 1:
            print("10*")
            new_step = s[randint(0, 3)]
            while new_step == LEFT or new_step == reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif x == wfield:
            print("11*")
            new_step = s[randint(0, 3)]
            while new_step == DOWN or new_step == reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif y == wfield:
            print("12*")
            new_step = s[randint(0, 3)]
            while new_step == RIGHT or new_step == reverse[old_step]:
                new_step = s[randint(0, 3)]
        if b == UP and c == RIGHT and d == DOWN:
            new_step = s[randint(0, 3)]
            while new_step == LEFT or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
                if x == 1:
                    print("9*")
                    new_step = s[randint(0, 3)]
                    while new_step == UP or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == 1:
                    print("10*")
                    new_step = s[randint(0, 3)]
                    while new_step == LEFT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif x == wfield:
                    print("11*")
                    new_step = s[randint(0, 3)]
                    while new_step == DOWN or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == wfield:
                    print("12*")
                    new_step = s[randint(0, 3)]
                    while new_step == RIGHT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
            print("1*")
        elif b == UP and c == LEFT and d == DOWN:
            new_step = s[randint(0, 3)]
            while new_step == RIGHT or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
                if x == 1:
                    print("9*")
                    new_step = s[randint(0, 3)]
                    while new_step == UP or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == 1:
                    print("10*")
                    new_step = s[randint(0, 3)]
                    while new_step == LEFT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif x == wfield:
                    print("11*")
                    new_step = s[randint(0, 3)]
                    while new_step == DOWN or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == wfield:
                    print("12*")
                    new_step = s[randint(0, 3)]
                    while new_step == RIGHT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
            print("2*")
        elif b == DOWN and c == RIGHT and d == UP:
            new_step = s[randint(0, 3)]
            while new_step == LEFT or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
                if x == 1:
                    print("9*")
                    new_step = s[randint(0, 3)]
                    while new_step == UP or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == 1:
                    print("10*")
                    new_step = s[randint(0, 3)]
                    while new_step == LEFT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif x == wfield:
                    print("11*")
                    new_step = s[randint(0, 3)]
                    while new_step == DOWN or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == wfield:
                    print("12*")
                    new_step = s[randint(0, 3)]
                    while new_step == RIGHT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
            print("3*")
        elif b == DOWN and c == LEFT and d == UP:
            print("4*")
            new_step = s[randint(0, 3)]
            while new_step == RIGHT or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
                if x == 1:
                    print("9*")
                    new_step = s[randint(0, 3)]
                    while new_step == UP or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == 1:
                    print("10*")
                    new_step = s[randint(0, 3)]
                    while new_step == LEFT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif x == wfield:
                    print("11*")
                    new_step = s[randint(0, 3)]
                    while new_step == DOWN or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == wfield:
                    print("12*")
                    new_step = s[randint(0, 3)]
                    while new_step == RIGHT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
        elif b == LEFT and c == DOWN and d == RIGHT:
            print("5*")
            new_step = s[randint(0, 3)]
            while new_step == UP or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
                if x == 1:
                    print("9*")
                    new_step = s[randint(0, 3)]
                    while new_step == UP or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == 1:
                    print("10*")
                    new_step = s[randint(0, 3)]
                    while new_step == LEFT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif x == wfield:
                    print("11*")
                    new_step = s[randint(0, 3)]
                    while new_step == DOWN or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == wfield:
                    print("12*")
                    new_step = s[randint(0, 3)]
                    while new_step == RIGHT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
        elif b == LEFT and c == UP and d == RIGHT:
            print("6*")
            new_step = s[randint(0, 3)]
            while new_step == DOWN or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
                if x == 1:
                    print("9*")
                    new_step = s[randint(0, 3)]
                    while new_step == UP or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == 1:
                    print("10*")
                    new_step = s[randint(0, 3)]
                    while new_step == LEFT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif x == wfield:
                    print("11*")
                    new_step = s[randint(0, 3)]
                    while new_step == DOWN or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == wfield:
                    print("12*")
                    new_step = s[randint(0, 3)]
                    while new_step == RIGHT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
        elif b == RIGHT and c == DOWN and d == LEFT:
            print("7*")
            new_step = s[randint(0, 3)]
            while new_step == UP or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
                if x == 1:
                    print("9*")
                    new_step = s[randint(0, 3)]
                    while new_step == UP or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == 1:
                    print("10*")
                    new_step = s[randint(0, 3)]
                    while new_step == LEFT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif x == wfield:
                    print("11*")
                    new_step = s[randint(0, 3)]
                    while new_step == DOWN or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == wfield:
                    print("12*")
                    new_step = s[randint(0, 3)]
                    while new_step == RIGHT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
        elif b == RIGHT and c == UP and d == LEFT:
            print("8*")
            new_step = s[randint(0, 3)]
            while new_step == DOWN or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
                if x == 1:
                    print("9*")
                    new_step = s[randint(0, 3)]
                    while new_step == UP or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == 1:
                    print("10*")
                    new_step = s[randint(0, 3)]
                    while new_step == LEFT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif x == wfield:
                    print("11*")
                    new_step = s[randint(0, 3)]
                    while new_step == DOWN or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
                elif y == wfield:
                    print("12*")
                    new_step = s[randint(0, 3)]
                    while new_step == RIGHT or new_step == reverse[old_step]:
                        new_step = s[randint(0, 3)]
        if x == 1 and y == 1:
            print("13*")
            new_step = s[randint(0, 3)]
            while new_step == UP or new_step == LEFT or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif x == wfield and y == 1:
            print("14*")
            new_step = s[randint(0, 3)]
            while new_step == LEFT or new_step == DOWN or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif x == 1 and y == wfield:
            print("15*")
            new_step = s[randint(0, 3)]
            while new_step == UP or new_step == RIGHT or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif x == wfield and y == wfield:
            print("16*")
            new_step = s[randint(0, 3)]
            while new_step == RIGHT or new_step == DOWN or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]

    memsize = memsize + 3
    mem = f"{new_step} " + mem
    fout.write(f"{new_step}\n")
    fout.write(f"{memsize}\n")
    fout.write(mem)
    fout.close()
    print("new_step = " + new_step)
    print(infile, outfile)