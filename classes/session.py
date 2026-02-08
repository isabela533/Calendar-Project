from classes.gestor_json import Gestor_json
from classes.resources import Resources_Manager
from classes.working_team import Team_Manager
from classes.restrictions import Restrictions
from gestor.add_event import add_event as gestor_add_event
from gestor.delete_event import delete_event as gestor_del_event
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
        self.add_resources(resources) 
        
        self.emp_mg = Team_Manager() 
        self.add_employee(employees)
        
        # restricciones
        self.restrictions = Restrictions(co_requisites, exclusions)
 
        
    @property 
    def data(self):
        return self.json.data
    
    def refresh_data(self):
        self.json.save_data(self.data)

    # region -> Manejo de eventos
    def add_event(self, event : dict):
        if event in self.data["events"]:
            raise Exception(" Ummm 🤔 This event is already registered in the system.")
        result = gestor_add_event(event, self)
        if result["success"]:
            self.data["money"] -= event["cost"]
            self.data["events"].append(event)
            self.refresh_data()
            return True
        elif "suggestions" in result:
            return False, result["suggestions"]   
        elif "error" in result: 
            raise Exception(result["error"]) 

    def show_events(self): 
        events = self.data.get("events", []) 
        if not events: 
            print("No events registered.") 
        else: 
            print("📅 Events:") 
            for ev in events: 
                print(f"- {ev['name']} | {ev['init']} -> {ev['end']} | Cost: {ev['cost']}")

    def valid_cost(self, cost):
        data = self.data 
        presupuesto = float(data["money"])

        if(cost > presupuesto):
            raise Exception("The agency's budget is not enough")
    
    def delete_event(self, event : dict):
        gestor_del_event(self, event)
        events: list[dict] = self.data["events"]
        if event in events: 
            self.data["money"] += event["cost"]
            events.remove(event)
            self.refresh_data()
            return True
        else:
            raise Exception("Event not found")  #lanza excepcion si el evento no fue encontrado
    
    # endregion
       
    # region -> Manejo de recursos
    def add_resources(self, rc : list[list]):
        self.rc_mg.add_resources(rc)
        self.sync_resources_to_json()

    def get_rcs(self, rcs : list[list]):
        rc = self.rc_mg.get_rcs(rcs)
        self.sync_resources_to_json()
        return rc
        
    def remove_resources(self, rc : list[list]):
        self.rc_mg.remove_resources(rc)
        self.sync_resources_to_json()

    def ocupar_resource(self, name, cant):
        self.rc_mg.ocupar_resource(name, cant)
        self.sync_resources_to_json()

    def liberar_resource(self, name, cant):
        self.rc_mg.liberar_resource(name, cant)
        self.sync_resources_to_json()

    def show_rc(self):
        self.rc_mg.show_resources()
    #endregion

    # region -> Manejo de empleados
    def add_employee(self, emp : list[list]):
        self.emp_mg.add_employees(emp)
        self.sync_employees_to_json()

    def get_emp(self, emp : list[list]):
        em = self.emp_mg.get_emp(emp)
        self.sync_employees_to_json()
        return em

    def remove_employee(self, emp : list[list]):
        self.emp_mg.delete_employees(emp)
        self.sync_employees_to_json()

    def ocupar_employee(self, rol, cant):
        self.emp_mg.ocupar_employee(rol, cant)
        self.sync_employees_to_json()
    
    def liberar_employee(self, rol, cant):
        self.emp_mg.liberar_employee(rol, cant)
        self.sync_employees_to_json()

    def show_employees(self):
        self.emp_mg.show_employees()
    #endregion

    #region -> Manejo de restricciones
    def add_exclusion(self, r1, r2):
        self.restrictions.add_exclusion(r1, r2)
        self.sync_restrictions_to_json()

    def add_co_rq(self, recurso : str, dependencias : list[str]):
        self.restrictions.add_co_requisito(recurso, dependencias)
        self.sync_restrictions_to_json()

    def remove_exclusion(self, r1 : str, r2: str):
        self.restrictions.delete_exclusion(r1, r2)
        self.sync_restrictions_to_json()

    def remove_co_rq(self, rc : str, dep: str):
        self.restrictions.delete_co_requisito(rc, dep)
        self.sync_restrictions_to_json()

    def show_restrictions(self):
        self.restrictions.show_restrictions()
    #endregion 
    
    #region -> some aditional tools (sync to json)
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
        self.refresh_data()
    # endregion 



