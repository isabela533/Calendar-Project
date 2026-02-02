from tools.check_time import is_time_valid, is_available
from typing import TYPE_CHECKING 
if TYPE_CHECKING: from classes.session import Session

def show_options(suggestions : list[tuple]):
    for i, (sug_init, sug_end) in enumerate(suggestions, start=1):
            print(f"{i}. {sug_init} -> {sug_end}")
            
    choice = int(input("Please choose an option: "))    #dar a escoger 
    chosen_slot = suggestions[choice - 1]
    return chosen_slot

# los eventos en el json tienen la forma de lista de diccionarios en donde cada evento es un diccionario
def add_event(new_event: dict, session : "Session"):
    #validar presupuesto
    session.valid_cost(new_event["money"])    

    #validar fecha
    init = new_event["init"]  # tomando los valores de inicio y final del evento 
    end = new_event["end"]

    valid = is_time_valid(init, end) #validar fecha
    if(valid is not True):
        return False, valid
    
    #verificar si la fecha dada esta disponible y sugerir nuevas fechas
    result = is_available(init, end, session.data)

    #si no esta disponible, sugerir fechas, y reconfigurar el evento
    if not (result["available"]):
        print("This date is already taken by another event, "
              "but here are some dates that are available at this moment:")
        
        chosen_slot = show_options(result["suggestions"])
        new_event["init"], new_event["end"] = chosen_slot   #reconfigurar el evento

    # validar los recursos y los empleados que se necesitan 
    rsc = session.rc_mg.get_rcs(new_event["resources"], session) 
    emp = session.emp_mg.get_emp(new_event["team"], session) 

    # verificar si hay alguna restriccion que se cumpla 
    # validar la union de las dos listas -> nombres y roles de recursos materiales y humanos
    session.restrictions.validate(rsc + emp)
        







    
    
    