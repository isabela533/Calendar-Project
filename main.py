from classes.session import Session
import json
import os 

def main():
    correo = input("Enter your email: ") 
    if os.path.exists(f"data/{correo}.json"): 
        # Login 
        session = Session(correo, create=False) 
        print("✅ Session started successfully.") 
    else: 
    # Create account 
        money = float(input("Enter initial money: ")) #revisar
        session = Session( correo, money=money, resources=[], employees=[], co_requisites={}, exclusions=[], create=True ) 
        print("✅ Account created successfully.")
    hola = list[list](input("Agrega un recurso: (name, type, cant, dispo)"))
    session.rc_mg.add_resources(hola, session)
if __name__ == "__main__":
    main()

#probar add resources S    P
#probar add employees S    P
# delete employees S   P
# delete resources S   p
# add restrictions S    P
#delete restrictions S   P
# add event S    P
#delete event S    P