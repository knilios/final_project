import time

print("Counting down:")
for i in range(9, 0, -1):
    print(i, end='\r')
    time.sleep(1)
print("Blast off!")

import os

# clear the console screen
os.system('cls' if os.name == 'nt' else 'clear')