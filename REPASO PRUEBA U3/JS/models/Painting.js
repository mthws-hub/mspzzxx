const mongoose = require('mongoose');

const PaintingSchema = new mongoose.Schema({
    id: { type: String, required: true, unique: true },
    name: { type: String, required: true },
    price: { type: Number, required: true },
    colors: { type: [String], default: [] },
    priceWithIva: { type: Number }
});

module.exports = mongoose.model('Painting', PaintingSchema);