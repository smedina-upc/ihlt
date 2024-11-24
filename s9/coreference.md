class: center, middle

### Introduction to Human Language Technologies

# Lab.9: Coreference

Gerard Escudero, Salvador Medina, Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

- .cyan[Coreference]

- Exercise

---

# Coreference in spaCy Experimental (I)

### Requirements

```python3
!pip install spacy-experimental
!pip install https://github.com/explosion/spacy-experimental/releases/download/v0.6.1/en_coreference_web_trf-3.4.0a2-py3-none-any.whl

import spacy
```

### Use

```python3
nlp = spacy.load("en_coreference_web_trf")
doc = nlp(u'My sister has a dog. She loves him.')

doc.spans
👉  {'coref_clusters_1': [My sister, She], 'coref_clusters_2': [a dog, him]}
```

### spaCy pipeline

See [spaCy documentation](https://spacy.io/api/coref/) for including it in the spaCy pipeline.

---


# Coreference in spaCy Experimental (II)

### With this module, we can use the spaCy's training pipeline
#### In order to do so, we should define coreferences as spans
```python
nlp = spacy.load('en_core_web_sm')
coref = nlp.add_pipe("experimental_coref")
train_data = [
     (
            "Yes, I noticed that many friends around me received it. It seems that almost everyone received this SMS.",
            {
                "spans": {
                    f"coref_clusters_1": [
                        (5, 6, "MENTION"),      # I
                        (40, 42, "MENTION"),    # me

                    ],
                    f"coref_clusters_2": [
                        (52, 54, "MENTION"),     # it
                        (95, 103, "MENTION"),    # this SMS
                    ]
                }
            },
        ),
]
```


---

# Coreference in spaCy Experimental (III)

### Train coreference model

```python
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "experimental_coref"]
with nlp.disable_pipes(*other_pipes):
    # Train the model
    optimizer = nlp.initialize()
    for i in range(100):
        random.shuffle(train_data)
        for text, clusters in train_data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, clusters)
            loss = nlp.update([example], sgd=optimizer)
            print("Loss", loss)
```
### Run the trained model
```python
doc = nlp( "Yes, I noticed that many friends around me received it. It seems that almost everyone received this SMS.",)
print(doc.spans)
```

---

# Coreference in spaCy Plugins (I)

## coreferee

### Requirements

```python3
!python3 -m pip install coreferee
!python3 -m coreferee install en
```

### Use

```python3
nlp = spacy.load('en_core_web_trf')
nlp.add_pipe('coreferee')
doc = nlp("Although he was very busy with his work, Peter had had enough of it. He and his wife decided they needed a holiday. They travelled to Spain because they loved the country very much.")
```

```python3
doc._.coref_chains.print()
👉  0: he(1), his(6), Peter(9), He(16), his(18)    1: work(7), it(14)    2: [He(16); wife(19)], they(21), They(26), they(31)    3: Spain(29), country(34)
```
```python3
doc[16]._.coref_chains.print()
👉  0: he(1), his(6), Peter(9), He(16), his(18)    2: [He(16); wife(19)], they(21), They(26), they(31)
```
```python3
doc._.coref_chains.resolve(doc[31])
👉  [Peter, wife]
```

---

# Coreference in spaCy Plugins

## crosslingual-coreference

### Requirements

```python3
!pip install crosslingual-coreference
```

### Use

```python3
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe(
    "xx_coref", config={"chunk_size": 2500, "chunk_overlap": 2, "device": 0}
)
doc = nlp("Do not forget about Momofuku Ando! He created instant noodles in Osaka. At that location, Nissin was founded. Many students survived by eating these  noodles, but they don't even know him.")
```
```python3
print(doc._.coref_clusters)
👉  [[[4, 5], [7, 7], [27, 27], [36, 36]], [[12, 12], [15, 16]], [[9, 10], [27, 28]], [[22, 23], [31, 31]]]
```
```python3
print(doc._.cluster_heads)
👉  {Momofuku Ando: [5, 6], instant noodles: [11, 12], Osaka: [14, 14], Nissin: [21, 21], Many students: [26, 27]}
```

---

# Coreference in Textserver

### Requirements

```python3
from google.colab import drive
import sys
drive.mount('/content/drive')
sys.path.insert(0, '/content/drive/My Drive/Colab Notebooks/plh')
from textserver import TextServer
```

### Use

```python3
ts = TextServer('usuari', 'passwd', 'coreferences')

ts.coreferences("My sister has a dog. She loves him.")
👉  [['My sister', 'him'], ['a dog', 'She']]
```

---
class: left, middle, inverse

# Outline

- .brown[Coreference]

- .cyan[Exercise]

---

# Exercise

* Consider the first paragraph in Alice’s Adventures in Wonderland, by Lewis Carroll:
```
Alice was beginning to get very tired of sitting by her sister on the bank, 
and of having nothing to do: once or twice she had peeped into the book her 
sister was reading, but it had no pictures or conversations in it, ‘and what 
is the use of a book,’ thought Alice ‘without pictures or conversations?’
```

* It can be downloaded from: <br>
[http://www.gutenberg.org/files/11/11-0.txt](http://www.gutenberg.org/files/11/11-0.txt)

* Apply the spaCy coreference solver to the previous paragraph.

* Show the coreference chains. 

* What do you think about them? Justify your answer.


