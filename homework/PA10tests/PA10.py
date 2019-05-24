import traceback

#huffman_encode: Takes in a single String input_string, which is
# the string to be encoded.  Computes the optimal binary encoding
# of the string and encodes it, returning a String of 0s and 1s.
# This is not an actual Python binary string, just a normal String
# that happens to contain only 0s and 1s.
def huffman_encode(input_string):
    

    #TODO: Complete this function
    dictionary = {}
    min_heap = []
    for char in input_string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    for char in dictionary:
        min_heap_insert(min_heap,Node(char,dictionary[char]))

    i=0
    lens=len(min_heap)-1
    while i <lens:
        low_first = heap_extract_min(min_heap)
        low_second = heap_extract_min(min_heap)
        new_node = Node(low_first.char + low_second.char, low_first.frequency + low_second.frequency)
        new_node.left = low_first
        new_node.right = low_second
        min_heap_insert(min_heap, new_node)
        i+=1
        


    code = ""
    for char in input_string:
        node = new_node
        while (char != node.char):
            if (char in node.left.char):
                node = node.left
                code = code + "0"
            else: 
                node = node.right
                code = code + "1"

    return code
    
class Node:
    def __init__(self,char,frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

def min_heapify(min_heap,i):
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if l < len(min_heap) and min_heap[l].frequency < min_heap[smallest].frequency:
        smallest = l
    if r < len(min_heap) and min_heap[r].frequency < min_heap[smallest].frequency:
        smallest = r
    if i != smallest:
        min_heap[i],min_heap[smallest] = min_heap[smallest],min_heap[i]
        min_heapify(min_heap,smallest)
        
    
def heap_extract_min(min_heap):
    if len(min_heap) == 1:
        return min_heap.pop()
    minElement = min_heap[0]
    min_heap[0] = min_heap.pop()
    min_heapify(min_heap,0)
    return minElement

def min_heap_insert(min_heap,node):
    min_heap.append(node)
    i = len(min_heap) - 1
    while i > 0 and min_heap[int((i-1)/2)].frequency > min_heap[i].frequency:
        min_heap[int((i-1)/2)],min_heap[i] = min_heap[i],min_heap[int((i-1)/2)]
        i = int((i-1)/2)


    


#  DO NOT EDIT BELOW THIS LINE

tests = ['message0.txt','message1.txt','message2.txt','message3.txt',
         'message4.txt','message5.txt']
correct = ['message0encoded.txt','message1encoded.txt',
           'message2encoded.txt','message3encoded.txt',
           'message4encoded.txt','message5encoded.txt']


#Run test cases, check whether encoding correct
count = 0

try:
    for i in range(len(tests)):
        ("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Reading message from:",tests[i])
        fp = open(tests[i])
        message = fp.read()
        fp.close()
        print("Reading encoded message from:",correct[i])
        fp2 = open(correct[i])
        encoded = fp2.read()
        fp2.close()
        output = huffman_encode(message)
        if i < 5:
            print("Running: huffman_encode on '"+message+"'\n")
            print("Expected:",encoded,"\nGot     :",output)
        assert encoded == output, "Encoding incorrect!"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(tests),"tests passed.")


