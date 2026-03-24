# Define a class called LinearModel.
# Give it an __init__ method that
# initializes two attributes: weight and bias.

class LinearModel:
    def __init__(self, weight=0.0, bias=0.0):
        self.weight = weight
        self.bias = bias

model1 = LinearModel() #w: 0.0 , b: 0.0
model2 = LinearModel(2.5, 1.0)

print(model1.weight, model1.bias)
print(model2.weight, model2.bias)
# Understanding classes and objects
# is vital for building model architectures