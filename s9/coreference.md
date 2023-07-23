class: center, middle

### Introduction to Human Language Technologies

# Lab.9: Coreference

Gerard Escudero & Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

- .cyan[Coreference]

- Exercici

---

# Coreference in spaCy I

### Requirements

```python3
!pip install spacy==2.1.0
!python -m spacy download en_core_web_sm
!pip install neuralcoref

import spacy
import neuralcoref

nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)
```

### Use

```python3
doc = nlp(u'My sister has a dog. She loves him.')

doc._.has_coref  👉  True

doc._.coref_clusters
👉  [My sister: [My sister, She], a dog: [a dog, him]]
```

---

# Coreference in spaCy II

### Visual Representation

![:scale 95%](figures/neuralcoref.png)


### Reference

* Neural Coreference - Hugging Face <br>
[https://huggingface.co/coref/](https://huggingface.co/coref/)

---

# Coreference in Textserver

### Requirements

```python3
from google.colab import drive
import sys
drive.mount('/content/drive')
sys.path.insert(0, '/content/drive/My Drive/Colab Notebooks/plh')
from textserver import TextServer
```

### Use

```python3
ts = TextServer('usuari', 'passwd', 'coreferences')

ts.coreferences("My sister has a dog. She loves him.")
👉  [['My sister', 'him'], ['a dog', 'She']]
```

---
class: left, middle, inverse

# Outline

- .brown[Coreference]

- .cyan[Exercici]

---

# Exercise

* Consider the first paragraph in Alice’s Adventures in Wonderland, by Lewis Carroll:
```
Alice was beginning to get very tired of sitting by her sister on the bank, 
and of having nothing to do: once or twice she had peeped into the book her 
sister was reading, but it had no pictures or conversations in it, ‘and what 
is the use of a book,’ thought Alice ‘without pictures or conversations?’
```

* It can be downloaded from: <br>
[http://www.gutenberg.org/files/11/11-0.txt](http://www.gutenberg.org/files/11/11-0.txt)

* Apply the spaCy coreference solver to the previous paragraph.

* Show the coreference chains. 

* What do you think about them? Justify your answer.


