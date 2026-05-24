"""
main.py — Punto de entrada del Sistema de Notas Académicas
Caso 01: POO 4TO Test Práctico de Modelado en Python
"""
from modelo.registro_notas import RegistroNotas


def separador(titulo: str = ""):
    linea = "─" * 50
    print(f"\n{linea}")
    if titulo:
        print(f"  {titulo}")
        print(linea)


def main():
    registro = RegistroNotas()

    # ── 1. Registrar estudiantes ────────────────────────────────────────────
    separador("REGISTRO DE ESTUDIANTES")
    e1 = registro.agregar_estudiante("MAT-001", "Ana García")
    e2 = registro.agregar_estudiante("MAT-002", "Luis Pérez")
    print(f"  ✔ {e1}")
    print(f"  ✔ {e2}")

    # ── 2. Registrar asignaturas ────────────────────────────────────────────
    separador("REGISTRO DE ASIGNATURAS")
    a1 = registro.agregar_asignatura("POO-101", "Programación Orientada a Objetos")
    a2 = registro.agregar_asignatura("MAT-201", "Matemáticas Discretas")
    print(f"  ✔ {a1}")
    print(f"  ✔ {a2}")

    # ── 3. Registrar notas ──────────────────────────────────────────────────
    separador("REGISTRO DE NOTAS")
    n1 = registro.registrar_nota("MAT-001", "POO-101", 9.0)
    n2 = registro.registrar_nota("MAT-001", "MAT-201", 7.5)
    n3 = registro.registrar_nota("MAT-002", "POO-101", 8.0)
    print(f"  ✔ {n1}")
    print(f"  ✔ {n2}")
    print(f"  ✔ {n3}")

    # ── 4. Mostrar notas y promedio de Ana García ───────────────────────────
    separador("NOTAS DE ANA GARCÍA (MAT-001)")
    notas_ana = registro.obtener_notas_estudiante("MAT-001")
    for nota in notas_ana:
        print(f"  • {nota.asignatura.nombre:40s} → {nota.calificacion:.2f}")

    promedio_ana = registro.promedio_estudiante("MAT-001")
    print(f"\n  Promedio final: {promedio_ana:.2f} / 10.00")

    # ── 5. Mostrar promedio de Luis Pérez ───────────────────────────────────
    separador("NOTAS DE LUIS PÉREZ (MAT-002)")
    notas_luis = registro.obtener_notas_estudiante("MAT-002")
    for nota in notas_luis:
        print(f"  • {nota.asignatura.nombre:40s} → {nota.calificacion:.2f}")

    promedio_luis = registro.promedio_estudiante("MAT-002")
    print(f"\n  Promedio final: {promedio_luis:.2f} / 10.00")

    separador()
    print("  Sistema de Notas Académicas — Ejecución completada.")
    print("─" * 50)


if __name__ == "__main__":
    main()
