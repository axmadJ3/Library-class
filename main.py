import json
from typing import List, Dict, Optional


class Book:
    """Класс для представления книги."""
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict:
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """Создает объект книги из словаря."""
        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])


class Library:
    """Класс для управления библиотекой."""
    def __init__(self, data_file: str = "library.json"):
        self.data_file = data_file
        self.books: List[Book] = []
        self.load_books()

    def load_books(self):
        """Загружает данные из файла."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            print("Ошибка: Невозможно прочитать файл данных.")

    def save_books(self):
        """Сохраняет данные в файл."""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавляет новую книгу в библиотеку."""
        book_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' успешно добавлена.")

    def remove_book(self, book_id: int):
        """Удаляет книгу из библиотеки по ID."""
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} успешно удалена.")
        else:
            print("Ошибка: Книга с таким ID не найдена.")

    def search_books(self, key: str, value: str):
        """Ищет книги по указанному параметру."""
        found_books = [book for book in self.books if str(getattr(book, key, "")).lower() == value.lower()]
        if found_books:
            print("Найденные книги:")
            self.display_books(found_books)
        else:
            print("Книги не найдены.")

    def display_books(self, books: Optional[List[Book]] = None):
        """Отображает список книг."""
        books = books or self.books
        if books:
            for book in books:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
        else:
            print("Библиотека пуста.")

    def update_status(self, book_id: int, new_status: str):
        """Обновляет статус книги."""
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            book.status = new_status
            self.save_books()
            print(f"Статус книги с ID {book_id} обновлен на '{new_status}'.")
        else:
            print("Ошибка: Книга с таким ID не найдена.")


def main():
    """Основная функция для взаимодействия с пользователем."""
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ").strip()
        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания: "))
                library.add_book(title, author, year)
            except ValueError:
                print("Ошибка: Год издания должен быть числом.")
        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                library.remove_book(book_id)
            except ValueError:
                print("Ошибка: ID должен быть числом.")
        elif choice == "3":
            key = input("Введите параметр поиска (title, author, year): ").strip().lower()
            if key in {"title", "author", "year"}:
                value = input("Введите значение для поиска: ").strip()
                library.search_books(key, value)
            else:
                print("Ошибка: Некорректный параметр поиска.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги: "))
                new_status = input("Введите новый статус (в наличии/выдана): ").strip()
                if new_status in {"в наличии", "выдана"}:
                    library.update_status(book_id, new_status)
                else:
                    print("Ошибка: Некорректный статус.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Некорректный выбор.")


if __name__ == "__main__":
    main()
