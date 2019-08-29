class: center, middle

### Introduction to Human Language Technologies

# Lab.5: Lexical Semantics

Gerard Escudero i Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[WordNet]

* WordNet Similarities

* Paraphrases

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

* [view](codes/wordnet.html) / [download](codes/wordnet.ipynb)

---
class: left, middle, inverse

# Outline

* .brown[WordNet]

* .cyan[WordNet Similarities]

* Paraphrases

---

# WordNet similarities

[http://www.nltk.org/howto/wordnet.html](http://www.nltk.org/howto/wordnet.html)

* `path_similarity`

* `lch_similarity`

* `wup_similarity`

* `lin_similarity`

* `lowest_common_hypernyms`

Example:

* [view](codes/similarities.html) / [download](codes/similarities.ipynb)

---
class: left, middle, inverse

# Outline

* .brown[WordNet]

* .brown[WordNet Similarities]

* .cyan[Paraphrases]

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
