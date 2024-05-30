import pymongo as mon


class DBConnect:
    def __init__(self):
        self._client = mon.MongoClient("localhost", 27017)
        self._db = self._client["cveDB"]
        self._collection = self._db["cveListV5"]

    def get_all_cves(self):
        return self._collection.find()


if __name__ == "__main__":
    obj = DBConnect()
    cves = obj.get_all_cves()
    for cve in cves:
        print(cve)
        break
