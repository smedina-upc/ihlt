class: center, middle

### Introduction to Human Language Technologies

# Lab Blocks: Lexical Level

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[Spelling corrector]

* SMS Spam Filtering

* WordNet & WSD

* Sentiment analysis

* SensEval Lexical Sample

---

# Levenshtein edit distance

The edit distance is the number of characters that need to be substituted, inserted, or deleted, to transform the first string to the second one.

* Example: <br>
`rain → sain → shin → shine` <br>
It is needed at least 3 steps

* NLTK example:

```python3
from nltk.metrics.distance import edit_distance

edit_distance('something', 'soothing')   # output: 2
```

---

# Spelling corrector

#### Attached resources:

* [wordsEn.txt](resources/wordsEn.txt) : list of english words <br>
[http://www-01.sil.org/linguistics/wordlists/english/](http://www-01.sil.org/linguistics/wordlists/english/)

#### Statement

Implement a simple approach for spelling correction based on a list of words:

* Input: word to be corrected.

* Output: input word (if it belongs to the list) or the word in the list with minimum edit distance to the input word

Contents:

* Read the word list from the attached file

* Implement this basic approach

* Use the approach to correct the words: `something`, `soemthing` and some other of your choose

---

# Towards a real approach

In order to implement a real system, some issues should be studied:

* *edit distance* is a high time consuming function.<br>
generating the candidates for only search among them

* In an interactive solution the output should be those words with minimum distance.
`sat → set, sit, sad`

* For an automatic solution we need some kind of language model <br>
Resource: Birkbeck spelling error corpus from the Oxford Text Archive.

* New approaches use context information

See the Peter Norvig’s article How to [Write a Spelling Corrector](http://www.norvig.com/spell-correct.html) for delving into the topic.

---
class: left, middle, inverse

# Outline

* .brown[Spelling corrector]

* .cyan[SMS Spam Filtering]

* WordNet & WSD

* Sentiment analysis

* SensEval Lexical Sample

---

# SMS Spam Filtering

*Spam filtering* is a type of *text categorization*, such as *language identification* and *sentiment analysis*.

* Classification algorithm in Machine Learning

* How we represent text by means of features?

  - *bag of words*: boolean codifying the presence of the indexed words (`nltk.FreqDist`)

  - *term frequency* (tf): frequency of the indexed word in the sentence (`nltk.text.tf`)

  - *term-frequency times inverse document-frequency* (tf/idf): as above re-weighting to avoid effect of too common words such as english word the (`nltk.text.tf_idf`)

* [sklearn](http://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) : great Machine Learning library for python

---

# SMS Spam Collection Data Set

* source: [UCI repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)

  - 5574 examples

  - 2 classes: `ham` and `spam`

  - Example: <br>
`ham    What you doing?how are you?`

* experiment design

  - single validation (50% - 50%)

  - randomly shuffle

  - punctuation removed

  - strings lowered

---

# Approaches

* Adapting ML algorithms to the problem 

  - *k Nearest Neighbors* + *jaccard* distance

* Text categorization in *sklearn*

* Example: [view](codes/sms.html) / [download](codes/sms.ipynb)

* Support Vector Machines

  - Define a user kernel for sets: <br>
$\kappa(S_1, S_2) = 2^{\vert S1 \cap S2\vert}$

  - Define a user kernel for tf/idf: <br>
$\kappa(d_1,d_2)=\sum_t w(t)^2tf(t,d_1)tf(t,d_2)$ <br>  <br>
where $tf$ is the term frequency, <br>
$w(t)=\frac{l}{df(t)}$, <br>
$l$ the number of documents and <br>
$df(t)$ is the number of documents which contains the term $t$.

---

# SMS Spam Filtering

#### Attached resources:

* [smsspamcollection.zip](resources/smsspamcollection.zip) : sms data set

#### Statement:

* Implement **ONE** of the approaches below and apply it to the SMS Spam Collection data set.

  - kNN with jaccard distance

  - set kernel for SVMs (requires advanced skills in Machine Learning)

  - tf/idf kernel for SVMs (requires advanced skills in Machine Learning)

  - preprocessing text components and ML algorithms in sklearn

* Extend the solution to the use of lemmas and other preprocess issues.

---
class: left, middle, inverse

# Outline

* .brown[Spelling corrector]

* .brown[SMS Spam Filtering]

* .cyan[WordNet & WSD]

* Sentiment analysis

* SensEval Lexical Sample

---

# WordNet & WSD

#### 1. Statement (WordNet):

* Develop a function to search and show the shortest path between two noun synset.

* Show the results as a tree.

* Apply it to show the shortest path between `dog.n.01` and `cat.n.01`.

#### 2. Statement (Lesk):

* Implement some of the variants of the Lesk’s algorithm.

Note: A possible variant is: stopwords, cosine, examples and hypernyms. But the solution is up to you.

---
class: left, middle, inverse

# Outline

* .brown[Spelling corrector]

* .brown[SMS Spam Filtering]

* .brown[WordNet & WSD]

* .cyan[Sentiment analysis]

* SensEval Lexical Sample

---

# Sentiment analysis data

#### NLTK’s Movie Reviews Corpus

* polarity corpus

  - 1000 positive examples

  - 1000 negative examples

* use in NLTK

```python3
from nltk.corpus import movie_reviews as mr

mr.fileids('pos')   # list of exemples:
        # ['pos/cv000_29590.txt', ...]

mr.words('pos/cv000_29590.txt')   # exemple as list of words:
        # ['films', 'adapted', ...]
```

*  System requirements:

```python3
import nltk
nltk.download('movie_reviews')
```

---

# SentiWordnet in NLTK

#### Example:

```python3
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

# getting the wordnet synset
synset = wn.synset('good.a.1')

# getting the sentiwordnet synset
sentiSynset = swn.senti_synset(synset.name())

# getting the score: positivity, negativity and objectivity
sentiSynset.pos_score(), sentiSynset.neg_score(), sentiSynset.obj_score()

        # result: (0.75, 0.0, 0.25)
```

*  System requirements:

```python3
import nltk
nltk.download('sentiwordnet')
```

---

# Sentiment analysis

#### Statement (unsupervised polarity system):

1. Get the first synset (most frequent) of one of the next alternatives:

  * nouns, verbs, adjectives and adverbs

  * nouns, adjectives and adverbs

  * only adjectives

2. Sum all the positive scores and negative ones to get the polarity

3.  Apply the system to the movie reviews corpus and give the accuracy

4.  Give some conclusions about the work

#### Notes:

  * We can assign the proper sense, instead of the first one, using a Word Sense Disambiguation tagger (such as Lesk). 

---
class: left, middle, inverse

# Outline

* .brown[Spelling corrector]

* .brown[SMS Spam Filtering]

* .brown[WordNet & WSD]

* .brown[Sentiment analysis]

* .cyan[SensEval Lexical Sample]

---

# NLTK’s Naı̈ve Bayes Example

#### Data format

```python3
[({'artificial': True, 'daughters': True, 'get': True, 'set': True}, 'neg'),
 ({'revelation': True, 'set': True, 'somewhere': True, 'strange': True}, 'pos'),
 ...]
```

#### Training

```python3
from nltk.classify import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(trainSet)
```

#### Classification and evaluation

```python3
from nltk.classify.util import accuracy
'Acc: ' + str(round(accuracy(classifier, testSet),2))  # 'Acc: 0.7'
```

#### Classification of a sample


```python3
str(classifier.classify(testSet[0][0])) + '==' + str(testSet[0][1]) + '?'
```

---

# SensEval Lexical Sample

#### Attached resource:

* [line-n.xml](resources/line-n.xml)

#### Statement:

* Use *Naïve Bayes* and *bag of words* for building a WSD classifier for the noun line

#### Description of the attached data

* 4146 samples of 6 senses (classes)

| samples | sense |
|--------:|:------|
| 373     | cord  |
| 376     | division |
| 349     | formation |
| 429     | phone |
| 2218    | product |
| 404     | text |

