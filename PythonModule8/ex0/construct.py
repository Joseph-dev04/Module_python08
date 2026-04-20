import sys
import os
import site

def is_virtual_env():
    # Detecta si estamos en un entorno virtual
    return (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix)
    )


def get_venv_name():
    return os.path.basename(sys.prefix)


def main():
    print()

    if is_virtual_env():
        print("MATRIX STATUS: Welcome to the construct")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_venv_name()}")
        print(f"Environment Path: {sys.prefix}")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("\nPackage installation path:")
        for path in site.getsitepackages():
            if sys.prefix in path:
                print(path)

    else:
        print("MATRIX STATUS: You're still plugged in")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print("\nThen run this program again.")


class pepe():
    def __init__(self):
        self.name = "pepe"


if __name__ == "__main__":
    #hasarrt : Herramienta de introspeccion, lo que quiere decir es que nos ayuda a revisar nuestros objetos
    #en tiempo de ejecucion, ademas devuelve true o false, si lo probaramos directamente sys.real_prefix
    # nos daria una excepcion.
    #Lo unico que hace este metodo es buscar de un objeto (modulo) una variable, metodo, clases y propiedades
    #simplemente buscara la coincidencia y si existe TRUE de lo contrario FALSE
    #getattr() -> Devuelve el valor en caso de encontrarlo
    #setattr() -> Modifica el valor
    #delattr() -> Elimina el valor
    #ENTONCES PARA QUE BUSCAMOS REAL_PREFIX, BASE_PREFIX, PREFIX
    #Estas variables son una forma de identificar al sistema, en su tiempo se determinaron estas variables
    #real_prefix -> Es para ubicar entornos virtuales pero con un sistema antiguo llamado virtualenv
    #solo se verifica en caso de que se este usando una herramienta antigua
    #prefix -> Es una variable que indica el entorno de trabajo en el que te encuentras
    #base_prefix -> Es la ruta en donde esta el sistema principal todo en donde se mezcla las intalaciones con pip
    #Por tanto si yo estoy en un entorno virtual base_prefix cambia y es diferente a prefix de esta forma sabemos
    #que estamos en un entorno virtual, si son iguales estamos en el entorno global
    print(hasattr(sys, 'real_prefix'))
    print(hasattr(sys, 'base_prefix'))
    print(hasattr(sys, 'prefix'))
    #Ejemplo con una clase pepe
    print(hasattr(pepe(), 'name'))
    #tendra apellido?
    print(hasattr(pepe(), 'lastname'))
    #cual es su nombre?
    print(getattr(pepe(), 'name'))

    #Siguiente modulo os que tiene que ver con el sistema operativo
    #Usamos os.path -> porque esta clase en concreto o modulo, tiene un juego de herramienta que nos permiten manejar
    #rutas tenemos os.path.join(), os.path.split(), os.path.basename() entre varios utiles
    #En este caso os.path.basename(ruta) -> se le pasa una ruta y este nos devuelve el ultimo nombre que contiene
    #la ruta en cuestion. digamos jp/42Madrid/venv -> de esta ruta nos devolveria venv
    print(os.path.basename("/jp/42madrid/venv"))

    #Terminamos con site
    #site este modulo se encarga de encontrar y gestionar los paquetes intalados de terceros mediante pip
    #site.getsitepackages() devuelve las rutas de instalacion de los paquetes
    #si estuvieramos en un entorno virtual estas rutas seria personalizadas al entorno virtual
    print(site.getsitepackages())

    main()