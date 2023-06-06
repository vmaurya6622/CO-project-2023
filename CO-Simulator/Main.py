#IMPORTANT Vineet(2022575) has NOT contributed anything towards the completion of simulator.
code={'00000': 'add', '00001': 'sub', '00010': 'movi', '00011': 'mov', '00100': 'ld', '00101': 'st',
    '00110': 'mul', '00111': 'div', '01000': 'rs', '01001': 'ls', '01010': 'xor', '01011': 'or',
    '01100': 'and', '01101': 'not', '01110': 'cmp', '01111': 'jmp', '11100': 'jlt', '11101': 'jgt',
    '11111': 'je', '11010': 'hlt'}
import sys
val2={'000': 'R0', '001': 'R1', '010': 'R2', '011': 'R3',
    '100': 'R4', '101': 'R5', '110': 'R6','111':'FLAGS'}

registers = {"add": 2, "sub": 2, "movi":1, "mov": 5,"ld": 1, "st": 1, "mul": 2, "div": 5, "rs": 1, "ls": 1, 
            "xor": 2, "or": 2, "and": 2, "not": 5, "cmp": 5, "jmp": 4, "jlt": 4, "jgt": 4, "je": 4, "hlt": 11}

val= {2: ['and','sub','mul'], 1: ['ls','movi'], 5: ['cmp','mov'], 4: ['je'], 11: ['hlt']}

register_values={"R0":"0000000000000000","R1":"0000000000000000","R2":"0000000000000000","R3":"0000000000000000",
                "R4":"0000000000000000","R5":"0000000000000000","R6":"0000000000000000"}

flag_register=['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
printing_LIST=[]
global program_counter
program_counter=0

file_path = r"E:\One Drive\OneDrive - indraprashtha institute of information technology\Practise code\python\Assignment\simulator\input1.txt"
f = open(file_path)

main_list  =  f.readlines()
for i in range(len(main_list)):
    if "\n" in main_list[i]:
        main_list[i] = main_list[i][:-1]

# main_list = sys.stdin.readlines()  #Taking input from STDIN if BASH runs in UBUNTU

Memory = ["0"*16 for i in range(128)]

for i in range(len(main_list)):
    Memory[i] = main_list[i]

# print(Memory)

def binary_to_decimal(binary_string):
    decimal = int(binary_string, 2)
    return decimal

def decimal_to_binary(decimal_number):
    binary_string = bin(decimal_number)[2:].zfill(16)
    return binary_string

def subtract(input_string):
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


def multiply(input_string):
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


def divide(input_string):
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
    
    
def addition(input):
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


def movRegister(input):
    reg1 = input[-3 : ]
    reg2 = input[-6 : -3]
    lst = []
    lst.append(val2[reg1])
    lst.append(val2[reg2])
    
    if (reg1 == "111"):
        register_values[lst[1]] = "".join(flag_register)
        return
    
    register_values[lst[1]] = register_values[lst[0]]

def movImmediate(input):
    immediate = input[-7 : ]
    reg = input[-10 : -7]

    temp = binary_to_decimal(immediate)
    value = decimal_to_binary(temp)

    reg1 = val2[reg]
    register_values[reg1] = value

def compare(input):
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

def load(data):
    imm = str(data[-7:])
    Reg = str(data[-10:-7])
    
    decimal_imm = binary_to_decimal(imm)    
    register_values[val2[Reg]] = "0"*(16-7) + Memory[decimal_imm]
    

def store(data):
    imm = str(data[-7:])
    Reg = str(data[-10:-7])
    
    decimal_imm = binary_to_decimal(imm)    
    Memory[decimal_imm] = register_values[val2[Reg]]


def Right_shift(data):
    imm = str(data[-7:])
    Reg = str(data[-10:-7])
    
    decimal_imm = binary_to_decimal(imm)
    binary_reg =register_values[val2[Reg]]
    
    for i in range(decimal_imm):
        binary_reg = binary_reg[1:] + binary_reg[0]
        
    # print(binary_reg)
    register_values[val2[Reg]] = binary_reg
    
    
def Left_shift(data):
    imm = str(data[-7:])
    Reg = str(data[-10:-7])
    
    decimal_imm = binary_to_decimal(imm)
    binary_reg =register_values[val2[Reg]]
    
    for i in range(decimal_imm):
        binary_reg =  binary_reg[-1] + binary_reg[:-1]
        
    # print(binary_reg)
    register_values[val2[Reg]] = binary_reg
    
    
def XOR(data):
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
    
def OR(data):
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

def AND(data):
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
    
def NOT(data):
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


def unconditional_jump(data):
    imm = str(data[-7:])
    decimal_imm = binary_to_decimal(imm)
    return decimal_imm
    
def jump_if_less(data,program_counter):
    imm = str(data[-7:])
    decimal_imm = binary_to_decimal(imm)
    if (flag_register[-3] == 1):
        flag_register[-4] = "0"
        flag_register[-3] = "0"
        flag_register[-2] = "0"
        flag_register[-1] = "0"
        return decimal_imm
    else:
        return program_counter
    
def jump_if_greater(data,program_counter):
    imm = str(data[-7:])
    decimal_imm = binary_to_decimal(imm)
    if (flag_register[-2] == 1):
        flag_register[-4] = "0"
        flag_register[-3] = "0"
        flag_register[-2] = "0"
        flag_register[-1] = "0"
        return decimal_imm
    else:
        return program_counter
    
def jump_if_equal(data,program_counter):
    imm = str(data[-7:])
    decimal_imm = binary_to_decimal(imm)
    if (flag_register[-1] == 1):
        flag_register[-4] = "0"
        flag_register[-3] = "0"
        flag_register[-2] = "0"
        flag_register[-1] = "0"
        return decimal_imm
    else:
        return program_counter
    
# def hlt(lst):
    # quit()

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

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ BONUS +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

def program_counter_binary_handler(decimal):
    binary = "{0:07b}".format(decimal)
    return binary

j = 0
check = 0
while (j < len(main_list)):
    
    i = main_list[j]
    s=i[0:5]
    
    if(s=='00000'):
        addition(i)

    elif(s=='00001'):
        subtract(i)

    elif(s=='00010'):
        movImmediate(i)

    elif(s=='00011'):
        movRegister(i)

    elif(s=='00100'):
        load(i)

    elif(s=='00101'):
        store(i)
        
    elif(s=='00110'):
        multiply(i)
        
    elif(s=='00111'):
        divide(i)
        
    elif (s=='01000'):
        Right_shift(i)
        
    elif(s=='01001'):
        Left_shift(i)
        
    elif(s=='01010'):
        XOR(i)
        
    elif(s=='01011'):
        OR(i)
        
    elif(s=='01100'):
        AND(i)
        
    elif(s=='01101'):
        NOT(i)
        
    elif(s=='01110'):
        compare(i)

    elif(s=='01111'):
        program_counter = unconditional_jump(i)
        
    elif(s=='11100'):
        program_counter = jump_if_less(i,program_counter)
        if (j != program_counter):
            check == 1
        else:
            check == 0
        
    elif(s=='11101'):
        program_counter = jump_if_greater(i,program_counter)
        if (j != program_counter):
            check == 1
        else:
            check == 0
        
    elif(s=='11111'):
        program_counter = jump_if_equal(i)
        if (j != program_counter):
            check == 1
        else:
            check == 0
        
    elif(s=='11010'):
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
        
    string =""
    string += str(program_counter_binary_handler(program_counter))
    string += "        "

    for i in register_values:
        string += (register_values[i])
        string += (" ")
        
    string += "".join(i for i in flag_register)
    printing_LIST.append(string)

    if (check == 0):
        j += 1
        program_counter += 1
    else:
        j = program_counter
        
    check = 0


for i in printing_LIST:
    print(i)
    
for i in range(128):
    print(Memory[i])


# for i in printing_LIST:         #Printing the binary list line by line into the needed file.
#     sys.stdout.write(i)
# for i in range(128):
#     sys.stdout.write(Memory[i])
