# Transportation Cipher

# original: this_is_a_secret_message_that_i_want_to_transmit
# encrypted version: hsi__ertmsaeta__att_rnmtti_sasce_esg_htiwn_otasi

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = lent(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddchars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

        if len(oddChars) < len(evenChars):
            plainText = plainText + evenChars[-1]

        return plainText

# write a stripSpace(text) function here:

def encryptMessage():
    msg = input("Enter the message to encrypt: ")
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is:", cipherText)

# write a ceaserEncrypt(plainText, shift)

def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # encrypt uppercase charecters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        return result
# Time to see if it works...
text = "I HOPE IT WORKS"
s = 4

print("plain Text : ") + text
print("shift pattern : ") + str(s)
print ("cipher: ") + encrypt(text,s)

# write a ceaserDecrypter(cipherText, shift)

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(letters)):
    translated = ''
    for symbol in message:
        if symbol in letters:
            num = letters.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(letters)
            translated = translated + letters[num]
        else:
            translated = translated + symbol



