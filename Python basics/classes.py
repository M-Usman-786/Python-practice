class Point:
    def move(self):
        print("MOVE")
    def draw(self):
        print("DRAW")


#object
point1 = Point()
point1.x = 10
point1.y = 20

point1.draw()
print(point1.x)
