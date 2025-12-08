import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
from datetime import date
from pymongo import MongoClient
from tkinter import messagebox

class FrmContacts(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CONTACTS BOOK")
        self.geometry("850x750")
        
        self.mongo_uri = "mongodb+srv://Mathews:Mathews2007@cluster0.6l9ibfh.mongodb.net/"
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client['ContactBook'] 
        self.collection = self.db['Contact']

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1) 
        self.grid_rowconfigure(2, weight=0) 
        self.grid_columnconfigure(0, weight=1)

        self.button_group_sex = tk.StringVar(value="Unknown")
        self._initComponents()
        
    def _initComponents(self):


        self.jPanel1 = ctk.CTkFrame(self, fg_color="#F0F0F0") 
        self.jPanel2 = ctk.CTkFrame(self, fg_color="#F0F0F0")
        self.jPanel3 = ctk.CTkFrame(self, fg_color="#F0F0F0")


        self.jPanel3.grid_columnconfigure(1, weight=1) 
        self.jPanel3.grid_columnconfigure(3, weight=1) 
        
        content_parent = self.jPanel3
        
        self.txtId = ctk.CTkEntry(content_parent)
        self.txtFirstName = ctk.CTkEntry(content_parent)
        self.txtLastName = ctk.CTkEntry(content_parent)
        self.cmbType = ctk.CTkComboBox(content_parent, values=["Family", "Friend", "Job", "Unknown"])
        self.jTextArea1 = ctk.CTkTextbox(content_parent, height=100)
        self.Calendar = Calendar(content_parent, selectmode='day', date_pattern='dd/MM/yyyy', date=date.today()) 
        
        self.radSexMale = ctk.CTkRadioButton(content_parent, text="Male", variable=self.button_group_sex, value="Male", command=self._radSexMaleActionPerformed)
        self.radSexFemale = ctk.CTkRadioButton(content_parent, text="Female", variable=self.button_group_sex, value="Female", command=self._radSexFemaleActionPerformed)
        self.txtAge = ctk.CTkLabel(content_parent, text="--")
        self.jScrollPane1 = ctk.CTkFrame(content_parent) 
        
        hobbies_list = ["Play Soccer", "Djing", "Read", "Cook", "Swim", "Sing", "Play an instrument"]
        self.lstHobbies = tk.Listbox(self.jScrollPane1, listvariable=tk.StringVar(value=hobbies_list), height=5, 
                                     selectmode=tk.MULTIPLE, relief=tk.FLAT)

        self.jScrollPane1.grid_rowconfigure(0, weight=1)
        self.jScrollPane1.grid_columnconfigure(0, weight=1)
        self.lstHobbies.grid(row=0, column=0, sticky="nsew") 
        
        self.jLabel1 = ctk.CTkLabel(self.jPanel1, text="CONTACTS", font=ctk.CTkFont(family="Britannic Bold", size=30, slant="italic"), text_color="#006699")

        self.jButton1 = ctk.CTkButton(self.jPanel2, text="SAVE", font=ctk.CTkFont(family="Footlight MT Light", size=16), fg_color="#000099",command=self._save_to_mongodb)


        self.jPanel1.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        self.jPanel3.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.jPanel2.grid(row=2, column=0, sticky="ew", padx=10, pady=(5, 10))

        self.jPanel1.grid_columnconfigure(0, weight=1)
        self.jLabel1.grid(row=0, column=0, pady=40, sticky="n") 
        
        ctk.CTkLabel(content_parent, text="id:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(content_parent, text="First Name:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.txtFirstName.grid(row=1, column=1, padx=5, pady=5, sticky="ew") 

        ctk.CTkLabel(content_parent, text="Last Name:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.txtLastName.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        ctk.CTkLabel(content_parent, text="Birth Day:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.Calendar.grid(row=3, column=1, rowspan=2, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(content_parent, text="Age:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.txtAge.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        ctk.CTkLabel(content_parent, text="Type:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=1, column=2, padx=5, pady=5, sticky="w") # Etiqueta Type
        self.cmbType.grid(row=1, column=3, padx=5, pady=5, sticky="ew") 
        
        ctk.CTkLabel(content_parent, text="Sex:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=2, column=2, padx=5, pady=5, sticky="w") # Etiqueta Sex
        self.radSexMale.grid(row=2, column=3, padx=(5, 70), pady=5, sticky="w") 
        self.radSexFemale.grid(row=2, column=3, padx=(70, 5), pady=5, sticky="e") 

        ctk.CTkLabel(content_parent, text="Hobbies:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=3, column=2, padx=5, pady=5, sticky="nw")
 
        self.jScrollPane1.grid(row=3, column=3, rowspan=3, padx=5, pady=5, sticky="nsew")

        ctk.CTkLabel(content_parent, text="Comments:", font=ctk.CTkFont(family="Footlight MT Light", size=16), text_color="#000099").grid(row=6, column=0, columnspan=4, padx=5, pady=(20, 5), sticky="w")

        self.jTextArea1.grid(row=7, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        self.jPanel2.grid_columnconfigure(0, weight=1)
        self.jButton1.grid(row=0, column=0, pady=30) 

        self.Calendar.bind("<<CalendarSelected>>", self._CalendarPropertyChange)
        
    def _calculateAge(self, birth_date):
        if birth_date is None:
            return 0
        birth = birth_date
        now = date.today()
        age = now.year - birth.year
        if (now.month, now.day) < (birth.month, birth.day):
            age -= 1
        return age
    
    def _radSexMaleActionPerformed(self):
        self.radSexFemale.configure(state='disabled' if self.button_group_sex.get() == "Male" else 'normal')

    def _radSexFemaleActionPerformed(self):
        self.radSexMale.configure(state='disabled' if self.button_group_sex.get() == "Female" else 'normal')

    def _CalendarPropertyChange(self, event):
        try:
            date_selected = self.Calendar.selection_get() 
            age = self._calculateAge(date_selected)
            self.txtAge.configure(text=str(age))
        except Exception as e:
            self.txtAge.configure(text="N/A")

    def _save_to_mongodb(self):
        try:
            selected_indices = self.lstHobbies.curselection()
            selected_hobbies = [self.lstHobbies.get(i) for i in selected_indices]
            document = {
                "id": self.txtId.get(),
                "firstName": self.txtFirstName.get(),
                "lastName": self.txtLastName.get(),
                "age": self.txtAge.cget("text"),
                "type": self.cmbType.get(),
                "sex": self.button_group_sex.get(),
                "hobbies": selected_hobbies,
                "comments": self.jTextArea1.get("1.0", "end-1c")
            }
            confirm = messagebox.askyesno("Save", f"Do you want to save {document['firstName']}?")
            if confirm:
                self.collection.insert_one(document)
                messagebox.showinfo("Successful", "Contact saved successfully in the cloud.")
                self._empty_fields()
                
        except Exception as e:
            messagebox.showerror("Error", f"Could not save: {str(e)}")
    def _empty_fields(self):
        self.txtId.delete(0, 'end')
        self.txtFirstName.delete(0, 'end')
        self.txtLastName.delete(0, 'end')
        self.jTextArea1.delete("1.0", "end")
        self.lstHobbies.selection_clear(0, 'end')
        self.txtAge.configure(text="0")

if __name__ == "__main__":
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    app = FrmContacts()
    app.mainloop()