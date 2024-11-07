import spacy
import re

# Load the pre-trained spaCy model # change the path if needed
nlp = spacy.load("en_core_web_trf")  # Transformer-based model for better accuracy

def extract_entities(text: str) -> dict:
    """
    Extract entities such as names, phone numbers, emails, job titles, company names from the text,
    and use proximity-based relationships to link entities (e.g., a name next to a job title or company).
    """
    doc = nlp(text)
    entities = {
        "names": [],
        "emails": [],
        "phones": [],
        "job_titles": [],
        "companies": [],
        "locations": []
    }

    # Extract standard entities using spaCy
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["names"].append(ent.text)
        elif ent.label_ == "ORG":
            entities["companies"].append(ent.text)
        elif ent.label_ == "EMAIL":
            entities["emails"].append(ent.text)
        elif ent.label_ == "GPE":
            entities["locations"].append(ent.text)

    # Extract phone numbers using regex (optional)
    phones = re.findall(r'\(?\+?\d{1,3}\)?[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{1,4}[\s\-]?\d{1,4}', text)
    entities["phones"] = phones

    # Extract job titles using proximity-based analysis... Will add titles in a csv.
    job_titles_keywords = ["CEO", "Manager", "Engineer", "Developer", "Director", "Lead", "President", "Founder"]
    
    # Look for job titles in proximity to people's names or company names
    for i, token in enumerate(doc):
        # If we find a name (PERSON entity), check the nearby words for potential job titles
        if token.ent_type_ == "PERSON":
            # Look at the following tokens for job title keywords
            for j in range(i + 1, min(i + 4, len(doc))):  # Look ahead at the next 4 words
                if doc[j].text in job_titles_keywords:
                    entities["job_titles"].append(doc[j].text)
        # Similarly, we can look for company names (ORG) and infer job titles near them
        elif token.ent_type_ == "ORG":
            for j in range(i + 1, min(i + 4, len(doc))):  # Look ahead at the next 4 words
                if doc[j].text in job_titles_keywords:
                    entities["job_titles"].append(doc[j].text)

    return entities

# Example usage:
text = """
John Doe, the CEO of Acme Corp., can be reached at johndoe@acme.com or by calling (123) 456-7890. 
Jane Smith, an experienced Software Engineer at XYZ Solutions, is available at jane.smith@xyz.com. 
Contact us for more information.
"""

extracted_entities = extract_entities(text)
print(extracted_entities)
