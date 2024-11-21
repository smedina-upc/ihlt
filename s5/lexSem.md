class: center, middle

### Introduction to Human Language Technologies

# Lab.5: Lexical Semantics

Gerard Escudero, Salvador Medina, Jordi Turmo

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

* SentiWordNet

* Exercise

---

# WordNet

**Synsets**: content, definitions, examples and lemmas

```python3
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
nltk.download('omw-1.4')

wn.synsets('age','n')
👉  [Synset('age.n.01'),
     Synset('historic_period.n.01'),
     Synset('age.n.03'),
     Synset('long_time.n.01'),
     Synset('old_age.n.01')]
```

```python3
age = wn.synset('age.n.1')

age.definition()  👉  'how long something has existed'

age.examples()  👉  ['it was replaced because of its age']

[l.name() for l in wn.synset('historic_period.n.01').lemmas()]
👉  ['historic_period', 'age']
```

Reference: [http://www.nltk.org/howto/wordnet.html](http://www.nltk.org/howto/wordnet.html)
---

# Hyponyms & hyperonyms

.cols5050[
.col1[
**Direct relation**:

```python3
age.hyponyms()
👉  
[Synset('bone_age.n.01'),
 Synset('chronological_age.n.01'),
 Synset('developmental_age.n.01'),
 Synset('fetal_age.n.01'),
 Synset('mental_age.n.01'),
 Synset('newness.n.01'),
 Synset('oldness.n.01'),
 Synset('oldness.n.02'),
 Synset('youngness.n.01')]

age.hypernyms()
👉
[Synset('property.n.02')]

age.root_hypernyms()
👉
[Synset('entity.n.01')]
```
]
.col2[
**Claussure**:

```python3
hyper = lambda s: s.hypernyms()

list(age.closure(hyper))
👉
[Synset('property.n.02'),
 Synset('attribute.n.02'),
 Synset('abstraction.n.06'),
 Synset('entity.n.01')]

age.tree(hyper)
👉
[Synset('age.n.01'),
 [Synset('property.n.02'),
  [Synset('attribute.n.02'),
   [Synset('abstraction.n.06'), 
   [Synset('entity.n.01')]]]]]
```
]]

---

# Other relations

**Antonyms** (*variant*):
```python3
good = wn.synset('good.a.01')
good.lemmas()[0].antonyms()
👉
[Lemma('bad.a.01.bad')]
```

**Relations of Synsets**:

.cols5050[
.col1[
```python3
rels = getRelations(age)
for rel in rels:
  for s in rels[rel]:
    print(rel, s.name())
👉
hypernyms property.n.02
hyponyms bone_age.n.01
hyponyms chronological_age.n.01
hyponyms developmental_age.n.01
hyponyms fetal_age.n.01
hyponyms mental_age.n.01
hyponyms newness.n.01
hyponyms oldness.n.01
```
]
.col2[
<br><br><br>
```python3
hyponyms oldness.n.02
hyponyms youngness.n.01
attributes immature.a.04
attributes mature.a.03
attributes new.a.01
attributes old.a.01
attributes old.a.02
attributes young.a.01
```
]]

---

# *getRelations* function

```python3
def getRelations(ss):
  lexRels = ['hypernyms', 'instance_hypernyms', 'hyponyms', \
       'instance_hyponyms', 'member_holonyms', 'substance_holonyms', \
       'part_holonyms', 'member_meronyms', 'substance_meronyms', \
       'part_meronyms', 'attributes', 'entailments', 'causes', 'also_sees', \
       'verb_groups', 'similar_tos']

  def getRelValue(ss, name):
    method = getattr(ss, rel)
    return method()

  results = {}
  for rel in lexRels:
    val = getRelValue(ss, rel)
    if val != []:
      results[rel] = val
  return results
```

---
class: left, middle, inverse

# Outline

* .brown[WordNet]

* .cyan[WordNet Similarities]

* SentiWordNet

* Exercise

---

# WordNet similarities


```python3
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
nltk.download('omw-1.4')

dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')
```

```python3
dog.lowest_common_hypernyms(cat)  👉  [Synset('carnivore.n.01')]

dog.path_similarity(cat)  👉  0.2

dog.lch_similarity(cat)  👉  2.0281482472922856

dog.wup_similarity(cat)  👉  0.8571428571428571

nltk.download('wordnet_ic')
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')

dog.lin_similarity(cat,brown_ic)  👉  0.8768009843733973
```

---
class: left, middle, inverse

# Outline

* .brown[WordNet]

* .brown[WordNet Similarities]

* .cyan[SentiWordNet]

* Exercise

---

# SentiWordnet in NLTK

```python3
import nltk
nltk.download('wordnet')
nltk.download('sentiwordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
```

```python3
# getting the wordnet synset
synset = wn.synset('good.a.1')

# getting the sentiwordnet synset
sentiSynset = swn.senti_synset(synset.name())
```

**Scores**: positive, negative and objectivity
```python3
sentiSynset.pos_score(), sentiSynset.neg_score(), sentiSynset.obj_score()
👉  (0.75, 0.0, 0.25)
```

---
class: left, middle, inverse

# Outline

* .brown[WordNet]

* .brown[WordNet Similarities]

* .brown[SentiWordNet]

* .cyan[Exercise]

---

# Exercise

* Given the following (lemma, category) pairs:

```
(’the’,’DT’), (’man’,’NN’), (’swim’,’VB’), (’with’, ’PR’), (’a’, ’DT’),
(’girl’,’NN’), (’and’, ’CC’), (’a’, ’DT’), (’boy’, ’NN’), (’whilst’, ’PR’),
(’the’, ’DT’), (’woman’, ’NN’), (’walk’, ’VB’)
```
* For each pair, when possible, print their most frequent WordNet synset

* For each pair of words, when possible, print their corresponding least common subsumer (LCS) and their similarity value, using the following functions:

  - Path Similarity

  - Leacock-Chodorow Similarity

  - Wu-Palmer Similarity

  - Lin Similarity

Normalize similarity values when necessary. What similarity seems better?
