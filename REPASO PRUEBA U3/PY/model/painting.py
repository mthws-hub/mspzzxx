class Painting:
    def __init__(self, id_painting, name, price, colors, price_with_iva=None):
        self.id = str(id_painting)
        self.name = name
        self.price = float(price)
        # Aseguramos que sea lista
        self.colors = colors if isinstance(colors, list) else []
        self.price_with_iva = float(price_with_iva) if price_with_iva is not None else 0.0

    def __str__(self):
        return f"{self.name} (${self.price_with_iva})"