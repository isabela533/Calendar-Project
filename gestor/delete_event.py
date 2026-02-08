from typing import TYPE_CHECKING 
if TYPE_CHECKING: 
    from classes.session import Session

def free_resources(session : "Session", resources, employees):
    for name, _, cant, _ in resources:    
        session.liberar_resource(name, cant)

    for rol, cant, _ in employees:
        session.liberar_employee(rol, cant)

def delete_event(session: "Session", event : dict):
    #liberar los recursos que estaban ocupados por este evento
    free_resources(session, event["resources"], event["team"])
    



    
     

    