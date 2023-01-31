import random
import csv
import uuid

# create the set of user IDs
user_ids = set()
while len(user_ids) < 1000:
    user_ids.add(str(uuid.uuid4()))
    
# create the set of query IDs
query_ids = set()
while len(query_ids) < 10000:
    query_ids.add("Q"+str(uuid.uuid4()))

# create the utility matrix
utility_matrix = []

# add the first row (query IDs)
utility_matrix.append(list(query_ids))

# add the rest of the rows (user IDs and random values)
for user_id in user_ids:
    row = [user_id]
    for query_id in query_ids:
        if random.random() < 0.5:
            row.append(random.randint(1,100))
        else:
            row.append('')
    utility_matrix.append(row)

# write the utility matrix to a CSV file
with open('utility_matrix.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(utility_matrix)
