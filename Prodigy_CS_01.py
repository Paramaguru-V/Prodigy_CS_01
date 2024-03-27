def encrption(sentences,key):
    Cipher_text=''
    for i in sentences:
        if i.isupper():
            Cipher_text +=chr((ord(i) +key-65)%26 +65) 
        elif i.islower():
            Cipher_text +=chr((ord(i) +key-97)%26 +97)
        elif i.isdigit():
            Cipher_text +=chr((ord(i) +key-48)%10 +48)
        else:
             Cipher_text +=i
    return Cipher_text

def decrption(cipher_text,key):
    sentence=''
    for i in cipher_text:
        if i.isupper():
            sentence +=chr((ord(i) -key-65)%26 +65) 
        elif i.islower():
            sentence +=chr((ord(i) -key-97)%26 +97)
        elif i.isdigit():
            sentence +=chr((ord(i) -key-48)%10 +48)
        else:
            sentence +=i
    return sentence

def main():
    while True:
        print("What would You liked to do\n1.Encription\n2.Decription\n3.Exit")
        choice=int(input("\nChoice: "))
        if choice==1:
            sentences=str(input("Enter the text to be Encripted: "))
            key=int(input("Enter the key value"))
            print("The encrypted text is",encrption(sentences,key))
        elif choice==2:
            cipher_text=str(input("Enter the Cipher text to be Decripted: "))
            key=int(input("Enter the key value"))
            print("The decrypted text is",decrption(cipher_text,key))
        elif choice==3:
            break
        else:
            print("Give Correct number as input")

main()
