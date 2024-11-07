import spacy
from spacy.training.example import Example

def train_spacy_model(train_data: list, model_output_dir: str):
    """
    Train a spaCy model for entity recognition.
    """
    # Load a blank spaCy model
    nlp = spacy.blank("en")
    
    # Add the entity recognizer
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner, last=True)
    
    # Add labels to the NER component
    for _, annotations in train_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])
    
    # Training the model
    optimizer = nlp.begin_training()
    for epoch in range(30):
        for text, annotations in train_data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.5)
    
    # Save the model
    nlp.to_disk(model_output_dir)
    print("Model saved at", model_output_dir)

# Examples training data format
train_data = [
    ("John Doe is a Software Engineer at ABC Corp.", {"entities": [(0, 8, "PERSON"), (25, 40, "ORG"), (12, 28, "JOB_TITLE")]}),
    ("Email me at johndoe@example.com", {"entities": [(12, 34, "EMAIL")]})
]

# Calls the training function
train_spacy_model(train_data, "models/spacy_model")
 
