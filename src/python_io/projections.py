"""
TSG-to-Scalar Projection Engine
Transforms non-activating Tonal Spiral Geometry ontology blocks into bounded scalar fields.
"""

# Hardcoded ordinal weights to preserve absolute scale metrics across runs
STAGE_WEIGHTS = {
    "entry": 0.25,
    "tightening": 0.50,
    "compression": 0.75,
    "closure": 1.00
}

BAND_WEIGHTS = {
    "symbolic": 0.15,
    "legal": 0.40,
    "digital": 0.60,
    "proxy": 0.75,
    "physical": 0.90,
    "lethal": 1.00
}

# Fine-grained institutional resistance / friction mapping
MODALITY_WEIGHTS = {
    "admin-pressure": 0.30,
    "visa-control": 0.45,
    "platform-moderation": 0.50,
    "family-leverage": 0.70,
    "financial-freeze": 0.80,
    "border-detain": 0.85,
    "legal-harassment": 0.90,
    "digital-intrusion": 0.95
}

def project_tsg_to_vector(stage: str, band: str, modality: str, immunity: bool, accessibility_barrier: float) -> list[float]:
    """
    Maps 5 distinct qualitative variables onto an un-normalized coordinate space in R^5.
    Returns: [Jurisdictional Force, Compulsion, Immunity Density, Barrier Interception, Repression Surface]
    """
    x1 = STAGE_WEIGHTS.get(stage.strip().lower(), 0.0)
    x2 = BAND_WEIGHTS.get(band.strip().lower(), 0.0)
    x3 = MODALITY_WEIGHTS.get(modality.strip().lower(), 0.1)
    x4 = 1.0 if immunity else 0.0
    x5 = float(accessibility_barrier)

    # Return as flat array primitive for easy serialization
    return [x1, x2, x3, x4, x5]
