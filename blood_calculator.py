def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
         print("Make a choice")
         print("9 - quit")
         choice = int(input("Make a choice: "))
         print(type(choice))
         if choice ==9:
            keep_running = False
        
   
    print(choice)
    return choice

interface()