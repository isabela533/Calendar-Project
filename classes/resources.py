class Resources:
    def __init__(self, name : str, type, cant : int = 1, dispo : bool = True):
        self.name = name
        self.type = type 
        self.cant = cant
        self.dispo = dispo
        
    # para que se vea bonito en el debug 
    def __repr__(self):
        return f"Resources(name={self.name}, type = {self.type}, cant={self.cant}, dispo={self.dispo})"
    
class Resources_Manager:
    def __init__(self):
        self.recursos: dict[str, Resources] = {}    #este es mi inventario de recursos 

    def show_resources(self): 
        if not self.recursos: 
            print("No resources in inventory.") 
        else: 
            print("📦 Material Resources:") 
            for res in self.recursos.values(): 
                print(f"- {res.name} ({res.type}) | Quantity: {res.cant} | Available: {res.dispo}")

    def get_rcs(self, list_names : list[list]):
        resources = []
        for name, type, cant, dispo in list_names:
            self.ocupar_resource(name, cant)
            resources.append(self.recursos[name].name)   #anadir instancia real a la lista
        return resources

    #liberar recurso del inventario
    def liberar_resource(self, name, cant):  
        # el recurso existe y está disponible 
        if self.is_available(name): 
            self.recursos[name].cant += cant # dispo ya es True, se mantiene así 
        
        # el recurso existe pero no está disponible 
        elif name in self.recursos: 
            self.recursos[name].cant += cant 
            self.recursos[name].dispo = True 
            
        #el recurso no existe en el inventario, lanzar error 
        else: 
            raise Exception(f"Resource {name} does not exist in inventory, cannot be released.")
           
    #ocupar recurso del inventario 
    def ocupar_resource(self, name, cant):
        if not name in self.recursos:
            raise Exception(f"Not resource called {name} found")
        
        # verificar si esta disponible 
        if not self.is_available(name): 
            raise Exception(f"Resource {name} is not available."
                            f"You can use it once it becomes free, or free it up by deleting an event that’s using it.") 
        
        # verificando cantidad  
        if self.recursos[name].cant < cant: 
            raise Exception(f"Not enough {name} available to occupy {cant}."
                            f"You can use it once it becomes free, or free it up by deleting an event that’s using it.")
         
        # ocupar el recurso  
        self.recursos[name].cant -= cant 

        # si ya no queda, marcar como no diponible  
        if self.recursos[name].cant == 0: 
            self.recursos[name].dispo = False

    #verificar si esta available
    def is_available(self, name: str) -> bool: 
        return name in self.recursos and self.recursos[name].dispo and self.recursos[name].cant > 0  

    # metodo para agregar resources 
    def add_resources(self, resources : list[list]):
        for name, type, cant, dispo in resources:
            self.add_to_inventory(name, type, cant, dispo)

    # metodo para quitar recursos
    def remove_resources(self, resources : list[list]):
        for name, type, cant, dispo in resources:
            self.remove_from_inventory(name, cant)
            
    # metodo para agregar al deposito
    def add_to_inventory(self, name : str, type, cant: int, dispo: bool = True):
        if name in self.recursos:   #si ya tiene el target, aumentarle la cant
            self.recursos[name].cant += cant
        else:
            self.recursos[name] = Resources(name, type, cant, dispo) # agregar uno nuevo

    # metodo para remover del deposito
    def remove_from_inventory(self, name, cant : int):
        # si el recurso no existe 
        if name not in self.recursos: 
            raise Exception( f"Resource '{name}' does not exist in your inventory. " 
                            f"Please check the resource name or add it first before trying to remove." ) 
        
        # si hay cantidad insuficiente 
        if self.recursos[name].cant < cant: 
            raise Exception( f"Cannot remove {cant} units of '{name}'. " 
                            f"Only {self.recursos[name].cant} available in inventory." )
        
        # restar  
        self.recursos[name].cant -= cant 

        # si ya no queda ninguno, eliminar del inventario 
        if self.recursos[name].cant == 0: del self.recursos[name]
                
        
