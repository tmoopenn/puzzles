#optimization: use largest bus id as basis for search to increment faster
def brute_force(bus_ids):
    t = curr_t = bus_ids[0][0]
    base_index = bus_ids[0][1]
    found_t = False 
    m = 1 
    vals = bus_ids[1:]
    while not found_t:
        a_t = curr_t * m 
        #print(a_t)
        divisble = True
        for id, offset in vals:
            if offset > base_index:
                val = a_t + offset 
            else:
                val = a_t - offset
            if val % id != 0:
                divisble = False 
                break 
        if divisble:
            found_t = True
        m += 1 
    return a_t

#ideas 
# binary-type search 
# use largest value as search basis 

if __name__ == "__main__":
    f = open("sample.txt", "r")
    earliest_time = int(f.readline().rstrip('\n'))
    ids = f.readline().split(',')
    bus_ids = [(int(id.rstrip('\n')),i) for i,id in enumerate(ids) if id != 'x']
    bus_ids = sorted(bus_ids, key=lambda x: x[0], reverse=True)
    print(bus_ids)
    ans = brute_force(bus_ids)
    print(ans)