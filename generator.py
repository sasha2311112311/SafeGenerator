import random

def generator2():
    print("процесс генерации почты запущен!")  
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    dlina = int(input("длина почты символы после @ не в счет:   "))
    formats = int(input('формат почты 1-@gmail.com 2-@mail.ru:   '))
    if formats == 1:
        print(*random.sample(letters, dlina), "@gmail.com", sep='')
    elif formats == 2:
        print(*random.sample(letters, dlina), "@mail.ru", sep='')
    else:
        print("введи 1 или 2!")

def generator():
    print("процесс генерации пароля запущен!")
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    length = int(input('введи длину пароля: '))
    total = int(input('введи сколько раз мне сгенерировать пароль: '))
    for i in range(total):
        result = ''.join(random.choices(letters, k=length))
        print(result)

print('Привет! Я Генератор. Могу сгенерировать тебе email(формата gmail или mail) или надежный пароль ')
bem = input('Чтобы сгенерировать надежный пароль нажмите 1 чтобы сгенерировать email нажмите 2: ')

print(f"Вы ввели: '{bem}'")  
if bem == '1':
    generator()
elif bem == '2':
    generator2()
else:
    print("дурак! введи 1 или 2")

input("press enter to exit")