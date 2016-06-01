
import collections
# You can enqueue lists
dq = collections.deque([1, 2, 3, 4, 5])
print(dq)
# and string literals
dq = collections.deque('abcdefg')
print(dq)

# Iterable
for i in dq:
    print(i)

# Supports many methods

# Count number of times search term appears in queue
print(dq.count('a'))
# Add items to the right of the queue
dq.extend([1, 2, 3, 4, 5])
print(dq)
# Add items to the left of the queue
dq.extendleft('!@#$%')
print(dq)
# Insert item at index x
dq.insert(5, '5th place')
print(dq)
# Return index of first match from search term (option range argument for start/stop of index)
print(dq.index('g'))  # ('d', 0, 10)

dq = collections.deque([1, 2, 3])
print(dq)
# reverse queue, does not return anything
dq.reverse()
print(dq)
# remove and return element from the right
print(dq.pop())
print(dq)
# Remove and return element from the left
print(dq.popleft())
print(dq)
# Remove first match of specified value
dq.remove(2)
print(dq)

dq = collections.deque('-*-')
print(dq)
# Rotate elements right x spaces, or left -x spaces
dq.rotate(1)
print(dq)