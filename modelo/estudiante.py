class Estudiante:
    """Representa a un estudiante con matrícula y nombre."""

    def __init__(self, matricula: str, nombre: str):
        self._matricula = matricula
        self._nombre = nombre

    @property
    def matricula(self) -> str:
        return self._matricula

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    def __str__(self) -> str:
        return f"Estudiante({self._matricula}, {self._nombre})"

    def __repr__(self) -> str:
        return self.__str__()
