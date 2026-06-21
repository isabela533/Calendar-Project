from tools.check_time import is_time_valid, is_available
from typing import TYPE_CHECKING 
if TYPE_CHECKING: from classes.session import Session

# los eventos en el json tienen la forma de lista de diccionarios en donde cada evento es un diccionario
def add_event(new_event: dict, session : "Session"):
    try:
        session.valid_cost(new_event["cost"])
    except Exception as e:
        return {"success": False, "error": str(e)}

    init, end = new_event["init"], new_event["end"]
    valid = is_time_valid(init, end)
    if valid is not True:
        return {"success": False, "error": valid}

    availability = is_available(init, end, session.data)
    if not availability["available"]:
        return {"success": False, "suggestions": availability["suggestions"]}
    
    rsc_names = [session.rc_mg.recursos[name].name 
                 for name, type_, cant, dispo in new_event.get("resources", [])
                 if name in session.rc_mg.recursos]
    emp_names = [session.emp_mg.work_team[rol].rol 
                 for rol, cant, dispo in new_event.get("team", [])
                 if rol in session.emp_mg.work_team]

    try:
        session.restrictions.validate(rsc_names + emp_names)
    except Exception as e:
        return {"success": False, "error": str(e)}

    ocupados_rc  = []  # track de recursos ocupados exitosamente
    ocupados_emp = []  # track de empleados ocupados exitosamente

    try:
        for name, type_, cant, dispo in new_event.get("resources", []):
            session.ocupar_resource(name, cant)
            ocupados_rc.append((name, cant))  # solo agrega si no lanzó excepción

        for rol, cant, dispo in new_event.get("team", []):
            session.ocupar_employee(rol, cant)
            ocupados_emp.append((rol, cant))  # solo agrega si no lanzó excepción

    except Exception as e:
        # Falló al ocupar — revertir SOLO los que sí se ocuparon
        for name, cant in ocupados_rc:
            session.liberar_resource(name, cant)
        for rol, cant in ocupados_emp:
            session.liberar_employee(rol, cant)
        return {"success": False, "error": str(e)}

    return {"success": True}







    
    
    