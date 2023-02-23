def mov(dict,x,y):
    if y in dict:
        dict[x] = dict[y]
    else:
        dict[x] = int(y)
    return dict

def inc(dict,x):
    dict[x] += 1
    return dict

def dec(dict,x):
    dict[x] = dict[x] - 1
    return dict

def add(dict,x,y):
    if y in dict:
        dict[x] += dict[y]
    else:
        dict[x] += int(y)
    return dict

def sub(dict,x,y):
    if y in dict:
        dict[x] -= dict[y]
    else:
        dict[x] -= int(y)
    return dict

def mul(dict,x,y):
    if y in dict:
        dict[x] *= dict[y]
    else:
        dict[x] *= int(y)
    return dict

def div(dict,x,y):
    if y in dict:
        dict[x] /= dict[y]
    else:
        dict[x] /= int(y)
    return dict

def 

def simple_assembler(program):
    print(program)
    dict_registers = {}
    function_list = []
    for instruction in program:
        function_list.append(instruction.split())
    i = 0
    while i < len(function_list):
        function = function_list[i]
        if function[0] == "mov":
            if function[1] not in dict_registers:
                dict_registers[function[1]] = 0
            mov(dict_registers,function[1],function[2])
        if function[0] == "inc":
            inc(dict_registers,function[1])
        if  function[0] == "dec":
            dec(dict_registers,function[1])
        if function[0] == "jnz":
            if function[1] in dict_registers and dict_registers[function[1]] != 0:
                if function[2] in dict_registers:
                    i = i + dict_registers[function[2]]
                else:
                    i = i + int(function[2])
            if function[1] not in dict_registers and function[1] != 0:
                if function[2] in dict_registers:
                    i = i + dict_registers[function[2]]
                else:
                    i = i + int(function[2])
            if function[1] in dict_registers and dict_registers[function[1]] == 0:
                i = i = i + 1
            continue
        i = i + 1
    return dict_registers