import re

# for loop format:
# f[<var>;<min>;<max>]...| / f[<var>;<iterable>]...|
FOR_LOOP_PATTERN = "f\[([A-Za-z]+)((;[a-zA-Z0-9]+){1,2})\]"
# if condition format:
# i[<var><condition><var>]...|
IF_CONDI_PATTERN = "i\[([A-Za-z0-9.])+([=><!])([A-Za-z0-9.])+\]"

PATTERN_DICT = {
    "for": FOR_LOOP_PATTERN,
    "if": IF_CONDI_PATTERN
}

number_of_tab = 0

program = "f[i;2;30]i[i<0]print(i)||"
program = "ouiouiouii[i<0]print(i)"
#program = "print(\"oui\")"

output_program = ""


first_match = {key: re.search(value, program) for key, value in PATTERN_DICT.items()}
first_match = {key: value.span() for key, value in first_match.items() if value != None}

if first_match != {}:
    f_m_pattern = min(first_match, key=first_match.get) # get the first occurence
    f_m_index = first_match[f_m_pattern]

    output_program += program[0:f_m_index[0]]
    
    program = program[f_m_index[1]:]
elif len(program) > 0:
    output_program += program
    pass
else:
    # fin du programe
    pass
print(f"{output_program=}")
