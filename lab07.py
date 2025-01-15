def conversation():
    print("Do you like coding in python? Answer yes or no")
    answer = input().strip().lower()

    if  answer == "yes":
        print("Thats good - the United States needs more coders!!")
    
    elif answer == "no":
        print("Perhaps you will change your mind")
    else:
        print("I dont understand")
    conversation()

def main():
    print("Welcome to my conversation program")
    conversation ()
    print("Thanks for chatting with me ")

if __name__ == "__main__":
    main()