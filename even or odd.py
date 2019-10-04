while True:
    
    try:
        a = int(input("Enter the Number:"))
        break
    
    except:
        print("Please enter a WHOLE NUMBER!")

if a%2:
    print("ODD")
    
else:
    print("EVEN")
