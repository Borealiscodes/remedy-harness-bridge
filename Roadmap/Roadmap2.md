This updated engineering roadmap integrates Tonal Spiral Geometry (TSG) as your qualitative annotation vocabulary and CAUSA as your mathematical validation engine, feeding a unified Python-Julia hybrid ingestion pipeline.

<pre>
  

[Stage 1 Legal Text] ──> [Python: TSG Annotation Parser] ──> [Python: CAUSA Causal Engine]
                                                                         │
[Tri-System Manifest] <── [Julia: Zero-Heap Tensor Engine] <── [Permutation Baseline Pass]

</pre>

🛠️ Phase 1: Environment & Token Dependency Lock

Objective: Establish isolation protocols and freeze runtime dependencies for the hybrid architecture.
* Isolate Python Environment: Clone CAUSA into a sub-module and verify Python 3.10+ execution.
* Configure Julia Runtime: Initialize Project.toml with StaticArrays.jl and JSON3.jl.
* Establish Cross-Repo Paths: Configure local .env pointers linking us-domestic-remedy-exhaustion-stage1, Shared-Horizon, and Tri-System-Analysis-Harness.

📝 Phase 2: TSG Annotation Tokenizer (Python Layer)

Objective: Parse raw legal tracking logs into discrete taxonomy buckets using the non-activating TSG schema.
* Extract Metadata Frontmatter: Build regex parsers in src/python_io/parser.py to index structural tags.
* Map TSG Categories: Standardize raw text records into strict TSG object schemas:
  * TSG.spiral_stage (e.g., entry, tightening, compression, closure).
	* TSG.tonal_band (e.g., symbolic, legal, admin-pressure, physical).
	* TSG.modality_key (e.g., visa-control, financial-freeze, legal-harassment).
* Emit Token Payload: Standardize these annotations into flat intermediate JSON structures.

📊 Phase 3: CAUSA Causal Verification (Python Layer)

Objective: Project qualitative TSG classifications into numeric vector spaces to falsify the "illusion of institutional remedy."
* Construct Projection Matrix: Define ordinal scalar values (0.0 to 1.0) for TSG strings within src/python_io/projections.py.
* Model System State Vectors:
  * Populate state_before using initial case posture traits.
	* Populate state_predicted based on mandatory, non-discretionary statutory steps.
	* Populate state_after using actual observed executive, judicial, or administrative outcomes.
* Execute Permutation Baselines: Run CAUSA’s permutation_baseline across logs with 1,000 shuffles.
* Filter Systemic Noise: Drop any episodes where the observed causal score fails to clear the shuffled baseline mean.

📐 Phase 4: High-Stability Geometric Compilation (Julia Layer)

Objective: Ingest causal vectors that pass verification and cast them into zero-heap static manifolds to guarantee numerical tracking boundaries.
* Initialize Immutable Types: Define fixed-size SVector{5, Float64} primitives within src/julia_engine/Types.jl.
* Enforce Core Invariants: Implement compile-time assertions protecting the lower-bound vector magnitude:julia
@assert norm(coords) > 1e-12 "Axiomatic Collapse: Subnormal rounding drift risk detected."
Use code with caution.
* Map Independent Manifolds: Direct vectors into completely isolated tensor representations:
  * Manifold A (\(\mathcal{M}_{A}\)): Judicial branch metrics and immunity walls.
	* Manifold B (\(\mathcal{M}_{B}\)): Municipal policing and administrative actions.
	* Manifold C (\(\mathcal{M}_{C}\)): International/Treaty boundary statuses.

🚀 Phase 5: Harness Ingestion & Sanity Testing

Objective: Compile the verified geometric representations into the exact payload expected by the enclave orchestrator.
* Generate Enclave Manifest: Format the static vector collections into a single, clean manifest.json.
* Execute Math-Washing Defenses: Run the harness's test_math_washing.jl file against the generated file.
* Validate Angular Divergence: Confirm that high-magnitude administrative noise in \(\mathcal{M}_{A}\) calculates an exact divergence delta (\(d_{\mathrm{geo}} = 1.0\)) without polluting tracking horizons for \(\mathcal{M}_{B}\) or \(\mathcal{M}_{C}\).
To begin coding the adapter, let me know:
• Should we first write the Python TSG-to-CAUSA projection dictionary to lock down your scalar values?
• Do you want the Julia-native type structures drafted to handle the validated vector inputs?
