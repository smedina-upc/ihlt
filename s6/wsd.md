class: center, middle

### Introduction to Human Language Technologies

# Lab.6: Word Sense Disambiguation

Gerard Escudero & Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[Lesk in NLTK]

* UKB in TextServer

* Exercise

---

# Lesk in NLTK

**Requirements**:

```python3
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
```

**Use**:

```python3
context = ['I', 'went', 'to', 'the', 'bank', 'to', 'deposit', 'money', '.']

synset = nltk.wsd.lesk(context, 'bank', 'n')
```

**Result**:

```python3
synset.name(), synset.definition()
👉
('savings_bank.n.02',
 'a container (usually with a slot in the top) for keeping money at home')
```

---
class: left, middle, inverse

# Outline

* .brown[Lesk in NLTK]

* .cyan[UKB in TextServer]

* Exercise

---

# UKB in TextServer

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
ts = TextServer('usuari', 'passwd', 'senses') 
ts.senses("The boy plays with a black dog.")
👉
[[['The', 'the', 'DT', 'determiner', 'N/A'],
  ['boy', 'boy', 'NN', 'noun', '10285313-n'],
  ['plays', 'play', 'VBZ', 'verb', '01079480-v'],
  ['with', 'with', 'IN', 'preposition', 'N/A'],
  ['a', 'a', 'DT', 'determiner', 'N/A'],
  ['black', 'black', 'JJ', 'adjective', '00392812-a'],
  ['dog', 'dog', 'NN', 'noun', '02084071-n'],
  ['.', '.', 'Fp', 'punctuation', 'N/A']]]
```

---
class: left, middle, inverse

# Outline

* .brown[Lesk in NLTK]

* .brown[UKB in TextServer]

* .cyan[Exercise]

---

# Exercise

1. Read all pairs of sentences of the *SMTeuroparl* files of test set within the
evaluation framework of the project.

2. Apply WSD algorithms to the words in the sentences.

3. Compute their similarities by considering senses and Jaccard coefficient.

4. Compare the results with those in session 2 (document) and 3 (morphology) in which words and lemmas were considered.

5. Compare the results with gold standard by giving the pearson correlation between them.

#### Resources:

- [`test-gold.tgz`](../sts/resources/test-gold.tgz)

