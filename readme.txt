PROYECTO SISTEMA ESCOLAR

este proyecto esta pensado para ser un sistema controlador de notas, su uso es para los maestros.

app accounts:
controla los usuarios de la api

app panel:
controla las notas de los alumnos con un sistema CRUD
se planea que posea las vistas: PANEL (seleccion de unidades), MANEJO(notas y cuadros).

Se crea un grado, luego se crea una clase por grado, luego se crea una unidad por clase
luego se crean los estudiantes. Al final se usarán los scores como notas.

POSIBLES IMPLEMENTACIONES:
-sistema de mensajeria
-posible uso por parte de los alumnos

api:
user/ da el usuario actual

grades/ da todos los grados en la base de datos relacionados con el profesor en sesión  

classes/ da todas las clases en la base de datos relacionadas con el grado y al profesor en sesión

units/ da todas las unidades en la base de datos relacinadas con la clase y el profesor en sesión

students/ da todos los estudiantes en la base de datos
studnet/x dara la id del estudiante talvez

scores/ da todas las notas en la base de datos
score/x da la nota especificada por id