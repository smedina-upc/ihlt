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

* .cyan[Session requirements]

* Word Sense Disambiguation

* Paraphrases

---

# Session requirements

PoS tagger & lemmatizer:

```python3
import nltk

nltk.download('wordnet')
```

Attached resources:

[`test-gold.tgz`](../sts/resources/test-gold.tgz)

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .cyan[Word Sense Disambiguation]

* Paraphrases

---

# Word Sense Disambiguation

Lesk in NLTK:

* [view](codes/s6a.html) / [download](codes/s6a.ipynb)

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .brown[Word Sense Disambiguation]

* .cyan[Paraphrases]

---

# Mandatory exercise

Statement:

1. Read all pairs of sentences of the *SMTeuroparl* files of test set within the
evaluation framework of the project.

2. Apply Lesk’s algorithm to the words in the sentences.

3. Compute their similarities by considering senses and Jaccard coefficient.

4. Compare the results with those in session 2 (document) and 3 (morphology) in which words and lemmas were considered.

5. Compare the results with gold standard by giving the pearson correlation between them.



