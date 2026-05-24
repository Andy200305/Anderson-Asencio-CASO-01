from modelo.estudiante import Estudiante
from modelo.asignatura import Asignatura
from modelo.nota import Nota
from typing import List, Optional


class RegistroNotas:
    """
    Clase fachada que administra el registro de Estudiantes,
    Asignaturas y Notas del sistema académico.
    """

    def __init__(self):
        self._estudiantes: List[Estudiante] = []
        self._asignaturas: List[Asignatura] = []
        self._notas: List[Nota] = []

    # ── Estudiantes ────────────────────────────────────────────────────────────

    def agregar_estudiante(self, matricula: str, nombre: str) -> Estudiante:
        """Crea y registra un nuevo Estudiante."""
        if self._buscar_estudiante(matricula):
            raise ValueError(f"Ya existe un estudiante con matrícula '{matricula}'.")
        estudiante = Estudiante(matricula, nombre)
        self._estudiantes.append(estudiante)
        return estudiante

    def _buscar_estudiante(self, matricula: str) -> Optional[Estudiante]:
        for e in self._estudiantes:
            if e.matricula == matricula:
                return e
        return None

    # ── Asignaturas ────────────────────────────────────────────────────────────

    def agregar_asignatura(self, codigo: str, nombre: str) -> Asignatura:
        """Crea y registra una nueva Asignatura."""
        if self._buscar_asignatura(codigo):
            raise ValueError(f"Ya existe una asignatura con código '{codigo}'.")
        asignatura = Asignatura(codigo, nombre)
        self._asignaturas.append(asignatura)
        return asignatura

    def _buscar_asignatura(self, codigo: str) -> Optional[Asignatura]:
        for a in self._asignaturas:
            if a.codigo == codigo:
                return a
        return None

    # ── Notas ──────────────────────────────────────────────────────────────────

    def registrar_nota(self, matricula: str, codigo_asignatura: str,
                       calificacion: float) -> Nota:
        """Registra una Nota para un Estudiante en una Asignatura."""
        estudiante = self._buscar_estudiante(matricula)
        if not estudiante:
            raise ValueError(f"Estudiante con matrícula '{matricula}' no encontrado.")

        asignatura = self._buscar_asignatura(codigo_asignatura)
        if not asignatura:
            raise ValueError(f"Asignatura con código '{codigo_asignatura}' no encontrada.")

        nota = Nota(estudiante, asignatura, calificacion)
        self._notas.append(nota)
        return nota

    # ── Consultas ──────────────────────────────────────────────────────────────

    def obtener_notas_estudiante(self, matricula: str) -> List[Nota]:
        """Devuelve la lista de notas de un estudiante."""
        return [n for n in self._notas if n.estudiante.matricula == matricula]

    def promedio_estudiante(self, matricula: str) -> float:
        """Calcula y retorna el promedio de calificaciones de un estudiante."""
        notas = self.obtener_notas_estudiante(matricula)
        if not notas:
            return 0.0
        return sum(n.calificacion for n in notas) / len(notas)

    def listar_estudiantes(self) -> List[Estudiante]:
        return list(self._estudiantes)

    def listar_asignaturas(self) -> List[Asignatura]:
        return list(self._asignaturas)
