import pandas as pd
import numpy as np


chat_id = 232444196 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    time = 4 
    S = np.mean(x) 
    a = 2 * S / (time * time)
    return a
