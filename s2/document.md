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

* .cyan[Session requirements]

* Textual zones

* Text level

---

# Session requirements

#### Tokenizer:

```
import nltk

nltk.download('punkt')
```

#### Attached resources:

[`test-gold.tgz`](../sts/resources/test-gold.tgz)

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .cyan[Textual zones]

* Text level


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

* .brown[Session requirements]

* .brown[Textual zones]

* .cyan[Text level]

---

# Text level in *nltk* library

* Standard functions for [tokenization](http://www.nltk.org/_modules/nltk/tokenize.html) (recommended by *nltk*):

  - Sentence splitting: <br>
`s_list = nltk.sent_tokenize(T, [language='LANG'])`

  - Direct tokenization: <br> 
`t_list = nltk.word_tokenize(s, [language='LANG'])`

  - `LANG` can be:
czech, danish, ducth, english, estonian, finnish, french,
german, greek, italian, norwegian, polish, portuguese,
slovene, spanish, swedish or turkish

* Depending on the needs, text can be splitted into
sentences before tokenizing or it can be directly tokenized.

* Transform from Unicode strings: <br>
`T.decode('utf8')`

* Example: [view](codes/s2c.html) / [download](codes/s2c.ipynb)

---

# Similarities

Set-oriented methods (similarities between sets of words):

* $S_{dice}(X,Y)=\frac{2\cdot \vert X \cap Y\vert}{\vert X\vert+\vert Y\vert}$

* $S_{jaccard}(X,Y)=\frac{\vert X \cap Y\vert}{\vert X \cup Y\vert}$

* $S_{overlap}(X,Y)=\frac{\vert X \cap Y\vert}{min(\vert X\vert,\vert Y\vert)}$

* $S_{cosine}(X,Y)=\frac{\vert X \cap Y\vert}{\sqrt{\vert X\vert\cdot\vert Y\vert}}$

Above similarities are in [0, 1] and can be used as distances simply
subtracting: $D = 1 − S$.

* Example: [view](codes/s2d.html) / [download](codes/s2d.ipynb)

---

# Mandatory exercise

Statement:

1. Read all pairs of sentences of the *SMTeuroparl* files of test set within the
evaluation framework of the project.

2. Compute their similarities by considering words and
Jaccard distance. A distance should be obtained for each pair of sentences (a vector of similarities).

3. Compare the previous results with gold standard by giving
the pearson correlation between them. Only a global measure should be obtained from all previous distances.<br>
`from scipy.stats import pearsonr` <br>
`pearsonr(refs, tsts)[0]`


Notes:

* Template example ([view](codes/readPars.html) / [notebook](codes/readPars.ipynb))
* Justify the answer.




