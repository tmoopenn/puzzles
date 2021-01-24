def main(bus_ids, earliest_time):
    best_time = float('inf')
    best_id = None
    for id in bus_ids:
        prev_time = ((earliest_time-1) // id ) * id
        next_time = prev_time + id
        if next_time < best_time:
            best_time = next_time
            best_id = id
    return (best_time - earliest_time) * best_id
        

if __name__ == "__main__":
    f = open("sample.txt", "r")
    earliest_time = int(f.readline().rstrip('\n'))
    ids = f.readline().split(',')
    bus_ids = [int(id.rstrip('\n')) for id in ids if id != 'x']
    ans = main(bus_ids, earliest_time)
    print(ans)