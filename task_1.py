from queue import Queue 
import random
from lists import Authors, RequestTitles

class Request:
    def __init__(self, title = None, author = None):
        
        if not title:
            title = RequestTitles[random.randint(0, len(RequestTitles) - 1)]
            
        if not author:
            author = Authors[random.randint(0, len(Authors) - 1)]
        
        self.title = title
        self.author = author
        self.number = AutoNumber.get_number()
    
    def __str__(self) -> str:
        return f"Request #: {self.number} from {self.author} about {self.title}"



    
queue = Queue()
    
class AutoNumber:
    
    number = 0
        
    def get_number():
        AutoNumber.number += 1
        return "{:0>5}".format(AutoNumber.number)
    
    
def generate_request(title: str = None, author: str = None):
    request = Request(title, author)
    queue.put(request)
    
    print(f"Add new request {request}")
    
def process_request():
    if not queue.empty():
        processed_request = queue.get()
        print(f"Processed: {processed_request}")
    else:
        print("Queue is empty")

print("Start queue demo...")
print("Press Ctrl+C to exit")
    
while True:
    
    qty = int(input("Number of requests to generate: "))
    
    for i in range(0, qty):
        generate_request()
        
    print()
    print("Process random number of requests")
    
    for i in range(1, random.randrange(2, 10)):
        process_request()
    
    print()
    print(f"In queue requests: {queue.qsize()}")
    print()
    