import spacy
from spacy.matcher import Matcher
from strings import ejemplo
import patterns
import metodos
from spacy.matcher import DependencyMatcher

nlp_es = spacy.load("es_dep_news_trf")


"""
*************** MATCHER **********************************
"""

#matcher = Matcher(nlp_es.vocab)
matcher = DependencyMatcher(nlp_es.vocab)
#matcher.add("bigramas", [patterns.pattern_esp_1, patterns.pattern_esp_2])
matcher.add("bigramas_dep", [patterns.pattern_sin])

"""
************** PASAJE DE TEXTO A SU RAIZ **********************************
"""

doc = nlp_es(ejemplo)

#lemma_text = "".join([token.lemma_ + " " for token in doc])
#lemma_doc = nlp_es(lemma_text)
#print(lemma_text.pos_)


# mando el texto al matcher
#matches = matcher(lemma_doc)
matches = matcher(doc)

"""
*********************** OUTPUTS *********************************
"""

#estrucutra_final = metodos.armar_estructura(doc, matches);
lista_token = []
print("Esto seria: TEXT - DEP - POS")
for token in doc:
    print("Token:", token.text, token.dep_, token.pos_ )
    lista_token.append(token)
print("Resultados Matcher")
print(matches)
for match_id, aux in matches:
    print("match sintactico...")
    print(lista_token[aux[0]])
    print(lista_token[aux[0]].dep_)
    print(lista_token[aux[1]])
"""
print(doc)
#print(matches)
#print("Resultados:", [lemma_doc[start:end].text for match_id, start, end in matches])
for match_id, start, end in matches:
    print("Token:", doc[start:end].text )
"""
