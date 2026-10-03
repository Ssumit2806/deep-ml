import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    if not scores:
        return []
    
    # Subtract the max for numerical stability (prevents overflow in exp)
    max_score = max(scores)
    exps = [math.exp(s - max_score) for s in scores]
    total = sum(exps)
    
    return [e / total for e in exps]
    pass