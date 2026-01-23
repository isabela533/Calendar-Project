from classes.session import Session
class Resources:
    def __init__(self, name : str, type, cant : int = 1, dispo : bool = True):
        self.name = name
        self.type = type 
        self.cant = cant
        self.dispo = dispo
        
    # para que se vea bonito en el debug 
    def __repr__(self):
        return f"Resources(name={self.name}, cant={self.cant}, dispo={self.dispo})"
    
class Resources_Manager:
    def __init__(self):
        self.recursos: dict[str, Resources] = {}    #este es mi inventario de recursos 

    def get_rcs(self, list_names : list[list]):
        resources = []
        for name, type, cant, dispo in list_names:
            self.ocupar_resource(name, cant)
            resources.append(self.recursos[name].name)   #anadir instancia real a la lista
        return resources

    #liberar recurso del inventario
    def liberar_resource(self, name, cant, session : Session):  
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
        session.sync_resources_to_json()
    
    #ocupar recurso del inventario 
    def ocupar_resource(self, name, cant, session : Session):
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
        session.sync_resources_to_json()

    #verificar si esta available
    def is_available(self, name: str) -> bool: 
        return name in self.recursos and self.recursos[name].dispo and self.recursos[name].cant > 0  

    # metodo para agregar resources 
    def add_resources(self, resources : list[list], session : Session):
        for name, type, cant, dispo in resources:
            self.add_to_inventory(name, type, cant, dispo)
        session.sync_resources_to_json()

    # metodo para quitar recursos
    def remove_resources(self, resources : list[list], session : Session):
        for name, type, cant, dispo in resources:
            self.remove_from_inventory(name, cant)
        session.sync_resources_to_json()

    # metodo para agregar al deposito
    def add_to_inventory(self, name : str, type, cant: int, dispo: bool = True):
        if name in self.recursos:   #si ya tiene el target, aumentarle la cant
            self.recursos[name].cant += cant
        else:
            self.recursos[name] = Resources(name, type, cant, dispo) # agregar uno nuevo

    # metodo para remover del deposito
    def remove_from_inventory(self, name, cant : int):
        if(name in self.recursos and self.recursos[name].cant >= cant):   #si ya tiene el target, disminuirle la cant
            self.recursos[name].cant -= cant
            if(self.recursos[name].cant <= 0):
                del self.recursos[name] #borrar el recurso del dict 
        else:
            raise Exception(f"The resource {name} could not be removed from your inventory.")
                
                
        
