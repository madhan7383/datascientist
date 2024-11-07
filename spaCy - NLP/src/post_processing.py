def filter_invalid_entries(entities: dict) -> dict:
    """
    Filter out invalid or non-relevant contact details.
    """
    # Example filter: Removing empty or None values
    filtered_entities = {key: [item for item in value if item] for key, value in entities.items()}
    
    # Remove keys with no extracted data
    filtered_entities = {key: value for key, value in filtered_entities.items() if value}
    
    return filtered_entities
 
