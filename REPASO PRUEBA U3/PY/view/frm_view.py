import tkinter as tk
from tkinter import ttk, messagebox
from controller.painting_controller import PaintingController

class FrmView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = PaintingController()
        
        # Configuración Ventana
        self.title("Art Gallery Management (Python MVC)")
        self.geometry("900x600")
        self.configure(bg="#E0E0E0")
        
        self.create_widgets()
        self.load_table_data()

    def create_widgets(self):
        # Panel Principal
        main_frame = tk.Frame(self, bg="#E0E0E0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # --- Fila 1 ---
        row1 = tk.Frame(main_frame, bg="#E0E0E0")
        row1.pack(fill=tk.X, pady=5)

        tk.Label(row1, text="Name:", bg="#E0E0E0").pack(side=tk.LEFT)
        self.txt_name = tk.Entry(row1, width=20)
        self.txt_name.pack(side=tk.LEFT, padx=5)

        tk.Label(row1, text="Base Price ($):", bg="#E0E0E0").pack(side=tk.LEFT)
        self.txt_price = tk.Entry(row1, width=10)
        self.txt_price.pack(side=tk.LEFT, padx=5)

        tk.Label(row1, text="ID:", bg="#E0E0E0").pack(side=tk.LEFT)
        self.txt_id = tk.Entry(row1, width=15)
        self.txt_id.pack(side=tk.LEFT, padx=5)

        tk.Button(row1, text="Find", command=self.btn_find_action).pack(side=tk.LEFT, padx=10)

        # --- Fila 2 ---
        row2 = tk.Frame(main_frame, bg="#E0E0E0")
        row2.pack(fill=tk.X, pady=5)
        tk.Label(row2, text="Colors (comma separated):", bg="#E0E0E0").pack(side=tk.LEFT)
        self.txt_colors = tk.Entry(row2, width=60)
        self.txt_colors.pack(side=tk.LEFT, padx=5)

        # --- Fila 3 (Botones) ---
        row3 = tk.Frame(main_frame, bg="#E0E0E0")
        row3.pack(fill=tk.X, pady=15)
        
        tk.Button(row3, text="Create New", bg="#4CAF50", fg="white", command=self.btn_create_action).pack(side=tk.LEFT, padx=5)
        tk.Button(row3, text="Update", bg="#2196F3", fg="white", command=self.btn_update_action).pack(side=tk.LEFT, padx=5)
        tk.Button(row3, text="Delete", bg="#F44336", fg="white", command=self.btn_delete_action).pack(side=tk.LEFT, padx=5)
        tk.Button(row3, text="Clear Form", command=self.btn_cancel_action).pack(side=tk.LEFT, padx=5)

        # --- Tabla ---
        tk.Label(main_frame, text="Inventory:", bg="#E0E0E0", font=("Arial", 11, "bold")).pack(anchor="w", pady=(20, 5))
        
        columns = ("id", "name", "colors", "price", "price_iva")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("colors", text="Colors")
        self.tree.heading("price", text="Price ($)")
        self.tree.heading("price_iva", text="Price + IVA ($)")
        
        self.tree.column("id", width=80)
        self.tree.column("name", width=150)
        self.tree.column("colors", width=200)
        self.tree.column("price", width=80)
        self.tree.column("price_iva", width=80)

        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Evento de Selección
        self.tree.bind("<<TreeviewSelect>>", self.on_table_select)

    # --- Helpers ---
    def parse_colors(self, text):
        if not text: return []
        return [c.strip() for c in text.split(',') if c.strip()]

    def clear_form(self):
        self.txt_id.delete(0, tk.END)
        self.txt_name.delete(0, tk.END)
        self.txt_price.delete(0, tk.END)
        self.txt_colors.delete(0, tk.END)
        # Limpiar selección visual
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def load_table_data(self, data_list=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if data_list is None:
            data_list = self.controller.get_all_paintings()
            
        for p in data_list:
            colors_str = ", ".join(p.colors)
            self.tree.insert("", tk.END, values=(p.id, p.name, colors_str, p.price, p.price_with_iva))

    # --- Actions ---
    def on_table_select(self, event):
        selected_item = self.tree.selection()
        if not selected_item: return
        
        values = self.tree.item(selected_item[0])['values']
        
        self.txt_id.delete(0, tk.END); self.txt_id.insert(0, str(values[0]))
        self.txt_name.delete(0, tk.END); self.txt_name.insert(0, str(values[1]))
        self.txt_colors.delete(0, tk.END); self.txt_colors.insert(0, str(values[2]))
        self.txt_price.delete(0, tk.END); self.txt_price.insert(0, str(values[3]))

    def btn_create_action(self):
        try:
            id_val = self.txt_id.get()
            name = self.txt_name.get()
            price = float(self.txt_price.get())
            colors = self.parse_colors(self.txt_colors.get())

            if self.controller.create_painting(id_val, name, price, colors):
                messagebox.showinfo("Success", "Painting Saved")
                self.clear_form()
                self.load_table_data()
            else:
                messagebox.showerror("Error", "Could not save (Check ID duplicate)")
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")

    def btn_update_action(self):
        id_val = self.txt_id.get()
        if not id_val:
            messagebox.showwarning("Warning", "Select a painting to update.")
            return

        try:
            name = self.txt_name.get()
            price = float(self.txt_price.get())
            colors = self.parse_colors(self.txt_colors.get())

            updated = self.controller.update_painting(id_val, name, price, colors)

            if updated:
                messagebox.showinfo("Success", "Painting Updated Successfully")
                self.load_table_data()
                self.clear_form()
            else:
                messagebox.showerror("Error", "Update Failed: ID not found in Database.")
        except ValueError:
             messagebox.showerror("Error", "Price must be a number")

    def btn_delete_action(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a painting from the table to delete.")
            return

        values = self.tree.item(selected_item[0])['values']
        id_to_delete = str(values[0])

        if messagebox.askyesno("Confirm", f"Delete painting ID: {id_to_delete}?"):
            if self.controller.delete_painting(id_to_delete):
                messagebox.showinfo("Success", "Deleted from MongoDB.")
                self.load_table_data()
                self.clear_form()
            else:
                messagebox.showerror("Error", "Delete Failed: ID not found.")

    def btn_find_action(self):
        id_search = self.txt_id.get()
        if not id_search:
            self.load_table_data()
        else:
            found = self.controller.find_painting_by_id(id_search)
            if found:
                self.load_table_data([found])
            else:
                messagebox.showinfo("Info", "Painting not found")
                self.load_table_data()

    def btn_cancel_action(self):
        self.clear_form()
        self.load_table_data()