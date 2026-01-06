from utils.mongo_connection import MongoConnection
from model.painting import Painting

class PaintingController:
    def __init__(self):
        self.db = MongoConnection.get_database()
        self.collection = self.db["paintings"]
        self.IVA_RATE = 0.15

    def calculate_iva(self, price):
        result = price * (1 + self.IVA_RATE)
        return round(result, 2)

    # --- CREATE ---
    def create_painting(self, id_painting, name, price, colors):
        try:
            price_with_iva = self.calculate_iva(price)
            
            doc = {
                "id": id_painting,
                "name": name,
                "price": price,
                "colors": colors,
                "priceWithIva": price_with_iva
            }
            
            self.collection.insert_one(doc)
            return True
        except Exception as e:
            print(f"Error creating painting: {e}")
            return False

    # --- READ ---
    def get_all_paintings(self):
        paintings = []
        try:
            for doc in self.collection.find():
                paintings.append(self._map_document_to_painting(doc))
        except Exception as e:
            print(f"Error reading paintings: {e}")
        return paintings

    # --- FIND ---
    def find_painting_by_id(self, id_painting):
        try:
            doc = self.collection.find_one({"id": id_painting})
            if doc:
                return self._map_document_to_painting(doc)
        except Exception as e:
            print(f"Error finding painting: {e}")
        return None

    # --- UPDATE (Con lógica corregida: matched_count) ---
    def update_painting(self, id_painting, name, price, colors):
        try:
            price_with_iva = self.calculate_iva(price)

            result = self.collection.update_one(
                {"id": id_painting},
                {"$set": {
                    "name": name,
                    "price": price,
                    "colors": colors,
                    "priceWithIva": price_with_iva
                }}
            )
            # Retorna True solo si encontró el documento
            return result.matched_count > 0
        except Exception as e:
            print(f"Error updating: {e}")
            return False

    # --- DELETE (Con lógica corregida: deleted_count) ---
    def delete_painting(self, id_painting):
        try:
            result = self.collection.delete_one({"id": id_painting})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting: {e}")
            return False

    # --- Helper Mapper ---
    def _map_document_to_painting(self, doc):
        id_val = doc.get("id")
        if id_val is None:
            id_val = str(doc.get("_id"))
        
        name = doc.get("name", "")
        price = doc.get("price", 0.0)
        colors = doc.get("colors", [])
        
        price_iva = doc.get("priceWithIva")
        if price_iva is None:
            price_iva = self.calculate_iva(price)
            
        return Painting(id_val, name, price, colors, price_iva)