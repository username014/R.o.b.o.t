import sys


class Robot(object):
    def __init__(self, objects):
        self.objects = objects
        self.mapping = {"Down": (0, 1), "Up": (0, -1), "Left": (-1, 0), "Right": (1, 0)}
        self.vector = self.mapping["Right"]
    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

if __name__ == '__main__':
    infile, outfile = sys.argv[1:3]
    fout = open(outfile, "w")
    fout.write("0+\n")
    fout.write("0\n")
    fout.write("")
    fout.close()
    print(infile, outfile)