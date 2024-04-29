from collections import deque 

def is_palindrom(row: str):
    
    queue = deque(row.lower().replace(" ", ""))
    
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

print("Start palindrom checker...")
print("Press Ctrl+C to exit")

while True:

    input_str = input("Enter the string: ")
    print(f"Is palindrom: {is_palindrom(input_str)}")