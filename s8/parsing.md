class: center, middle

### Introduction to Human Language Technologies

# Lab.8: Parsing

Gerard Escudero i Jordi Turmo

Natural Language Research Group

<br>

## Master on Artificial Intelligence

<br>

![:scale 75%](fib.png)

---
class: left, middle, inverse

# Outline

* .cyan[Constituency parsing with NLTK]

* Dependency parsing with NLTK

---

# Constituency parsing with NLTK

#### Non-probabilistic parsers:

* ChartParser (default parser is BottomUpLeftCornerChartParser)

* BottomUpChartParser, LeftCornerChartParser

* TopDownChartParser, EarleyChartParser

* ...

#### Probabilistic parsers:

* InsideChartParser, RandomChartParser, LongestChartParser (they are bottom-up parsers)

* ViterbiParser

* CoreNLPParser (third-party’s parser)

* ...

---

# Non-probabilistic parsers: Charts

Example:

* [view](codes/charts.html) / [download](codes/charts.ipynb)


Main differences of non-probabilistic chart parsers:

* BottomUpChartParser: bottom-up strategy

* BottomUpLeftCornerChartParser (ChartParser): bottom-up strategy filtering out edges without any word subsumtion (e.g., `[0,0]: X →. Y Z`)

* LeftCornerChartParser: bottom-up strategy filtering out edges without new word subsumptions (e.g., if we already got `[0,1] Y→y.` and `[1,2] Z→z.` then `[0,1] A→Y.Z` is filtered out whereas `[0,2] A→Y Z.` is fired)

* TopDownChartParser: top-down strategy

* EarleyChartParser: incremental top-down strategy (more efficient)

```python3
from nltk import TopDownChartParser
parser = nltk.TopDownChartParser(grammar)
parse = parser.parse(sent)
```

---

# Mandatory Exercise

Statement:

* Consider the following sentence: <br>
`Lazy cats play with mice.`

* Expand the grammar of the example related to non-probabilistic chart parsers in order to subsume this new sentence.

* Perform the constituency parsing using a BottomUpChartParser, a BottomUpLeftCornerChartParser and a LeftCornerChartParser.

* For each one of them, provide the resulting tree, the number of edges and the list of explored edges.

* Which parser is the most efficient for parsing the sentence?

* Which edges are filtered out by each parser and why?

---

# Probabilistic parsers: Charts

Example:

* [view](codes/probParsing.html) / [download](codes/probParsing.ipynb)


Main differences of probabilistic chart parsers:

* They use the bottom-up strategy

* InsideChartParser: select edges in decreasing order of their trees’ inside probs. `p→A,B ⇒ Prob=P(p)P(A)P(B)`

* RandomChartParser: select edges in random order.

* LongestChartParser: select longer edges before shorter ones.

---

# Probabilistic parsers: Viterbi

Example:

* Probabilistic Viterbi parser

* Learn a PCFG

* Apply the learnt PCFG to Viterbi parser

* [view](codes/viterbi.html) / [download](codes/viterbi.ipynb)

### CoreNLP parser

Previous notebook includes also a CoreNLP parser example.

---
class: left, middle, inverse

# Outline

* .brown[Constituency parsing with NLTK]

* .cyan[Dependency parsing with NLTK]

---

# Dependency parsing

CoreNLP dependency parser example:

* [view](codes/dependency.html) / [download](codes/dependency.ipynb)

# Mandatory exercise

Statement:

1. Read all pairs of sentences of the trial set within the evaluation framework of the project.

2. Compute the Jaccard similarity of each pair using the dependency triples from CoreNLPDependencyParser.

3. Show the results. Do you think it could be relevant to use NEs to compute the similarity between two sentences? Justify the answer.

