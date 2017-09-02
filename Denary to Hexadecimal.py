#DISCLAIMER
#I ACIDENTALLY NAMED THE FINALLY DENARY. IT SHOULD BE DECIMAL.

global hexArray

hexArray = ["A","B","C","D","E","F"]

def decimalToHexa(inputDec):
    finalHex = ""
    while inputDec > 0:

        tempNum = inputDec % 16
        tempStr = ""

        if tempNum >= 10:
            tempNum = tempNum - 10
            tempStr = hexArray[tempNum]

        else:
            tempStr = str(tempNum)

        finalHex = tempStr + finalHex
        inputDec = inputDec/16
    return finalHex

def hexaToDecimal(inputHexa):
    count = 0
    finalDec = 0
    tempNum = 0
    hexaLen = len(inputHexa)
    index = hexaLen-1

    while (hexaLen > 0):
        currentChar = inputHexa[index]
        try:
            int(currentChar)
            currentChar = int(currentChar)
            tempNum = currentChar * 16 ** count
        except ValueError:
            print("exception")

            for x in range(0, len(hexArray)):
                if hexArray[x] == currentChar:
                    print("this is the current: " + currentChar)
                    decimalVersion = x + 10
                    #print("aisudasd" + decimalVersion)
                    tempNum = decimalVersion * 16 ** count
                    break

        tempNum = int(tempNum)
        finalDec = tempNum + finalDec
        index -= 1
        hexaLen -= 1
        count += 1
    print(finalDec)




while True:
    choice = input("Hello.\nWould you like to: "
                     "\n1) Convert binary to hexadecimal."
                     "\n2) Convert hexadecimal to binary."
                     "\n3) Exit.")
    if choice == 1:
        inputDec = input("\nPlease enter the decimal number you would like to convert: ")
        print("\nYour hexadecimal number is this: "+ decimalToHexa(inputDec))

    elif choice == 2:
        inputHex = raw_input("\nPlease enter the hexadecimal number you would like to convert: ")
        hexaToDecimal(inputHex)
    elif choice == 3:
        print("bye")
        break
    else:
        print("Try again.")


    print("\n\n")
