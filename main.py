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

if __name__ == "__main__":
    main()