#!/c/Users/narayac/AppData/Local/Programs/Python/Python39/python
import json

class Subscription:
    def __init__(self, shortname, longname, profile):
        self.name = longname
        self.alias = shortname

    def create(self):
        print("Calling subscription creation :", self.name)
        id = {
            "subscription_id": "e4148e6d-1440-4160-9529-ac19265cbf69",
            "status": "success"
        }
        return json.dumps(id)

    def list(self):
        print("Listing subscription :", self.name)
        id = {
            "subscription_id": "e7ba1dd4-c5f3-11ec-9d64-0242ac120002",
            "status": "success"
        }
        return json.dumps(id)

    def delete(self):
        print("Calling subscription delete :", self.name)
        id = {
            "subscription_id": "e7ba1dd4-c5f3-11ec-9d64-0242ac120002",
            "status": "success"
        }
        return json.dumps(id)        

if __name__ == "__main__":
    sub = Subscription("subs01", "subscription01", "des")

    print(sub.create())
    print(sub.list())
    print(sub.create())

