import random, sys, time

WIDTH = 70 # Number of columns

try: 
    columns = [0] * WIDTH
    while True:
    # Loop over each column:
        for i in range(WIDTH):
            # Each columns will have 2% chance to be chosen for stream.
            if random.random() < 0.02:
                # Decides how many times 0 and 1 will print.
                columns[i] = random.randint(4, 14) 

            if columns[i] == 0:
                print(' ', end='')
            else:
                print(random.choice([0, 1]), end='')
                columns[i] -= 1
        print() # prints new line after each complete sequence of 0 and 1.
        time.sleep(0.3) # Each row pause for 0.3 second.
except KeyboardInterrupt:
    sys.exit() # runs until CTRL+C is pressed.