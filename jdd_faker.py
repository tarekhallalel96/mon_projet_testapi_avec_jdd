import pandas as pd
from faker import Faker
import json
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

environment = {
    "id": "test-environment",
    "name": "Test Environment",
    "values": []
}

# Parcourir chaque ligne du DataFrame pour créer les variables d'environnement
for idx, row in df.iterrows():
    for col in df.columns:
        environment["values"].append({
            "key": f"{col}_{idx + 1}",
            "value": row[col],
            "enabled": True
        })

# Sauvegarder en fichier JSON
with open('jdd.json', 'w') as json_file:
    json.dump(environment, json_file, indent=4)

print("Fichier jdd.json généré avec succès.")