import csv
import uuid
import pandas as pd

user_ids = set()
while len(user_ids) < 20000:
    user_ids.add(str(uuid.uuid4()))

# convert the set to dataframe
user_ids_df = pd.DataFrame(list(user_ids), columns=["user_id"])

# write the dataframe to a csv file
user_ids_df.to_csv("user_ids.csv", index=False)

