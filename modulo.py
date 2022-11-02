def listar_personas():
    nom = open("nombre.txt", "r")
    ap = open("apellido.txt", "r")
    dn = open("dni.txt", "r")
    print("\n Lista de personas")
    print("\n Nombre --- Apellido --- DNI  \n")
    while(True):
        nombre = nom.readline()
        apellido = ap.readline()
        dni = dn.readline()
        nombre = nombre.strip("\n")
        apellido = apellido.strip("\n")
        dni = dni.strip("\n")
        print ("{:<15} {:<15} {:<10}".format(nombre,apellido,dni))
        if not nombre:
            break
        
        
def agregar_personas():
    nuevoNombre = input("Nombre: ")
    archivoNombre = open("nombre.txt","at")
    archivoNombre.write("\n" + nuevoNombre)
    nuevoApellido = input("Apellido: ")
    archivoApellido = open("apellido.txt", "at")
    archivoApellido.write("\n" + nuevoApellido)
    nuevoDNI = input("DNI: ")
    archivoDNI = open("dni.txt", "at")
    archivoDNI.write("\n" + nuevoDNI)
    archivoNombre.close()
    archivoApellido.close()
    archivoDNI.close()
    
    
