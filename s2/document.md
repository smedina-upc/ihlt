class: center, middle

### Introduction to Human Language Technologies

# Lab.2: Document structure

Gerard Escudero & Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[Textual zones]

* Tokenizers

* Similarities

* Exercise

---

# Beautiful Soup 

Getting raw text from HTML:

* Example: [view](codes/s2a.html) / [download](codes/s2a.ipynb)

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) also allows to treat HTML in all forms:

* Output: raw text ( .get text() ), pretty-printing...
* Manipulating tags: name, attributes, content...
* Navigating the tree: children, parent, siblings...
* Searching the tree: string, regular expressions, functions...
* Modifying the tree
* Encoding
* Parsing only a part of a document
* ...

---

# XML options

* Beautiful Soup

  - Just changing the second argument of the constructor <br>
`soup = BeautifulSoup(dt, ’xml’)`

* [xml.etree.ElementTree](https://docs.python.org/3.7/library/xml.etree.elementtree.html)

  - Standard python library

  - Builds a tree and provides methods for navigating, searching and modifying it

* [xml.sax](https://docs.python.org/3.7/library/xml.sax.html)

  - Standard python library

  - Processes the xml file without building the tree

  - It works based on events

  - It allows to process very big xml files such as big corpora

  - Example: [view](codes/s2b.html) / [download](codes/s2b.ipynb)

---
class: left, middle, inverse

# Outline

* .brown[Textual zones]

* .cyan[Tokenizers]

* Similarities

* Exercise

---

# NLTK Tokenizer

### Requirements

```
import nltk
nltk.download('punkt')
```

### Sentence Splitting

```
nltk.sent_tokenize('Men want children. They get relaxed with kids.')

👉 ['Men want children.', 'They get relaxed with kids.']
```

### Tokenizer

```
nltk.word_tokenize('Men want children.')

👉 ['Men', 'want', 'children', '.']
```

---

# spaCy Tokenizer (I)

### Requirements

```
import spacy
nlp = spacy.load('en_core_web_sm')
```

### Text Processing

```
doc = nlp('Men want children. They get relaxed with kids.')
```

### Sentence Splitting

```
[s.text for s in doc.sents]

👉 ['Men want children.', 'They get relaxed with kids.']
```

---

# spaCy Tokenizer (II)


### Tokenizer

```
s = next(doc.sents)
[(token.text, token.is_stop) for token in s]

👉 [('Men', False), 
    ('want', False), 
    ('children', False), 
    ('.', False)]
```

---

# Tokenització amb TextServer (FreeLing)

### Requeriments

- Script auxiliar: [textserver.py](../codes/textserver.py)

```
from google.colab import drive
import sys

drive.mount('/content/drive')
sys.path.insert(0, '/content/drive/My Drive/Colab Notebooks/ihlt')
from textserver import TextServer
```

### Use

```
ts = TextServer('user', 'passwd', 'tokenizer') 

ts.tokenizer('Men want children. They get relaxed with kids.')
👉  [['Men', 'want', 'children', '.'],
     ['They', 'get', 'relaxed', 'with', 'kids', '.']]
```

---
class: left, middle, inverse

# Outline

* .brown[Textual zones]

* .brown[Tokenizers]

* .cyan[Similarities]

* Exercise

---

# Similarities

Set-oriented methods (similarities between sets of words):

.cols5050[
.col1[
* $S_{dice}(X,Y)=\frac{2\cdot \vert X \cap Y\vert}{\vert X\vert+\vert Y\vert}$

* $S_{jaccard}(X,Y)=\frac{\vert X \cap Y\vert}{\vert X \cup Y\vert}$
]
.col2[
* $S_{overlap}(X,Y)=\frac{\vert X \cap Y\vert}{min(\vert X\vert,\vert Y\vert)}$

* $S_{cosine}(X,Y)=\frac{\vert X \cap Y\vert}{\sqrt{\vert X\vert\cdot\vert Y\vert}}$
]]

Above similarities are in [0, 1] and can be used as distances simply
subtracting: $D = 1 − S$.

### Example: 

```
from nltk.metrics import jaccard_distance

jaccard_distance(set(['The','eats','fish','.']),
                 set(['The','eats','blue','fish','.']))

👉  0.2
```

---
class: left, middle, inverse

# Outline

* .brown[Textual zones]

* .brown[Tokenizers]

* .brown[Similarities]

* .cyan[Exercise]

---

# Exercise

1. Read all pairs of sentences of the *SMTeuroparl* files of test set within the
evaluation framework of the project.

2. Compute their similarities by considering words and
Jaccard distance. A distance should be obtained for each pair of sentences (a vector of similarities).

3. Compare the previous results with gold standard by giving
the pearson correlation between them. Only a global measure should be obtained from all previous distances.<br>
`from scipy.stats import pearsonr` <br>
`pearsonr(refs, tsts)[0]`

4. Justify the answer.

.cols5050[
.col1[
#### Notes:
* Template example: <br> ([view](codes/readPars.html) / [notebook](codes/readPars.ipynb))
]
.col2[
#### Attached resources:
* [`test-gold.tgz`](../sts/resources/test-gold.tgz)
]]



