import re

def decoder(program):
    output_program = ""

    # looking for "for" loop
    # they must be in format "f[<var>;<iterable>]...|" or "f[<var>;<begin>;<end>]...|""
    for_pattern = r"f\[([A-Za-z]+)((;[a-zA-Z0-9]+){1,2})\](.*?)\|"
    if re.match(for_pattern, program):
        for_loop = re.search(for_pattern, program)
        argument = for_loop.group(2)[1:].split(";")
        if len(argument) > 1:
            parse_str = f"in range({int(argument[0])}, {int(argument[1])}):"
        else:
            parse_str = f"in {argument}:"
        
        output_program = f"for {for_loop.group(1)} {parse_str}\n\t{for_loop.group(4)}"

    return output_program
