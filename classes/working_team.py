class Work_team:
    def __init__(self, rol : str, cant : int = 1, dispo : bool = True):
        self.rol = rol
        self.cant = cant
        self.dispo = dispo
        
    #para que se vea bonito en el debug
    def __repr__(self):
        return f"WorkTeam(rol={self.rol}, cant={self.cant}, dispo={self.dispo})"
    
class Team_Manager:
    def __init__(self):
        self.work_team : dict[str, Work_team] = {}
    
    def show_employees(self): 
        if not self.work_team: 
            print("No employees in team.") 
        else: 
            print("👥 Human Resources:") 
            for emp in self.work_team.values(): 
                print(f"- Role: {emp.rol} | Quantity: {emp.cant} | Available: {emp.dispo}")

    #metodo para ocupar empleados
    def get_emp(self, list_names : list[list] ):
        work_team = [] 
        for rol, cant, dispo in list_names:
            self.ocupar_employee(rol, cant)
            work_team.append(self.work_team[rol].rol)
        return work_team
    
    def liberar_employee(self, rol, cant ):
        if not rol in self.work_team:
            raise Exception(f"No {rol} team found")
        
        # el empleado existe y está disponible 
        if self.is_available(rol): 
            self.work_team[rol].cant += cant # dispo ya es True, se mantiene así 
        
        # el empleado existe pero no está disponible 
        elif rol in self.work_team: 
            self.work_team[rol].cant += cant 
            self.work_team[rol].dispo = True 
            
        #el empleado no existe en el inventario, lanzar error 
        else: 
            raise Exception(f"{rol} team does not exist in inventory, cannot be released.")
        
    def ocupar_employee(self, rol, cant ):
        # verificar si esta disponible el trabajador  
        if not self.is_available(rol): 
            raise Exception(f"Your {rol} team is unavailable and cannot assist at this event. " 
                            f"Free them up by deleting an event where at least one {rol} employee is participating, or wait until they become available.")
        
        # verificando cantidad  
        if self.work_team[rol].cant < cant: 
            raise Exception(f"Not enough {rol} employees available to occupy {cant}."
                            f"Free them up by deleting an event where at least one {rol} employee is participating, or wait until they become available.")
         
        # ocupar el trabajador  
        self.work_team[rol].cant -= cant 

        # si ya no queda, marcar como no diponible  
        if self.work_team[rol].cant == 0: 
            self.work_team[rol].dispo = False       

    def is_available(self, rol) -> bool:
        return rol in self.work_team and self.work_team[rol].dispo and self.work_team[rol].cant > 0

    def add_employees(self, employees : list[list] ):
        for rol, cant, dispo in employees:
            self.add_to_inventory(rol, cant, dispo)
    
    def delete_employees(self, employees : list[list] ): 
        for rol, cant, dispo in employees:
            self.remove_from_inventory(rol, cant)

    # metodo para agregar empleado
    def add_to_inventory(self, rol, cant = 1, dispo = True):
        if rol in self.work_team:   # se verifica si hay que aumentarle la cantidad o agregarle uno nuevo
            self.work_team[rol].cant += cant      # aumentamos la cantidad
        else:
            self.work_team[rol] = Work_team(rol, cant, dispo)   # agregarle uno nuevo 

    # metodo para remover empleado
    def remove_from_inventory(self, rol, cant : int):
        if rol not in self.work_team: 
            raise Exception(f"{rol} team does not exist in inventory, cannot be removed.") 
        if self.work_team[rol].cant < cant: 
            raise Exception(f"Cannot remove {cant} {rol} employees, only {self.work_team[rol].cant} available.") 
        
        # restar cantidad 
        self.work_team[rol].cant -= cant 

        # si ya no queda ninguno, elimino el rol del inventario 
        if self.work_team[rol].cant == 0: 
            del self.work_team[rol]