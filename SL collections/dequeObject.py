import collections

q = collections.deque([5,10,15,20,25])



q.appendleft(0)
q.append(30)
print(q)

q.pop()
q.popleft()
print(q)

