from classes.session import Session

def main():
    correo = input("Please, write your email contact")
    resources : list[list] = input("Make your inventory with your resources")
    employees : list[list] = input("Write your employees' roles")
    session = Session(correo, resources, employees, co_requisites, exclusions)

if __name__ == "__main__":
    main()