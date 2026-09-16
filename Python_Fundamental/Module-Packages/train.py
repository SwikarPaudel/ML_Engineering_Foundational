# Method A: Import the entire module
import ml_math

result = ml_math.calculate_accuracy(90, 100)
print(f"Model Accuracy: {result}%")

# Method B: Import specific functions directly (Cleaner)
from ml_math import get_learning_rate

lr = get_learning_rate()
print(f"Current Learning Rate: {lr}")
