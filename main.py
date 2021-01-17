from tkinter import *
root = Tk()
root.title("R.o.b.o.t")
root.mainloop()
WIDTH = 800
HEIGHT = 600
Z = 1
IN_GAME = True
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
c.focus_set()
class Object(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                         x, y,
                         fill="white")

class Robot(object):
    def __init__(self, objects):
        self.objects = objects
        self.mapping = {"Down": (0, 1), "Up": (0, -1), "Left": (-1, 0), "Right": (1, 0)}
        self.vector = self.mapping["Right"]

    def move(self):
        for index in range(len(self.objects) - 1):
            object = self.objects[index].instance
            x1, y1, x2, y2 = c.coords(self.objects[index + 1].instance)
            c.coords(object, x1, y1, x2, y2)
        x1, y1, x2, y2 = c.coords(self.objects[-2].instance)
        c.coords(self.objects[-1].instance,
                 x1 + self.vector[0] * Z,
                 y1 + self.vector[1] * Z,
                 x2 + self.vector[0] * Z,
                 y2 + self.vector[1] * Z)

    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

objects = [Object(Z, Z)]
s = Robot(objects)
