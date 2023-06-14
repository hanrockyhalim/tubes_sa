from queue import PriorityQueue
  
q = PriorityQueue()
  
# insert into queue
q.put((2, 'g'))
q.put((3, 'e'))
q.put((4, 'k'))
q.put((5, 's'))
q.put((1, 'e'))
q.put((2, 'f'))
  
# remove and return 
# lowest priority item
print(q.get())
print(q.get())
print(q.get())
print(q)
  
# check queue size
print('Items in queue :', q.qsize())
  
# check if queue is empty
print('Is queue empty :', q.empty())
  
# check if queue is full
print('Is queue full :', q.full())