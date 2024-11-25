# Icelandic Error Corpus (IceEC)

The Icelandic Error Corpus (IceEC) is a collection of texts in modern Icelandic annotated for mistakes related to spelling, grammar, and other issues. The texts are organized by genre, which include sentences from highschool student essays, online news texts and Wikipedia articles. The version included in MultiGEC-2025 is the subset of student essays. Sentences within texts in the student essays had to be shuffled due to the license which they were originally published under, but neither the online news texts nor the Wikipedia articles needed to be shuffled.

Citing the Error Corpus:

Anton Karl Ingason, Lilja Björk Stefánsdóttir, Þórunn Arnardóttir, and Xindan Xu. 2021. The Icelandic Error Corpus (IceEC). Version 1.1. (https://github.com/antonkarl/iceErrorCorpus)

## IceL2EC: the Icelandic L2 Error Corpus

The Icelandic L2 Error Corpus (IceL2EC) is a collection of texts in modern Icelandic, written by adult learners of Icelandic as a second language. They have been annotated for mistakes related to spelling, grammar, and other issues. Each mistake is marked according to error type using an error code, so that the original corpus consists of 101 files with 24,948 categorized error instances.
The corpus is described in [Glisic & Ingason(2022)](https://www.researchgate.net/publication/361876310_The_Nature_of_Icelandic_as_a_Second_Language_An_Insight_from_the_Learner_Error_Corpus_for_Icelandic), with corpus data provided [here](https://repository.clarin.is/repository/xmlui/handle/20.500.12537/280).

Original essays have been corrected and annotated by professional linguists, annotating both for grammatical error correction and fluency. Each edit was manually classified into 6 main error type categories with 258 specific error codes in total.
Detailed annotation scheme is provided [here](https://github.com/antonkarl/iceErrorCorpus/blob/master/errorCodes.tsv).

# Note:

Download all domains from https://github.com/spraakbanken/multigec-2025-participants/tree/main/icelandic/ and place in this folder:

```txt
icelandic
|-- Readme.md
|-- is-IceEC-orig-dev.md
|-- is-IceEC-orig-test.md
|-- is-IceEC-orig-train.md
|-- is-IceEC-ref1-dev.md
|-- is-IceEC-ref1-train.md
|-- is-IceL2EC-orig-dev.md
|-- is-IceL2EC-orig-test.md
|-- is-IceL2EC-orig-train.md
|-- is-IceL2EC-ref1-dev.md
`-- is-IceL2EC-ref1-train.md
```
