from classes.gestor_json import Gestor_json
from classes.resources import Resources_Manager
from classes.working_team import Team_Manager
from classes.restrictions import Restrictions

class Session:
    def __init__(self, correo, money = None, resources = None, employees = None, co_requisites = None, exclusions = None, create = False):
        self.correo = correo
        self.json = Gestor_json(correo)
        
        if create: # crear cuenta nueva 
            self.money = money or 0 
            resources = resources or [] 
            employees = employees or [] 
            co_requisites = co_requisites or {} 
            exclusions = exclusions or [] 
            self.json.save_initial_data(self.money, resources, employees, co_requisites, exclusions)

        else: # abrir sesión existente 
            data = self.json.charge_data() 
            self.money = data["money"] 
            resources = data["resources"] 
            employees = data["employees"] 
            co_requisites = data["co_requisites"] 
            exclusions = data["exclusions"]

        #inventario en memoria y en json 
        self.rc_mg = Resources_Manager()
        self.rc_mg.add_resources(resources, self) 
        
        self.emp_mg = Team_Manager() 
        self.emp_mg.add_employees(employees, self)
        
        # restricciones
        self.restrictions = Restrictions(co_requisites, exclusions)
 
        
    @property 
    def data(self):
        return self.json.data
    
    def refresh_data(self):
        self.json.save_data(self.data)

    def add_event(self, event):
        events : list[dict] = self.data["events"]
        events.append(event)
        self.refresh_data()

    def valid_cost(self, cost):
        data = self.data 
        presupuesto = float(data["presupuesto"])

        if(cost > presupuesto):
            raise Exception("The agency's budget is not enough")
    
    def delete_event(self, event):
        events: list[dict] = self.data["events"]
        if event in events: 
            events.remove(event)
            self.refresh_data()
            return True
        return False
       

    #region : some aditional tools
    #sobreescribir los rcs del json
    def sync_resources_to_json(self): 
        self.data["resources"] = [[res.name, res.type, res.cant, res.dispo] 
                                       for res in self.rc_mg.recursos.values()] 
        self.refresh_data() 

    #sobreescribir los emp del json
    def sync_employees_to_json(self): 
        self.data["employees"] = [[emp.rol, emp.cant, emp.dispo] 
                                       for emp in self.emp_mg.work_team.values()] 
        self.refresh_data() 

    def sync_restrictions_to_json(self):
        self.json.data["co_requisites"] = self.restrictions.co_requisites 
        self.json.data["exclusions"] = self.restrictions.exclusions 
        self.refresh_data(self.data)
    # endregion 



