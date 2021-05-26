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

* .cyan[Session requirements]

* PoS Models

* Exercise

---

# Session requirements

Pen treebank corpus:
```python3
import nltk
nltk.download('treebank')
```

*crf*:
```
!pip install python-crfsuite
```

No attached resources.

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .cyan[PoS Models]

* Exercise

---

# PoS Models

Different options:

* Use the default POS tagger (averaged perceptron) or a predefined one

* Learn a POS tagger

  - Statistical: <br>
    *HMM*: [view](codes/s4a.html) / [download](codes/s4a.ipynb) <br>
    *TnT*: [view](codes/s4b.html) / [download](codes/s4b.ipynb) <br>
    *perceptron*: [view](codes/s4c.html) / [download](codes/s4c.ipynb) <br>
    *CRF*: [view](codes/s4d.html) / [download](codes/s4d.ipynb) <br>

  - Rule based: <br>
    *Brill*

* Use third-parties’ code:
  - Senna
  - Stanford
  - hunpos

---

# Saving & loading models

Save/Load a learned model:

* CRF uses their own.

```python3
# Training and save:
CRF.train(train data,"fileName")
# Load
CRF.set_model_file("fileName")
```

* *HMM*, *Perceptron* and *TnT* can use *dill*. 

```python3
import dill
# saving
with open("tnt_treebank_pos_tagger", "wb") as f:
    dill.dump(TnT, f)
# loading
with open("tnt_treebank_pos_tagger", "rb") as f:
    TnT = dill.load(f)
```

* *Perceptron* and *TnT* can also use *pickle* <br>
(`dump` and `load` functions).

---
class: left, middle, inverse

# Outline

* .brown[Session requirements]

* .brown[PoS Models]

* .cyan[Exercise]

---

# Mandatory exercise

Statement:

1. Consider Treebank corpus. 

  * Train HMM, TnT, perceptron and
CRF models using the first 500, 1000, 1500, 2000, 2500 and
3000 sentences. 

  * Evaluate the resulting 24 models using
sentences from 3001.

2. Provide a figure with four learning curves, each per model type
(X=training set size; Y=accuracy). 

  * Which model would you select? Justify the answer.

Upload the jupyter file of the exercise to the Raco.
