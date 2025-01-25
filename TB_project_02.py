def main():
    print("Welcome to my conversation program")
    print("I will keep asking questions until you type 'exit'.")

    question_count= 0

    while True:

        name = input("1. What is your name?")
        if name.lower() == "exit":
         break
        question_count+= 1

        tvshow = input(f"2. What is your favorite show {name}?")
        if tvshow.lower() == "exit":
         break
        question_count+= 1

        answer = input(f"3.Do you like programming {name}?")
        if answer.lower() == "exit":
         break
        question_count+= 1

        hobbies = input(f"4.Whats a hobby you like to do {name}?")
        if hobbies.lower() == "exit":
         break
        question_count+= 1

    print(f"Goodbye!, you answered {question_count} questions. Thanks for chatting with me!")

if __name__ == "__main__":
    main()