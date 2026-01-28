from datetime import datetime, timedelta
import json 

#   ver validez de fechas (formato y validez)
def is_time_valid(init, end):
    #   formato
    try:
        init = datetime.strptime(init, "%Y-%m-%d %H:%M")
        end = datetime.strptime(end, "%Y-%m-%d %H:%M")
    except ValueError:
        return "❌ Invalid format. Use YYYY-MM-DD HH:MM"
    
    # validez : verificar cuando las fechas coincidan en el mismo dia 
    now = datetime.now()
    if(init > end or init < now or end < now):
        return "❌ Invalid dates. Please use a valid date"
    
    return True     #  si todo esta bien, retornar true


# ver si esta ocupada o no esa fecha y buscar un hueco 
def is_available(init, end, data :dict):
    events = data.get("events", [])

    #preparar variables, en formato datetime
    init_dt = datetime.strptime(init, "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M")

    # crear una lista de los dias que estan ocupados y llenarla con las fechas de los eventos guardados
    ocuped_days = []
    solapado = False
    for ev in events:
        ev_start = datetime.strptime(ev["init"], "%Y-%m-%d %H:%M")
        ev_end = datetime.strptime(ev["end"], "%Y-%m-%d %H:%M")

        ocuped_days.append((ev_start, ev_end))  # lo agrego a la lista de fechas ocupadas
       
        # si se solapan
        if not (end_dt <= ev_start or init_dt >= ev_end):
            solapado = True

    # si hubo solapamiento, sugerir nuevas fechas
    if solapado: 
        suggestions = suggest_slot(init_dt, end_dt, ocuped_days)
        return {"available": False, "suggestions": suggestions}
    
    return {"available":True}   
 
    
def suggest_slot(init, end, ocuped_days: list):
    ocuped_days.sort(key=lambda x: x[0])    #se organiza por fecha de inicio

    duration = end - init   #duracion del evento 

    # recorriendo intervalos 
    suggestions = []
    for i in range(len(ocuped_days) - 1):
        current_end = ocuped_days[i][1]     #dia que termina un evento
        next_start = ocuped_days[i + 1][0]  #dia que empieza el otro evento

        # si hay hueco, sugerir las fechas entre ambos eventos
        if (next_start - current_end) >= duration:
            suggested_start : datetime = current_end
            suggested_end : datetime = suggested_start + duration
            suggestions.append((suggested_start.strftime("%Y-%m-%d %H:%M"), suggested_end.strftime("%Y-%m-%d %H:%M")))
            

    # si no hay huecos entre eventos, sugerir el ultimo
    last_end : datetime = ocuped_days[-1][1]
    finish_end : datetime= last_end + duration
    suggestions.append((last_end.strftime("%Y-%m-%d %H:%M"), finish_end.strftime("%Y-%m-%d %H:%M")))

    return suggestions
    



    
    