message_freq_order = ['X', 'E', 'K', 'I', 'C', 'J', 'T', 'A', 'R', 'Z', 'H', 'N', 'P', 'D', 'O', 'Q', 'V', 'S', 'G', 'U', 'M', 'F', 'L', 'B', 'W', 'Y']

file_path = '/home/valentina/Desktop/mensaje.txt'
spanish_freq_order = ['E', 'A', 'R', 'O', 'I', 'N', 'L', 'D', 'C', 'U', 'T', 'S', 'M', 'P', 'F', 'B', 'Y', 'Q', 'J', 'G', 'H', 'X', 'Z', 'V', 'K', 'W']
# Las paso a minuscula para evitar conflicto entre letras cambiadas y letras originales
spanish_freq_order = list(map(str.lower, spanish_freq_order))

for i in range(26):
    with open(file_path, 'r') as file :
        data = file.read()

    # Replace the target string
    data = data.replace(message_freq_order[i], spanish_freq_order[i])

    # Write the file out again
    with open(file_path, 'w') as file:
        file.write(data)

