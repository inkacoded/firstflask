from email.message import Message

from flask import Flask, request

app = Flask(__name__)

# right now we will store data in a list, but usually it should be a databse.
stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store") # http://127.0.0.1:5000/store
def get_store():
    return {"stores": stores}


@app.get("/store/<string:name>") # http://127.0.0.1:5000/store
def get_store_name(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found!"}, 404



@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201 # 201 means data accepted

#dynamic endpoint
@app.post("/store/<string:name>/item")
def create_items(name):
    request_data = request.get_json()
    item_name = request_data["name"]
    price = request_data["price"]
    for store in stores:
        if name == store["name"]:
            new_item = {"name": item_name, "price": price }
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found!"}, 404 # only 404 is the store is not found


#handling QSP query string parameters

#handling headers

