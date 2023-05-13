# IMPORTANT :- vineet(2022575) has not contributed significantly in the completion of the project.

file_location=r"E:\One Drive\OneDrive - indraprashtha institute of information technology\Practise code\python\Assignment\test2.txt"
f = open(file_location,"r") #provide the file name here
List = f.readlines()
f.close()
import sys
Instruction_list = []
variables = []
check = 0
global flag
flag=1

def binary_convertor(n):
    x=bin(n)
    x=x[2:]
    tk=[]
    for i in range(7-len(x)):
        tk.append("0")
    tk.append(str(x))
    x="".join(tk)
    return(x)

label_dict = {}
instruction_index = 0

for i in range(len(List)):
    if (List[i] != "\n"):
        lnew = List[i].strip().split()
        if lnew[0] == "var":
            if check == 0:
                variables.append(lnew[1])
            else:
                flag = 0
                print("\nERROR!: Variables not declared at the beginning\n")
                quit()
        
        elif (lnew[0][-1] == ":"):
            label_dict[lnew[0][:-1]] = binary_convertor(instruction_index)
            lnew = lnew[1:]
            length = len(lnew)
            lnew[length-1] = lnew[length-1][:]
            Instruction_list.append(lnew)
            check = 1
            instruction_index += 1
        
        else:        
            length = len(lnew)
            lnew[length-1] = lnew[length-1][:]
            Instruction_list.append(lnew)
            check = 1
            instruction_index += 1
            
Instruction_function = [Instruction_list[i][0] for i in range(len(Instruction_list))]
# print(Instruction_function)
# print(label_dict)
# print(Instruction_list)

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

# print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+  WELCOME TO ASSEMBLY TO MACHINE CODE EXCHANGER  =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
opcode = {"add": "00000", "sub": "00001","movi":"00010", "mov": "00011", "ld": "00100", "st": "00101", "mul": "00110", 
    "div": "00111","rs": "01000", "ls": "01001", "xor": "01010", "or": "01011", "and": "01100", "not": "01101", "cmp": "01110", 
    "jmp": "01111", "jlt": "11100", "jgt": "11101", "je": "11111", "hlt": "11010"}
registers = {"R0": "000", "R1": "001", "R2": "010", "R3": "011",
            "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}
unused_bit = {"add": 2, "sub": 2, "movi":1, "mov": 5,"ld": 1, "st": 1, "mul": 2, "div": 5, "rs": 1, "ls": 1, 
            "xor": 2, "or": 2, "and": 2, "not": 5, "cmp": 5, "jmp": 4, "jlt": 4, "jgt": 4, "je": 4, "hlt": 11}

if("hlt" in Instruction_function):
    if(Instruction_function[-1]!="hlt"):
        print("\nhlt not being used as the last instruction\n")
        quit()
else:
    print(f"\nError! : Missing hlt instruction!.\n")
    quit()
# quit()

# print(opcode)
# print(registers)
# print(unused_bit)
"""
total bits = 16
register = 3
op code = 5
immediate value = 7
memory address = 7
unused bit = depends
halt = 5 op code + 11 unused
"""

Binary_list=[]

#Vishal Kumar Maurya 2022580 code Commences  -/-/-/

def substraction(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    print("\n",q,'_'.join(new_lst))
    Binary_list.append("".join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def move_register(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    print("\n",q,'_'.join(new_lst))
    Binary_list.append(''.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def divide(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(lst[2])
    print("\n",q,'_'.join(new_lst))
    Binary_list.append(''.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def store(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(variable_dict[lst[2]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

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
    x="".join(tk)
    new_lst.append(registers[lst[1]])
    new_lst.append(x)
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

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
    print("\n",y,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

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
    print("\n",q,'_'.join(new_lst))
    Binary_list.append(''.join(new_lst))
    value = lst[0] + "i"
    print(f"// {unused_bit[value]} unused bits.\n")

def load(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]]) 
    new_lst.append(registers[lst[1]])
    new_lst.append(variable_dict[lst[2]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def multiply(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

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
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

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
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def invert(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def jumpifgreaterthan(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(label_dict[lst[1]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f'// {unused_bit["jgt"]} unused bits.\n')

def unconditionaljump(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(label_dict[lst[1]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f'// {unused_bit["jmp"]} unused bits.\n')

def halt(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))

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
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def And(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]]) 
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    new_lst.append(registers[lst[3]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def compare(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])  # add unused bits
    new_lst.append(registers[lst[1]])
    new_lst.append(registers[lst[2]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f"// {unused_bit[lst[0]]} unused bits.\n")

def jump_if_lessthan(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(label_dict[lst[1]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f'// {unused_bit["jlt"]} unused bits.\n')

def jump_if_equal(lst,q):
    new_lst = []
    new_lst.append(opcode[lst[0]])
    new_lst.append('0' * unused_bit[lst[0]])
    new_lst.append(label_dict[lst[1]])
    Binary_list.append(''.join(new_lst))
    print("\n",q,'_'.join(new_lst))
    print(f'// {unused_bit["je"]} unused bits.\n')

# vineet 2022575 code terminates -/-/-/
counter = 0
# cck=

for i in range(len(Instruction_list)):
    if flag == 1:
        x=bin(counter)
        x=x[2:]
        tk=[]
        # print(counter)
        for j in range(7-len(x)):
            tk.append("0")
        tk.append(str(x))
        x="".join(tk)
        x=x+" : "
        # print("HE",x)
        # print("i: ",i)
        if (Instruction_list[i][0] == "add"):
            try:
                addition(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")
                # break

        elif (Instruction_list[i][0] == "sub"):
            try:
                substraction(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")
                # break

        elif (Instruction_list[i][0] == "mov"): #OK
            if (Instruction_list[i][2][0]== "$"):
                try:
                    if(0<=int(Instruction_list[i][2][1:])<=127):
                        move_immediate(Instruction_list[i],x)
                    else:
                        flag = 0
                        print("\nERROR! Line No. :",counter+1,"Immediate value must be between [0,127]\n")
                        # sys.exit()   
                except:
                    flag = 0
                    print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

                
            else:
                try:
                    move_register(Instruction_list[i],x)
                except:
                    flag=0
                    print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

        elif (Instruction_list[i][0] == "mul"):
            try:
                multiply(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

        elif (Instruction_list[i][0] == "div"):
            try:
                divide(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

        elif (Instruction_list[i][0] == "rs"):
            try:
                    if(0<=int(Instruction_list[i][2][1:])<=127):
                        right_shift(Instruction_list[i],x)
                    else:
                        flag = 0
                        print("\nERROR! Line No. :",counter+1,"Immediate value must be between [0,127]\n")
                        # sys.exit()   
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

        elif (Instruction_list[i][0] == "ls"):
            try:
                    if(0<=int(Instruction_list[i][2][1:])<=127):
                        left_shift(Instruction_list[i],x)
                    else:
                        flag = 0
                        print("\nERROR!: Immediate value must be between [0,127]\n")
                        # sys.exit()   
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

        elif (Instruction_list[i][0] == "xor"):
            try:
                xor_operation(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

        elif (Instruction_list[i][0] == "or"):
            try:
                Or(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

        elif (Instruction_list[i][0] == "and"):
            try:
                And(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name")

        elif (Instruction_list[i][0] == "not"):
            try:
                invert(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name")

        elif (Instruction_list[i][0] == "cmp"):
            try:
                compare(Instruction_list[i],x)
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name")

        elif (Instruction_list[i][0] == "ld"):
            try:
                if(Instruction_list[i][2] in variables):
                    load(Instruction_list[i],x)
                else:
                    flag = 0
                    if (Instruction_list[i][2] in label_dict):
                        print("\nERROR! Line No. :",counter+1,"Misuse of labels as variables\n")
                    else:
                        print("\nERROR!Line No. :",counter+1,"Use of undefined variables\n")
  
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name\n")

        elif (Instruction_list[i][0] == "st"):
            try:
                if(Instruction_list[i][2] in variables):
                    store(Instruction_list[i],x)
                else:
                    flag = 0
                    if (Instruction_list[i][2] in label_dict):
                        print("\nERROR! Line No. :",counter+1,"Misuse of labels as variables\n")
                    else:
                        print("\nERROR!Line No. :",counter+1,"Use of undefined variables\n")  
            except:
                flag = 0
                print("\nERROR! Line No. :",counter+1,"Typos in instruction name or register name")
                
        elif (Instruction_list[i][0] == "jmp"):
            try:
                unconditionaljump(Instruction_list[i],x)
            except:
                flag = 0
                if (Instruction_list[i][1] in variable_dict):
                    print("\nERROR! Line No. :",counter+1,"Misuse of variables as labels\n")
                else:
                    print("\nERROR!Line No. :",counter+1,"Use of undefined labels\n")
            
        elif (Instruction_list[i][0] == "jlt"):
            try:
                jump_if_lessthan(Instruction_list[i],x)
            except:
                flag = 0
                if (Instruction_list[i][1] in variable_dict):
                    print("\nERROR! Line No. :",counter+1,"Misuse of variables as labels\n")
                else:
                    print("\nERROR!Line No. :",counter+1,"Use of undefined labels\n")
            
        elif (Instruction_list[i][0] == "jgt"):
            try:
                jumpifgreaterthan(Instruction_list[i],x)
            except:
                flag = 0
                if (Instruction_list[i][1] in variable_dict):
                    print("\nERROR! Line No. :",counter+1,"Misuse of variables as labels\n")
                else:
                    print("\nERROR!Line No. :",counter+1,"Use of undefined labels\n")

            
        elif (Instruction_list[i][0] == "je"):
            try:
                jump_if_equal(Instruction_list[i],x)  
            except:
                flag = 0
                if (Instruction_list[i][1] in variable_dict):
                    print("\nERROR!Line No. :",counter+1," Misuse of variables as labels\n")
                else:
                    print("\nERROR! Line No. :",counter+1,"Use of undefined labels\n")
            
        elif (Instruction_list[i][0] == "hlt"):
            try:
                halt(Instruction_list[i],x)
                flag=0
            except:
                # print("sv",len(List),counter)
                if(counter+1 != len(variables)+len(Instruction_list)):
                    flag=0
                    print(f"\nGeneral Syntax Error! in line no. {counter+1} :- found hlt more than once.")
        else:
            flag=0
            print("\nERROR!: Typos in instruction name")
        counter+=1

#Printing the file :
# print(Binary_list)
to_print=r'E:\One Drive\OneDrive - indraprashtha institute of information technology\Practise code\python\Assignment\printer.txt'
if (flag==1):
    with open(to_print,"w") as f:
        for i in Binary_list:
            f.write(i+"\n")
        f.close()      
        
