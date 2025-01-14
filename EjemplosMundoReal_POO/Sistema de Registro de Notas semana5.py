# Sistema de Registro de Notas de Estudiantes
# Este programa permite gestionar las calificaciones de estudiantes,
# calculando promedios y determinando su estado de aprobación.

def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas
    Parámetro:
        notas (list): Lista de notas (números float)
    Retorna:
        float: Promedio calculado
    """
    return sum(notas) / len(notas)


def determinar_estado(promedio):
    """
    Determina si el estudiante aprobó basado en su promedio
    Parámetro:
        promedio (float): Promedio del estudiante
    Retorna:
        bool: True si aprobó, False si no
    """
    nota_minima_aprobacion = 4.0
    return promedio >= nota_minima_aprobacion


def mostrar_reporte(nombre_estudiante, notas, promedio, aprobado):
    """
    Muestra un reporte completo del estudiante
    Parámetros:
        nombre_estudiante (str): Nombre del estudiante
        notas (list): Lista de notas
        promedio (float): Promedio calculado
        aprobado (bool): Estado de aprobación
    """
    print("\n=== Reporte de Calificaciones ===")
    print(f"Estudiante: {nombre_estudiante}")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {'Aprobado' if aprobado else 'Reprobado'}")


def main():
    # Tipos de datos utilizados:
    # string - nombre_estudiante
    # list (float) - notas_estudiante
    # float - promedio_estudiante
    # boolean - estado_aprobacion
    # integer - cantidad_notas

    # Entrada de datos
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    cantidad_notas = int(input("Ingrese la cantidad de notas a registrar: "))

    # Lista para almacenar las notas
    notas_estudiante = []

    # Ingreso de notas
    for i in range(cantidad_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1} (1.0 - 7.0): "))
                if 1.0 <= nota <= 7.0:
                    notas_estudiante.append(nota)
                    break
                else:
                    print("Error: La nota debe estar entre 1.0 y 7.0")
            except ValueError:
                print("Error: Ingrese un número válido")

    # Cálculos
    promedio_estudiante = calcular_promedio(notas_estudiante)
    estado_aprobacion = determinar_estado(promedio_estudiante)

    # Mostrar resultados
    mostrar_reporte(nombre_estudiante, notas_estudiante,
                    promedio_estudiante, estado_aprobacion)


if __name__ == "__main__":
    main()