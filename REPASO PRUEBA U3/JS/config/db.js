const mongoose = require('mongoose');

const CONNECTION_STRING = "mongodb+srv://Mathews:Mathews2007@cluster0.6l9ibfh.mongodb.net/ArtGalleryDB?appName=Cluster0";

const connectDB = async () => {
    try {
        await mongoose.connect(CONNECTION_STRING);
        console.log("Conexión a MongoDB exitosa.");
    } catch (err) {
        console.error("Error conectando a MongoDB:", err.message);
        process.exit(1);
    }
};

module.exports = connectDB;