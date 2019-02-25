from app import app, db
from app.models.tables import Client
import urllib, json


url = "https://jsonplaceholder.typicode.com/users"

response = urllib.urlopen(url)
data = json.loads(response.read())

for d in data:
    client = Client.query.filter_by(id=d['id']).first()
    if client:
        print("Atualizando")
        client.client_id = d['id']
        client.client_name = d['name']
        db.session.commit()
    else:
        print("Cadastrando")
        client = Client(d['id'], d['name'])
        db.session.add(client)
        db.session.commit()
