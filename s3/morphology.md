class: center, middle

### Introduction to Human Language Technologies

# Lab.3: Morphology

Gerard Escudero i Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[Session requirements]

* Lexical Level in *nltk*

* Paraphrases

---

# Session requirements

PoS tagger & lemmatizer:

* Both Linux & Windows (via python shell)

```python3
import nltk

nltk.download('averaged perceptron tagger')

nltk.download('wordnet')
```

Attached resources:

* [trial.tgz](resources/trial.tgz): trial set of the project

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .cyan[Lexical Level in *nltk*]

* Paraphrases

---

# Lexical level in *nltk* library

* Words

  - Tokenization achieves words. 
  - Multiwords (e.g. ”Even though”) are not recognized. 
  - MWETokenizer is not useful.

* POS tags <br>
`t_POS_list = nltk.pos_tag(t_list)`

* Lemmas

```python3
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()
wnl.lemmatize(token, pos=[POS])     # POS can be: ’n’,’v’, ...
```

* Senses

  - We will see in the sessions related to WSD and WordNet.

* Example:

  - [view](codes/lemmatizer.html) / [download](codes/lemmatizer.ipynb)

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .brown[Lexical Level in *nltk*]

* .cyan[Paraphrases]

---

# Mandatory exercise

Statement:

1. Read all pairs of sentences of the trial set within the evaluation framework of the project.

2. Compute their similarities by considering lemmas and Jaccard distance.

3. Compare the results with those in session 2 (*document structure*) in which words were considered.

4. Compare the results with gold standard by giving the *pearson correlation* between them.

5. Questions (justify the answers):

  - Which is better: words or lemmas? 

  - Do you think that could perform better for any pair of texts? 

