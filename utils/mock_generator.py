"""
Mock Case Log Generator for Stress Testing
Simulates high-throughput fractured legal files across varied systemic trajectories.
"""
import os
import random
from pathlib import Path

# Qualitative taxonomy vocabularies matching the TSG v1.0 standard
STAGES = ["entry", "tightening", "compression", "closure"]
BANDS = ["symbolic", "legal", "digital", "proxy", "physical", "lethal"]
MODALITIES = ["admin-pressure", "visa-control", "platform-moderation", "family-leverage", "financial-freeze"]

def generate_mock_markdown(case_id: str, trajectory_type: str) -> str:
    """
    Generates a structured case file with specialized embedded signals.
    """
    # Baseline setup
    immunity = "false"
    keywords = []
    
    if trajectory_type == "obstructed":
        # Forcing a clear signal of procedural closure and immunity blockades
        stage = "closure"
        band = "legal"
        modality = "financial-freeze"
        immunity = "true"
        keywords = ["absolute judicial immunity", "clerk rejected", "dismissed", "denied", "exhausted"]
    elif trajectory_type == "random_noise":
        # Chaos trajectory with unpredictable metadata distributions
        stage = random.choice(STAGES)
        band = random.choice(BANDS)
        modality = random.choice(MODALITIES)
        immunity = random.choice(["true", "false"])
        keywords = ["arbitrary scheduling", "administrative delay", "pending"]
    else:
        # Standard progressive tightening trajectory
        stage = "tightening"
        band = "admin-pressure"
        modality = "visa-control"
        keywords = ["repeated constraint", "narrowing avenues", "travel restricted"]

    keyword_block = " ".join(keywords)
    
    # Format the file body with valid YAML frontmatter blocks
    content = f"""---
tsg:
  stage: "{stage}"
  band: "{band}"
  modality: "{modality}"
  immunity: {immunity}
---
# Case Log Tracking Document: {case_id}
Trajectory Vector Profile: {trajectory_type}

## Narrative Log Notes
The target profile shows signs of specialized pressure patterns matching the target profile matrix. 
{keyword_block}. The systemic boundary state continues to evolve under active oversight structures.
"""
    return content

def populate_mock_stage1_repo(target_root: str, cases_per_type: int = 50):
    """
    Stands up a mock us-domestic-remedy-exhaustion-stage1 tree for boundary testing.
    """
    root_path = Path(target_root)
    sub_dirs = ["01federalstatutes", "02judicialbranch_constraints", "03municipalpolicing_DC"]
    
    for sub in sub_dirs:
        os.makedirs(root_path / sub, exist_ok=True)
        
    print(f"🏗️  Populating mock Stage 1 repository environment at: {root_path.resolve()}")
    
    total_generated = 0
    profiles = ["obstructed", "random_noise", "clean_tightening"]
    
    for profile in profiles:
        for i in range(cases_per_type):
            case_id = f"CASE_{profile.upper()}_{i:03d}"
            # Evenly distribute files across the active subsystem folders
            target_sub = sub_dirs[total_generated % len(sub_dirs)]
            file_name = root_path / target_sub / f"{case_id}.md"
            
            file_content = generate_mock_markdown(case_id, profile)
            
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(file_content)
                
            total_generated += 1
            
    print(f"✨ Successfully generated {total_generated} mock tracking assets across profiles.")

if __name__ == "__main__":
    # Point directly to a test workspace directory
    MOCK_WORKSPACE = "../test-mock-stage1-repo"
    populate_mock_stage1_repo(MOCK_WORKSPACE, cases_per_type=60)
