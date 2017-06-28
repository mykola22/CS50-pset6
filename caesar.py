import sys

def main ():
    #checking proper number of arguments and format of argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print ("Give me another argument.")
        exit(1)
    
    #creating the key for encrypting 
    key = int(sys.argv[1])
    
    #get the text from user 
    print("plaintext:", end=" ")
    text = input()
    
    #start printing the final message 
    print("ciphertext:", end=" ")
    
    # encrypting the message
    for i in text:
        if i.isupper():
            print(chr(((ord(i) - 65 + key) % 26)+65), end="")
        elif i.islower():
            print(chr(((ord(i) - 97 + key) % 26)+97), end="")
        else:
            print(i, end="")
    print("")
            
if __name__ == "__main__":
    main()