"""
Python Layer Assertion Tests
Validates frontmatter text tokenization and scalar projection constraints.
"""
import pytest
from src.python_io.parser import TSGParser
from src.python_io.projections import project_tsg_to_vector

def test_tsg_parser_heuristics():
    parser = TSGParser()
    
    # Mock case log text simulating a court blocking remedy
    mock_log = """
    # Case Entry: Judicial Obstruction
    This entry details how absolute judicial immunity was used to create a total enclosure.
    The clerk rejected the filing, citing complex procedural rules that created a massive barrier.
    """
    
    tokens = parser.parse_case_log(mock_log)
    
    assert tokens["stage"] == "compression"  # Triggered by 'enclosure'
    assert tokens["band"] == "legal"          # Triggered by 'judicial'
    assert tokens["immunity"] is True         # Triggered by 'immunity'
    assert tokens["barrier_score"] > 0.0      # Triggered by 'barrier/rejected'

def test_project_tsg_to_vector_bounds():
    # Verify that valid tokens stay within the normalized [0.0, 1.0] metric space
    vector = project_tsg_to_vector("compression", "legal", "legal-harassment", True, 0.8)
    
    assert len(vector) == 5
    assert vector[0] == 0.75  # compression stage weight
    assert vector[1] == 0.40  # legal band weight
    assert vector[3] == 1.0   # absolute immunity present
    assert vector[4] == 0.8   # barrier score forwarded directly

