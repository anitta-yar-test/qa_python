## 🐍 QA Python Tests

## Список тестов

| № | Название теста | Описание |
|---|----------------|----------|
| 1 | `test_add_new_book_add_two_books` | Проверяет, что добавлены 2 книги |
| 2 | `test_add_new_book_add_no_genre` | Проверяет, что у новой добавленной книги нет жанра |
| 3 | `test_set_book_genre_not_null` | Проверяет, установлен ли книге жанр |
| 4 | `test_get_book_genre_success` | Проверяет, что удается получить жанр книги по её имени |
| 5 | `test_get_books_with_specific_genre_empty_collection` | Проверяем получение книг по жанру из пустой коллекции"|
| 6 | `test_get_books_genre_full` | Проверяем, не пуст ли словарь `books_genre` |
| 7 | `test_get_books_for_children_one` | Проверяем, что лишнего не выдадим детям |
| 8 | `test_add_book_in_favorites_book_not_exists` |Проверяем, что книга не добавится в избранное если ее нет в списке |
| 9 | `test_delete_book_from_favorites_book_exists` | проверим, что книга удалится из избранного если она там была |
|10 | `test_get_list_of_favorites_books_if_genre_change_success` |Проверим, что если изменить жанр книги она останется в избранном|