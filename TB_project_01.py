def main():
    print("Welcome! I would like to get to know you a little better!")
    print("Here's a few questions.")

    name, college, highschool = conversation()

    print(f"{name}, Thank you for sharing some details about you.")
    print("I learned that you currently attend at {}".format(college))
    print("And you also went to {} highschool!".format(highschool))
    print(f"{name}, It was nice getting to know you!")

def conversation():
    print("What is your name?")
    name = input()
    print(f"{name}, What college do you attend to?")
    college = input()
    print(f"{name}, What highschool did you go to?")
    highschool = input()
    
    return name, college, highschool

if __name__ == "__main__":
    main()