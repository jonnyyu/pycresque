from pycresque import Cresque

q = Cresque(host='localhost', port=6379)

for i in range(5):
    q.enqueue('math', 'add', [1,i])
