import traceback, turtle, time

#Change this value to adjust the time between turtle actions in seconds
draw_delay = 0.3

#Set this to False to turn off turtle entirely.
enable_turtle = True

#hyperspace_jump_route: takes in two arguments:
#   star_list is a list of Star objects (nodes), in order of index.
#   jump_matrix is a matrix (2D list) of edge weights for the graph.
#   One way to get the edge weight between Star object u and Star object v
#   is jump_matrix[u.index][v.index].  You can also access this through
#   either u or v's .jump_times instance variable (see Star class)
#This function must use Dijkstra's algorithm to compute the shortest path
#   from the red star (star_list[0]) to the orange star (star_list[1]).
#Must return a LIST representing every star in the shortest weighted path
#   from the start node (star_list[0]) to the goal node (star_list[1]),
#   inclusive.
def hyperspace_jump_route(star_list,jump_matrix):
    #TODO: Implement this function
    start = None
    target = None
    min_heap = []
    for star in star_list:
        star.set_dist(float("inf"))
        star.prev = None
        if star.color =="orange":
            target = star
        if star.color == "red":
            start = star
        min_heap_insert(min_heap,star)


    start.set_dist(0)
    

    while min_heap != []:
        u = heap_extract_min(min_heap)
        for e in u.adj:
            a = u.get_dist() + jump_matrix[u.index][e.index]
            if e.get_dist() > a :
                e.prev = u
                i = min_heap.index(e)
                heap_decrease_key(min_heap,i,a)
                
    Result = []
    while target.prev != None:
        Result.append(target)
        target = target.prev
    Result.append(target)
    Result.reverse()
    return Result



def min_heapify(min_heap,i):
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if l < len(min_heap) and min_heap[l].get_dist() < min_heap[smallest].get_dist():
        smallest = l
    if r < len(min_heap) and min_heap[r].get_dist() < min_heap[smallest].get_dist():
        smallest = r
    if i != smallest:
        min_heap[i],min_heap[smallest] = min_heap[smallest],min_heap[i]
        min_heapify(min_heap,smallest) 


def min_heap_insert(min_heap,node):
    min_heap.append(node)
    i = len(min_heap) - 1
    while i > 0 and min_heap[int((i-1)/2)].get_dist() > min_heap[i].get_dist():
        min_heap[int((i-1)/2)],min_heap[i] = min_heap[i],min_heap[int((i-1)/2)]
        i = int((i-1)/2)

def heap_extract_min(min_heap):
    if len(min_heap) == 1:
        return min_heap.pop()
    minElement = min_heap[0]
    min_heap[0] = min_heap.pop()
    min_heapify(min_heap,0)
    return minElement

def heap_decrease_key(min_heap,i,key):
    min_heap[i].set_dist(key)
    while i > 0 and min_heap[int((i-1)/2)].get_dist() > min_heap[i].get_dist():
        min_heap[i],min_heap[int((i-1)/2)] = min_heap[int((i-1)/2)],min_heap[i]
        i = int((i-1)/2)

    


#  DO NOT EDIT BELOW THIS LINE

#Star class
#This class represents a single vertex within the Star Map.
#Relevant Instance variables:
#   self.index: number between 0 and # of total Stars - 1.
#       Represents the index of this Star within the list/matrix
#   self.adj: a list of other Star objects to which
#       this object is adjacent (the weight of their edge is not infinity)
#   self.jump_times: a list of integers representing the edge weights
#       between this and every other Star, in order of index number.
#       So if u and v are Star objects, the weight of the edge from u to v
#       can be accessed through u.jump_times[v.index]
#   self.__dist: the .d instance variable from the textbook algorithm, representing
#       the total distance from the start node to this node.  Private, so can only be
#       accessed through getter and setter method below.
#   self.prev: previous Star in shortest path from start to here.
#
#Instance variables used only for turtle graphics:
#   self.color: what color this star will be represented as on
#       the graph.
#   self.x, self.y: where this star will be drawn on the star map.

class Star:
    def __init__(self,index,color,x,y,dist):
        self.index = index
        self.color = color
        self.adj = []
        self.jump_times = []
        self.__dist = dist
        self.x = x
        self.y = y
        self.prev = None

    #Getter and setter for the private variable __dist, which represents the
    #distance this node is from the start node.
    def set_dist(self,dist):
        self.__dist = dist
        if enable_turtle:
            self.draw(self.t)

    def get_dist(self):
        return self.__dist

    #Draw this node on the Star Map
    def draw(self,t):
        #t = turtle.Turtle()
        self.t = t
        t.hideturtle()
        t.speed(0)
        t.color(self.color)
        t.penup()
        t.setpos(self.x,self.y-15)
        t.pendown()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        if(self.color not in ["yellow","orange"]):
            t.color("white")
        else:
            t.color("black")
        if self.__dist != float("inf"):
            t.write(self.__dist,align="center",font=("Arial",20,"normal"))


        
    #Draw an edge from this node to other on the Star Map.
    #   with weight d.  path is a boolean: if False the edge is
    #   drawn normally (white), if True it's drawn cyan
    def draw_edge(self,t,other,d,path):
        if d == float("inf"):
            return
        #t = turtle.Turtle()
        t.hideturtle()
        t.fillcolor(self.color)
        t.color("white")
        t.penup()
        t.speed(1)
        dx = other.x - self.x
        dy = other.y - self.y
        dist = (dx*dx+dy*dy)**(0.5)
        sx = dx*(15/dist)
        sy = dy*(15/dist)
        startx = self.x+sx
        starty = self.y+sy
        endx = other.x-sx
        endy = other.y-sy
        halfx = (startx+endx)/2
        halfy = (starty+endy)/2
        t.pensize(2)
        if path:
            t.color("cyan")
            t.pensize(4)

        
        t.setpos(startx,starty)
        t.pendown()
        t.setpos(endx,endy)
        t.penup()
        t.setpos(halfx,halfy-10)
        t.fillcolor("black")
        t.color("black")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.color("white")
        if path:
            t.color("cyan")
        t.write(d,align="center",font=("Arial",15,"normal"))
        
    #String representation of a Star object: color:distance
    def __repr__(self):
        if self.__dist != float("inf"):
            return self.color+":"+str(self.__dist)
        else:
            return self.color
    
    #Check equality between two Star objects.
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.color == other.color

#StarMap class
#Instance variables:
#   star_list: a list of Star objects, ordered by
#       index indexber
#   jump_times: a matrix of integers representing the weight of each
#       edge in the graph.  Infinity for edges that don't exist
#   
class StarMap:
    def __init__(self,star_list,jump_times):
        self.star_list = star_list
        n = len(self.star_list)
        self.jump_times = jump_times
        for c1 in self.star_list:
            c1.jump_times = jump_times[c1.index]
            for i in range(n):
                if jump_times[c1.index][i] != float("inf"):
                    c1.adj.append(self.star_list[i])
    def draw_everything(self,t):
        for c1 in self.star_list:
            c1.draw(t)
        for c1 in self.star_list:
            for c2 in self.star_list:
                c1.draw_edge(t,c2,c1.jump_times[c2.index],False)

#Test case
i = float("inf")

def make_star_list(n):
    red = Star(0,"red",-256, 23,float("inf"))
    orange = Star(1,"orange",265, -70,float("inf"))
    yellow = Star(2,"yellow",12,215,float("inf"))
    green = Star(3,"green",68,12,float("inf"))
    blue = Star(4,"blue",-180,189,float("inf"))
    indigo = Star(5,"brown",141,-96,float("inf"))
    violet = Star(6,"purple",-73,-153,float("inf"))
    full_list = [red,orange,yellow,green,blue,indigo,violet]
    return full_list[:n]
    

star_list1 = make_star_list(2)
jump_times = [[i,2],
             [2,i]]
star_map1 = StarMap(star_list1,jump_times)

star_list2 = make_star_list(3)
jump_times = [[i,5,2],
             [5,i,2],
             [2,2,i]]
star_map2 = StarMap(star_list2,jump_times)

star_list3 = make_star_list(4)
jump_times = [[i,i,3,2],
             [i,i,1,4],
             [3,1,i,i],
             [2,4,i,i]]
star_map3 = StarMap(star_list3,jump_times)

star_list4 = make_star_list(5)
jump_times = [[i,7,2,3,i],
             [7,i,6,12,4],
             [2,6,i,i,3],
             [3,12,i,i,1],
             [i,4,3,1,i]]
star_map4 = StarMap(star_list4,jump_times)
        
star_list5 = make_star_list(6)
jump_times = [[i,i,i,11,2,16],
             [i,i,13,4,i,1],
             [i,13,i,5,3,12],
             [11,4,5,i,7,2],
             [2,i,3,7,i,i],
             [16,1,12,2,i,i]]
star_map5 = StarMap(star_list5,jump_times)

star_list6 = make_star_list(7)
jump_times = [[i,26,9,i,i,i,2],
             [26,i,i,i,i,8,i],
             [9,i,i,9,4,6,i],
             [i,i,9,i,1,i,i],
             [i,i,4,1,i,5,6],
             [i,8,6,i,5,i,17],
             [2,i,i,i,6,17,i]]
star_map6 = StarMap(star_list6,jump_times)


star_lists = [star_list1,star_list2,star_list3,
       star_list4,star_list5,star_list6]
star_maps = [star_map1,star_map2,star_map3,star_map4,star_map5,star_map6]
time_limit = [2,4,4,7,12,21]
correct = [[Star(0,"red",-256, 23,0),
            Star(1,"orange",265, -70,2)],
           [Star(0,"red",-256, 23,0),
            Star(2,"yellow",12,215,2),
            Star(1,"orange",265, -70,4)],
           [Star(0,"red",-256, 23,0),
            Star(2,"yellow",12,215,3),
            Star(1,"orange",265, -70,4)],
           [Star(0,"red",-256, 23,0),
            Star(1,"orange",265, -70,7)],
           [Star(0,"red",-256, 23,0),
            Star(4,"blue",-180,189,2),
            Star(3,"green",68,12,9),
            Star(5,"brown",141,-96,11),
            Star(1,"orange",265, -70,12)],
           [Star(0,"red",-256, 23,0),
            Star(6,"purple",-73,-153,2),
            Star(4,"blue",-180,189,8),
            Star(5,"brown",141,-96,13),
            Star(1,"orange",265, -70,21)]]

#Run test cases, check whether final MST correct
count = 0

def draw_counter(t,i,color):
    t.penup()
    t.setpos(-100+i*10,-225)
    t.color(color)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

time_counter = None
empire_ship = None
cyan_turtle = None
draw_turlte = None
if enable_turtle:
    time_counter = turtle.Turtle()
    empire_ship = turtle.Turtle()
    cyan_turtle = turtle.Turtle()
    draw_turtle = turtle.Turtle()

def to_time_list(star, adj, mat):
    st = ""
    for star2 in adj:
        st += star2.color + "("
        st += str(mat[star.index][star2.index]) + ")"
        st += ", "
    return st[:-2]

try:
    for i in range(len(correct)):
        print("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Star list", star_lists[i],'\n')
        if enable_turtle:
            turtle.resetscreen()

            turtle.bgcolor("black")
            turtle.delay(0)
            turtle.tracer(0,0)
            star_maps[i].draw_everything(draw_turtle)
            
                 
            empire_ship.hideturtle()
            empire_ship.color("gray")
            empire_ship.penup()
            empire_ship.setpos(star_lists[i][1].x,star_lists[i][1].y)
            empire_ship.pendown()
            empire_ship.setpos(star_lists[i][1].x,star_lists[i][1].y+30)
            empire_ship.right(90)
            empire_ship.showturtle()

            time_counter.hideturtle()
            time_counter.penup()
            time_counter.setpos(-150,-235)
            time_counter.color("yellow")
            time_counter.write("Time left:",align='center',font=('Arial',15,'normal'))
        
            for j in range(time_limit[i]):
                draw_counter(time_counter,j,"yellow")

            cyan_turtle.hideturtle()
            cyan_turtle.color("cyan")
            cyan_turtle.shape("turtle")
            cyan_turtle.penup()
            cyan_turtle.setpos(star_lists[i][0].x,star_lists[i][0].y)
            cyan_turtle.showturtle()
            turtle.update()
            time.sleep(draw_delay*2)
        else:
            print("Jump Times (Edge Weights):")
            print("Format:")
            print("Source Star: Destination1(Weight), Desintation2(Weight), etc.\n")
            for star in star_lists[i]:
                print(star.color+": "+to_time_list(star,star.adj,star_maps[i].jump_times))
            print()
        route = hyperspace_jump_route(star_lists[i],star_maps[i].jump_times)
        route_queue = list(route)
        time_left = time_limit[i]
        to_next = 0
        jump_len = 0
        next_star = star_lists[i][0]

        print("Expected:",correct[i],"\nGot     :",route)
        
        assert len(route) > 1, "Route must have length at least 2"
        assert next_star == route_queue.pop(0), "Route must start at red star"
        if enable_turtle:
            
            while time_left > 0:
                assert (route_queue != [] or to_next != 0), "Route ended before destination reached"
                if to_next == 0:
                    prev_star = next_star
                    next_star = route_queue.pop(0)
                    jump_len = prev_star.jump_times[next_star.index]
                    
                    if jump_len == float("inf"):
                        prev_star.draw_edge(draw_turtle,next_star,"inf",True)
                    else:
                        prev_star.draw_edge(draw_turtle,next_star,jump_len,True)
                    to_next = jump_len
                if jump_len != 0:
                    assert jump_len < float("inf"), "No hyperspace link to next jump point"
                    to_next -= 1
                    time_left -= 1
                    draw_counter(time_counter,time_left,"gray")
                    xpos = (prev_star.x*to_next+next_star.x*(jump_len-to_next))/jump_len
                    ypos = (prev_star.y*to_next+next_star.y*(jump_len-to_next))/jump_len
                    cyan_turtle.setpos(xpos,ypos)
                    turtle.update()
                    time.sleep(draw_delay)
                    
            if next_star != star_lists[i][1] or to_next != 0:
                star_lists[i][1].color = "black"
                star_lists[i][1].set_dist(star_lists[i][1].get_dist())
                assert False, "Ran out of time, base assimilated"
            else:
                empire_ship.hideturtle()
                empire_ship.color("cyan")
                empire_ship.penup()
                empire_ship.setpos(star_lists[i][1].x,star_lists[i][1].y)
                empire_ship.pendown()
                empire_ship.setpos(star_lists[i][1].x,star_lists[i][1].y+30)
                empire_ship.showturtle()
            turtle.update()
            time.sleep(draw_delay*2)
        assert correct[i] == route, "Final path incorrect"
        
        
        #assert star_maps[i].tree == correct[i], "Tree incorrect"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)

except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(correct),"tests passed.")




