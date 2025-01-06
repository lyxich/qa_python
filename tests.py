from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # Проверяем установку жанра для книги, которая уже есть в коллекции
    def test_set_genre_existing_book(self):
        collector = BooksCollector()
        name = "Книга1"
        genre = "Фантастика"

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre


    # Проверяем получение жанра для книги, которая есть в коллекции.
    def test_get_genre_existing_book(self):
        collector = BooksCollector()
        name = "Книга1"
        genre = "Фантастика"

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        result_genre = collector.get_book_genre(name)

        assert result_genre == genre


    # Проверяем получение списка книг определённого жанра для книги, которая есть в коллекции
    def test_get_existing_book_of_genre(self):
        collector = BooksCollector()
        name1 = "Книга1"
        genre = "Фантастика"

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre)

        name2 = "Книга2"
        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre)

        result_books = collector.get_books_with_specific_genre(genre)

        expected_result = [name1, name2]
        assert result_books == expected_result


    # Проверяем получение списка жанров книг
    def test_get_books_genres(self):
        collector = BooksCollector()
        name1 = "Книга1"
        genre1 = "Фантастика"

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        name2 = "Книга2"
        genre2 = "Ужасы"

        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre2)

        result_genres = collector.get_books_genre()

        expected_result = {name1: genre1, name2: genre2}
        assert result_genres == expected_result


    # Проверяем получение списка книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        name1 = "Книга1"
        genre1 = "Фантастика"

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        name2 = "Книга2"
        genre2 = "Ужасы"

        collector.add_new_book(name2)
        collector.set_book_genre(name2, genre2)

        result_books = collector.get_books_for_children()

        expected_result = [name1]
        assert result_books == expected_result


    # Проверяем добавление книги в избранное
    def test_add_book_to_favorites(self):
        collector = BooksCollector()
        name1 = "Книга1"
        genre1 = "Фантастика"

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        result_before = collector.favorites
        collector.add_book_in_favorites(name1)

        result_after = collector.favorites

        expected_result = [name1]
        assert result_after == expected_result


    # Проверяем удаление книги из избранного
    def test_delete_book_to_favorites(self):
        collector = BooksCollector()
        name1 = "Книга1"
        genre1 = "Фантастика"

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        result_before = collector.favorites
        collector.delete_book_from_favorites(name1)

        result_after = collector.favorites

        expected_result = []
        assert result_after == expected_result


    # Проверяем получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        name1 = "Книга1"
        genre1 = "Фантастика"

        collector.add_new_book(name1)
        collector.set_book_genre(name1, genre1)

        result_before = collector.favorites
        collector.delete_book_from_favorites(name1)

        result_after = collector.get_list_of_favorites_books()

        expected_result = []
        assert result_after == expected_result

        # Добавляем книгу в избранное
        collector.add_book_in_favorites(name1)

        result_favorite_books = collector.get_list_of_favorites_books()

        expected_favorite_result = [name1]
        assert result_favorite_books == expected_favorite_result