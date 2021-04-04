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
    mem = ""
    memsize = int(lines[5])
    if memsize != 0:
        mem = lines[6]
    if hod == 0:
        (x, y) = map(int, lines[2].split())
    else:
        (x, y) = mem.split()[:2]
        x = int(x)
        y = int(y)  # x=y y=x
    old_step = lines[3]






    waller = lines[4]

    prev_steps = mem.split()[:6]

    print(hod, lines)
    print(f"Prev 3: {prev_steps}")

    b = "00"
    if hod > 0:
        b = prev_steps[0]
        print(b, sep=' ')

    banned = set()
    banned.add(reverse[old_step])
    if x == -1 or y == -1:
        if waller == 'w':
            if old_step == UP and y == -1:
                y = 1
            elif old_step == LEFT and x == -1:
                x = 1

    if waller != "w":
        if y != -1:
            if old_step == UP:
                y-=1
            elif old_step == DOWN:
                y+=1
        if x != -1:
            if old_step == LEFT:
                x-=1
            elif old_step == RIGHT:
                x+=1




    if x==-1 and y==-1:
        new_step = UP

    elif x==-1 and y==1:
        new_step = LEFT

    else:
        new_step = s[randint(0, 3)]
        while new_step == reverse[old_step]:
            new_step = s[randint(0, 3)]
        if x == 1:
            print("9*")
            new_step = s[randint(0, 3)]
            while new_step == LEFT or new_step == reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif y == 1:
            print("10*")
            new_step = s[randint(0, 3)]
            while new_step == UP or new_step == reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif x == wfield:
            print("11*")
            new_step = s[randint(0, 3)]
            while new_step == RIGHT or new_step == reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif y == wfield:
            print("12*")
            new_step = s[randint(0, 3)]
            while new_step == DOWN or new_step == reverse[old_step]:
                new_step = s[randint(0, 3)]
        if x == 1 and y == 1:
            print("13*")
            new_step = s[randint(0, 3)]
            while new_step == UP or new_step == LEFT or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif x == wfield and y == 1:
            print("14*")
            new_step = s[randint(0, 3)]
            while new_step == RIGHT or new_step == UP or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif x == 1 and y == wfield:
            print("15*")
            new_step = s[randint(0, 3)]
            while new_step == DOWN or new_step == LEFT or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]
        elif x == wfield and y == wfield:
            print("16*")
            new_step = s[randint(0, 3)]
            while new_step == RIGHT or new_step == DOWN or new_step==reverse[old_step]:
                new_step = s[randint(0, 3)]


    memsize = memsize + 6
    mem = f"{x} {y} " + mem
    print(f"mem ={mem.__str__()}")
    fout.write(f"{new_step}\n")
    fout.write(f"{memsize}\n")
    fout.write(mem)
    fout.close()
    print("new_step = " + new_step)

