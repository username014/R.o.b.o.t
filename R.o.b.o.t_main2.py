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
    (x, y) = map(int, lines[2].split())          #x=y y=x
    old_step = lines[3]

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

    banned = set()
    banned.add(reverse[old_step])






    new_step = s[randint(0, 3)]
    while new_step in banned:
        new_step = s[randint(0, 3)]


    memsize = memsize + 3
    mem = f"{new_step} " + mem
    fout.write(f"{new_step}\n")
    fout.write(f"{memsize}\n")
    fout.write(mem)
    fout.close()
    print("new_step = " + new_step)

