from resources import Resources

class Restrictions:
    def __init__(self, co_requisites=None, exclusions=None):
        self.co_requisites = co_requisites or {}   # {"Proyector": ["Pantalla"]}
        self.exclusions = exclusions or []       # [("Sala A", "Sala B")]

    # para que el usuario ponga sus propias restricciones 
    def add_co_requisito(self, recurso, dependencias):
        self.co_requisites[recurso] = self.co_requisites.get(recurso, []) + dependencias

    def add_exclusion(self, r1, r2):
        self.exclusions.append((r1, r2))

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
