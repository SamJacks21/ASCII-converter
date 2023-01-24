import re

def DecimalToText():
    inputs = input("Please give values, needs to be in a space seperated list\n").split()
    output = ''
    for i in inputs:
        output += chr(int(i))
    print(output)

def AsciiToText():
    inputs = input("Please give values, needs to be in a space seperated list\n").split()
    output = []
    for i in inputs:
        cleansedInput = re.sub('[a-zA-Z]', '', i)
        output.append(chr(int(cleansedInp)))
    print(''.join(output))

def TextFlipper():
    inputs = input("Please give input to switch around\n")
    listOutput = []
    for i in range(0, len(inputs), 4):
        byte = inputs[i:(i+4)]
        listOutput.append(''.join(byte))
    textOutput = ''
    for i in reversed(listOutput):
        textOutput = textOutput + i[::-1]
    print(textOutput)

def main():
    action = input("What do you want to complete:\n"
    +"1. Convert Decimal to Text\n"
    +"2. Convert Ascii to Text\n"
    +"3. Flip some Text\n")

    match action:
        case "1":
            DecimalToText()
        case "2":
            AsciiToText()
        case "3":
            TextFlipper()
        case _:
            quit()

if __name__ == "__main__":
    main()