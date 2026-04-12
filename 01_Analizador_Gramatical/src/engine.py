import spacy

class AnalizadorNLP:
    def __init__(self, modelo="es_core_news_sm"):
        try:
            self.nlp = spacy.load(modelo)
        except OSError:
            print(f"Descargando modelo {modelo}...")
            from spacy.cli import download
            download(modelo)
            self.nlp = spacy.load(modelo)

    def obtener_pos(self, texto):
        doc = self.nlp(texto)
        return [(token.text, token.pos_, token.morph) for token in doc]

if __name__ == "__main__":
    # Prueba rápida
    app = AnalizadorNLP()
    resultado = app.obtener_pos("Hola Mundo.")
    for pal, pos, morph in resultado:
        print(f"{pal}: {pos}")