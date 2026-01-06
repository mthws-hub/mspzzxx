const API_URL = 'http://localhost:3000/api/paintings';

// --- Cargar Tabla ---
async function loadTable(data = null) {
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = ''; // Limpiar duplicados

    let paintings = data;
    
    if (!paintings) {
        try {
            const res = await fetch(API_URL);
            paintings = await res.json();
        } catch (err) {
            console.error("Error cargando datos:", err);
            return;
        }
    }

    if (!Array.isArray(paintings)) paintings = [paintings];

    paintings.forEach(p => {
        const row = tbody.insertRow();
        
        // Validación extra visual: Si por alguna razón sigue siendo null, lo calculamos aquí
        let displayIva = p.priceWithIva;
        if (displayIva === null || displayIva === undefined) {
             displayIva = (p.price * 1.15).toFixed(2);
        }

        row.innerHTML = `
            <td>${p.id}</td>
            <td>${p.name}</td>
            <td>${p.colors.join(', ')}</td>
            <td>${p.price}</td>
            <td>${displayIva}</td>
        `;
        row.onclick = () => selectRow(row, p);
    });
}

// --- Seleccionar Fila ---
function selectRow(row, data) {
    document.querySelectorAll('tr').forEach(r => r.classList.remove('selected'));
    row.classList.add('selected');

    document.getElementById('txtId').value = data.id;
    document.getElementById('txtName').value = data.name;
    document.getElementById('txtPrice').value = data.price;
    document.getElementById('txtColors').value = data.colors.join(', ');
}

// --- CREATE ---
async function createPainting() {
    const data = getFormData();
    if (!data) return;

    try {
        const res = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await res.json();
        alert(result.message);
        
        if (result.success) {
            clearForm();
            loadTable();
        }
    } catch (err) {
        alert("Error de conexión");
    }
}

// --- UPDATE ---
async function updatePainting() {
    const data = getFormData();
    if (!data) return;
    const id = document.getElementById('txtId').value;
    
    if(!id) { alert("Select a painting first"); return; }

    try {
        const res = await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await res.json();
        alert(result.message);
        if (result.success) {
            loadTable();
            clearForm();
        }
    } catch (err) {
        alert("Error actualizando");
    }
}

// --- DELETE ---
async function deletePainting() {
    const id = document.getElementById('txtId').value;
    if (!id) { alert("Select a painting to delete"); return; }

    if (!confirm(`Are you sure to delete ID: ${id}?`)) return;

    try {
        const res = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });

        const result = await res.json();
        alert(result.message);
        if (result.success) {
            loadTable();
            clearForm();
        }
    } catch (err) {
        alert("Error eliminando");
    }
}

// --- FIND ---
async function findPainting() {
    const id = document.getElementById('txtId').value;
    if (!id) { loadTable(); return; }

    try {
        const res = await fetch(`${API_URL}/${id}`);
        if (res.ok) {
            const data = await res.json();
            loadTable(data);
        } else {
            alert("Painting not found");
            loadTable();
        }
    } catch (err) {
        alert("Error buscando");
    }
}

// Helpers
function getFormData() {
    const id = document.getElementById('txtId').value;
    const name = document.getElementById('txtName').value;
    const price = document.getElementById('txtPrice').value;
    const colorsText = document.getElementById('txtColors').value;

    if (!id || !name || !price) {
        alert("Fill all fields");
        return null;
    }

    return {
        id, 
        name, 
        price: Number(price), 
        colors: colorsText.split(',').map(c => c.trim()).filter(c => c)
    };
}

function clearForm() {
    document.getElementById('txtId').value = '';
    document.getElementById('txtName').value = '';
    document.getElementById('txtPrice').value = '';
    document.getElementById('txtColors').value = '';
    document.querySelectorAll('tr').forEach(r => r.classList.remove('selected'));
}

loadTable();