import csv
import uuid

# Column names of the book dataset
column_names = ['bookID', 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages', 'ratings_count', 'text_reviews_count', 'publication_date', 'publisher']

# Number of queries to be generated
num_queries = 1000

# List to store queries
queries = []

# Open the book dataset CSV file
with open('book_dataset.csv', 'r') as book_file:
    # Create a CSV reader
    reader = csv.DictReader(book_file, fieldnames=column_names)
    # Iterate through rows of the book dataset
    for i, row in enumerate(reader):
        # Generate a query ID
        query_id = 'Q' + str(i)
        # Create a list to store the conditions
        conditions = []
        # Iterate through the columns of the book dataset
        for column_name in column_names:
            # Skip the first column (bookID)
            if column_name == 'bookID':
                continue
            # Add the condition to the list
            conditions.append(column_name + '=' + row[column_name])
        # Join the conditions with comma separator
        conditions_str = ','.join(conditions)
        # Append the query to the list
        queries.append([query_id, conditions_str])
        # Break the loop after generating the specified number of queries
        if i == num_queries:
            break

# Write the queries to a CSV file
with open('queries.csv', 'w', newline='') as query_file:
    writer = csv.writer(query_file)
    writer.writerows(queries)
