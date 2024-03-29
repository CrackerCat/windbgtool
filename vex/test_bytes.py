import sys
import os
import analyzer

def Dis(bytes):
    disasm=analyzer.Disassembler(mode=32)
    address=0

    for instruction in disasm.Disasm(bytes,address):       
        operands_str=''
        for operand in instruction['Operands']:
            if operands_str!='':
                operands_str+=', '
            operands_str+=operand['Value']
            
        print(instruction['Opcode'], operands_str)

for i in range(0,0xff,1):
    print('>> %.2x' % i)
    Dis(b'\x8b' + str.encode(chr(i)))
