import random
def generate_secret_word():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_word = ''
    for i in range(4):
        random_index = random.randint(0, len(digits) - 1)
        secret_word += str(digits[random_index])
        digits.pop(random_index)
    return secret_word
def calculate_bulls_count(user_word, secret_word):
    counter = 0
    for i in range(len(secret_word)):
        if secret_word[i] == user_word[i]:
            counter += 1
    return counter

def calculate_cows_count(user_word, secret_word):
    counter = 0
    for i in range(len(secret_word)):
        if secret_word[i] != user_word[i] and user_word[i] in secret_word:
            counter += 1
    return counter
def game():
    secret_word = generate_secret_word()
    while True:    
        print("Найдите число, задуманое компьютером!")
        user_word = input()
        bulls_count = calculate_bulls_count(user_word, secret_word)
        cows_count = calculate_cows_count(user_word, secret_word)
    
        print(bulls_count, 'быкаов', cows_count, 'коров')
    
        if bulls_count == 4:
            print('УРА! Ты победил!')
            print('Вы хотите еще сыграть? (Да/Нет)')
            answer = input()
            if answer == 'Да':
                game()
            break
game()