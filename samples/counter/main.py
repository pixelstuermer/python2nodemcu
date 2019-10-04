import time

SLEEP = 1.0
counter = 0

while True:
    counter += 1
    print("Iteration # " + str(counter))
    time.sleep(SLEEP)
