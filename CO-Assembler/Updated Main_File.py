# IMPORTANT :- vineet(2022575) has NOT contributed significantly in the completion of the project.

#Providing file location of the file to test into the program (INPUT)
#file_location=r"C:\Users\PC\Documents\co-project\normal\project.txt"

#f = open(file_location,"r") #provide the file name here
# List = sys.system.readlines()
#f.close()

#Providing the location to which the binary Converted data will be printed.(OUTPUT)
#to_print=r"C:\Users\PC\Documents\co-project\normal\output.txt"


import sys
List = sys.stdin.readlines()  #Taking input from STDIN if BASH runs in UBUNTU



Instruction_list = []      # Main list of all the instructions present in the input file
variables = []             #All the variables which were declared at the beginning of the program will be kept in this list.
check = 0
global flag     #Declaring flag as the global variable.
flag=1

def binary_convertor(n):        #Function to convert any immediate number to its binary form and adding zero(s) in front of it to make it of 7 bits.
    x=bin(n)
    x=x[2:]
    tk=[]
    for i in range(7-len(x)):
        tk.append("0")
    tk.append(str(x))
    x="".join(tk)
    return(x)

label_dict = {}        #Dictionary of all the labels present in the testing file.
instruction_index = 0  #Who store the index of the instructions so that easy traversal can be possible.
Line_index = 0
Line_index_check = 0

for i in range(len(List)):
    if (List[i] != "\n"):
        lnew = List[i].strip().split()    #.strip().split() Has been used to remove all the white spaces and new line characters.
        if lnew[0] == "var":
            if check == 0:
                variables.append(lnew[1])
            else:                        #If the variables are declared after an instruction or Not at the beginning then the program should exit.
                flag = 0
                print(f"\nERROR! Line no : {i+1}  Variables not declared at the beginning\n")
                quit()
        
        elif (lnew[0][-1] == ":"):
            label_dict[lnew[0][:-1]] = binary_convertor(instruction_index)
            lnew = lnew[1:]
            length = len(lnew)
            lnew[length-1] = lnew[length-1][:]
            Instruction_list.append(lnew)
            check = 1
            instruction_index += 1
            if (Line_index_check == 0):
                Line_index = i
                Line_index_check = 1
        
        else:        
            length = len(lnew)
            lnew[length-1] = lnew[length-1][:]
            Instruction_list.append(lnew)
            check = 1
            instruction_index += 1
            if (Line_index_check == 0):
                Line_index = i
                Line_index_check = 1

Instruction_function = [Instruction_list[i][0] for i in range(len(Instruction_list))]

length = len(Instruction_list)

variable_dict = {}

if len(variables)!=0:
    for i in variables:
        x=bin(length)
        x=x[2:]
        tk=[]
        for j in range(7-len(x)):
            tk.append("0")
        tk.append(str(x))
        x = "".join(tk)
        variable_dict[i] = x
        length = length + 1

"""
These were the Parameters that were considered by us to complete the project.
total bits = 16
register = 3
op code = 5
immediate value = 7        
memory address = 7
unused bit = depends
halt = 5 op code + 11 unused
"""
#print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+  WELCOME TO ASSEMBLY TO MACHINE CODE EXCHANGER  =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
#Making the dictionaries naming OP codes, registers and unused bits. it will be useful and easy to get an access to all of them.

opcode = {"add": "00000", "sub": "00001","movi":"00010", "mov": "00011", "ld": "00100", "st": "00101", "mul": "00110", 
    "div": "00111","rs": "01000", "ls": "01001", "xor": "01010", "or": "01011", "and": "01100", "not": "01101", "cmp": "01110", 
    "jmp": "01111", "jlt": "11100", "jgt": "11101", "je": "11111", "hlt": "11010"}
registers = {"R0": "000", "R1": "001", "R2": "010", "R3": "011",
            "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}    
unused_bit = {"add": 2, "sub": 2, "movi":1, "mov": 5,"ld": 1, "st": 1, "mul": 2, "div": 5, "rs": 1, "ls": 1, 
            "xor": 2, "or": 2, "and": 2, "not": 5, "cmp": 5, "jmp": 4, "jlt": 4, "jgt": 4, "je": 4, "hlt": 11}

if("hlt" in Instruction_function):
    if(Instruction_function[-1]!="hlt"):
        print("\nhlt not being used as the last instruction\n")  #HLT must be used as the last instruction.
        quit()
else:     #Checking if HLT is present in the program if it doesn't exist the program will not continue.
    print(f"\nError: No hlt instruction present.\n")
    quit()

Binary_list=[]      #Most important! this list will store the binary conversion in the form of strings.

#We all have divided the work into four parts every person completes 5 functions.

#Vishal Kumar Maurya 2022580 code Commences  -/-/-/

def substraction(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    Binary_list.append("".join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def move_register(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def divide(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(lst[2])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def store(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(variable_dict[lst[2]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def left_shift(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    value=int(lst[2][1:])
    x=bin(value)
    x=x[2:]
    tk=[]
    for i in range(7-len(x)):
        tk.append("0")
    tk.append(x)
    x="".join(tk)         #Converting the immediate value into the binary form and adding zeros in the front to make it look like 16 bit form.
    new_lst.append(registers[lst[1]])
    new_lst.append(x)
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

#Vishal kumar Maurya 2022580 code Terminates  -/-/-/
#subham maurya 2022510 code commences   -/-/-/

def addition(lst,y):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]]) 
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    Binary_list.append(''.join(new_lst))
    # print("\n",y,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def move_immediate(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]+"i"])
    new_lst.append('0' * unused_bit[lst[0]+"i"])
    new_lst.append(registers[lst[1]])
    value=int(lst[2][1:])
    x=bin(value)
    x=x[2:]
    tk=[]
    for i in range(7-len(x)):
        tk.append("0")
    tk.append(str(x))
    x="".join(tk)
    new_lst.append(x)
    Binary_list.append(''.join(new_lst))
    value = lst[0] + "i"
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[value]} unused bits.\n")

def load(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]]) 
    new_lst.append(registers[lst[1]])
    new_lst.append(variable_dict[lst[2]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def multiply(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # adding unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def right_shift(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(registers[lst[1]])
    value=int(lst[2][1:])
    x=bin(value)
    x=x[2:]
    tk=[]
    for i in range(7-len(x)):
        tk.append("0")
    tk.append(str(x))
    x="".join(tk)
    new_lst.append(x)
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

#subham maurya 2022510 code terminates    -/-/-/
#Wasif Ali 2022583 code commences -/-/-/
def Or(lst,q):
    # print("hello")
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append(('0' * unused_bit[lst[0]])) 
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def invert(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # adding unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def jumpifgreaterthan(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(label_dict[lst[1]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f'// {unused_bit["jgt"]} unused bits.\n')

def unconditionaljump(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(label_dict[lst[1]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f'// {unused_bit["jmp"]} unused bits.\n')

def halt(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    Binary_list.append(''.join(new_lst))
    #print("\n",q,'_'.join(new_lst))
    #print(f'// {unused_bit["hlt"]} unused bits.\n')
#wasif ali 2022583 code Terminates  -/-/-/  
#Vineet 2022575 code commences -/-/-/

def xor_operation(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]]) 
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def And(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]]) 
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    # print(f"// {unused_bit[lst[0]]} unused bits.\n")

def compare(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    Binary_list.append(''.join(new_lst))
    #print("\n",q,'_'.join(new_lst))
    #print(f"// {unused_bit[lst[0]]} unused bits.\n")

def jump_if_lessthan(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(label_dict[lst[1]])
    Binary_list.append(''.join(new_lst))
    # print("\n",q,'_'.join(new_lst))
    #print(f'// {unused_bit["jlt"]} unused bits.\n')

def jump_if_equal(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(label_dict[lst[1]])
    Binary_list.append(''.join(new_lst))
    #print("\n",q,'_'.join(new_lst))
    #print(f'// {unused_bit["je"]} unused bits.\n')

# vineet 2022575 code terminates -/-/-/

counter = 0           #This variable will act as a program counter.It will also show the line number at which error has been caught.
Newline_after = 0
List = List[Line_index:]

for i in range(len(List)):
    if (List[i]!='\n'): 
        if flag == 1:           #Loop will only run when the flag is equal to "1" i.e. all the instruction up to the program counter are correct and relevant.
            x=bin(counter)
            x=x[2:]
            tk=[]
            for j in range(7-len(x)):
                tk.append("0")
            tk.append(str(x))
            x="".join(tk)
            x=x+" : "            #Converting the program counter into binary and adding zero in front of it to make it of seven bitsto show the execution line by line on the terminal.
            
            #Now we are checking each instruction from the instruction list and performing the operation as required to convert it into Binary.
            #Flag will be set to zero if any ambiguity is found and code will not execute after that.

            if (Instruction_list[counter][0] == "add"):
                try:
                    if len(Instruction_list[counter]) == 4:
                        if ("FLAGS" in Instruction_list[counter]):
                            print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                            flag = 0
                        else:
                            addition(Instruction_list[counter],x)
                    else:
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,": add must contain 3 parameters\n")
                        flag = 0
                except:
                    flag = 0
                    print("\nError in Line",Line_index +  Newline_after  + counter + 1,": Typos in instruction name or register name\n")
                    # break

            elif (Instruction_list[counter][0] == "sub"):
                try:
                    if len(Instruction_list[counter]) == 4:
                        if ("FLAGS" in Instruction_list[counter]):
                            print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                            flag = 0
                        else:
                            substraction(Instruction_list[counter],x)
                    else:

                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,": sub must contain 3 parameters\n")
                        flag = 0
                except:
                    flag = 0
                    print("\nError in Line",Line_index +  Newline_after  + counter + 1,": Typos in instruction name or register name\n")
                    # break

            elif (Instruction_list[counter][0] == "mov"): #OK
                if (Instruction_list[counter][2][0]== "$"):
                    if ("FLAGS" in Instruction_list[counter]):
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                        flag = 0
                    else:
                        try:
                            if(0<=int(Instruction_list[counter][2][1:])<=127):
                                move_immediate(Instruction_list[counter],x)
                            else:
                                flag = 0
                                print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Immediate value must be between [0,127]\n")
                                # sys.exit()   
                        except:
                            flag = 0
                            print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

                elif (Instruction_list[counter][2][0].isnumeric()):
                        print("\"",Instruction_list[counter][2],"\" is not defined\n")
                        flag = 0
                else:
                    try:
                        move_register(Instruction_list[counter],x)
                    except:
                        flag=0
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "mul"):
                try:
                    if len(Instruction_list[counter]) == 4:
                        if ("FLAGS" in Instruction_list[counter]):
                            print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                            flag = 0
                        else:
                            multiply(Instruction_list[counter],x)
                    else:
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,": add must contain 3 parameters\n")
                        flag = 0
                except:
                    flag = 0
                    print("\nError in Line",Line_index +  Newline_after  + counter + 1,": Typos in instruction name or register name\n")
                    # break

            elif (Instruction_list[counter][0] == "div"):
                try:
                    if len(Instruction_list[counter]) == 4:
                        if ("FLAGS" in Instruction_list[counter]):
                            print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                            flag = 0
                        else:
                            divide(Instruction_list[counter],x)
                    else:
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,": add must contain 3 parameters\n")
                        flag = 0
                except:
                    flag = 0
                    print("\nError in Line",Line_index +  Newline_after  + counter + 1,": Typos in instruction name or register name\n")
                    # break
                    
            elif (Instruction_list[counter][0] == "rs"):
                try:
                    if(0<=int(Instruction_list[counter][2][1:])<=127):
                        right_shift(Instruction_list[counter],x)
                    elif(isinstance(Instruction_list[counter][2][1:], int)==False):
                        flag=0
                        print(f"\nError! : {Instruction_list[counter][2][1:]} is not an integer")
                    elif ("FLAGS" in Instruction_list[counter]):
                        flag = 0
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                    else:
                        flag = 0
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Immediate value must be between [0,127]\n")
                        #sys.exit()   
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "ls"):
                try:
                    if(0<=int(Instruction_list[counter][2][1:])<=127):
                        left_shift(Instruction_list[counter],x)
                    elif(isinstance(Instruction_list[counter][2][1:], int)==False):
                        flag=0
                        print(f"\nError! : {Instruction_list[counter][2][1:]} is not an integer")
                    elif ("FLAGS" in Instruction_list[counter]):
                        flag = 0
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                    else:
                        flag = 0
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Immediate value must be between [0,127]\n")
                        #sys.exit()   
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "xor"):
                try:
                    if ("FLAGS" in Instruction_list[counter]):
                        flag = 0
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                    else:
                        xor_operation(Instruction_list[counter],x)
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "or"):
                try:
                    if ("FLAGS" in Instruction_list[counter]):
                        flag = 0
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                    else:
                        Or(Instruction_list[counter],x)
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "and"):
                try:
                    if ("FLAGS" in Instruction_list[counter]):
                        flag = 0
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                    else:
                        And(Instruction_list[counter],x)
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name")

            elif (Instruction_list[counter][0] == "not"):
                try:
                    if ("FLAGS" in Instruction_list[counter]):
                        flag = 0
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                    else:
                        invert(Instruction_list[counter],x)
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name")

            elif (Instruction_list[counter][0] == "cmp"):
                try:
                    if ("FLAGS" in Instruction_list[counter]):
                        flag = 0
                        print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                    else:
                        compare(Instruction_list[counter],x)
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name")

            elif (Instruction_list[counter][0] == "ld"):
                try:
                    if(Instruction_list[counter][2] in variables):
                        if ("FLAGS" in Instruction_list[counter]):
                            flag = 0
                            print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                        else:
                            load(Instruction_list[counter],x)
                    else:
                        flag = 0
                        if (Instruction_list[counter][2] in label_dict):
                            print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of labels as variables \"",Instruction_list[counter][2],"\"\n")
                        else:
                            print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined variables \"",Instruction_list[counter][2],"\" \n") 
    
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "st"):
                try:
                    if(Instruction_list[counter][2] in variables):
                        if ("FLAGS" in Instruction_list[counter]):
                            flag = 0
                            print("\nError in Line",Line_index +  Newline_after  + counter + 1,"FLAGS cannot be used as Register\n")
                        else:
                            store(Instruction_list[counter],x)
                    else:
                        flag = 0
                        if (Instruction_list[counter][2] in label_dict):
                            print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of labels as variables \"",Instruction_list[counter][2],"\"\n")
                        else:
                            print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined variables \"",Instruction_list[counter][2],"\" \n")  
                except:
                    flag = 0
                    print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name")
                    
            elif (Instruction_list[counter][0] == "jmp"):
                try:
                    unconditionaljump(Instruction_list[counter],x)
                except:
                    flag = 0
                    if (Instruction_list[counter][1] in variable_dict):
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of variables as labels\n")
                    else:
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined labels\n")
                
            elif (Instruction_list[counter][0] == "jlt"):
                try:
                    jump_if_lessthan(Instruction_list[counter],x)
                except:
                    flag = 0
                    if (Instruction_list[counter][1] in variable_dict):
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of variables as labels\n")
                    else:
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined labels\n")

            elif (Instruction_list[counter][0] == "jgt"):
                try:
                    jumpifgreaterthan(Instruction_list[counter],x)
                except:
                    flag = 0
                    if (Instruction_list[counter][1] in variable_dict):
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of variables as labels\n")
                    else:
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined labels\n")

            elif (Instruction_list[counter][0] == "je"):
                try:
                    jump_if_equal(Instruction_list[counter],x)  
                except:
                    flag = 0
                    if (Instruction_list[counter][1] in variable_dict):
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1," Misuse of variables as labels\n")
                    else:
                        print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined labels\n")

            elif (Instruction_list[counter][0] == "hlt"):
                if(counter == len(Instruction_list) - 1):
                    halt(Instruction_list[counter],x)
                    #print(f"\nFound 'hlt' at Line No.:- {Line_index +  Newline_after  + counter + 1}.")
                    break
                else:
                    flag=0      # we have considered this condition also as an error BTW you can comment it to print the conversion into the file for the data before 'hlt' line.
                    print(f"\nERROR! : 'hlt' not being used as the Last Instruction. Can't execute lines after hlt, Found at Line no. :- {Line_index +  Newline_after  + counter + 1}.\n")
                    
            else:    #Checking error for wrong typos in instruction name.
                flag=0
                print(f"\nError in Line {Line_index +  Newline_after  + counter + 1} : Invalid operand")
            counter+=1
            
    else:
        Newline_after += 1


#if you want to print the output in another file...
# if (flag==1):                         #Printing only when there are no errors in the test file or flag equals to 1.
#     with open(to_print,"w") as f:
#         for i in Binary_list:         #Printing the binary list line by line into the needed file.
#             f.write(i+"\n")
#         f.close()  



#Printing the binary codes at ::STDOUT
if (flag==1):                         #Printing only when there are no errors in the test file or flag equals to 1.
    for i in Binary_list:         #Printing the binary list line by line into the needed file.
        sys.stdout.write(i)
        sys.stdout.write("\n")
