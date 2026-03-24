# Given a list of training loss values [0.9, 0.7, 0.5, 0.3, 0.1],
# write a for loop that iterates through the list and prints "Convergence achieved" only when the loss drops below 0.4.
training_losses = [0.9, 0.7, 0.5, 0.3, 0.1]

for loss in training_losses:
    if loss < 0.4:
        print("Covergence achieved!")