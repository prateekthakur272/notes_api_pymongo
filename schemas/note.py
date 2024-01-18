def note_to_dict(item) -> dict:
    return {
        'id': str(item['_id']),
        'title': item['title'],
        'description': item['description']
    }
    
def notes_to_dict(items) -> list[dict]:
    return [note_to_dict(item) for item in items]