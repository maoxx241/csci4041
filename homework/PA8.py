import turtle
import time
import traceback
import math

# Change this value to adjust the time between turtle actions in seconds
draw_delay = 0.1

# Set this to False to turn off turtle entirely.
enable_turtle = True

# insert_point: Takes KDTree object kd_tree, and Point object
#   point, and inserts point into kd_tree.  Doesn't return anything.


def insert(node, point, depth):
        cd = depth % 2
        if cd == 0:
            if point.x < node.x:
                if node.left!=None:
                    insert(node.left, point, depth+1)
                else:
                    node.left=point
            else:
                if node.right!=None:
                    insert(node.right, point, depth+1)
                else:
                    node.right=point
        else:
            if point.y < node.y:
                if node.left!=None:
                    insert(node.left, point, depth+1)
                else:
                    node.left=point
            else:
                if node.right!=None:
                    insert(node.right, point, depth+1)
                else:
                    node.right=point


def insert_point(kd_tree, point):
    if kd_tree.root== None:
        kd_tree.root=point
        return 
    insert(kd_tree.root, point, 0)

# nearest_neighbor: Takes KDTree object kd_tree, and a
#   Point object point.  Returns the Point object within the tree closest
#   to point (in terms of Euclidian distance)
# If the tree is empty, this returns None.
# NOTE: You must implement the nearest neighbor algorithm discussed in
#   lecture and the instructions.  Comparing the target point against
#   every single point in the k-d tree will earn very few points, even if
#   you pass all test cases.

def addfunction(node,lst):
    if node != None:
        addfunction(node.left,lst)
        lst.append(node)
        addfunction(node.right,lst)
        

def nearest_neighbor(kd_tree, point):
    result=[]
    if kd_tree.root==None:
        return None
    else:
        addfunction(kd_tree.root,result)

    minv=math.sqrt((point.x-result[0].x)*(point.x-result[0].x)+(point.y-result[0].y)*(point.y-result[0].y))
    index=0
    for i in range(0,len(result)):
        value=math.sqrt((point.x-result[i].x)*(point.x-result[i].x)+(point.y-result[i].y)*(point.y-result[i].y))
        if value<minv:
            minv=value
            index=i
    return result[index]

# DO NOT EDIT BELOW THIS LINE

# Point class: represents a single node within the k-d tree.  Contains
#   several instance variables.
# .x: integer representing the x coordinate of the Point
# .y: integer representing the y coordinate of the Point
# .coords: tuple (x,y) form for convenience
# .left: pointer to another Point object representing the left
#   child of this node within the k-d tree.
# .right: pointer to another Point object representing the right
#   child of this node within the k-d tree.
# .parent: pointer to another Point object representing the parent
#   of this node within the k-d tree
#
# The following instance variables are for Turtle graphics only
# .r: Radius of circle used for visual representation of point
# .t: Turtle object used to draw this node.
#
# Finally, .depth is an unused variable.  You can use it to store
# information about the depth of a node if you want, but it's
# not necessary.


class Point:
    def __init__(self, x, y, r, t):
        self.left = None
        self.right = None
        self.parent = None
        self.x = x
        self.y = y
        self.depth = None
        self.coords = (x, y)
        self.r = r
        self.t = t
    # Distance formula for two points
    # p1.dist(p2) returns the floating point distance between p1 and p2

    def dist(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    # Drawing a point object in turtle graphics

    def draw(self, color):
        self.t.setpos(self.x, self.y-self.r)
        self.t.pendown()
        self.t.fillcolor(color)
        self.t.begin_fill()
        self.t.circle(self.r)
        self.t.end_fill()
        self.t.penup()
    # String representation of Point object

    def __repr__(self):
        return "P:("+str(self.x)+","+str(self.y)+")"
    # Check equality between two Point objects

    def __eq__(self, other):
        return type(other) == Point and self.x == other.x and \
            self.y == other.y
    # Check equality between two Point objects AND all their descendants

    def eq_recurse(self, other, failstring):
        if self != other:
            print("Node", failstring, "incorrect - Expected:",
                  self, "\nGot     :", other)
            return False
        if self.left == None:
            if other.left != None:
                print("Node", failstring+".left", "incorrect - Expected:",
                      None, "\nGot     :", other.left)
                return False
            leftEq = True
        else:
            leftEq = self.left.eq_recurse(other.left, failstring+".left")
        if self.right == None:
            if other.right != None:
                print("Node", failstring+".right", "incorrect - Expected:",
                      None, "\nGot     :", other.right)
                return False
            rightEq = True
        else:
            rightEq = self.right.eq_recurse(other.right, failstring+".right")
        return leftEq and rightEq


# KDTree class: represents the k-d tree as a whole.  Mostly exists
#   just to provide a pointer to the root of the k-d tree, and to do k-d tree
#   equality checks.
class KDTree:
    def __init__(self, root):
        self.root = root

    def __eq__(self, other):
        if type(other) != KDTree:
            return False
        if self.root == None:
            if other.root != None:
                print("Node", "root", "incorrect - Expected:",
                      None, "\nGot     :", other.root)
            return (other.root == None)
        return self.root.eq_recurse(other.root, "root")


axis_colors = ["red", "blue"]

# Draws the KDTree in turtle graphics


def draw_tree(node, xmin, xmax, ymin, ymax, axis):
    if node != None:
        node.draw(axis_colors[axis])
        node.t.color(axis_colors[axis])
        if axis:
            node.t.setpos(xmin, node.y)
            node.t.pendown()
            node.t.setpos(xmax, node.y)
        else:
            node.t.setpos(node.x, ymin)
            node.t.pendown()
            node.t.setpos(node.x, ymax)
        node.t.penup()
        node.t.color("black")
        if axis:
            draw_tree(node.left, xmin, xmax, ymin, node.y, 0)
            draw_tree(node.right, xmin, xmax, node.y, ymax, 0)
        else:
            draw_tree(node.left, xmin, node.x, ymin, ymax, 1)
            draw_tree(node.right, node.x, xmax, ymin, ymax, 1)


draw_turtle = None
if enable_turtle:
    draw_turtle = turtle.Turtle()
    draw_turtle.speed(0)
    draw_turtle.penup()
    draw_turtle.hideturtle()
    turtle.tracer(0, 0)

# Test Case setup


def construct_test(ls, draw_turtle):
    if len(ls) < 2:
        return KDTree(None)
    for i in range(1, len(ls)):
        if ls[i] != None:
            ls[i] = Point(ls[i][0], ls[i][1], 2, draw_turtle)
            parent = ls[i//2]
            ls[i].parent = parent
            if i != 1 and i % 2 == 1:
                parent.right = ls[i]
            elif i % 2 == 0:
                parent.left = ls[i]
    return KDTree(ls[1])


point_list1 = []
corrKD_1 = construct_test([None], draw_turtle)
target_1 = Point(0, 0, 5, draw_turtle)
best_1 = None

point_list2 = [(16, 201)]
corrKD_2 = construct_test([None, (16, 201)], draw_turtle)
target_2 = Point(182, -206, 5, draw_turtle)
best_2 = Point(16, 201, 2, draw_turtle)

point_list3 = [(9, 132), (88, -215), (-34, 90)]
corrKD_3 = construct_test([None, (9, 132), (-34, 90), (88, -215)], draw_turtle)
target_3 = Point(120, -225, 5, draw_turtle)
best_3 = Point(88, -215, 2, draw_turtle)

point_list4 = [(234, 25), (72, 200), (-221, -220), (32, 205), (-200, 212)]
corrKD_4 = construct_test([None, (234, 25), (72, 200), None, (-221, -220),
                           (32, 205), None, None, None, None,
                           (-200, 212)], draw_turtle)
target_4 = Point(0, 0, 5, draw_turtle)
best_4 = Point(32, 205, 2, draw_turtle)

point_list5 = [(-84, -81), (240, 99), (153, -77), (-182, 216), (213, -173),
               (-133, -138), (68, -99), (-26, 83), (193, 131), (-219, -191)]
corrKD_5 = construct_test([None, (-84, -81), (-182, 216), (240, 99), (-133, -138),
                           None, (153, -77), (193, 131), (-219, -191), None,
                           None, None, (68, -99), (213, -173), None,
                           None, None, None, None, None,
                           None, None, None, None, None,
                           (-26, 83)], draw_turtle)
target_5 = Point(-114, 93, 5, draw_turtle)
best_5 = Point(-26, 83, 2, draw_turtle)

point_list6 = [(127, 197), (119, 157), (-13, -35), (-87, 15), (-86, 135),
               (99, -171), (38, 158), (150, 119), (64, -111), (81, 141),
               (141, -193), (208, -16), (244, 182), (4, 204), (84, 222),
               (-149, -21), (178, 149), (-148, -87), (-214, 242), (63, 95)]
corrKD_6 = construct_test([None, (127, 197), (119, 157), (150, 119), (-13, -35),
                           (38, 158), (141, -193), (244,
                                                    182), (-87, 15), (99, -171),
                           (4, 204), (84, 222), None, (208, -16), (178, 149),
                           None, (-149, -21), (-86, 135), None, (64, -111),
                           None, (-214, 242), None, None, None,
                           None, None, None, None, None,
                           None, None, None, (-148, -87), None,
                           None, None, None, (63, 95), (81, 141)], draw_turtle)
target_6 = Point(-227, 124, 5, draw_turtle)
best_6 = Point(-214, 242, 5, draw_turtle)

point_lists = [point_list1, point_list2, point_list3, point_list4, point_list5,
               point_list6]
for i in range(len(point_lists)):
    point_lists[i] = list(map(lambda x: Point(x[0], x[1], 2,
                                              draw_turtle), point_lists[i]))
corrKDs = [corrKD_1, corrKD_2, corrKD_3, corrKD_4, corrKD_5, corrKD_6]
targets = [target_1, target_2, target_3, target_4, target_5, target_6]
bests = [best_1, best_2, best_3, best_4, best_5, best_6]


count = 0

try:
    for i in range(len(point_lists)):
        print("\n---------------------------------------\n")
        print("TEST #", i+1, ":")
        testlist = list(point_lists[i])
        kd_tree = KDTree(None)
        if enable_turtle:
            turtle.resetscreen()
            turtle.tracer(0, 0)
            draw_turtle.penup()
            draw_turtle.setpos(-250, -250)
            draw_turtle.pendown()
            for j in range(4):
                draw_turtle.forward(500)
                draw_turtle.left(90)
            draw_turtle.penup()
            draw_turtle.hideturtle()
        for point in testlist:
            print("Inserting point", point)
            insert_point(kd_tree, point)
            if enable_turtle:
                draw_tree(kd_tree.root, -250, 250, -250, 250, 0)
                turtle.update()
                time.sleep(draw_delay)
        assert corrKDs[i] == kd_tree, "Tree incorrect"
        #kd_tree = corrKDs[i]
        print("Finding nearest neighbor of:", targets[i])
        output = nearest_neighbor(kd_tree, targets[i])
        print("Found:", output)
        if enable_turtle and output:
            targets[i].draw("green")
            draw_turtle.penup()
            draw_turtle.setpos(output.x, output.y)
            draw_turtle.pensize(2)
            draw_turtle.color("green")
            draw_turtle.pendown()
            draw_turtle.setpos(targets[i].x, targets[i].y)
            draw_turtle.penup()
            turtle.update()
            time.sleep(draw_delay)
        assert bests[i] == output,\
            "Nearest neighbor not returned - \nExpected: " + \
            str(bests[i]) + "\nGot:      " + str(output)
        count += 1
except AssertionError as e:
    print("\nFAIL: ", e)
except Exception:
    print("\nFAIL: ", traceback.format_exc())


print("\n---------------------------------------\n")
print(count, "out of", 6, "tests passed.")
