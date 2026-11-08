"""
AST Tokenizer & Frontmatter Extractor
Safely parses Stage 1 text documents into clean qualitative dictionaries.
"""
import re
import yaml

class TSGParser:
    def __init__(self):
        # Strict pattern matching for inline qualitative tracking blocks
        self.frontmatter_regex = re.compile(r"^---\s*(.*?)\s*---", re.DOTALL | re.MULTILINE)

    def parse_case_log(self, file_content: str) -> dict:
        """
        Parses text files to extract explicit metadata arrays and evaluate keyword densities.
        """
        parsed_data = {
            "stage": "entry",
            "band": "symbolic",
            "modality": "admin-pressure",
            "immunity": False,
            "barrier_score": 0.1
        }

        # 1. Check for YAML frontmatter configuration blocks
        match = self.frontmatter_regex.match(file_content)
        if match:
            try:
                meta = yaml.safe_load(match.group(1))
                if "tsg" in meta:
                    parsed_data.update(meta["tsg"])
                    return parsed_data
            except Exception:
                pass # Fall back to structural heuristics if serialization fails

        # 2. Heuristic Keyword Structural Tokenization
        content_lower = file_content.lower()
        
        if "closure" in content_lower or "immobilization" in content_lower:
            parsed_data["stage"] = "closure"
        elif "compression" in content_lower or "enclosure" in content_lower:
            parsed_data["stage"] = "compression"
        elif "tightening" in content_lower:
            parsed_data["stage"] = "tightening"

        if "mandamus" in content_lower or "statute" in content_lower:
            parsed_data["band"] = "legal"
        elif "embassy" in content_lower or "diplomatic" in content_lower:
            parsed_data["band"] = "proxy"
        elif "surveillance" in content_lower or "hacking" in content_lower:
            parsed_data["band"] = "digital"

        if "immunity" in content_lower:
            parsed_data["immunity"] = True
            
        # Count explicit disability barriers or administrative rejections
        barriers = len(re.findall(r"(barrier|dismissed|rejected|denied|exhausted)", content_lower))
        parsed_data["barrier_score"] = min(1.0, barriers * 0.2)

        return parsed_data
