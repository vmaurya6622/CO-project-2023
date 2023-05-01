opcode = {'add': '00000', 'sub': '00001', 'mov': '00011', 'ld': '00100', 'st': '00101', 'mul': '00110', 'div': '00111', 
    'rs': '01000', 'ls': '01001', 'xor': '01010', 'or': '01011', 'and': '01100', 'not': '01101', 'cmp': '01110', 
    'jmp': '01111', 'jlt': '11100', 'jgt': '11101', 'je': '11111', 'hlt': '11010'}

registers = {'R0' : '000','R1' : '001','R2' : '010','R3' : '011',
            'R4' : '100','R5' : '101','R6' : '110','FLAGS' : '111'}

unused_bit = {'add': 2, 'sub': 2, 'mov': 5, 'ld': 1, 'st': 1, 'mul': 2, 'div': 5, 'rs': 1, 'ls': 1, 
            'xor': 2, 'or': 2, 'and': 2, 'not': 5, 'cmp': 5, 'jmp': 4, 'jlt': 4, 'jgt': 4, 'je': 4, 'hlt': 11}

print(opcode)
print(registers)
print(unused_bit)

"""
total bits = 16
register = 3
op code = 5
immediate value = 7
memory address = 7
unused bit = depends
halt = 5 op code + 11 unused_bit

"""

