class: center, middle

### Introduction to Human Language Technologies

# Lab.1: Framework

Gerard Escudero i Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[Presentation]

* Session requirements

* Framework

* Additional information

---

# Goal of IHLT lab sessions

* Learn to use basic NLP functions for managing text content

* Solve simple programming exercises

--

<br>

* Programming platform: Jupyter (python3)

* NLP package for Python: nltk

<br>

* Similar open-source NLP suites out of this framework: <br>
  - Stanford CoreNLP
  - Freeling
  - Apache OpenNLP
  - IXA Pipes

---

# Evaluation of IHLT lab

#### Mandatory exercises & projects:

* a set of exercises solved in lab sessions (individual)

* a set of 3 small projects, one per block among diferent
propossals (in pairs)

* the project Semantic Textual Similarity (in pairs)

--

<br>

* Grade = 0.3 * Project + 0.1 Blocks + 0.1 * Sessions <br>
(this represents the 50% of the final IHLT grade)

<br>

* Jupyter notebooks of exercises & projects should be
uploaded to [https://raco.fib.upc.edu](https://raco.fib.upc.edu)

---

# Topic of the project (STS)

#### How similar two sentences are between them? compare different approaches

* Relevance of the topic: <br><br>
IR, QA, summarization, automatic translation, plagiarism
detection, ...

* *Paraphrase* : pair of texts with the same meaning but different words

* Example from trial of project data set: <br><br>
`The bird is bathing in the sink.` <br><br>
`Birdie is washing itself in the water basin.`

---

# Project description

#### Deadline: 12/12/2019 (oral presentation)

* Implement some approaches to detect paraphrase using
sentence similarity metrics. 
  - Explore some lexical dimensions.
  - Explore the syntactic dimension alone.
  - Explore the combination of both previous.

* Compare and comment the results achieved by these approaches
among them and among the official results.

* Use data set and description of task Semantic Textual Similarity in SemEval 2012: <br>
[https://www.cs.york.ac.uk/semeval-2012/task6/index.html](https://www.cs.york.ac.uk/semeval-2012/task6/index.html)

* Deliver to raco:
  - Jupyter notebook: sts-[Student1]-[Student2].ipynb
  - Slides: sts-[Student1]-[Student2].pdf

---

# Small projects (blocks)

#### Deadline: 12/12/2019

* Text level:
  - Language identifier

* Lexical level (only one of them):
  - Spelling corrector
  - SMS spam filtering
  - WordNet & WSD
  - Sentiment analysis
  - SensEval Lexical Sample

* Sequence Level (only one of them):
  - NER
  - Chunking

---

# Framework installation (Linux)

#### Framework (python3, jupyter, nltk, numpy, scipy):

```
> sudo apt-get install python3    

> pip3 install -U pip

> pip3 install jupyter

> sudo pip3 install -U numpy

> sudo pip3 install -U nltk

> sudo pip3 install -U scipy

> jupyter notebook

Select `New/Python3`.

Stop server with `Ctrl-C`.
```

---

# Framework installation (Windows)

#### Framework (python3, jupyter, nltk, numpy, scipy):

* Download [python3](http://www.python.org)

* Install it checking the option <br> `Add python to the path`

* Start the shell `cmd`:

```
> pip install jupyter

> pip install -U numpy

> pip install -U nltk

> pip install -U scipy

> jupyter notebook

Select `New/Python3`.

Stop server with `Ctrl-C`.
```

---

# Execution test

#### Validate the installation process

* Open a new python3 jupyter notebook 

* Change the name of the session to `S1-[Student1]-[Student2]`

* Import without errors `nltk` library

* Save the session and exit jupyter server.

---
class: left, middle, inverse

# Outline

* .brown[Presentation]

* .cyan[Session requirements]

* Framework

* Additional information

---

# Session requirements

#### Gutenberg corpus:

Both Linux & Windows (via python shell)
```
> import nltk

> nltk.download('gutenberg')

> nltk.download('stopwords')
```

#### Attached resources:
[`pg35688.txt`](resources/pg35688.txt)

---
class: left, middle, inverse

# Outline

* .brown[Presentation]

* .brown[Session requirements]

* .cyan[Framework]

* Additional information

---

# NLTK Resources

#### Python library:

List of [resources](http://www.nltk.org/nltk_data/).

Download non-default resources from nltk:

```python3
import nltk
nltk.download()
```

#### Content

* *Corpora and lexical resources*: Brown corpus (PoS
annotations), sentence polarity corpus... 

* *Lexical resources* such as WordNet, SentiWordNet and specialized word lists.

* *Toy grammars*: grammars for English, Spanish, ...

* *Models*: Named Entity recognizer, taggers for English and
Russian, ...

---

# Corpus reader

[http://www.nltk.org/howto/corpus.html](http://www.nltk.org/howto/corpus.html)

corpus reader objects & classes: <br>
`from nltk.corpus import *resource* [as *variable name*]`

Gutenberg corpora:

```python3
nltk.download('gutenberg')
nltk.corpus.gutenberg.fileids()
txt = nltk.corpus.gutenberg.words('austen-persuasion.txt')
```

Example of *Corpus reader* using the *Gutenberg corpora*: 

* [view](codes/corpus.html) / [download](codes/corpus.ipynb)

---

# Stopwords reader

Provide the list of stop words of a specific language. 

Words that do not have individual meaning 
* pronouns
* determiners
* auxiliary verbs
* ...

Example of *Stopwords reader*:

* [view](codes/stopwords.html) / [download](codes/stopwords.ipynb)

---

# Session exercise

1. Develop a jupyter notebook that show the 25
non-stopwords with more number of occurrences in the file
'blake-poems.txt' of Gutenberg corpus.

Upload the jupyter file of the exercise to the Raco.

---
class: left, middle, inverse

# Outline

* .brown[Presentation]

* .brown[Session requirements]

* .brown[Framework]

* .cyan[Additional information]

---

# Class Text

It allows:

* Consulting occurrences of words

* Consulting contexts

* Drawing dispersion plots

Example of *Class Text*:

* [view](codes/text.html) / [download](codes/text.ipynb)


.col5050[
.col1[
## Plain Text

Loading corpus from a text file:

* [view](codes/plain.html) / [download](codes/plain.ipynb)
]
.col2[
## Web Example

Fetching web data as string: 

* [view](codes/web.html) / [download](codes/web.ipynb)
]
]

