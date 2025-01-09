# Clase que representa un estudiante
class Estudiante:
    def __init__(self, nombre, matricula):
        # Atributos de la clase Estudiante
        self.nombre = nombre  # Nombre del estudiante
        self.matricula = matricula  # Número de matrícula del estudiante
        self.cursos = []  # Lista de cursos en los que está inscrito el estudiante

    # Método para inscribir al estudiante en un curso
    def inscribir_curso(self, curso):
        self.cursos.append(curso)  # Agrega el curso a la lista de cursos del estudiante
        curso.estudiantes.append(self)  # Agrega al estudiante a la lista de estudiantes del curso

    # Método para mostrar los cursos en los que está inscrito el estudiante
    def mostrar_cursos(self):
        print(f"Estudiante: {self.nombre}")
        for curso in self.cursos:  # Itera sobre los cursos del estudiante
            print(f"- {curso.nombre}")  # Muestra el nombre de cada curso

# Clase que representa un curso
class Curso:
    def __init__(self, nombre, codigo):
        # Atributos de la clase Curso
        self.nombre = nombre  # Nombre del curso
        self.codigo = codigo  # Código único del curso
        self.estudiantes = []  # Lista de estudiantes inscritos en el curso

    # Método para mostrar los estudiantes inscritos en el curso
    def mostrar_estudiantes(self):
        print(f"Curso: {self.nombre}")
        for estudiante in self.estudiantes:  # Itera sobre los estudiantes inscritos
            print(f"- {estudiante.nombre}")  # Muestra el nombre de cada estudiante

# Ejemplo de uso
curso1 = Curso("Matemáticas", "MAT101")  # Crear un curso llamado Matemáticas
curso2 = Curso("Historia", "HIS202")    # Crear un curso llamado Historia

estudiante1 = Estudiante("Ana", "12345")  # Crear un estudiante llamado Ana
estudiante2 = Estudiante("Luis", "67890")  # Crear un estudiante llamado Luis

estudiante1.inscribir_curso(curso1)  # Inscribir a Ana en Matemáticas
estudiante2.inscribir_curso(curso2)  # Inscribir a Luis en Historia

curso1.mostrar_estudiantes()  # Mostrar estudiantes inscritos en Matemáticas
estudiante1.mostrar_cursos()  # Mostrar los cursos de Ana

