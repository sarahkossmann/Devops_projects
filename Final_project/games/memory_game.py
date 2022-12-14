from random import randint
from time import sleep

difficulty_list_memory_game = []

def memory_game():
    while True:
        try:
            difficulty = int(input("Choose the level of difficulty between 1 to 5: "))
        except ValueError:
            print("ERROR! Not an number! Please enter only numeric characters.")
            continue
        if difficulty > 5:
            print("Please choose a number not higher than 5")
            continue
        attempts = 3
        print("A sequence of numbers will appear for one second. Remember them.")
        sleep(2)
        sequence_of_numbers = [(randint(1, 100)) for i in range(difficulty)]
        sleep(2)
        print(sequence_of_numbers, end="")
        sleep(1)
        print(" " * len(sequence_of_numbers), end="\r")
        sleep(1)

        while True:
            while attempts > 0:
                user_answer_number = str(input("Guess the number(s) you just saw (in the right order). \nProvide list of numbers separated by comma, e.g. 1,2,3. \nType the sequence here: "))
                user_answer_split = user_answer_number.split(',')

                if len(user_answer_split) != difficulty:
                    print(f'Please enter {difficulty} numbers')
                    continue

                flag = True
                for elem in user_answer_split:
                    if not elem.isnumeric():
                        flag = False
                        break
                if not flag:
                    print('Please enter only numbers')
                    break

                for i in range(len(sequence_of_numbers)):
                    sequence_of_numbers[i] = str(sequence_of_numbers[i])
                if sequence_of_numbers == user_answer_split:
                    print('Congrats! You won!')
                    difficulty_list_memory_game.append(difficulty)
                    return
                else:
                    attempts -= 1
                    print(f"You have {attempts} attempt(s) left.")

            if attempts == 0:
                print('Game over')
                difficulty_list_memory_game.append(0)
                return