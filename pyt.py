import os
import re
 
 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
 
 

 
def task1():
    clear()
    print("Завдання 1: кількість речень\n")
 
    text = input("Введіть текст: ")
 
    # Речення закінчується на . ! або ?
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    count = len(sentences)
 
    print(f"\nКількість речень: {count}")
 

 
def task2():
    clear()
    print("Завдання 2: паліндром\n")
 
    text = input("Введіть рядок: ")
 

    cleaned = re.sub(r'[^а-яёіїєa-z]', '', text.lower())
 
    if cleaned == cleaned[::-1]:
        print(f'\n"{text}" — це паліндром')
    else:
        print(f'\n"{text}" — не є паліндромом')
 
 
 
RESERVED = {"python", "клас", "функція", "змінна", "цикл", "рядок", "список", "словник"}
 
def task3():
    clear()
    print("Завдання 3: зарезервовані слова\n")
    print("Зарезервовані слова:", ", ".join(sorted(RESERVED)))
    print()
 
    text = input("Введіть текст: ")
 
    def replace_word(match):
        word = match.group()
        if word.lower() in RESERVED:
            return word.upper()
        return word
 
    result = re.sub(r'\b\w+\b', replace_word, text)
 
    print(f"\nЗмінений текст:\n{result}")
 

 
def task4():
    clear()
    print("Завдання 4: видалення між двома символами\n")
 
    text  = input("Введіть рядок:    ")
    char1 = input("Перший символ:    ")
    char2 = input("Другий символ:    ")
 
    pos1 = text.find(char1)
    pos2 = text.find(char2)
 
    if pos1 == -1:
        print(f"\nСимвол '{char1}' не знайдено у рядку.")
        return
    if pos2 == -1:
        print(f"\nСимвол '{char2}' не знайдено у рядку.")
        return
 

    left  = min(pos1, pos2)
    right = max(pos1, pos2)
 
    result = text[:left] + text[right + 1:]
 
    print(f"\nРезультат: {result}")
 
 

 
def task5():
    clear()
    print("Завдання 5: видалення слів із забороненими символами\n")
 
    text    = input("Введіть текст:    ")
    symbols = input("Набір символів:   ")
 
    bad = set(symbols)
 
    words  = text.split()
    result = [w for w in words if not any(ch in bad for ch in w)]
 
    print(f"\nРезультат: {' '.join(result)}")
 
 

 
def task6():
    clear()
    print("Завдання 6: зворотний текст \n")
 
    text = input("Введіть текст: ")
 
    words   = text.split()
    result  = ' '.join(reversed(words))
 
    print(f"\nЗворотний текст: {result}")
 
 
 
TASKS = {
    "1": ("Підрахунок речень у тексті",                         task1),
    "2": ("Перевірка на паліндром",                             task2),
    "3": ("Зарезервовані слова → ВЕРХНІЙ регістр",              task3),
    "4": ("Видалення символів між двома символами",             task4),
    "5": ("Видалення слів із забороненими символами",           task5),
    "6": ("Зворотний текст (переворот на рівні слів)",          task6),
}
 
 
def show_menu():
    clear()
    print("1.Підрахунок речень у тексті")
    print("2.Перевірка на паліндром")
    print("3.Зарезервовані слова → ВЕРХНІЙ регістр")
    print("4.Видалення символів між двома символами")
    print("5.Видалення слів із забороненими символами")
    print("6.Зворотний текст (переворот на рівні слів)")
    print("0.".format("Вийти"))
 
 

while True:
    show_menu()
    choice = input("\nВаш вибір: ").strip()

    if choice == "0":
        clear()
        print("До побачення!")
        break
    elif choice in TASKS:
        _, func = TASKS[choice]
        func()
        input("\nНатисніть Enter, щоб повернутися до меню...")
    else:
        print("Невірний вибір. Спробуйте ще раз.")
        input("Натисніть Enter...")


