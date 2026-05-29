def encrypt(text, shift):
    res = ""
    for char in text:
    
        res += chr(ord(char) + shift)
    return res

def decrypt(text, shift):
    res = ""
    for char in text:
        
        res += chr(ord(char) - shift)
    return res


while True:
    word = input("Enter the word: ")
    if word == "0":
        break
    shift = 3  

    
    secret = encrypt(word, shift)
    print("Encrypted:", secret)

    
    original = decrypt(secret, shift)
    print("Decrypted:", original)
