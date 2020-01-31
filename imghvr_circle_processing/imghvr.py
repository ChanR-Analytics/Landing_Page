from os import getcwd, listdir

data_path = getcwd() + "/imghvr_circle_processing"
sorted(listdir(data_path))

lines = []

with open(f"{data_path}/{sorted(listdir(data_path))[2]}", 'r') as file:
    for line in file.readlines():
        lines.append(line)


with open(f"{data_path}/{sorted(listdir(data_path))[0]}", 'w') as new_file:
    for line in lines:
        if 'imghvr-' in line:
            line = line.replace('imghvr-', 'imghvr-circle')
        new_file.write(line)
