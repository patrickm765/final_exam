# Question 1

C = 299792458 


def calc_f(v_values, fo_values):
    f_values = []
    for v, fo in zip(v_values, fo_values):
        f = (1 + v / C) * fo
        f_values.append(f)
    return f_values

def write_f(f_values):
    with open("f.txt", "w") as file:
        for i, f in enumerate(f_values):
            file.write(f"{i}: {f}\n")

def read_numbers(file_path):
    values = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                values.append(float(line.strip()))  # Convert each line to a float
    except FileNotFoundError:
        print(f"File '{file_path}' error")
    return values


v_values = read_numbers("v.txt")
fo_values = read_numbers("fo.txt")


if v_values and fo_values:
    f_values = calc_f(v_values, fo_values)

    
    write_f(f_values)