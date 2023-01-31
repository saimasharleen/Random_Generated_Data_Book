pip install faker
import os
import csv
from faker import Faker

fake = Faker()

with open('random_books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['bookID', 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages', 'ratings_count', 'text_reviews_count', 'publication_date', 'publisher'])
    for i in range(20000):
        writer.writerow([i, fake.catch_phrase(), fake.name(), fake.random_number(digits=2), fake.isbn10(separator="-"), fake.isbn13(separator="-"), fake.language_code(), fake.random_number(digits=3), fake.random_number(digits=5), fake.random_number(digits=3), fake.date_this_decade(), fake.company()])

os.rename('random_books.csv', 'book_dataset.csv')
