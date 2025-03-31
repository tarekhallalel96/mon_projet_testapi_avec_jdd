import pandas as pd
from faker import Faker
import random

faker = Faker()

N = 10


data = {
    "id": [faker.random_number() for _ in range(N)],
    "email": [faker.email() for _ in range(N)],
    "first_name": [faker.first_name() for _ in range(N)],
    "last_name": [faker.last_name() for _ in range(N)],
    "avatar": [faker.image_url() for _ in range(N)]  # Ajout d'un avatar fictif
}
df = pd.DataFrame(data)

df.to_json("jdd.json", orient="records", lines=True)

print(df)