from math import gcd 


def brute_force(bus_ids):
    #small optimization: use largest bus id as basis for search to increment faster
    bus_ids = sorted(bus_ids, key=lambda x: x[0], reverse=True)

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

def lcm(nums):
    lcm = nums[0]
    for i in range(1, len(nums)):
        y = nums[i]
        lcm = (lcm * y) // gcd(lcm, y)
    return lcm 

def main(bus_ids):
    aligned = [bus_ids[0][0]]
    base_index = bus_ids[0][1]
    timestamp = 0
    while len(aligned) < len(bus_ids):
        #print(timestamp)
        timestamp += lcm(aligned)
        for id, offset in bus_ids:
            if id not in aligned:
                if (timestamp + offset) % id == 0:
                    aligned.append(id) 
    return timestamp

if __name__ == "__main__":
    f = open("data1.txt", "r")
    earliest_time = int(f.readline().rstrip('\n'))
    ids = f.readline().split(',')
    bus_ids = [(int(id.rstrip('\n')),i) for i,id in enumerate(ids) if id != 'x']
    #ans = brute_force(bus_ids)
    ans = main(bus_ids)
    print(ans)