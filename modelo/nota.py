from modelo.estudiante import Estudiante
from modelo.asignatura import Asignatura


class Nota:
    """
    Representa la calificación de un Estudiante en una Asignatura.
    Una Nota no es solo un número: une al estudiante, la asignatura
    y la calificación en una única entidad con identidad propia.
    """

    def __init__(self, estudiante: Estudiante, asignatura: Asignatura, calificacion: float):
        if not isinstance(estudiante, Estudiante):
            raise TypeError("Se esperaba un objeto Estudiante.")
        if not isinstance(asignatura, Asignatura):
            raise TypeError("Se esperaba un objeto Asignatura.")
        if not (0.0 <= calificacion <= 10.0):
            raise ValueError("La calificación debe estar entre 0.0 y 10.0.")

        self._estudiante = estudiante
        self._asignatura = asignatura
        self._calificacion = calificacion

    @property
    def estudiante(self) -> Estudiante:
        return self._estudiante

    @property
    def asignatura(self) -> Asignatura:
        return self._asignatura

    @property
    def calificacion(self) -> float:
        return self._calificacion

    @calificacion.setter
    def calificacion(self, valor: float):
        if not (0.0 <= valor <= 10.0):
            raise ValueError("La calificación debe estar entre 0.0 y 10.0.")
        self._calificacion = valor

    def __str__(self) -> str:
        return (
            f"Nota({self._estudiante.nombre} | "
            f"{self._asignatura.nombre} | "
            f"{self._calificacion:.2f})"
        )

    def __repr__(self) -> str:
        return self.__str__()
