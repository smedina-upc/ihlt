class: center, middle

### Introduction to Human Language Technologies

# Lab.5: Lexical Semantics

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

* WordNet

* WordNet Similarities

* Exercise

---

# Session requirements

WordNet:
```python3
import nltk
nltk.download('wordnet')
nltk.download('wordnet_ic')
```

No attached resources.

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .cyan[WordNet]

* WordNet Similarities

* Exercise

---

# WordNet reader

[http://www.nltk.org/howto/wordnet.html](http://www.nltk.org/howto/wordnet.html)

Provide an interface to access WordNet data, such as:

* synsets of a given lemma+PoS pair,

* lemmas of a given synset,

* hypernyms and hyponyms of a given synset,

* synonyms and antonyms of a given lemma in a synset

* least common subsumers of a pair of synsets

* different measures of synset similarity

* ...

Example:

* [view](codes/s5a.html) / [download](codes/s5a.ipynb)

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .brown[WordNet]

* .cyan[WordNet Similarities]

* Exercise

---

# WordNet similarities

[http://www.nltk.org/howto/wordnet.html](http://www.nltk.org/howto/wordnet.html)

* `path_similarity`

* `lch_similarity`

* `wup_similarity`

* `lin_similarity`

* `lowest_common_hypernyms`

Example:

* [view](codes/s5b.html) / [download](codes/s5b.ipynb)

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .brown[WordNet]

* .brown[WordNet Similarities]

* .cyan[Exercise]

---

# Mandatory exercise

Statement:

* Given the following (lemma, category) pairs:

```
(’the’,’DT’), (’man’,’NN’), (’swim’,’VB’), (’with’, ’PR’), (’a’, ’DT’),
(’girl’,’NN’), (’and’, ’CC’), (’a’, ’DT’), (’boy’, ’NN’), (’whilst’, ’PR’),
(’the’, ’DT’), (’woman’, ’NN’), (’walk’, ’VB’)
```
* For each pair, when possible, print their most frequent WordNet synset,
their corresponding least common subsumer (LCS) and their similarity
value, using the following functions:

  - Path Similarity

  - Leacock-Chodorow Similarity

  - Wu-Palmer Similarity

  - Lin Similarity

Normalize similarity values when necessary. What similarity seems better?
