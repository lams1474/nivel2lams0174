class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.cursos = []

    def inscribir_curso(self, curso):
        self.cursos.append(curso)
        curso.estudiantes.append(self)

    def mostrar_cursos(self):
        print(f"Estudiante: {self.nombre}")
        for curso in self.cursos:
            print(f"- {curso.nombre}")


class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes = []

    def mostrar_estudiantes(self):
        print(f"Curso: {self.nombre}")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre}")


# Ejemplo de uso
curso1 = Curso("Matemáticas", "MAT101")
curso2 = Curso("Historia", "HIS202")

estudiante1 = Estudiante("Ana", "12345")
estudiante2 = Estudiante("Luis", "67890")

estudiante1.inscribir_curso(curso1)
estudiante2.inscribir_curso(curso2)
curso1.mostrar_estudiantes()
estudiante1.mostrar_cursos()
