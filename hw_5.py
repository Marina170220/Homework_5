easy_questions = [
    {"question": "She cannot talk ______ walk at the same time.",
     "options": ["and", "try", "if", "except", "while"],
     "answer": "and",
     },
    {"question": "I am American. I am from Boston. ______ hair is brown.",
     "options": ["The", "My", "Mine", "I", "These"],
     "answer": "My",
     },
    {"question": "Last Sunday they ______ to the football game.",
     "options": ["went", "go", "gone", "were", "going"],
     "answer": "went",
     }
]

normal_questions = [
    {"question": "The soldiers ______ all the villagers.",
     "options": ["listened", "killed", "waited", "died"],
     "answer": "killed",
     },
    {"question": "Chocolate is my greatest ______.",
     "options": ["weakness", "weakened", "weak", "weaken", "weakly"],
     "answer": "weakness",
     },
    {"question": "Some birds are sitting ______ the house.",
     "options": ["onto", "for", "to", "after", "on top of"],
     "answer": "on top of",
     }
]

hard_questions = [
    {"question": "Hello, how are you? ______",
     "options": ["Oh man, I's beat!", "I'm fine, thanks.", "I am doing finely."],
     "answer": "I'm fine, thanks.",
     },
    {"question": "______ is your house? It's the small grey one.",
     "options": ["When", "Which", "What", "Who", "Why"],
     "answer": "Which",
     },
    {"question": "How many days are there in February? ______",
     "options": ["There are 28.", "They are 28.", "In February, there are 28.", "Are only 28 days."],
     "answer": "There are 28.",
     }
]

letters = ['A', 'B', 'C', 'D', 'E']

answers = {  # Словарь для записи результатов ответов пользователя
    0: ['Низкая сложность', []],
    # Ключ-уровень, значение - список с указанием уровня сложности и списком результатов типа boolean
    1: ['Нормальная сложность', []],
    2: ['Высокая сложность', []],
}


def change_difficulty(answer, level):  # answer-boolean
    """
    Меняет уровень сложности
    """
    if answer:
        if level <= 1:
            level += 1
        elif level == 2:
            print('Вы остаётесь на прежнем уровне.')

    else:
        if level >= 1:
            level -= 1
        elif level == 0:
            print('Вы остаётесь на прежнем уровне.')

    return level


def next_question(level):
    """
    Возвращает очередной словарь с данными вопроса указанной сложности
    """
    if level == 0:
        next_question = easy_questions[len(answers[0][1])]
        # print(next_question)                  #Раскомментировать для проверки корректности работы кода
    elif level == 1:
        next_question = normal_questions[len(answers[1][1])]
        # print(next_question)                  #Раскомментировать для проверки корректности работы кода
    elif level == 2:
        next_question = hard_questions[len(answers[2][1])]
        # print(next_question)                  #Раскомментировать для проверки корректности работы кода

    return next_question


def correct_letter(letter_list, option_list, answer):
    """
    Возвращает букву, соответвующую правильному варианту ответа
    """
    correct_letter = ''  # буква, соответствующая верному варианту ответа

    for letter, option in zip(letter_list, option_list):
        if option == answer:
            correct_letter = letter

    # print(correct_letter)                    #Раскомментировать для проверки корректности работы кода

    return correct_letter


def print_options(letter_list, option_list):
    """
    Выводит список вариантов ответов
    """
    for letter, option in zip(letter_list, option_list):
        print(f'{letter}: {option}')


def print_statistics():
    """
    Выводит статистику
    """
    print(f'У нас закончились вопросы!\n'
          f'{answers[0][0]}: {sum(answers[0][1])}/{len(answers[0][1])}\n'
          f'{answers[1][0]}: {sum(answers[1][1])}/{len(answers[1][1])}\n'
          f'{answers[2][0]}: {sum(answers[2][1])}/{len(answers[2][1])}\n')


print('Добро пожаловать в адаптивный тренажер!')

amount_of_questions = 1  # количество заданных вопросов
difficulty = 1

while amount_of_questions <= 3:

    print(f'Вопрос {amount_of_questions}, {answers[difficulty][0]}\n'
          f'{next_question(difficulty)["question"]}')
    print('Выберите верный ответ: ')
    user = input(print_options(letters, next_question(difficulty)["options"]))
    if user.lower() == next_question(difficulty)["answer"].lower() or user.upper() == correct_letter(letters,
                                                                                                     next_question(
                                                                                                         difficulty)[
                                                                                                         "options"],
                                                                                                     next_question(
                                                                                                         difficulty)[
                                                                                                         "answer"]):
        users_answer = True
        print('Верно! Уровень сложности повышен!')
        answers[difficulty][1].append(users_answer)
        # print(f'Список результатов: {answers[difficulty][1]}')     #Раскомментировать для проверки корректности работы кода
        amount_of_questions += 1
        difficulty = change_difficulty(users_answer, difficulty)
        # print(f'Новый уровень сложности: {difficulty}')            #Раскомментировать для проверки корректности работы кода

    else:
        users_answer = False
        print(f'Неверно! Правильно – {next_question(difficulty)["answer"]}. Уровень сложности понижен.')
        answers[difficulty][1].append(users_answer)
        # print(f'Список результатов: {answers[difficulty][1]}')     #Раскомментировать для проверки корректности работы кода
        amount_of_questions += 1
        difficulty = change_difficulty(users_answer, difficulty)
        # print(f'Новый уровень сложности: {difficulty}')            #Раскомментировать для проверки корректности работы кода

    print_statistics()
