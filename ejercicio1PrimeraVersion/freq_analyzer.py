file_path = '/home/valentina/Desktop/original_message.txt'
freq = [0 for _ in range(26)]

for line in open(file_path).readlines():
    for word in line.split():
        for letter in word:
            if (letter.isalpha() and letter != 'v'):
                index = ord(letter) - ord('A')
                freq[index] = freq[index] + 1
print(freq)

message_freq_order = []

for i in range(26):
    maxNum = -1
    pos = 0
    for index, num in enumerate(freq):
        if (num > maxNum):
            maxNum = num
            pos = index
    message_freq_order.append(chr(pos + ord('A')))
    freq[pos] = -1

print(message_freq_order)
