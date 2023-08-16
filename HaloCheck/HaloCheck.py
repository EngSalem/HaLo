import numpy as np
from itertools import combinations
from summac.model_summac import SummaCZS

class HaloCheck:
    def __init__(self, device: str, granularity: str = "sentence", nli_model: str = "mnli"):
        try:
            self.summac_model = SummaCZS(granularity=granularity, model_name=nli_model, device=device)
            print(f"Initialized the entailment model with device {device}, granularity {granularity}, and NLI model {nli_model}...")
        except Exception as e:
            print(f"Error initializing the model: {e}")
        
    def score(self, samples: list[str]):
        try:
            # Compute pairwise combinations
            samples_combinations = list(combinations(samples, 2))
            
            # Compute entailment scores and calculate the mean
            scores = [self.summac_model.score([combination[0]], [combination[1]])["scores"][0] for combination in samples_combinations]
            mean_score = np.mean(scores)
            
            return mean_score
        except Exception as e:
            print(f"Error calculating scores: {e}")
            return None
