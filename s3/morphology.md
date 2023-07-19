class: center, middle

### Introduction to Human Language Technologies

# Lab.3: Morphology

Gerard Escudero & Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[Lexical Level]

* Exercise

---

## *Pen Treebank Part-of-Speech tags* 

.small[
.cols5050[
.col1[
| Tag | Description |
|----------|------------|
| CC  | Coordinating conjunction |
| CD  | Cardinal number |
| DT  | Determiner |
| EX  | Existential there |
| FW  | Foreign word |
| IN  | Preposition or subordinating conjunction |
| JJ  | Adjective |
| JJR | Adjective, comparative |
| JJS | Adjective, superlative |
| LS  | List item marker |
| MD  | Modal |
| NN  | Noun, singular or mass |
| NNS | Noun, plural |
| NNP | Proper noun, singular |
| NNPS | Proper noun, plural |
| PDT | Predeterminer |
| POS | Possessive ending |
| PRP | Personal pronoun |
]
.col2[
| Tag | Description |
|----------|------------|
| PRP$ | Possessive pronoun |
| RB  | Adverb |
| RBR | Adverb, comparative |
| RBS | Adverb, superlative |
| RP  | Particle |
| SYM | Symbol |
| TO  | to |
| UH  | Interjection |
| VB  | Verb, base form |
| VBD | Verb, past tense |
| VBG | Verb, gerund or present participle |
| VBN | Verb, past participle |
| VBP | Verb, non-3rd person singular present |
| VBZ | Verb, 3rd person singular present |
| WDT | Wh-determiner |
| WP  | Wh-pronoun |
| WP$ | Possessive wh-pronoun |
| WRB | Wh-adverb |
]]]

---

# NLTK Lexical Level

### Requirements

```
import nltk
nltk.download('averaged_perceptron_tagger')
```

### Use

```
words = ['women', 'played', 'with', 'small', 'children', 'happily']
nltk.pos_tag(words)

👉 [('women', 'NNS'),
    ('played', 'VBD'),
    ('with', 'IN'),
    ('small', 'JJ'),
    ('children', 'NNS'),
    ('happily', 'RB')]
```

---

# NLTK Lemmatizer

### Requirements

```
nltk.download('wordnet')
nltk.download('omw-1.4')

wnl = nltk.stem.WordNetLemmatizer()

def lemmatize(p):
  d = {'NN': 'n', 'NNS': 'n', 
       'JJ': 'a', 'JJR': 'a', 'JJS': 'a', 
       'VB': 'v', 'VBD': 'v', 'VBG': 'v', 'VBN': 'v', 'VBP': 'v', 'VBZ': 'v', 
       'RB': 'r', 'RBR': 'r', 'RBS': 'r'}
  if p[1] in d:
    return wnl.lemmatize(p[0], pos=d[p[1]])
  return p[0]
```

### Use

```
[lemmatize(pair) for pair in pairs]

👉 ['woman', 'play', 'with', 'small', 'child', 'happily']
```

---

# spaCy Lexical Level

### Requirements

```
import spacy
nlp = spacy.load("ca_core_news_sm")
```

### Use

```
doc = nlp("The boy play with a black dog.")
[(token.text, token.pos_, token.lemma_, token.is_stop) for token in doc]

👉 [('The', 'DET', 'the', True),
    ('boy', 'NOUN', 'boy', False),
    ('play', 'VERB', 'play', False),
    ('with', 'ADP', 'with', True),
    ('a', 'DET', 'a', True),
    ('black', 'ADJ', 'black', False),
    ('dog', 'NOUN', 'dog', False),
    ('.', 'PUNCT', '.', False)]
```

- [Model tags](https://spacy.io/models/en)

---

# TextServer Lexical Leval

### Requirements: [textserver.py](../codes/textserver.py)

```
from google.colab import drive
import sys

drive.mount('/content/drive')
sys.path.insert(0, '/content/drive/My Drive/Colab Notebooks/ihlt')
from textserver import TextServer
```

### Use

```
ts = TextServer('usuari', 'passwd', 'morpho') 

ts.morpho("The boy play with a black dog.")
👉  
[[['The', 'the', 'DT', 'determiner'],
  ['boy', 'boy', 'NN', 'noun'],
  ['play', 'play', 'VB', 'verb'],
  ['with', 'with', 'IN', 'preposition'],
  ['a', 'a', 'DT', 'determiner'],
  ['black', 'black', 'JJ', 'adjective'],
  ['dog', 'dog', 'NN', 'noun'],
  ['.', '.', 'Fp', 'punctuation']]]
```

---
class: left, middle, inverse

# Outline

* .brown[Lexical Level]

* .cyan[Exercise]

---

# Exercise

1. Read all pairs of sentences of the *SMTeuroparl* files of test set within the
evaluation framework of the project.

2. Compute their similarities by considering lemmas and Jaccard distance.

3. Compare the results with those in session 2 (*document structure*) in which words were considered.

4. Compare the results with gold standard by giving the *pearson correlation* between them.

5. Questions (justify the answers):

  - Which is better: words or lemmas? 

  - Do you think that could perform better for any pair of texts? 

#### Resources:

* [`test-gold.tgz`](../sts/resources/test-gold.tgz)

