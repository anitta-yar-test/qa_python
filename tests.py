from typing import Literal
import pytest 
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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    #Тест проверяет что у новой добавленной книги нет жанра
    @pytest.mark.parametrize('name_book',['Гиперион','1984','Оно','Преступление и наказание'])
    def test_add_new_book_add_no_genre(self, name_book: Literal['Гиперион'] | Literal['1984'] | Literal['Оно'] | Literal['Преступление и наказание']):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert  collector.get_book_genre(name_book) == '' 

   # проверят установлен ли книге жанр 
    def test_set_book_genre_not_null(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre("1984","Фантастика")
        assert collector.get_book_genre("1984")!=''
 
    # проверяет что удается получить  жанр книги по её имени
    def test_get_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre('Оно','Ужасы')
        assert  collector.get_book_genre('Оно') == 'Ужасы'

    # проверяет количество книг  с определённым жанром
    @pytest.mark.parametrize('name_book,genre',[
        ['Гиперион','Фантастика'],
        ['1984','Фантастика'],
        ['Оно', 'Ужасы'],
        ['Шрек','Мультфильмы']
        ])
    def test_get_books_with_specific_genre_one_book(self,name_book,genre):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book,genre)
        assert len(collector.get_books_with_specific_genre(genre))==1 and len(collector.get_books_with_specific_genre('Комедии'))==0

    # проверяем не пуст ли  словарь books_genre
    def test_get_books_genre_full(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre('Оно','Ужасы')
        assert  len(collector.get_books_genre())>0


    # проверим, что лишнего  не выдадим  детям
    @pytest.mark.parametrize('name_book,genre',[
        ['Гиперион','Фантастика'],
        ['1984','Фантастика'],
     #   ['Оно', 'Ужасы'],
        ['Шрек','Мультфильмы']
        ])
    def test_get_books_for_children_one(self, name_book, genre):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book,genre)
        assert  len(collector.get_books_for_children())==1

    # проверим, что книга не добавится в избранное если ее нет в списке
    def test_add_book_in_favorites_book_not_exists(self):
        collector = BooksCollector()        
        collector.add_book_in_favorites("Бриджит Джонс")        
        assert len(collector.get_list_of_favorites_books()) == 0


    # проверим, что книга удалится из избранного если она там была
    def test_delete_book_from_favorites_book_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Ни давности ни забвения")
        collector.add_book_in_favorites("Ни давности ни забвения")
        
        collector.delete_book_from_favorites("Ни давности ни забвения")
        
        assert "Ни давности ни забвения" not in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 0
    #проверим, что если изменить жанр книги она останется в избранном
    def test_get_list_of_favorites_books_if_genre_change_success(self):
        collector = BooksCollector()
        collector.add_new_book("Зверополис")
        collector.add_book_in_favorites("Зверополис")
        
        collector.set_book_genre("Зверополис", "Мультфильмы")
        collector.set_book_genre("Зверополис", "Ужасы")  
        
        assert "Зверополис" in collector.get_list_of_favorites_books()
