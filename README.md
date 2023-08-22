# Multipalabras
desarrollo de un identificador de multipalabras utilizando spaCy 

  """
        Detecta ngramas y devuelve un arreglo de ngramas 
        con referencia a alguna clase para poder reemplazar.
        formato de lista/diccionario:
        {'nombre': nombre_clase,
         'metodos': metodos_clase,
         'relaciones': relacion_entre_clases }
         output: los ngramas de la siguiente forma:
         arreglo: ('clase_detectada_de_lista', [lista de ngramas asociados])
    """
    return [('cuenta',['cuenta bancaria','cuenta en','cuenta la','la cuenta']),
        ('transferencia',['transferencia bancaria','tranferencia en la','transferencia x']),
        ('deposito',['deposito bancario','deposito en'])]