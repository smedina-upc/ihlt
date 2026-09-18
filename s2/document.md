class: center, middle

### Introduction to Human Language Technologies

# Lab.2: Document Structure

Gerard Escudero, Salvador Medina, Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

  * .cyan[Extracting Text from Documents]

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

  * .brown[Extracting Text from Documents]

  * .cyan[Tokenizers]

  * Similarities

  * Exercise

---

## NLTK Tokenizer

### Requirements

```
import nltk
nltk.download('punkt_tab')
```

### Sentence Splitting

The `sent_tokenize` function splits a text into a list of sentences.

```python
nltk.sent_tokenize('Men want children. They get relaxed with kids.')

👉 ['Men want children.', 'They get relaxed with kids.']
```

### Word Tokenization

The `word_tokenize` function splits a sentence into words and punctuation.

```python
nltk.word_tokenize('Men want children.')

👉 ['Men', 'want', 'children', '.']
```

---

# spaCy Tokenizer (I)

### Requirements

First, load a spaCy model. `en_core_web_sm` is the small English model.

```python
import spacy
# Make sure you have the model downloaded:
# python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')
```

### Text Processing

Processing a text with the `nlp` object creates a `Doc` object.

```python
doc = nlp('Men want children. They get relaxed with kids.')
```

### Sentence Splitting

You can iterate through the sentences in the `Doc` object using `doc.sents`.

```python
[sent.text for sent in doc.sents]

👉 ['Men want children.', 'They get relaxed with kids.']
```

---

# spaCy Tokenizer (II)

### Tokenization and Attributes

Each sentence in a `Doc` can be iterated to get individual `Token` objects, which come with rich linguistic annotations.

```python
first_sentence = next(doc.sents)

[(token.text, token.is_stop) for token in first_sentence]

👉 [('Men', False), 
    ('want', False), 
    ('children', False), 
    ('.', False)]
```

---

## Tokenization with TextServer (FreeLing)

### Requirements

This example uses a custom helper script to connect to a FreeLing server. The code below is typical for a Google Colab environment. Script: [textserver.py](../codes/textserver.py)

```
from google.colab import drive
import sys

drive.mount('/content/drive')
sys.path.insert(0, '/content/drive/My Drive/Colab Notebooks/ihlt')
from textserver import TextServer
```

### Usage

Once connected, you can send text to the server for tokenization.

```python
# Initialize with your user, password, and desired service
ts = TextServer('user', 'passwd', 'tokenizer') 

ts.tokenizer('Men want children. They get relaxed with kids.')
👉  [['Men', 'want', 'children', '.'],
     ['They', 'get', 'relaxed', 'with', 'kids', '.']]
```

---
class: left, middle, inverse

# Outline

  * .brown[Extracting Text from Documents]

  * .brown[Tokenizers]

  * .cyan[Similarities]

  * Exercise

---

## Similarity Metrics

**Set-oriented methods** measure the similarity between two sets of words.

.cols5050[
.col1[
* **Dice Coefficient**
  * $$S_{dice}(X,Y)=\frac{2 \cdot |X \cap Y|}{|X|+|Y|}$$
* **Jaccard Similarity**
  * $$S_{jaccard}(X,Y)=\frac{|X \cap Y|}{|X \cup Y|}$$
]
.col2[
* **Overlap Coefficient**
  * $$S_{overlap}(X,Y)=\frac{|X \cap Y|}{min(|X|,|Y|)}$$
* **Cosine Similarity** (Sets)
  * $$S_{cosine}(X,Y)=\frac{|X \cap Y|}{\sqrt{|X| \cdot |Y|}}$$
]
]

These similarity scores are all in the range $[0, 1]$. You can convert any of them into a **distance metric** by subtracting it from 1: $D = 1 - S$.

#### Example with NLTK
```python
from nltk.metrics.distance import jaccard_distance
jaccard_distance(set(['The','cat','eats','fish','.']), 
                 set(['The','cat','eats','blue','fish','.']))
👉  0.2
```

---
class: left, middle, inverse

# Outline

  * .brown[Extracting Text from Documents]

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



