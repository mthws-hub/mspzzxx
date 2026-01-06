const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const connectDB = require('./config/db');
const paintingRoutes = require('./routes/paintingRoutes');

const app = express();

// 1. Conectar a BD
connectDB();

// 2. Middlewares
app.use(cors());
app.use(bodyParser.json());
app.use(express.static('public')); 

// 3. Rutas
app.use('/api/paintings', paintingRoutes);

// 4. Servidor
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});