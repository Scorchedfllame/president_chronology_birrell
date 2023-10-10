from files.view import *
import random
import string
import time
import re


def remove_date(question: str):
    return re.sub("[\(].*?[\)]", "", question)


def main():
    alphabet = string.ascii_lowercase
    key = {}
    questions = []
    data = get_data()
    for i in data.values():
        questions += i
    answers = list(data.keys())
    for i in range(len(answers)):
        key[alphabet[i]] = answers[i]
    asked = []
    inverse = {}
    for i in data.items():
        for x in i[1]:
            inverse[x] = i[0]
    streak = 0
    answer = ''
    while len(asked) < len(questions):
        os.system('cls||clear')
        print(f'Question {len(asked) + 1}/{len(questions)}')
        print(f'Streak: {streak}\n')
        for i in key.items():
            print(f'{i[0]}: {i[1]}')
        question_number = random.randint(0, len(questions)-1)
        question = questions[question_number]
        if not(question in asked):
            asked.append(question)
            print(remove_date(question))
            answer = input().lower().strip()[0]
            if answer:
                if key[answer] == inverse[question]:
                    print("Yay")
                    time.sleep(1)
                    streak += 1
                else:
                    print(f"FAILURE: {inverse[question]}")
                    time.sleep(2)
                    streak = 0
            else:
                print(f"NOT RECOGNIZED. {inverse[question]}")
                time.sleep(2)


if __name__ == "__main__":
    main()
