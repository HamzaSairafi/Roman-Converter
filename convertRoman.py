def romanToInt(numeral):
    finalAnswer = 0

    if "CM" in numeral:
        finalAnswer += 900
        numeral = numeral.replace("CM" , " ")
    if "CD" in numeral:
        finalAnswer += 400
        numeral = numeral.replace("CD" , " ")
    if "XC" in numeral:
        finalAnswer += 90
        numeral = numeral.replace("XC" , " ")
    if "XL" in numeral:
        finalAnswer += 40
        numeral = numeral.replace("XL" , " ")
    if "IX" in numeral:
        finalAnswer += 9
        numeral = numeral.replace("IX" , " ")
    if "IV" in numeral:
        finalAnswer += 4
        numeral = numeral.replace("IV" , " ")
    
    for i in numeral:
        if i == 'I':
            finalAnswer += 1
        elif i == 'V':
            finalAnswer +=5
        elif i == 'X':
            finalAnswer +=10
        elif i == 'L':
            finalAnswer +=50
        elif i == 'C':
            finalAnswer +=100
        elif i == 'D':
            finalAnswer +=500
        elif i == 'M':
            finalAnswer +=1000

    print("The roman numerals you entered translates to: " + str(finalAnswer))


def intToRoman(num):
    romanAnswer = ''
    
    while num > 0:
        if num >= 1000:
            romanAnswer += 'M'
            num -= 1000
        elif num >= 900:
            romanAnswer += 'CM'
            num -=900
        elif num >= 500:
            romanAnswer += 'D'
            num -=500
        elif num >= 400:
            romanAnswer += 'CD'
            num -=400
        elif num >= 100:
            romanAnswer += 'C'
            num -=100
        elif num >= 90:
            romanAnswer += 'XC'
            num -=90
        elif num >= 50:
            romanAnswer += 'L'
            num -=50
        elif num >= 40:
            romanAnswer += 'XL'
            num -=40
        elif num >= 10:
            romanAnswer += 'X'
            num -=10
        elif num >= 9:
            romanAnswer += 'IX'
            num -=9
        elif num >= 5:
            romanAnswer += 'V'
            num -=5
        elif num >= 4:
            romanAnswer += 'IV'
            num -=4
        elif num >= 1:
            romanAnswer += 'I'
            num -=1
        else:
            break



    print("The roman numerals you entered translates to: " + str(romanAnswer))





which = input("Select '1' for Roman to inger or Select '2' for inger to Roman: ")

if which == '1':
    numeralInput = input("Enter the roman numerals you want to convert: ")
    romanToInt(numeralInput.upper())
elif which == '2':
    ingerInput = int(input("Enter the Intger you want to convert: "))
    intToRoman(ingerInput)


