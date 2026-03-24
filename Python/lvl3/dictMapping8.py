# Write a function that takes a list of category labels
# (e.g., ['cat', 'dog', 'cat']) and uses a loop to create
# a dictionary that maps each unique label to a unique integer ID.

def create_label_to_id_mapping(labels):
    """
    Converts list of category labels to dictionary mapping
    labels to unique integer IDs.
    """
    label_to_id = {}
    next_id = 0

    for label in labels:
        if label not in label_to_id:
            label_to_id[label] = next_id
            next_id += 1

    return label_to_id

labels = ['cat', 'shark', 'dog', 'bear', 'kingfisher']
mapping = create_label_to_id_mapping(labels)
print(mapping)
# Converting labels into numerical data is a fundamental requirement for classification models