# IMPORTANT :- vineet(2022575) has NOT contributed significantly in the completion of the project.

#Providing file location of the file to test into the program (INPUT)
file_location=r"E:\One Drive\OneDrive - indraprashtha institute of information technology\Practise code\python\Assignment\simulator\makeover.txt"

f = open(file_location,"r") #provide the file name here
List = f.readlines()
f.close()

#Providing the location to which the binary Converted data will be printed.(OUTPUT)
#to_print=r"C:\Users\PC\Documents\co-project\normal\output.txt"


# import sys
# List = sys.stdin.readlines()  #Taking input from STDIN if BASH runs in UBUNTU



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
            "R4": "100", "R5": "101", "R6": "110"}   

flag='111'
flag_register=['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

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
        if flag != 5:           #Loop will only run when the flag is equal to "1" i.e. all the instruction up to the program counter are correct and relevant.
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
                        addition(Instruction_list[counter],x)
                    else:
                        # print("\nError in Line",Line_index +  Newline_after  + counter + 1,": add must contain 3 parameters\n")
                        flag = 0
                except:
                    flag = 0
                    # print("\nError in Line",Line_index +  Newline_after  + counter + 1,": Typos in instruction name or register name\n")
                    # break

            elif (Instruction_list[counter][0] == "sub"):
                try:
                    if len(Instruction_list[counter]) == 4:
                        substraction(Instruction_list[counter],x)
                    else:
                        # print("\nError in Line",Line_index +  Newline_after  + counter + 1,": sub must contain 3 parameters\n")
                        flag = 0
                except:
                    flag = 0
                    # print("\nError in Line",Line_index +  Newline_after  + counter + 1,": Typos in instruction name or register name\n")
                    # break

            elif (Instruction_list[counter][0] == "mov"): #OK
                if (Instruction_list[counter][2][0]== "$"):
                    try:
                        if(0<=int(Instruction_list[counter][2][1:])<=127):
                            move_immediate(Instruction_list[counter],x)
                        else:
                            flag = 0
                            # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Immediate value must be between [0,127]\n")
                            # sys.exit()   
                    except:
                        flag = 0
                        # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

                elif (Instruction_list[counter][2][0].isnumeric()):
                        # print("\"",Instruction_list[counter][2],"\" is not defined\n")
                        flag = 0
                else:
                    try:
                        move_register(Instruction_list[counter],x)
                    except:
                        flag=0
                        # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "mul"):
                try:
                    multiply(Instruction_list[counter],x)
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "div"):
                try:
                    divide(Instruction_list[counter],x)
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "rs"):
                try:
                    if(0<=int(Instruction_list[counter][2][1:])<=127):
                        right_shift(Instruction_list[counter],x)
                    elif(isinstance(Instruction_list[counter][2][1:], int)==False):
                        flag=0
                        # print(f"\nError! : {Instruction_list[counter][2][1:]} is not an integer")
                    else:
                        flag = 0
                        # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Immediate value must be between [0,127]\n")
                        #sys.exit()   
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "ls"):
                try:
                        if(0<=int(Instruction_list[counter][2][1:])<=127):
                            left_shift(Instruction_list[counter],x)
                        else:
                            flag = 0
                            # print("\nERROR! : Immediate value must be between [0,127]\n")
                            #sys.exit()   
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "xor"):
                try:
                    xor_operation(Instruction_list[counter],x)
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "or"):
                try:
                    Or(Instruction_list[counter],x)
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "and"):
                try:
                    And(Instruction_list[counter],x)
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name")

            elif (Instruction_list[counter][0] == "not"):
                try:
                    invert(Instruction_list[counter],x)
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name")

            elif (Instruction_list[counter][0] == "cmp"):
                try:
                    compare(Instruction_list[counter],x)
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name")

            elif (Instruction_list[counter][0] == "ld"):
                try:
                    if(Instruction_list[counter][2] in variables):
                        load(Instruction_list[counter],x)
                    else:
                        flag = 0
                        # if (Instruction_list[counter][2] in label_dict):
                        #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of labels as variables \"",Instruction_list[counter][2],"\"\n")
                        # else:
                        #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined variables \"",Instruction_list[counter][2],"\" \n") 
    
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name\n")

            elif (Instruction_list[counter][0] == "st"):
                try:
                    if(Instruction_list[counter][2] in variables):
                        store(Instruction_list[counter],x)
                    else:
                        flag = 0
                        # if (Instruction_list[counter][2] in label_dict):
                        #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of labels as variables \"",Instruction_list[counter][2],"\"\n")
                        # else:
                        #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined variables \"",Instruction_list[counter][2],"\" \n")  
                except:
                    flag = 0
                    # print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Typos in instruction name or register name")
                    
            elif (Instruction_list[counter][0] == "jmp"):
                try:
                    unconditionaljump(Instruction_list[counter],x)
                except:
                    flag = 0
                    # if (Instruction_list[counter][1] in variable_dict):
                    #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of variables as labels\n")
                    # else:
                    #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined labels\n")
                
            elif (Instruction_list[counter][0] == "jlt"):
                try:
                    jump_if_lessthan(Instruction_list[counter],x)
                except:
                    flag = 0
                    # if (Instruction_list[counter][1] in variable_dict):
                    #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of variables as labels\n")
                    # else:
                    #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined labels\n")

            elif (Instruction_list[counter][0] == "jgt"):
                try:
                    jumpifgreaterthan(Instruction_list[counter],x)
                except:
                    flag = 0
                    # if (Instruction_list[counter][1] in variable_dict):
                    #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Misuse of variables as labels\n")
                    # else:
                    #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined labels\n")

            elif (Instruction_list[counter][0] == "je"):
                try:
                    jump_if_equal(Instruction_list[counter],x)  
                except:
                    flag = 0
                    # if (Instruction_list[counter][1] in variable_dict):
                    #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1," Misuse of variables as labels\n")
                    # else:
                    #     print("\nERROR! : Line No. :",Line_index +  Newline_after  + counter + 1,"Use of undefined labels\n")

            elif (Instruction_list[counter][0] == "hlt"):
                if(counter == len(Instruction_list) - 1):
                    halt(Instruction_list[counter],x)
                    #print(f"\nFound 'hlt' at Line No.:- {Line_index +  Newline_after  + counter + 1}.")
                    break
                else:
                    flag=0      # we have considered this condition also as an error BTW you can comment it to print the conversion into the file for the data before 'hlt' line.
                    # print(f"\nERROR! : 'hlt' not being used as the Last Instruction. Can't execute lines after hlt, Found at Line no. :- {Line_index +  Newline_after  + counter + 1}.\n")
                    
            else:    #Checking error for wrong typos in instruction name.
                flag=0
                # print(f"\nError in Line {Line_index +  Newline_after  + counter + 1} : Invalid operand")
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
# if (flag==1):                         #Printing only when there are no errors in the test file or flag equals to 1.
#     for i in Binary_list:         #Printing the binary list line by line into the needed file.
#         sys.stdout.write(i)
#         sys.stdout.write("\n")









# *****************************SIMULATOR STARTS HERE******************************









#IMPORTANT Vineet(2022575) has NOT contributed anything towards the completion of simulator.

code={'00000': 'add', '00001': 'sub', '00010': 'movi', '00011': 'mov', '00100': 'ld', '00101': 'st',
    '00110': 'mul', '00111': 'div', '01000': 'rs', '01001': 'ls', '01010': 'xor', '01011': 'or',
    '01100': 'and', '01101': 'not', '01110': 'cmp', '01111': 'jmp', '11100': 'jlt', '11101': 'jgt',
    '11111': 'je', '11010': 'hlt'}

import sys

val2={'000': 'R0', '001': 'R1', '010': 'R2', '011': 'R3',
    '100': 'R4', '101': 'R5', '110': 'R6','111':'FLAGS'}

all_operations = {"add": 2, "sub": 2, "movi":1, "mov": 5,"ld": 1, "st": 1, "mul": 2, "div": 5, "rs": 1, "ls": 1, 
            "xor": 2, "or": 2, "and": 2, "not": 5, "cmp": 5, "jmp": 4, "jlt": 4, "jgt": 4, "je": 4, "hlt": 11}

val= {2: ['and','sub','mul'], 1: ['ls','movi'], 5: ['cmp','mov'], 4: ['je'], 11: ['hlt']}

register_values={"R0":"0000000000000000","R1":"0000000000000000","R2":"0000000000000000","R3":"0000000000000000",
                "R4":"0000000000000000","R5":"0000000000000000","R6":"0000000000000000","FLAGS":"0000000000000000"}

flag_register=['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
printing_LIST=[]
global program_counter
program_counter=0

# file_path = r"E:\One Drive\OneDrive - indraprashtha institute of information technology\Practise code\python\Assignment\simulator\input1.txt"
# f = open(file_path)
# main_list  =  f.readlines()
# f.close()

main_list  =  Binary_list

# print(main_list)

for i in range(len(main_list)):
    if "\n" in main_list[i]:
        main_list[i] = main_list[i][:-1]

# main_list = sys.stdin.readlines()  #Taking input from STDIN if BASH runs in UBUNTU

Memory = ["0"*16 for i in range(128)]

for i in range(len(main_list)):
    Memory[i] = main_list[i]

def binary_to_decimal(binary_string):
    decimal = int(binary_string, 2)
    return decimal

def decimal_to_binary(decimal_number):
    binary_string = bin(decimal_number)[2:].zfill(16)
    return binary_string

def substract_sim(input_string):
    reg1 = val2[input_string[-3:]]
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = int((binary_to_decimal(register_values[reg1])) - (binary_to_decimal(register_values[reg2])))
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1"
        register_values[reg3]="0000000000000000"
        print("\nvalue overflow!")
    else:
        register_values[reg3] = decimal_to_binary(value)
        flag_register[-4] = "0"
        flag_register[-3] = "0"
        flag_register[-2] = "0"
        flag_register[-1] = "0"


def multiply_sim(input_string):
    reg1 = val2[input_string[-3:]]
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = int((binary_to_decimal(register_values[reg1])) * (binary_to_decimal(register_values[reg2])))
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1";
        print("\nvalue overflow!")
        register_values[reg3]="0000000000000000"
    
    else:
        register_values[reg3] = decimal_to_binary(value)
        flag_register[-4] = "0"
        flag_register[-3] = "0"
        flag_register[-2] = "0"
        flag_register[-1] = "0"


def divide_sim(input_string):
    reg1 = val2[input_string[-3:]]
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = int((binary_to_decimal(register_values[reg1])) / (binary_to_decimal(register_values[reg2])))
    # register_values[reg3] = decimal_to_binary(value)
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1"
        print("\nvalue overflow!")
        register_values[reg3]="0000000000000000"
    else:
        register_values[reg3] = decimal_to_binary(value)
        flag_register[-4] = "0"
        flag_register[-3] = "0"
        flag_register[-2] = "0"
        flag_register[-1] = "0"
    
    
def addition_sim(input):
    reg1 = input[-3 : ]
    reg2 = input[-6 : -3]
    reg3 = input[-9 : -6]
    lst = []
    lst.append(val2[reg1])
    lst.append(val2[reg2])
    lst.append(val2[reg3])
    reg_val1 = binary_to_decimal(register_values[lst[0]])
    reg_val2 = binary_to_decimal(register_values[lst[1]])
    reg_val3 = reg_val1 + reg_val2
    if (0 > reg_val3 or reg_val3 > 65535):
        flag_register[-4] = "1"
        print("\nvalue overflow!")
        register_values[reg3]="0000000000000000"

    else:
        register_values[lst[2]] = decimal_to_binary(reg_val3)
        flag_register[-4] = "0"
        flag_register[-3] = "0"
        flag_register[-2] = "0"
        flag_register[-1] = "0"


def movreg_sim(input):
    reg1 = input[-3 : ]
    reg2 = input[-6 : -3]
    lst = []
    lst.append(val2[reg1])
    lst.append(val2[reg2])
    
    if (reg1 == "111"):
        register_values[lst[1]] = "".join(flag_register)
        return
    
    register_values[lst[1]] = register_values[lst[0]]

def movImm_sim(input):
    immediate = input[-7 : ]
    reg = input[-10 : -7]

    temp = binary_to_decimal(immediate)
    value = decimal_to_binary(temp)

    reg1 = val2[reg]
    register_values[reg1] = value

def compare_sim(input):
    temp_reg1 = input[-3 : ]
    temp_reg2 = input[-6 : -3]

    reg1 = val2[temp_reg1]
    reg2= val2[temp_reg2]

    reg1_value = binary_to_decimal(register_values[reg1])
    reg2_value = binary_to_decimal(register_values[reg2])

    if(reg1_value > reg2_value):
        flag_register[-3] = "1"

    elif(reg2_value > reg1_value):
        flag_register[-2] = "1"

    else:
        flag_register[-1] = "1"

def load_sim(data):
    imm = str(data[-7:])
    Reg = str(data[-10:-7])
    
    decimal_imm = binary_to_decimal(imm)
    register_values[val2[Reg]] = Memory[decimal_imm]
    

def store_sim(data):
    imm = str(data[-7:])
    Reg = str(data[-10:-7])
    
    decimal_imm = binary_to_decimal(imm)    
    Memory[decimal_imm] = register_values[val2[Reg]]


def Right_shift_sim(data):
    imm = str(data[-7:])
    Reg = str(data[-10:-7])
    
    decimal_imm = binary_to_decimal(imm)
    binary_reg =register_values[val2[Reg]]
    
    for i in range(decimal_imm):
        binary_reg = binary_reg[1:] + binary_reg[0]
        
    register_values[val2[Reg]] = binary_reg
    
    
def Left_shift_sim(data):
    imm = str(data[-7:])
    Reg = str(data[-10:-7])
    
    decimal_imm = binary_to_decimal(imm)
    binary_reg =register_values[val2[Reg]]
    
    for i in range(decimal_imm):
        binary_reg =  binary_reg[-1] + binary_reg[:-1]
        
    register_values[val2[Reg]] = binary_reg
    
    
def XOR_sim(data):
    Reg3 = data[-3:]
    Reg2 = data[-6:-3]
    Reg1 = data[-9:-6]
    
    binary_Reg2 = register_values[val2[Reg2]]
    binary_Reg3 = register_values[val2[Reg3]]
    binary_Reg1 = ""
    
    for i in range(16):
        if binary_Reg2[i] != binary_Reg3[i]:
            binary_Reg1 += "1"
        else:
            binary_Reg1 += "0"
            
    register_values[val2[Reg1]] = binary_Reg1
    
def OR_sim(data):
    Reg3 = data[-3:]
    Reg2 = data[-6:-3]
    Reg1 = data[-9:-6]
    
    binary_Reg2 = register_values[val2[Reg2]]
    binary_Reg3 = register_values[val2[Reg3]]
    binary_Reg1 = ""
    
    for i in range(16):
        if binary_Reg2[i] == "0" and  binary_Reg3[i] == "0":
            binary_Reg1 += "0"
        else:
            binary_Reg1 += "1"
            
    register_values[val2[Reg1]] = binary_Reg1

def AND_sim(data):
    Reg3 = data[-3:]
    Reg2 = data[-6:-3]
    Reg1 = data[-9:-6]
    # print(Reg1,Reg2,Reg3)
    
    binary_Reg2 = register_values[val2[Reg2]]
    binary_Reg3 = register_values[val2[Reg3]]
    binary_Reg1 = ""
    
    for i in range(16):
        if binary_Reg2[i] == "1" and  binary_Reg3[i] == "1":
            binary_Reg1 += "1"
        else:
            binary_Reg1 += "0"
            
    register_values[val2[Reg1]] = binary_Reg1
    
def NOT_sim(data):
    Reg2 = data[-3:]
    Reg1 = data[-6:-3]
    # print(Reg1,Reg2)
    
    binary_Reg2 = register_values[val2[Reg2]]
    binary_Reg1 = ""
    
    for i in range(16):
        if binary_Reg2[i] == "1":
            binary_Reg1 += "0"
        else:
            binary_Reg1 += "1"
            
    register_values[val2[Reg1]] = binary_Reg1


def unconditional_jump_sim(data):
    imm = str(data[-7:])
    decimal_imm = binary_to_decimal(imm)
    return decimal_imm
    
def jump_if_less_sim(data,program_counter):
    imm = str(data[-7:])
    decimal_imm = binary_to_decimal(imm)
    if (flag_register[-3] == 1):
        return decimal_imm
    else:
        return program_counter
    
def jump_if_greaters_sim(data,program_counter):
    imm = str(data[-7:])
    decimal_imm = binary_to_decimal(imm)
    if (flag_register[-2] == 1):
        return decimal_imm
    else:
        return program_counter
    
def jump_if_equal_sim(data,program_counter):
    imm = str(data[-7:])
    decimal_imm = binary_to_decimal(imm)
    if (flag_register[-1] == 1):
        return decimal_imm
    else:
        return program_counter

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ BONUS +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

def floor_Division(input_string):
    reg1 = val2[input_string[-3:]]     # will be calculating R1 // R2 and storing at R3    <OPCODE>  floor R3 R2 R1
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = int((binary_to_decimal(register_values[reg1])) // (binary_to_decimal(register_values[reg2])))
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1"
        print("\nvalue overflow!")
    
    else:
        register_values[reg3] = decimal_to_binary(value)

def power_Generator(input_string):
    reg1 = val2[input_string[-3:]]  # will be calculating R1 ^ R2 and storing at R3    <OPCODE>  pow R3 R2 R1
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = int((binary_to_decimal(register_values[reg1])) ** (binary_to_decimal(register_values[reg2])))
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1"
        print("\nvalue overflow!")
    
    else:
        register_values[reg3] = decimal_to_binary(value)

def GET_LCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def LCM_Calculate(input_string):
    reg1 = val2[input_string[-3:]]  # will be calculating LCM(R1,R2) and storing at R3    <OPCODE>  pow R3 R2 R1
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = GET_LCM((binary_to_decimal(register_values[reg1])) , (binary_to_decimal(register_values[reg2])))
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1"
        print("\nvalue overflow!")
    
    else:
        register_values[reg3] = decimal_to_binary(value)

def GET_HCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

def calculate_HCF(input_string):
    reg1 = val2[input_string[-3:]]  # will be calculating gcd(R1,R2) and storing at R3    <OPCODE>  pow R3 R2 R1
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = GET_HCF((binary_to_decimal(register_values[reg1])) , (binary_to_decimal(register_values[reg2])))
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1"
        print("\nvalue overflow!")
    
    else:
        register_values[reg3] = decimal_to_binary(value)


def get_NPR(n, r):
    numerator = 1
    for i in range(n, n - r, -1):
        numerator *= i

    denominator = 1
    for i in range(1, r + 1):
        denominator *= i

    perm = numerator / denominator
    return int(perm)

def calculate_NPR(input_string):
    reg1 = val2[input_string[-3:]]  # will be calculating R1 P R2 and storing at R3    <OPCODE>  pow R3 R2 R1
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = get_NPR((binary_to_decimal(register_values[reg1])) , (binary_to_decimal(register_values[reg2])))
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1"
        print("\nvalue overflow!")
    
    else:
        register_values[reg3] = decimal_to_binary(value)


def get_NCR(n, r):
    numerator = 1
    for i in range(n, n - r, -1):
        numerator *= i

    denominator = 1
    for i in range(1, r + 1):
        denominator *= i

    combination = numerator // denominator
    return combination

# print(get_NCR(5, 2))
def calculate_NCR(input_string):
    reg1 = val2[input_string[-3:]]  # will be calculating R1 C R2 and storing at R3    <OPCODE>  pow R3 R2 R1
    reg2 = val2[input_string[-6:-3]]
    reg3 = val2[input_string[-9:-6]]
    value = get_NCR((binary_to_decimal(register_values[reg1])) , (binary_to_decimal(register_values[reg2])))
    if (0 > value or value > 65535):  #(2^n -1)
        flag_register[-4] = "1"
        print("\nvalue overflow!")
    
    else:
        register_values[reg3] = decimal_to_binary(value)

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ BONUS ENDS +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

def program_counter_binary_handler(decimal):
    binary = "{0:07b}".format(decimal)
    return binary

j = 0
check = 0

while (j < len(main_list)):
    
    i = main_list[j]
    s=i[0:5]
    
    if(s=='00000'):
        addition_sim(i)

    elif(s=='00001'):
        substract_sim(i)

    elif(s=='00010'):
        movImm_sim(i)
        flag_register = ['0' for j in range(16)]

    elif(s=='00011'):
        movreg_sim(i)
        flag_register = ['0' for j in range(16)]

    elif(s=='00100'):
        load_sim(i)
        flag_register = ['0' for j in range(16)]

    elif(s=='00101'):
        store_sim(i)
        flag_register = ['0' for j in range(16)]
        
    elif(s=='00110'):
        multiply_sim(i)
        
    elif(s=='00111'):
        divide_sim(i)
        
    elif (s=='01000'):
        Right_shift_sim(i)
        flag_register = ['0' for j in range(16)]
        
    elif(s=='01001'):
        Left_shift_sim(i)
        flag_register = ['0' for j in range(16)]
        
    elif(s=='01010'):
        XOR_sim(i)
        flag_register = ['0' for j in range(16)]
        
    elif(s=='01011'):
        OR_sim(i)
        flag_register = ['0' for j in range(16)]
        
    elif(s=='01100'):
        AND_sim(i)
        flag_register = ['0' for j in range(16)]
        
    elif(s=='01101'):
        NOT_sim(i)
        flag_register = ['0' for j in range(16)]
        
    elif(s=='01110'):
        compare_sim(i)

    elif(s=='01111'):
        program_counter = unconditional_jump_sim(i)
        flag_register = ['0' for j in range(16)]
        
    elif(s=='11100'):
        program_counter = jump_if_less_sim(i,program_counter)
        flag_register = ['0' for j in range(16)]
        if (j != program_counter):
            check == 1
        else:
            check == 0
        
    elif(s=='11101'):
        program_counter = jump_if_greaters_sim(i,program_counter)
        flag_register = ['0' for j in range(16)]
        if (j != program_counter):
            check == 1
        else:
            check == 0
        
    elif(s=='11111'):
        program_counter = jump_if_equal_sim(i,program_counter)
        flag_register = ['0' for j in range(16)]
        if (j != program_counter):
            check == 1
        else:
            check == 0
        
    elif(s=='11010'):
        flag_register = ['0' for j in range(16)]
        string =""
        string += str(program_counter_binary_handler(program_counter))
        string += "        "

        for i in register_values:
            string += (register_values[i])
            string += (" ")
            
        string += "".join(i for i in flag_register)
        printing_LIST.append(string)
        break

    else:
        a = 1
        
    string = ""
    string += str(program_counter_binary_handler(program_counter))
    string += "        "

    for i in register_values:
        string += register_values[i]
        string += " "
        
    string += "".join(i for i in flag_register)
    printing_LIST.append(string)

    # print(program_counter , j)
    if (check == 0 and program_counter >= j):
        j += 1
        program_counter += 1
    else:
        j = program_counter
        
    check = 0

# to_print=r'E:\One Drive\OneDrive - indraprashtha institute of information technology\Practise code\python\Assignment\simulator\OUTPUT.txt'
# with open(to_print,"w") as f:
#     for i in printing_LIST:         #Printing the binary list line by line into the needed file.
#         f.write(i)
#         f.write("\n")
#     for i in range(128):
#         f.write(Memory[i])
#         f.write("\n")
#     f.close()



for i in printing_LIST:
    print(i)
    
for i in range(128):
    print(Memory[i])


# for i in printing_LIST:         #Printing the binary list line by line into the needed file.
#     sys.stdout.write(i)
#     sys.write("\n")
# for i in range(128):
#     sys.stdout.write(Memory[i])
#     sys.write("\n")
