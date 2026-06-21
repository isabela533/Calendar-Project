import json 
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # sube desde classes/ a la raíz
DATA_DIR = os.path.join(ROOT_DIR, "data")

class Gestor_json:
    def __init__(self, correo):
        self.ruta = os.path.join(DATA_DIR, f"{correo}.json") 
        self.data = {}

    def charge_data(self):
        if os.path.exists(self.ruta):
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                self.data = json.load(archivo)
                return self.data
        else:
            raise Exception("Account not found")
        
    def save_initial_data (self, money: int, resources: list[list], employees: list[list], co_requisites: dict, exclusions: list[tuple]): 
        data = {
                "money": money, 
                "resources": resources,
                "employees": employees, 
                "co_requisites": co_requisites, 
                "exclusions": exclusions, 
                "events": [] 
            } 
        self.save_data(data) 
        return data

    def save_data(self, data):
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(data, archivo, indent=4, ensure_ascii=False)
        self.data = data
        print("Your data is saved")
        return self.data
    
        