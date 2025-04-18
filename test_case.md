# Тест-кейсы

## №1. "Создание нового клиента"

### Описание
Проверка функциональности создания нового клиента.

### Предусловие
- Открыта страница [Banking Project](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager).
- Открыта вкладка "Bank Manager Login".

### Шаги
1. Нажать на кнопку "Add Customer".
2. Ввести First Name, сгенерированное на основе Post Code.
3. Ввести Last Name.
4. Ввести Post Code (случайное 10-значное число).
5. Нажать "Add Customer".
6. Подтвердить всплывающее уведомление.

### **Ожидаемый результат**
- Появляется всплывающее окно с сообщением "Customer added successfully with customer id :(номер ID)".

### Постусловие
Нажать кнопку "Ok" во всплывающем окне.


## №2. "Сортировка клиентов по имени"

### Описание
Проверка функциональности сортировки списка клиентов по имени.

### Предусловия
- В системе должны быть добавлены клиенты с разными именами.

### Шаги
1. Перейти на вкладку "Customers".
2. Нажать на заголовок колонки "First Name" (должна выполниться сортировка по убыванию).
3. Нажать повторно (должна выполниться сортировка по возрастанию).
4. Сравнить порядок имен до и после сортировки.

### Ожидаемый результат
- После первого нажатия имена сортируются по убыванию.
- После второго нажатия имена сортируются по возрастанию.

### Постусловие
В системе сохраняется последний порядок сортировки.


## №3. Удаление клиента

### Описание
Проверка функциональности удаления клиента с именем, у которого длина будет ближе к среднему арифметическому.

### Предусловия
- В системе должны быть зарегистрированы несколько клиентов.

### Шаги
1. Перейти на вкладку "Customers".
2. Получить список всех имен клиентов.
3. Вычислить длину каждого имени.
4. Найти среднее арифметическое длины имен.
5. Найти имя, длина которого ближе всего к среднему значению.
6. Нажать кнопку "Delete", относящуюся к данному клиенту.
7. Проверить, что клиент исчез из списка.

### Ожидаемый результат
- Клиент с наиболее близкой длиной имени к среднему арифметическому удаляется.
- В таблице этот клиент больше не отображается.

### Постусловие
Список клиентов отображается только с оставшимися пользователями.