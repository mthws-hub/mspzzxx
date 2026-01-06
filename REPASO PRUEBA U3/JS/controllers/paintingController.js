const Painting = require('../models/Painting');
const IVA_RATE = 0.15;

// Helper para calcular IVA
const calculateIva = (price) => {
    return Math.round((price * (1 + IVA_RATE)) * 100) / 100;
};

// --- HELPER CRÍTICO: Rellena datos faltantes ---
// Si la BD devuelve un objeto sin IVA (null), lo calculamos aquí para visualización.
const fixPaintingData = (paintingDoc) => {
    // Convertimos el documento de Mongoose a objeto JS plano para poder modificarlo
    let p = paintingDoc.toObject(); 

    if (p.priceWithIva === null || p.priceWithIva === undefined) {
        p.priceWithIva = calculateIva(p.price);
    }
    return p;
};

// --- READ ALL ---
exports.getAllPaintings = async (req, res) => {
    try {
        const paintings = await Painting.find();
        
        // Mapeamos cada pintura para arreglar los nulos antes de enviar
        const fixedPaintings = paintings.map(p => fixPaintingData(p));
        
        res.json(fixedPaintings);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};

// --- FIND BY ID ---
exports.getPaintingById = async (req, res) => {
    try {
        const painting = await Painting.findOne({ id: req.params.id });
        if (painting) {
            // Arreglamos el nulo si existe
            res.json(fixPaintingData(painting));
        } else {
            res.status(404).json({ message: "Painting not found" });
        }
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
};

// --- CREATE ---
exports.createPainting = async (req, res) => {
    const { id, name, price, colors } = req.body;
    try {
        const priceWithIva = calculateIva(Number(price));
        
        const newPainting = new Painting({
            id, name, price, colors, priceWithIva
        });

        await newPainting.save();
        res.json({ success: true, message: "Painting Saved" });
    } catch (err) {
        res.status(400).json({ success: false, message: "Error saving (Check duplicate ID)" });
    }
};

// --- UPDATE ---
exports.updatePainting = async (req, res) => {
    const { id } = req.params;
    const { name, price, colors } = req.body;

    try {
        // Al actualizar, SIEMPRE recalculamos el IVA basándonos en el precio enviado
        const priceWithIva = calculateIva(Number(price));

        const result = await Painting.updateOne(
            { id: id }, 
            { $set: { name, price, colors, priceWithIva } }
        );

        if (result.matchedCount > 0) {
            res.json({ success: true, message: "Painting Updated and IVA fixed in DB" });
        } else {
            res.status(404).json({ success: false, message: "Update Failed: ID not found" });
        }
    } catch (err) {
        res.status(500).json({ success: false, message: err.message });
    }
};

// --- DELETE ---
exports.deletePainting = async (req, res) => {
    const { id } = req.params;
    try {
        const result = await Painting.deleteOne({ id: id });

        if (result.deletedCount > 0) {
            res.json({ success: true, message: "Deleted from MongoDB" });
        } else {
            res.status(404).json({ success: false, message: "Delete Failed: ID not found" });
        }
    } catch (err) {
        res.status(500).json({ success: false, message: err.message });
    }
};