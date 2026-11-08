import json
import re

def extract_legal_tokens(markdown_content):
    # Dumb regex/token pull: isolating specific legal friction points
    # No math or vector initialization allowed here!
    metadata = {
        "statute_id": re.search(r"id:\s*(.*)", markdown_content).group(1),
        "has_immunity": "immunity" in markdown_content.lower(),
        "nondiscretionary": "shall" in markdown_content.lower()
    }
    return metadata
