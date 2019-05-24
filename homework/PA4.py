import traceback

#For this assignment, you will be implementing a max-heap as a simple Python
#list.  You don't need to create a separate heap_size variable, just use
#.append every time you want to add things to the end of the list, or .pop()
#to remove the last element of the list.


#NOTE: max_heap_insert is a bit different than the textbook implementation
#Rather than taking as an argument a key, it takes as an argument the
#Task object you want to input.  Since heap_increase_key still works
#on a numerical key, you'll need to be careful that you're actually
#putting a new Task into the heap and not just overwriting an existing
#Task's priority number.
    
#Takes as input a heap (list) of Task objects task_heap, and a Task object task.
#Inserts task into the heap task_heap, while maintaining the
#  max-heap property.

def max_heapify(task_heap,i):
    l=2*i
    r=2*i+1
    if l <= len(task_heap)-1 and task_heap[l-1].priority>task_heap[i-1].priority:
        largest=l
    else:
        largest=i 
    
    if r <= len(task_heap)-1 and task_heap[r-1].priority>task_heap[largest-1].priority:
        largest=r

    if largest != i:
        task_heap[i-1],task_heap[largest-1]=task_heap[largest-1],task_heap[i-1]
        max_heapify(task_heap,largest)


def insert_task(task_heap,task):
    task_heap.append(task)
    increase_task_priority(task_heap,len(task_heap)-1,task.priority)
    
    
#Takes as input a heap (list) consisting of Task objects, task_heap
#Removes the Task of highest priority from the heap, and returns it.
#Returns None (without throwing an error) if the heap contains no Tasks
def extract_max_priority_task(task_heap):
    if len(task_heap)<1:
        return
    
    max_=task_heap[0]
    task_heap[0]=task_heap[len(task_heap)-1]
    task_heap.pop()
    max_heapify(task_heap,1)
    return max_


            
#Takes as input a heap (list) of Task objects task_heap, an index of that
#  heap i, and a number new_priority.
#Increases the priority of the Task at index i within heap task_heap
#  to new_priority, and adjusts the heap accordingly to
#  maintain the max-heap property.
#Immediately returns None if new_priority is less than the
#  target Task's current priority, without throwing an error.
def increase_task_priority(task_heap,i,new_priority):
    i=i+1
    if new_priority <task_heap[i-1].priority:
        return
    task_heap[i-1].priority=new_priority
    while i > 1 and task_heap[i//2-1].priority < task_heap[i-1].priority:
        task_heap[(i//2)-1], task_heap[i-1]=task_heap[i-1], task_heap[(i//2)-1]
        i=i//2


#  DO NOT EDIT BELOW THIS LINE
        

#Task class
#Each task has two instance variables:
#   self.description is a string describing what the task is
#   self.priority is a number representing the importance of the
#      task (higher values are more important)
class Task:
    def __init__(self,description,priority):
        self.description = description
        self.priority = priority
    def __repr__(self):
        return "\n{:5}:{}".format(str(self.priority),self.description)
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.description == other.description and \
               self.priority == other.priority



#Test cases:
    
t1 = Task("'Accidentally' run into love interest",76)
t2 = Task("Brood over inner darkness",61)
t3 = Task("Lunch with Powerdude and Megagal",61)
t4 = Task("Pick up Laundry",89)
t5 = Task("Go to boring normal job as alter-ego",65)
t6 = Task("Comic relief with useless sidekick",1)
t7 = Task("Help clean up collateral damage",84)
t8 = Task("Receive key to city",33)
t9 = Task("Prevent bank robbery",96)
t10 = Task("Training montage",46)

t11 = Task("Take a nap",20)
t12 = Task("Defeat King Explosion Murder", 20)
t13 = Task("Walk Ultradog the Annhilator", 20)
t14 = Task("Escape elaborate deathtrap", 97)
t15 = Task("Respond to fanmail",16)

#Duplicate objects, in case originals corrupted by student code
d1 = Task("'Accidentally' run into love interest",76)
d2 = Task("Brood over inner darkness",61)
d2updated = Task("Brood over inner darkness",90)
d3 = Task("Lunch with Powerdude and Megagal",61)
d4 = Task("Pick up Laundry",89)
d5 = Task("Go to boring normal job as alter-ego",65)
d6 = Task("Comic relief with useless sidekick",1)
d7 = Task("Help clean up collateral damage",84)
d8 = Task("Receive key to city",33)
d9 = Task("Prevent bank robbery",96)
d10 = Task("Training montage",46)

d11 = Task("Take a nap",20)
d12 = Task("Defeat King Explosion Murder", 20)
d13 = Task("Walk Ultradog the Annhilator", 20)
d13updated = Task("Walk Ultradog the Annhilator", 30)
d14 = Task("Escape elaborate deathtrap", 97)
d15 = Task("Respond to fanmail",16)

count = 0



funcs = [insert_task,insert_task,insert_task,insert_task,insert_task,
         insert_task,extract_max_priority_task,increase_task_priority,
         insert_task,insert_task,extract_max_priority_task,
         extract_max_priority_task,insert_task,extract_max_priority_task,
         insert_task,extract_max_priority_task,
         extract_max_priority_task,insert_task,insert_task,
         increase_task_priority,increase_task_priority,
         extract_max_priority_task,insert_task,extract_max_priority_task]


day1_tasks = []
day2_tasks = []
params1 = [day1_tasks,t8]
params2 = [day1_tasks,t2]
params3 = [day1_tasks,t3]
params4 = [day1_tasks,t10]
params5 = [day1_tasks,t6]
params6 = [day1_tasks,t5]
params7 = [day1_tasks]
params8 = [day1_tasks,2,90]
params9 = [day1_tasks,t9]
params10 = [day1_tasks,t4]
params11 = [day1_tasks]
params12 = [day1_tasks]
params13 = [day1_tasks,t7]
params14 = [day1_tasks]
params15 = [day2_tasks,t11]
params16 = [day2_tasks]
params17 = [day2_tasks]
params18 = [day2_tasks,t12]
params19 = [day2_tasks,t13]
params20 = [day2_tasks,1,10]
params21 = [day2_tasks,1,30]
params22 = [day2_tasks]
params23 = [day2_tasks,t14]
params24 = [day2_tasks]




func_params = [params1,params2,params3,params4,params5,params6,params7,
               params8,params9,params10,params11,params12,params13,
               params14,params15,params16,params17,params18,params19,
               params20,params21,params22,params23,params24]



corr_heap1 = [d8]
corr_heap2 = [d2,d8]
corr_heap3 = [d2,d8,d3]
corr_heap4 = [d2,d10,d3,d8]
corr_heap5 = [d2,d10,d3,d8,d6]
corr_heap6 = [d5,d10,d2,d8,d6,d3]
corr_heap7 = [d3,d10,d2,d8,d6]
corr_heap8 = [d2updated,d10,d3,d8,d6]
corr_heap9 = [d9,d10,d2updated,d8,d6,d3]
corr_heap10 = [d9,d10,d2updated,d8,d6,d3,d4]
corr_heap11 = [d2updated,d10,d4,d8,d6,d3]
corr_heap12 = [d4,d10,d3,d8,d6]
corr_heap13 = [d4,d10,d7,d8,d6,d3]
corr_heap14 = [d7,d10,d3,d8,d6]
corr_heap15 = [d11]
corr_heap16 = []
corr_heap17 = []
corr_heap18 = [d12]
corr_heap19 = [d12,d13]
corr_heap20 = [d12,d13]
corr_heap21 = [d13updated,d12]
corr_heap22 = [d12]
corr_heap23 = [d14,d12]
corr_heap24 = [d12]



corr_heaps = [corr_heap1,corr_heap2,corr_heap3,corr_heap4,corr_heap5,
              corr_heap6,corr_heap7,corr_heap8,corr_heap9,corr_heap10,
              corr_heap11,corr_heap12,corr_heap13,corr_heap14,corr_heap15,
              corr_heap16,corr_heap17,corr_heap18,corr_heap19,corr_heap20,
              corr_heap21,corr_heap22,corr_heap23,corr_heap24]
corr_outs = [None,None,None,None,None,None,d5,None,None,None,
             d9,d2updated,None,d4,None,d11,None,None,None,None,
             None,d13updated,None,d14]

def call_function(func,params,corr_heap,corr_output=None):
    if func == insert_task:
        print("Inserting task:",params[1])
        func(params[0],params[1])
    elif func == extract_max_priority_task:
        print("Epicperson seeks a task to complete!")
        print("Extracting maximum priority task:")
        out = func(params[0])
        print("Expected:",corr_output,"\n\nGot:",out)
        assert out == corr_output, "Extract max output incorrect"
    else:
        print("Increasing priority of",params[0][params[1]],"\nto",params[2])
        func(params[0],params[1],params[2])
    print("\nExpected Heap:",corr_heap,"\n\nGot:",params[0])
    assert params[0] == corr_heap, "Heap incorrect"



try:
    print("Day 1: Initial Task Queue Empty")
    for i in range(14):
        print("\n---------------------------------------\n")
        print("TEST #",i+1,":")
        call_function(funcs[i],func_params[i],corr_heaps[i],corr_outs[i])
        count = count + 1
    print("\n Day 1 Complete.\n")
    print("\n Day 2: Initial Task Queue Empty")
    for i in range(14,24):
        print("\n---------------------------------------\n")
        print("TEST #",i+1,":")
        call_function(funcs[i],func_params[i],corr_heaps[i],corr_outs[i])
        count = count + 1
except AssertionError as e:
    print("\nFAIL: ", e)
except Exception:
    print("\nFAIL: ", traceback.format_exc())

    


print(count,"out of 24 tests passed.")


