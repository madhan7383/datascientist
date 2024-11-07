 
from src.entity_recognition import extract_entities
from src.data_preprocessing import clean_text

def extract_contact_details(text: str) -> dict:
    """
    Given raw text, extract structured contact details including names, phone numbers, emails, etc.
    """
    # Step 1: Clean the text
    cleaned_text = clean_text(text)
    
    # Step 2: Extract entities using spaCy
    contact_details = extract_entities(cleaned_text)
    
    return contact_details

if __name__ == "__main__":
    # Example usage
    text = "John Doe, Senior Software Engineer at ABC Corp. Email: johndoe@example.com. Phone: (123) 456-7890"
    contact_info = extract_contact_details(text)
    print(contact_info)
