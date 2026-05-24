class Asignatura:
    """Representa una asignatura con código y nombre."""

    def __init__(self, codigo: str, nombre: str):
        self._codigo = codigo
        self._nombre = nombre

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre de la asignatura no puede estar vacío.")
        self._nombre = valor

    def __str__(self) -> str:
        return f"Asignatura({self._codigo}, {self._nombre})"

    def __repr__(self) -> str:
        return self.__str__()
