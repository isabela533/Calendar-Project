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

    result = is_available(init, end, session.data)
    if not result["available"]:
        return {"success": False, "suggestions": result["suggestions"]}

    # validar recursos y empleados
    rsc = session.get_rcs(new_event["resources"])
    emp = session.get_emp(new_event["team"])
    session.restrictions.validate(rsc + emp)

    # si todo está bien, agregar
    return {"success": True}

        







    
    
    