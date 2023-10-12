#search

import state
import frontier

def search(n):
    s=state.create(n)
    # print(s)
    f=frontier.create(s)
    removed, inserted = 0, 0
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        removed += 1
        if state.is_target(s):
            return f[1], removed, inserted
        ns=state.get_next(s)
        #print(ns)
        for i in ns:
            frontier.insert(f,i)
            inserted += 1
    return 0

import time
for s in range(2,4):
    depth = 0
    insertions = 0
    removals = 0
    print(f"search({s})")
    start = time.time()
    for i in range(100):
        a,b,c = search(s)
        depth += a
        insertions += b
        removals += c
    end = time.time()
    print(f"Depth: {depth/100}")
    print(f"Insertions: {insertions/100}")
    print(f"Removals: {removals/100}")
    print(f"Time: {end - start}")
    print()

def inner():
    s = 4
    depth = 0
    insertions = 0
    removals = 0
    print(f"search({s})")
    start = time.time()
    for i in range(1):
        a,b,c = search(s)
        depth += a
        insertions += b
        removals += c
    end = time.time()
    print(f"Depth: {depth/1}")
    print(f"Insertions: {insertions/1}")
    print(f"Removals: {removals/1}")
    print(f"Time: {end - start}")
    print()

inner()

"""
Output:

search(2)
Depth: 1.76
Insertions: 6.49
Removals: 7.11
Time: 0.003513336181640625

search(3)
Depth: 6.56
Insertions: 730.07
Removals: 1270.23
Time: 0.3583104610443115

search(4)
Depth: 15.0
Insertions: 278966.0
Removals: 594165.0
Time: 1.4511034488677979
"""