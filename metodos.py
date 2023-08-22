
def armar_estructura(doc, matches):
    lista_final = [];
    lista_aux = [];
    #guardo en la lista todas las palabras encontradas por el matcher
    #tengo que volver a poner esto con las prop de un token
    lista_matcheada = set([doc[start:end].text for match_id, start, end in matches])
    #print("lista matcheada :", lista_matcheada)
    for token in doc:
        #print("token pos: ", token.pos_)
        if(token.text in lista_matcheada) and (token.pos_ == 'NOUN') and (not token.text in lista_aux):
            palabra_base = token.text
            lista_asociados = list(filter(lambda a : palabra_base in a ,lista_matcheada))
            #print("")
            #print("lista asociados :", lista_asociados)
            lista_aux.append(palabra_base) 
            lista_final.append((palabra_base, lista_asociados))
    print("")
    print("lista final: ")
    #for elem in lista_final:
    #    print(elem)
    print(lista_final)
    return lista_final;


"""
for token in doc:
        #print("token pos: ", token.pos_)
        if(token.text in lista_matcheada) and (token.pos_ == 'NOUN') and (not token.text in lista_final):
            palabra_base = token.text
            lista_asociados = list(filter(lambda a : palabra_base in a ,lista_matcheada))
            #print("")
            #print("lista asociados :", lista_asociados)
            lista_final.append((palabra_base, lista_asociados))

            

for token in lista_matcheada:
        print("")
        print("tpken pos: ", token)
        #print("token pos: ", token.pos_)
        if(token.pos_ == 'NOUN') and (not token.text in lista_final):
            palabra_base = token.text
            lista_asociados = list(filter(lambda a : palabra_base in a ,lista_matcheada))
            #print("")
            #print("lista asociados :", lista_asociados)
            lista_final.append((palabra_base, lista_asociados))

"""