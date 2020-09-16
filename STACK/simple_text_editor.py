# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    t = int(input().strip())
    history = []
    currentstring = ""
    for _ in range(t):
        val = input().strip().split()
        if val[0] == '1':
            string = str(val[1])
            currentstring += string
            history.append([val[0], len(val[1])])

        elif val[0] == '2':
            cont = int(val[1])
            delete = currentstring[-cont:]
            currentstring = currentstring[:-cont] 
            history.append([val[0], delete])

        elif val[0] == '3':
            i = int(val[1])
            print(currentstring[i-1])

        elif val[0] == '4':
            undo = history.pop()
            if undo[0] == '1':
                currentstring = currentstring[:-int(undo[1])]
    
            elif undo[0] == '2':
                currentstring += undo[1]
