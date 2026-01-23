from classes.session import Session
class Restrictions:
    def __init__(self, co_requisites=None, exclusions=None):
        self.co_requisites = co_requisites or {}   # {"Proyector": ["Pantalla"]}
        self.exclusions = exclusions or []       # [("Sala A", "Sala B")]

    # para que el usuario ponga sus propias restricciones 
    def add_co_requisito(self, recurso, dependencias, session : Session):
        self.co_requisites[recurso] = self.co_requisites.get(recurso, []) + dependencias
        session.sync_restrictions_to_json()

    def add_exclusion(self, r1, r2, session : Session):
        self.exclusions.append((r1, r2))
        session.sync_restrictions_to_json()

    def delete_co_requisito(self, recurso, dependencias, session: Session):
        if recurso in self.co_requisites:
            self.co_requisites[recurso] = [ 
                dep for dep in self.co_requisites[recurso] 
                if dep not in dependencias ] #sobrescribiendo las dependencias 
        #aqui estoy verificando si ya no quedan mas dependencias, borrar la restriccion
        if not self.co_requisites[recurso]: del self.co_requisites[recurso]
        session.sync_restrictions_to_json() #sincronizar con json

    def delete_exclusion(self, r1, r2, session: Session):
        if (r1, r2) in self.exclusions: 
            self.exclusions.remove((r1, r2))
        elif (r2, r1) in self.exclusions:
            self.exclusions.remove((r2, r1))    #por si esta en orden inverso
        session.sync_restrictions_to_json()

    # validar las restricciones de default 
    def validate(self, event_resources: list[str]):
        errors = []

        # validar co-requisitos
        for resource, dependencies in self.co_requisites.items():
            if resource in event_resources:
                for dep in dependencies:
                    if dep not in event_resources:
                        errors.append(f"{resource} requires {dep}")

        # validar exclusiones 
        for r1, r2 in self.exclusions:
            if r1 in event_resources and r2 in event_resources:
                errors.append(f"{r1} can't be used with {r2}")

        if len(errors) > 0:
            # tirar un exception con todos los errores acumulados
            raise Exception("\n".join(errors))
