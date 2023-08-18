# This repository contains source code for the HaloCheck part as well as the QA dataset created of our HaLo paper
# "HaLo: Estimation and Reduction of Hallucinations in Open-Source Weak Large Language Models"

## Code/Package

### Installation
pip3 install git+https://github.com/EngSalem/HaLo.git


### HaloCheck is a BlackBox knowledge-free estimator for hallucination severity in LLM responses
### HaloCheck is built on the same concepts of selfcheckGPT[[link](https://github.com/potsawee/selfcheckgpt)https://github.com/potsawee/selfcheckgpt]
### HaloCheck primarily leverages cross entailment of sampled responses on sentence level granulaity (we developed our method prior to selfcheckGPT-NLI)
### HaloCheck assess that LLM genertes consistent information across its all samples, which makes it better in finegrained granularity estimation

## To use HaloCheck

```python
import HaloCheck as checker

incosistent_samples = ['The 1958 NBA Finals was played between the St. Louis Hawks and Boston Celtics. The Hawks won the series 4 games to 2 in the best of 7 playoff.', 'The 1958 NBA Finals was played between the Minneapolis Lakers and Boston Celtics and was won by the Lakers 4 games to 3.', 'The 1958 NBA Finals was played on April 17, 1958, between the Boston Celtics and the St. Louis Hawks.', 'The 1958 NBA Finals was played between the Boston Celtics and Minneapolis Lakers. The Celtics won the series 4 games to 2 for their 5th championship.', 'The 1958 NBA Finals was played between the Boston Celtics and Minneapolis Lakers. The MVP of the 1958 NBA Finals was Bill Russell.']

scorer= checker.HaloCheck(device='cpu', granularity='sentence', model='mnli') ## change to 'cuda' if gpu is available
print(scorer.score(incosistent_samples))
## expected score: -0.417 ## indicating inconsistency
```
