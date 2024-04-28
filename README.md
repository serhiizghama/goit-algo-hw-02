# goit-algo-hw-02

# Завдання 1

Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.

Ось псевдокод для завдання з використанням черги (Queue з модуля queue в Python) для системи обробки заявок:

```
import Queue

Створити чергу заявок

queue = Queue()

Функція generate_request():
Створити нову заявку
Додати заявку до черги

Функція process_request():
Якщо черга не пуста:
Видалити заявку з черги
Обробити заявку
Інакше:
Вивести повідомлення, що черга пуста


Головний цикл програми:
Поки користувач не вийде з програми:
Виконати generate_request() для створення нових заявок
Виконати process_request() для обробки заявок
```

У цьому псевдокоді використовуються дві основні функції: generate_request(), яка генерує нові заявки та додає їх до черги, та process_request(), яка обробляє заявки, видаляючи їх із черги. Головний цикл програми виконує ці функції, імітуючи постійний потік нових заявок та їх обробку.

# Завдання 2

Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.


# Завдання 3

У багатьох мовах програмування ми маємо справу з виразами, виділеними символами-розділювачами, такими як круглі ( ), квадратні [ ] або фігурні дужки { }.

Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі симетричні, несиметричні, наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.
