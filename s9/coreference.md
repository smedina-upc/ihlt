class: center, middle

### Introduction to Human Language Technologies

# Lab.9: Coreference

Gerard Escudero & Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
# Coreference

#### spaCy coreference example:

* [view](codes/s9a.html) / [download](codes/s9a.ipynb)

* [Neural Coreference - Hugging Face](https://huggingface.co/coref/?text=My%20sister%20has%20a%20dog.%20She%20loves%20him.)

![:scale 95%](figures/neuralcoref.png)


---

# Mandatory exercise

#### Statement:

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



