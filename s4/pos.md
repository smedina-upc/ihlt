class: center, middle

### Introduction to Human Language Technologies

# Lab.4: Part of Speech

Gerard Escudero & Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[Part-of-Speech Models]

* Exercise

---

# Part-of-Speech Models

- Statistical: <br>

  - *Hidden Markov Models*

  - *Conditional Random Fields*

  - *TnT*, *Perceptron*

  - ...

- Rule based: 

  - *Brill*

---

# Penn Treebank

### Requirements

```
import nltk
nltk.download('treebank')
```

### Access

```
len(nltk.corpus.treebank.tagged_sents()) 👉 3914

nltk.corpus.treebank.tagged_sents()[1]
👉 [('Mr.', 'NNP'),
    ('Vinken', 'NNP'),
    ('is', 'VBZ'),
    ('chairman', 'NN'),
    ('of', 'IN'),
    ('Elsevier', 'NNP'),
    ('N.V.', 'NNP'),
    (',', ','),
    ('the', 'DT'),
    ('Dutch', 'NNP'),
    ('publishing', 'VBG'),
    ('group', 'NN'),
    ('.', '.')]
```

---

# Hidden Markov Models I

### Single Validation Data

```
train = nltk.corpus.treebank.tagged_sents()[:3000]
test = nltk.corpus.treebank.tagged_sents()[3000:]
```

### Learning the model (MLE)

```
trainer = nltk.tag.hmm.HiddenMarkovModelTrainer()
HMM = trainer.train_supervised(train)

HMM.accuracy(test) 👉 0.36844377293330455

len(set(test).difference(train)) 👉 1629
```

---

# Hidden Markov Models II

### Learning the model (LID smoothing)

```
def LID(fd, bins):
  return nltk.probability.LidstoneProbDist(fd, 0.1, bins)

trainer = nltk.tag.hmm.HiddenMarkovModelTrainer()
HMM = trainer.train_supervised(train, estimator=LID)

HMM.accuracy(test) 👉 0.8984243470753291

```

### Learning the  model (LID smoothing)

```
HMM = nltk.HiddenMarkovModelTagger.train(train)

HMM.accuracy(test) 👉 0.8984243470753291

```

---

# Hidden Markov Models III

### Saving models

```
import dill
from google.colab import drive

drive.mount('/content/drive')

with open('/content/drive/My Drive/models/hmmTagger.dill', 'wb') as f:
    dill.dump(HMM, f)
```

### Loading models

```
with open('/content/drive/My Drive/models/hmmTagger.dill', "rb") as f:
    hmm = dill.load(f)
```

---

### TnT

```
TnT = nltk.tag.tnt.TnT()
TnT.train(train_data)
TnT.evaluate(test_data) c0.457
TnT.tag(['the', 'men', 'attended', 'to', 'the', 'meetings'])  👉  ...
```

### Perceptron

```
PER = nltk.tag.perceptron.PerceptronTagger(load=False)
PER.train(train_data)
PER.evaluate(test_data)  👉  0.644
PER.tag(['the', 'men', 'attended', 'to', 'the', 'meetings'])  👉  ...
```

### CRF

```
!pip install python-crfsuite
...

CRF = nltk.tag.CRFTagger()
CRF.train(train_data,'crf_tagger_model')
CRF.evaluate(test_data)  👉  0.685
CRF.tag(['the', 'men', 'attended', 'to', 'the', 'meetings'])  👉  ...
```

---
class: left, middle, inverse

# Outline

* .brown[Part-of-Speech Models]

* .cyan[Exercise]

---

# Exercise

1. Consider Treebank corpus. 

  * Train HMM, TnT, perceptron and
CRF models using the first 500, 1000, 1500, 2000, 2500 and
3000 sentences. 

  * Evaluate the resulting 24 models using
sentences from 3001.

2. Provide a figure with four learning curves, each per model type
(X=training set size; Y=accuracy). 

  * Which model would you select? Justify the answer.


