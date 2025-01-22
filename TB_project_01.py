def main():
    print("Welcome! I would like to get to know you a little better!")
    print("Here's a few questions.")

    name, college, highschool,institution = conversation()

    print(f"{name}, Thank you for sharing some details about you.")
    print("I learned that you currently attend at {}".format(college))
    print("And you also went to {} highschool!".format(highschool))
    print(f"You think {institution} is more fun than {highschool}.")
    print(f"{name}, It was nice getting to know you!")

def conversation():
    name = input("What is your name?")
    college = input(f"{name}, What college do you attend to?")
    highschool = input(f"{name}, What highschool did you go to?")
    institution = input(f"{name}, which institute is more fun?")
    
    return name, college, highschool, institution

if __name__ == "__main__":
    main()