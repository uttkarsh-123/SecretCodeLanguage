import random
randomCharSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
encodOrDecode = input("Enter \'0\' to encode and \'1\' to decode a string :\t")
if encodOrDecode == "0":
    str1 = input("Enter a random string to encode it : ")
    initialList = str1.split()
    finalList = []
    for initialword in initialList:
        if len(initialword)<4:
            finalList.append(initialword[::-1])
        else:
            finalWord = initialword[1:]
            finalWord += initialword[0]
            for i in range(3):
                finalWord += random.choice(randomCharSet)
            initialChars = random.choice(randomCharSet)
            for i in range(2):
                initialChars += random.choice(randomCharSet)
            finalWord = initialChars + finalWord
            finalList.append(finalWord)
    finalStr = ""
    for finalWord in finalList:
        finalStr = finalStr + finalWord + " "
    print(finalStr)
elif encodOrDecode == "1":
    str1 = input("Enter a string to decode it :")
    initialList = str1.split()
    finalList = []
    for initialword in initialList:
        if len(initialword)<4:
            finalList.append(initialword[::-1])
        else:
            finalWord = initialword[3:-3]
            finalWord = finalWord[:len(finalWord)-1]
            finalWord = initialword[-4] + finalWord
            finalList.append(finalWord)
    finalStr = ""
    for finalWord in finalList:
        finalStr = finalStr + finalWord + " "
    print(finalStr)
else:
    raise ValueError("Add a valid input.")
