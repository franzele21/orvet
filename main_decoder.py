import re

# for loop format:
# f[<var>;<min>;<max>]...| / f[<var>;<iterable>]...|
FOR_LOOP_PATTERN = "f\[([A-Za-z]+)((;[a-zA-Z0-9]+){1,2})\]"
# if condition format:
# i[<var><condition><var>]...|
IF_CONDI_PATTERN = "i\[([A-Za-z0-9.])+([=><!])([A-Za-z0-9.])+\]"

PRINT_PATTERN = "p\[(.*?)\]"

PATTERN_DICT = {
    "for": FOR_LOOP_PATTERN,
    "if": IF_CONDI_PATTERN,
    "print": PRINT_PATTERN
}


program = "f[i;2;30]i[i<0]print(i)||"
program = "i=3i[i>4]print(\"oui\")|q=0i[i<4]print(i);print(q)|print(q+i);print(i*q)"
#program = "print(\"oui\")"

output_program = ""

def translator(pattern, prgm, normal_context=True):
    def condition_translator(condition):
        if condition == "=":
            return "=="
        elif condition == "!":
            return "!="
        else:
            return condition

    def change_type(var):
        try:
            return int(var)
        except:
            try:
                return float(var)
            except:
                return var
                
    match pattern:
        case "if":
            if_condition = re.match(IF_CONDI_PATTERN, prgm)
            condition = f"{change_type(if_condition.group(1))} {condition_translator(if_condition.group(2))} {change_type(if_condition.group(3))}"
            statement = "if " + condition + ":" if normal_context else ""

            return statement

        case "for":
            pass
        case "print":
            pass
        case _:
            return prgm

def decode(program, output_prgm="", number_of_tab = 0):
    first_match = {key: re.search(value, program) for key, value in PATTERN_DICT.items()}
    first_match = {key: value.span() for key, value in first_match.items() if value != None}

    if first_match != {}:
        f_m_pattern = min(first_match, key=first_match.get) # get the first occurence
        f_m_index = first_match[f_m_pattern]

        tmp_program = "\n".join(program[0:f_m_index[0]].split(";")).split("|")
        for line in tmp_program:
            line = "\t" * number_of_tab + line
            line = line.replace("\n", ("\n"+"\t"*number_of_tab))
            output_prgm += line + "\n"
            number_of_tab = max(0, number_of_tab-1)
        
        output_prgm += "\t" * number_of_tab + translator(f_m_pattern, program[f_m_index[0]:f_m_index[1]+1]) + "\n"
        number_of_tab += 1
        
        
        return decode(program[f_m_index[1]:], output_prgm, number_of_tab)

    elif len(program) > 0:
        tmp_program = "\n".join(program.split(";")).split("|")
        print(tmp_program)
        
        for line in tmp_program:
            line= "\t" * number_of_tab + line
            line = line.replace("\n", ("\n"+"\t"*number_of_tab))
            output_prgm += line + "\n"
            number_of_tab -= 1

        return output_prgm
    else:
        return output_prgm

decoded_code = decode(program)
print(decoded_code)
exec(decoded_code)
