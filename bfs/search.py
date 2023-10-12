#search
import state
import frontier

def search(n):
    s=state.create(n)
    f=frontier.create(s)
    removed, inserted = 0, 0
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        removed += 1
        if state.is_target(s):
            return s,removed,inserted
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
            inserted += 1
    return 0

import time
for s in range(2,4):
    depth = 0
    insertions = 0
    removals = 0
    start = time.time()
    for i in range(100):
        a,b,c = search(s)
        depth += len(a[0])
        insertions += b
        removals += c
    end = time.time()
    print(f"search({s})")
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
    a,b,c = search(s)
    end = time.time()
    depth += len(a[0])
    insertions += b
    removals += c
    print(f"Depth: {depth}")
    print(f"Insertions: {insertions}")
    print(f"Removals: {removals}")
    print(f"Time: {end - start}")
    print()

inner()

"""
Output:

search(2)
Depth: 4.0
Insertions: 3.73
Removals: 3.52
Time: 0.002954244613647461

search(3)
Depth: 9.0
Insertions: 174.74
Removals: 297.98
Time: 0.08478069305419922

search(4)
Depth: 16
Insertions: 49705
Removals: 105875
Time: 0.30716633796691895
"""