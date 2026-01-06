const express = require('express');
const router = express.Router();
const controller = require('../controllers/paintingController');

router.get('/', controller.getAllPaintings);
router.get('/:id', controller.getPaintingById);
router.post('/', controller.createPainting);
router.put('/:id', controller.updatePainting);
router.delete('/:id', controller.deletePainting);

module.exports = router;