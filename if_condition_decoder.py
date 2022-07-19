import re

def decoder(program):
    output_program = ""

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
    
    # looking for "if" condition
    # they must be in format "i[<var><condition><var>]...|"
    # the conditions are: 
    # "==" to "="
    # "!=" to "!"
    # "<" and ">" are the same
    # ">=" and "<=" doesn't exist
    # a valid if: i[i<3]print(i)|
    if_pattern = "i\[([A-Za-z0-9.])+([=><!])([A-Za-z0-9.])+\](.*)\|"
    if re.match(if_pattern, program):
        if_condition = re.search(if_pattern, program)
        condition = f"{change_type(if_condition.group(1))} {condition_translator(if_condition.group(2))} {change_type(if_condition.group(3))}" 
        
        output_program = f"if {condition}:\n\t{if_condition.group(4)}"

    return output_program
