# Question: Extend your LinearModel class by adding a method called forward(x)
# This method should calculate the output using the formula: y = (weight * x) + bias.

class LinearModel:
    def __init__(self, weight = 0.0, bias = 0.0):
        self.weight = weight
        self.bias = bias

    def forward(self, x):
        """
        Forward pass: computes y = w * x + b
        """
        return self.weight * x + self.bias

model = LinearModel(weight=2.0,bias=1.0)
input_x = 3.5

output = model.forward(input_x)
print(f"Input: {input_x}, Output: {output}")

# Why it matters: This mirrors how a perceptron or basic neuron functions within a neural network