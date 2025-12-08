class Contact:
    def __init__(self, id: int, first_name: str, last_name: str, age: int, type_of_contact: str, sex: str, hobbies: list, comments: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.type_of_contact = type_of_contact
        self.sex = sex
        self.hobbies = list(hobbies)
        self.comments = comments
    
    toString = lambda self: f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age}, Type: {self.type_of_contact}, Sex: {self.sex }, Hobbies: {', '.join(self.hobbies)}, Comments: {self.comments}"

    def get_id(self):
        return self.id
    def set_id(self, id: int):
        self.id = id
    
    def get_first_name(self):
        return self.first_name
    def set_first_name(self, first_name: str):
        self.first_name = first_name
    
    def get_last_name(self):
        return self.last_name   
    def set_last_name(self, last_name: str):
        self.last_name = last_name
    
    def get_age(self):
        return self.age
    def set_age(self, age: int):
        self.age = age

    def get_type_of_contact(self):
        return self.type_of_contact 
    def set_type_of_contact(self, type_of_contact: str):
        self.type_of_contact = type_of_contact
    
    def get_sex(self):
        return self.sex
    def set_sex(self, sex: str):
        self.sex = sex
    
    def get_hobbies(self):
        return self.hobbies
    def set_hobbies(self, hobbies: list):
        self.hobbies = hobbies
    
    def get_comments(self):
        return self.comments   
    def set_comments(self, comments: str):
        self.comments = comments

    
    