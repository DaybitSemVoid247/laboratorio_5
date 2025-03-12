import json   
'''import archivo json '''
def cargar_alumnos(ruta_archivo):   #creando un afuncion para cargar los datos de los alumnos
    with open(ruta_archivo, 'r') as archivo:  #
        return json.load(archivo)

def buscar_alumno(alumnos, nombre): #funcion para buscar el nombre en la lista de alumnos
    for alumno in alumnos:    #repeticion en la lista para encontrar el nombre
        if alumno['nombre'].lower() == nombre.lower():  #si se encuentra el nombre del alumno
            return alumno
    return None

if __name__ == "__main__":    #inicio de la ejecucion del programa
    ruta = "laboratorio_5/alumnos.json"  #añadiendo la ruta del archivo json
    alumnos = cargar_alumnos(ruta)   
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")

    resultado = buscar_alumno(alumnos, nombre_buscar)   #resultado de la busqueda 
    if resultado:                    
        print(f"Alumno encontrado: {resultado}")
    else:
        print("Alumno no encontrado.")