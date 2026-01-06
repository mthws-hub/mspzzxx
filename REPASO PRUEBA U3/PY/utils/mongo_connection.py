from pymongo import MongoClient

class MongoConnection:
    _instance = None
    _client = None
    _database = None

    # Mismo string de conexión
    CONNECTION_STRING = "mongodb+srv://Mathews:Mathews2007@cluster0.6l9ibfh.mongodb.net/?appName=Cluster0"
    DATABASE_NAME = "ArtGalleryDB"

    @classmethod
    def get_database(cls):
        if cls._database is None:
            try:
                cls._client = MongoClient(cls.CONNECTION_STRING)
                cls._database = cls._client[cls.DATABASE_NAME]
                print("Conexión a MongoDB exitosa.")
            except Exception as e:
                print(f"Error conectando a MongoDB: {e}")
        return cls._database

    @classmethod
    def close(cls):
        if cls._client:
            cls._client.close()
            print("Conexión a MongoDB cerrada.")