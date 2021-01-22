def main():
    f = open("data1.txt", "r")
    lines = f.readlines()
    num_lines = len(lines)
    def do_func(cmd, val, index, total):
        val = int(val)
        if cmd == "acc":
            total += val
            index += 1  
        elif cmd == "jmp":
            index = (index + val) #% num_lines 
        else: # nop 
            index += 1 
        return index, total 
    
    def run(index, total, visited, num_changes):
        #print(index, total)
        if index == num_lines: # Success 
            return True, total
        if index in visited: # Failure 
            return False, total  
        success, acc = False, 0
        cmd, val = lines[index].split()

        # can make a change, optimistically change cmd if is jmp or nop
        if num_changes == 0: 
            if cmd != "acc": 
                cpy = visited.copy()
                cpy.add(index)
                mod_cmd = "jmp" if cmd == "nop" else "nop"
                idx, t = do_func(mod_cmd, val, index, total)
                success, acc = run(idx, t, cpy, num_changes+1)

        # if success is false, the path we executed ended in a cycle
        # we backtrack i.e. execute line as is     
        if not success: 
            cpy = visited.copy()
            cpy.add(index)
            index, total = do_func(cmd, val, index, total)
            return run(index, total, cpy, num_changes)
        return success, acc
 
    res, val = run(0, 0, set(), 0)
    print(res, val)

if __name__ == "__main__":
    main()