import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_catalog.settings')

django.setup()

from books.models import Author, Books, BookDetail

Author.objects.all().delete()
Book.objects.all().delete()
BookDetail.objects.all().delete()


authors = [
    Author(id=1, name='лев толстой', img_src='', years_of_age='1828-1910',
           bio='Русский писатель, философ, публицист, родоначальник толстовства.',
works='Война и мир, Анна Каренина'),
    Author(id=2, name='федор достоевский', img_src='', years_of_age='1821-1881',
           bio='Один из величайших русских писателей, мыслитель, философ.',
works='Преступление и наказание, Идиот'),
    Author(id=3, name='александр пушкин', img_src='', years_of_age='1799-1837',
           bio='Русский поэт, драматург, основоположник современного русского языка.',
works='Евгений Онегин, Борис Годунов'),
    Author(id=4, name='джордж оруэлл', img_src='', years_of_age='1903-1950',
           bio='Британский писатель и публицист, автор антиутопий.', works='1984, Скотный двор'),
    Author(id=5, name='фрэнсис скотт фицджеральд', img_src='', years_of_age='1896-1940',
           bio='Американский писатель, мастер прозы.', works='Великий Гэтсби, Ночь нежна')
]
Author.objects.bulk_create(authors)



books = [
    Book(id=1, title='война и мир', author_id=1, img_src='', publication_date='1869-01-01', short_desc='Эпическое произведение о войне 1812 года.'),
    Book(id=2, title='преступление и наказание', author_id=2, img_src='', publication_date='1866-01-01', short_desc='Рассказ о преступлении и его моральных последствиях.'),
    Book(id=3, title='евгений онегин', author_id=3, img_src='', publication_date='1833-01-01', short_desc='Роман в стихах о дворянском обществе.'),
    Book(id=4, title='1984', author_id=4, img_src='', publication_date='1949-06-08', short_desc='Антиутопия о тоталитарном обществе.'),
    Book(id=5, title='великий гэтсби', author_id=5, img_src='', publication_date='1925-04-10', short_desc='История о жизни американской элиты 1920-х годов.'),
]
Book.objects.bulk_create(books)




book_details = [
    BookDetail(id=1, book_id=1, description='История семьи Ростовых, Болконских и других в эпоху наполеоновских войн.'),
    BookDetail(id=2, book_id=2, description='Психологический роман о студенте, который совершает убийство.'),
    BookDetail(id=3, book_id=3, description="Классический роман в стихах, рассказывающий о любви и трагедии."),
    BookDetail(id=4, book_id=4, description="Мрачный прогноз будущего, где Большой Брат следит за всеми."),
    BookDetail(id=5, book_id=5, description="История любви и предательства в эпоху джаза."),
]
BookDetail.objects.bulk_create(book_details)

print('База данных успешно обновлена!')

