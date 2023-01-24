value = []
flag = ""
for number in nums:
    flag += chr(number)
print(flag)


flag = 'ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3ÿ~R}'

blocks = []
for i in range(0, len(flag), 4):
    chunk = flag[i::]
    if len(chunk) > 4:
        chunk = chunk[0:4]
    blocks.append(''.join(chunk))

output = ''
for i in blocks:
    output = output + i[::-1]

print(output)


ist = [chr(0x62),chr(0x64),chr(0x61),chr(0x36),chr(0x38),chr(0x66),chr(0x37),chr(0x35)]
for i in list:
    print(i)