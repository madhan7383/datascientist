import spacy
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score
import seaborn as sns
import os
from spacy import displacy
from typing import List, Dict, Any

# Load the pre-trained spaCy model for tokenization or use custom model
nlp = spacy.load("en_core_web_trf")

# --- Data Visualization Functions ---

def visualize_entities(text: str) -> None:

    doc = nlp(text)
    displacy.render(doc, style="ent", page=True)

def plot_entity_frequency(entity_dict: Dict[str, List[str]]) -> None:

    plt.figure(figsize=(10, 6))
    entity_counts = {key: len(value) for key, value in entity_dict.items()}
    sns.barplot(x=list(entity_counts.keys()), y=list(entity_counts.values()))
    plt.title("Entity Frequency")
    plt.xlabel("Entity Type")
    plt.ylabel("Count")
    plt.show()

# --- Model Performance Evaluation ---

def evaluate_performance(true_entities: Dict[str, List[str]], predicted_entities: Dict[str, List[str]]) -> Dict[str, float]:

    evaluation_metrics = {}
    for entity_type in true_entities.keys():
        true_set = set(true_entities[entity_type])
        predicted_set = set(predicted_entities[entity_type])
        
        # Precision, Recall, F1 Score
        precision = precision_score(list(true_set), list(predicted_set), average='binary', zero_division=0)
        recall = recall_score(list(true_set), list(predicted_set), average='binary', zero_division=0)
        f1 = f1_score(list(true_set), list(predicted_set), average='binary', zero_division=0)

        evaluation_metrics[entity_type] = {'precision': precision, 'recall': recall, 'f1': f1}

    return evaluation_metrics

# --- Helper Functions ---

def save_model(model: spacy.language.Language, model_name: str, output_dir: str) -> None:

    output_path = os.path.join(output_dir, model_name)
    model.save(output_path)
    print(f"Model saved to {output_path}")

def load_model(model_name: str, model_dir: str) -> spacy.language.Language:

    model_path = os.path.join(model_dir, model_name)
    model = spacy.load(model_path)
    return model

def tokenize_text(text: str) -> List[str]:

    doc = nlp(text)
    return [token.text for token in doc]

 
