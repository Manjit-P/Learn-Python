# Understanding double ended queue.

from collections import deque

dq = deque(range(10), maxlen=10) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(4) # deque([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], maxlen=10)
dq.rotate(-3) # deque([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], maxlen=10)
dq.append(0) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 0], maxlen=10)
             # maxlength is 10 so it will overwrite last element.
dq.appendleft(11) # deque([11, 1, 2, 3, 4, 5, 6, 7, 8, 0], maxlen=10)
dq.extend([12, 13, 14]) # deque([11, 1, 2, 3, 4, 5, 6, 12, 13, 14], maxlen=10)
dq.extendleft([15, 16, 17]) # deque([12, 16, 17, 3, 4, 5, 6, 7, 8, 0], maxlen=10)
print(dq)