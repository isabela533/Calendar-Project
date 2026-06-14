from datetime import datetime, timedelta, date
import json 

#   ver validez de fechas (formato y validez)
def is_time_valid(init, end):
    #   formato
    try:
        init = datetime.strptime(init, "%Y-%m-%d").date()
        end = datetime.strptime(end, "%Y-%m-%d").date()
    except ValueError:
        return "❌ Invalid format. Use YYYY-MM-DD"
    
    # validez : verificar cuando las fechas coincidan en el mismo dia 
    now = datetime.now().date()
    if(init > end or init < now or end < now):
        raise Exception("❌ Invalid dates. Please use a valid date")
    
    return True     #  si todo esta bien, retornar true

def suggest_slot(init, end, ocuped_days: list):
    ocuped_days.sort(key=lambda x: x[0])  # ordenar por inicio

    duration = end - init
    suggestions = []
    hoy = date.today()

    for i in range(len(ocuped_days) - 1):
        current_end = ocuped_days[i][1]
        next_start = ocuped_days[i + 1][0]

        gap = (next_start - current_end).days - 1
        if gap >= duration.days:
            suggested_start = current_end + timedelta(days=1)
            suggested_end = suggested_start + duration
            if suggested_start >= hoy:
                suggestion = (suggested_start.strftime("%Y-%m-%d"), suggested_end.strftime("%Y-%m-%d"))
                if suggestion not in suggestions:
                    suggestions.append(suggestion)

    # sugerir después del último evento
    last_end = ocuped_days[-1][1]
    finish_start = last_end + timedelta(days=1)
    finish_end = finish_start + duration
    if finish_start < hoy:
        finish_start = hoy
        finish_end   = hoy + duration
    suggestion = (finish_start.strftime("%Y-%m-%d"), finish_end.strftime("%Y-%m-%d"))
    if suggestion not in suggestions:
        suggestions.append(suggestion)

    return suggestions

    
# ver si esta ocupada o no esa fecha y buscar un hueco 
def is_available(init, end, data :dict):
    events = data.get("events", [])

    #preparar variables, en formato datetime
    init_dt = datetime.strptime(init, "%Y-%m-%d").date()
    end_dt = datetime.strptime(end, "%Y-%m-%d").date()

    # crear una lista de los dias que estan ocupados y llenarla con las fechas de los eventos guardados
    ocuped_days = []
    solapado = False
    for ev in events:
        ev_start = datetime.strptime(ev["init"], "%Y-%m-%d").date()
        ev_end = datetime.strptime(ev["end"], "%Y-%m-%d").date()

        ocuped_days.append((ev_start, ev_end))  # lo agrego a la lista de fechas ocupadas
       
        # si se solapan
        if init_dt <= ev_end and end_dt >= ev_start:
            solapado = True

    # si hubo solapamiento, sugerir nuevas fechas
    if solapado: 
        suggestions = suggest_slot(init_dt, end_dt, ocuped_days)
        return {"available": False, "suggestions": suggestions}
    
    return {"available":True}   
 
    



    
    