# Library-class
Консольное приложение для управления библиотекой книг. 
Позволяет добавлять, удалять, искать, изменять статус и просматривать список книг. Данные хранятся в формате JSON, что обеспечивает их сохранение между сеансами.

**ФУНКЦИОНАЛ**

**Добавление книги:**
Пользователь вводит название книги, автора и год издания.
Приложение автоматически генерирует уникальный идентификатор (ID) и устанавливает статус "в наличии".
Книга добавляется в библиотеку, и изменения сохраняются в файле library.json.

**Удаление книги:**
Пользователь вводит ID книги.
Если книга с указанным ID существует, она удаляется из библиотеки.
Данные обновляются в файле.

**Поиск книги:**
Возможность поиска книг по следующим параметрам:
Название (title)
Автор (author)
Год издания (year)
Результаты поиска отображаются в удобном формате.

**Отображение всех книг:**
Выводит список всех книг в библиотеке с указанием их ID, названия, автора, года издания и статуса.

**Изменение статуса книги:**
Пользователь вводит ID книги и новый статус ("в наличии" или "выдана").
Статус обновляется, и изменения сохраняются в файле.


**УСТАНОВКА**

1.Скачайте или клонируйте репозиторий:

	git clone https://github.com/axmadJ3/Library-class.git

2.Перейдите в папку проекта:

	cd Library-class

3.Убедитесь, что у вас установлен Python 3. Запустите приложение:

	python main.py


**ИСПОЛЬЗОВАНИЕ**

**Меню приложения**

После запуска программы будет отображаться меню:

	Меню:
	1. Добавить книгу
	2. Удалить книгу
	3. Найти книгу
	4. Показать все книги
	5. Изменить статус книги
	6. Выйти

**Примеры взаимодействия**

**Добавление книги:**

Введите название, автора и год издания:

	Введите название, автора и год издания:
	Введите название книги: Война и мир
	Введите автора книги: Лев Толстой
	Введите год издания: 1869

**Удаление книги:**

Введите ID книги, которую хотите удалить:

	Введите ID книги для удаления: 1

**Поиск книги:**

Введите параметр поиска (title, author, year) и значение:

	Введите параметр поиска (title, author, year): author
	Введите значение для поиска: Лев Толстой


**Изменение статуса книги:**

Укажите ID книги и новый статус:

	Введите ID книги: 1
	Введите новый статус (в наличии/выдана): выдана


**СТРУКТУРА ДАННЫХ**

Книги хранятся в файле library.json в формате:

	[
	    {
	        "id": 1,
	        "title": "Война и мир",
	        "author": "Лев Толстой",
	        "year": 1869,
	        "status": "в наличии"
	    },
	    {
	        "id": 2,
	        "title": "Преступление и наказание",
	        "author": "Фёдор Достоевский",
	        "year": 1866,
	        "status": "выдана"
	    }
	]
