from classes.gestor_json import Gestor_json
from classes.resources import Resources_Manager
from classes.working_team import Team_Manager
from classes.restrictions import Restrictions

class Session:
    def __init__(self, correo, resources, employees, co_requisites, exclusions):
        self.correo = correo
        self.json = Gestor_json(correo)
        self.rc_mg = Resources_Manager()
        self.rc_mg.add_resources(resources)  #hacer el inventario con resursos 
        self.emp_mg = Team_Manager()
        self.emp_mg.add_employees(employees)  #hacer el inventario con recursos humanos
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




