from classes.session import Session
from classes.resources import Resources
from classes.working_team import Work_team

def delete_event(session: Session, event : dict):
    #liberar los recursos que estaban ocupados por este evento
    free_resources(session, event["resources"], event["employees"])

    #eliminar finalmente el evento desde la estructura de datos y el json
    deleted = session.delete_event(event)
    if not deleted:
        raise Exception("Event not found")  #lanza excepcion si el evento no fue encontrado
    
def free_resources(session : Session, resources, employees):
    for name, _, cant, _ in resources:    
        session.rc_mg.liberar_resource(name, cant, session)

    for rol, cant, _ in employees:
        session.emp_mg.liberar_employee(rol, cant, session)



    
     

    