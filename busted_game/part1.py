
def main():
    f = open("data1.txt", "r")
    lines = f.readlines()
    num_lines = len(lines)
    visited = set() 
    total = 0 
    index = 0 
    loop = False 
    visited.add(0)
    while not loop: 
        line = lines[index]
        cmd, val = line.split()
        val = int(val)
        if cmd == "acc":
            total += val
            index += 1  
        elif cmd == "jmp":
            index = (index + val) % num_lines 
        else: # nop 
            index += 1 
        if index not in visited:
            visited.add(index)
        else:
            loop = True
    print(total)
    return total 

if __name__ == "__main__":
    main()
    