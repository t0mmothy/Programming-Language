import os, sys, time, random
global assi
assi = [] # Assigned numbers

def assign(line):
    num = ""
    count = 1
    while True:
        # Get a single charcter
        char = line[count]
        # If charcter is a line end then break out of loop
        if char == ";":
            break
        
        else:
            # Check if char is a number if not throw an error and quit
            if int(char) in [0,1,2,3,4,5,6,7,8,9]:
                num += char
                
            else:
                print(f"[ERROR] Invalid assignnment on line {count}")
                print(f"""|
V
[ERROR] Number not detected instead found {char}""")
                input()
                quit()



        count += 1
    # change number into a actual number
    num = int(num)
    return num

def ret(line, count):
    global assi
    num = ""
    Rcount = count 
    while True:
        # Get a single charcter
        char = line[Rcount]
        # If charcter is a line end then break out of loop
        if char == "^":
            break
        
        else:
            # Check if char is a number if not throw an error and quit
            try:
                int(char)
                INTable = True
            except:
                INTable = False
                    
            if INTable:
                if int(char) <= len(assi):
                    num += str(assi[int(char)])
                else:
                    print(f"[ERROR] Retrieval out of bounds: attempted retrieval - {int(char)}, assignment order length - {len(assi)}")
                    input()
                    quit()
                
            else:
                print(f"[ERROR] Invalid assignnment on line {Rcount}")
                print(f"""|
V
[ERROR] Number not detected instead found {char}""")
                input()
                quit()
        Rcount += 1
    num = int(num)
    return [num, len(list(str(num)))]

def asc(line):
    strgn = ""
    count = 2
    while True:
        # Get a single charcter
        char = line[count]
        # If charcter is a line end then break out of loop
        if char == "^":
            break
        
        else:
            # Check if char is a number if not throw an error and quit
            if char == "r":
                #count += 1
                num = ret(line, count)

                try:
                    int(char)
                    INTable = True
                except:
                    INTable = False
                    
                if INTable:
                    strng += num
                    #count -= 1
                
                else:
                    print(f"[ERROR] Invalid assignnment on line {count}")
                    print(f"""|
V
[ERROR] Number not detected instead found {char}""")
                    input()
                    quit()

            else:
                try:
                    int(char)
                    INTable = True
                except:
                    INTable = False
                    
                if INTable:
                    strgn += char
                
                else:
                    print(f"[ERROR] Invalid assignnment on line {count}")
                    print(f"""|
V
[ERROR] Number not detected instead found {char}""")
                    input()
                    quit()

        count += 1
    return [chr(int(strgn)), len(strgn)]


def output(line):
    otp = ""
    count = 0
    while True:
        # Get a single charcter
        char = line[count]

        # Check for line end
        if char == ";":
            break

        # Check for commands like 'r' or 'a' for retrievals or ascii's
        if char == "r":
            num = ret(line, 0)
            otp += str(num[0])
            count += num[1]

        elif char == "a":
            strng = asc(line)
            otp += strng[0]
            count += strng[1]

        else:
            try:
                int(char)
                INTable = True
            except:
                INTable = False
                
            if INTable:
                otp += char

        count += 1

    return otp










## Open file and read contents
#file = sys.argv[1] # Umake as comment later
file = 'example.pl'
with open(file, "r") as filehandle:
    code = filehandle.readlines()

print(file, code)

## Start interpretation
for i in range(len(code)):
    line = code[i]

    # The first thing the interpretor checks for is a blank item
    if line[0] == "":
        continue
    else:
        # The Second thing the interpreter looks for is an assignment
        if line[0] == "<":
            # Get the number being assigned
            assinum = assign(line)
            assi.append(assinum)

        # Check for an output on the first char
        if line[0] == ">":
            otp = output(line)
            print(otp)

input()
