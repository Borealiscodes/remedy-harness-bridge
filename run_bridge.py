"""
Master Orchestration Pipeline (remedy-harness-bridge)
Coordinates the Python text extraction and the Julia geometric compilation loop.
"""
import os
import sys
import json
import subprocess
from pathlib import Path
from src.python_io.parser import TSGParser
from src.python_io.evaluator import IngestionEvaluator

def run_pipeline(stage1_repo_path: str, output_manifest_path: str):
    print("🚀 Initializing remedy-harness-bridge Pipeline...")
    
    parser = TSGParser()
    evaluator = IngestionEvaluator(n_permutations=1000)
    
    stage1_root = Path(stage1_repo_path)
    if not stage1_root.exists():
        print(f"❌ Error: Target Stage 1 repository not found at {stage1_repo_path}")
        sys.exit(1)

    print(f"📂 Scanning Stage 1 directories under: {stage1_root.name}")
    
    # Heuristically discover active legal tracking logs
    # Using 01, 02, 03 prefixes mapped out in your repo architecture
    target_dirs = ["01federalstatutes", "02judicialbranch_constraints", "03municipalpolicing_DC"]
    
    for target in target_dirs:
        dir_path = stage1_root / target
        if not dir_path.exists():
            continue
            
        for file_path in dir_path.glob("*.md"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Extract qualitative snapshot data
            snapshot = parser.parse_case_log(content)
            
            # For simulation baseline evaluation, we mock the 'before' and 'predicted'
            # trajectories relative to the current observed file position
            case_id = f"{target[:2]}_{file_path.stem}"
            
            # Construct a theoretical progression track for CAUSA analysis
            before = snapshot.copy()
            before["stage"] = "entry"  # Baseline origin point
            
            predicted = snapshot.copy()
            predicted["stage"] = "compression" # Mandatory non-discretionary geodesic path
            
            evaluator.register_episode(
                case_id=case_id,
                before_dict=before,
                predicted_dict=predicted,
                actual_dict=snapshot
            )

    print("🔬 Executing CAUSA Causal Falsification Pass (Permutation Baselines)...")
    verified_payload = evaluator.run_falsification_audit()
    
    if not verified_payload:
        print("⚠️ Pipeline Halted: Zero tracking instances cleared the permutation baseline.")
        return

    # Serialize verified payload to a flat JSON block for the Julia handshake
    json_payload = json.dumps(verified_payload)
    
    # Save a copy locally for auditing / high-altitude visualization
    os.makedirs(os.path.dirname(output_manifest_path), exist_ok=True)
    with open(output_manifest_path, "w", encoding="utf-8") as f:
        f.write(json_payload)
    print(f"💾 Verified text payload cached at {output_manifest_path}")

    print("☀️ Invoking Native Julia Geometry Compiler Engine...")
    
    # Path to the inline Julia wrapper script
    julia_runner = os.path.join(os.path.dirname(__file__), "src", "julia_engine", "run_audit.jl")
    
    try:
        # Stream the JSON string directly into Julia via stdin to prevent disk I/O bottlenecks
        process = subprocess.Popen(
            ["julia", "--project=.", julia_runner],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=json_payload)
        
        print("\n=== JULIA OUT-OF-BAND ENGINE REPORT ===")
        print(stdout)
        if stderr:
            print("⚠️ Julia System Error log:", stderr)
        print("=======================================")
        
    except FileNotFoundError:
        print("❌ Error: Native 'julia' runtime executable could not be found on system PATH.")

if __name__ == "__main__":
    # Fallback paths for immediate dry-run execution profiles
    STAGE1_DIR = os.getenv("STAGE1_REPO_PATH", "../us-domestic-remedy-exhaustion-stage1")
    MANIFEST_OUT = "data/manifest.json"
    
    run_pipeline(STAGE1_DIR, MANIFEST_OUT)
