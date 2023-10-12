#search

import state
import frontier

def search(n):
    inserte, remove = 0, 0
    s=state.create(n)
    # print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        remove += 1
        if state.is_target(s):
            return [s, f[1]], inserte, remove
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
            inserte += 1
    return 0
removes, inserts, total_cost = 0, 0, 0
import time
for s in range(2,5):
    start = time.time()
    for i in range(100):
        a, b, c = search(s)
        removes+=c
        inserts+=b
        total_cost+= len(a[0][1])
    end = time.time()
    print(f"search({s})")
    print(f"Depth: {total_cost/100}")
    print(f"Inserts: {inserts/100}")
    print(f"Removals: {removes/100}")
    print(f"Time: {(end - start)/100}")
    print()

"""

Output:
Uniform:
search(2)
Depth: 1.0
Inserts: 3.0
Removals: 3.0
Time: 6.890296936035156e-05

search(3)
Depth: 5.0
Inserts: 53.0
Removals: 31.0
Time: 0.00044536590576171875



H1:

search(3)
Depth: 6.0
Inserts: 13.0
Removals: 8.0
Time: 0.00011944770812988281

search(4)
Depth: 23.0
Inserts: 2210.0
Removals: 1045.0
Time: 0.15645942687988281

H2:
search(2)
Depth: 1.58
Inserts: 2.48
Removals: 2.65
Time: 2.1545886993408204e-05

search(3)
Depth: 7.72
Inserts: 29.16
Removals: 18.2
Time: 0.0006533622741699219

search(4)
Depth: 24.49
Inserts: 1746.16
Removals: 877.29
Time: 0.13814905166625976


"""