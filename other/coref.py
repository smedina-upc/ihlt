# Load your usual SpaCy model (one of SpaCy English models)
import spacy
nlp = spacy.load('en')

# load NeuralCoref and add it to the pipe of SpaCy's model
import neuralcoref
coref = neuralcoref.NeuralCoref(nlp.vocab)
nlp.add_pipe(coref, name='neuralcoref')

# You're done. You can now use NeuralCoref the same way you usually manipulate a SpaCy document and it's annotations.
doc = nlp(u'My sister has a dog. She loves him.')

print(doc._.has_coref)
print(doc._.coref_clusters)
