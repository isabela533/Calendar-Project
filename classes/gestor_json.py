import json 
import os

class Gestor_json:
    def __init__(self, correo):
        self.ruta = f"data/{correo}.json"
        try: 
            self.data = self.charge_data() 
        except Exception as e: 
            print(f"⚠️ {e} → initializing empty data") #cuando se mande esta excepcion tengo que hacer un crear cuenta nueva

    def charge_data(self):
        if os.path.exists(self.ruta):
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                self.data = json.load(archivo)
                return self.data
        else:
            raise Exception("Account not found")

    #el data es un diccionario 
    def save_data(self, data: dict):
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(data, archivo, indent=4, ensure_ascii=False)
        print("Your data is saved")
        return self.data
    
    def add_to_json(self, key, value : dict):  
        data : dict = self.charge_data()  
        
        if key not in data:
            raise Exception("An invalid key was sent") 
        
        target : list = data[key] # el target es una lista de diccionarios
        if isinstance(target, list): 
            target.append(value) # agregarle un nuevo diccionario a la lista de diccionarios 
        else:
            raise Exception("Your key is not a list")  
        self.save_data(data) 
        
    def delete_from_json(self, key, value): 
        data = self.charge_data() 

        if key not in data and not isinstance(data[key], list):    
            return False
        
        target : list = data[key] # el target es una lista de diccionarios
        if value in target: 
            target.remove(value) 
            self.save_data(data) 
            return True
        
        return False 
        