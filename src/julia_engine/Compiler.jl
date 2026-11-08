module Compiler

using JSON3
using StaticArrays
using ..Types

export compile_manifest_stream

function assign_manifold_target(case_id::String)::Symbol
    # Route tracking layers cleanly based on tracking ID taxonomy
    if startswith(case_id, "01") || startswith(case_id, "02")
        return :M_A  # Judicial Branch Constraints
    elif startswith(case_id, "03") || startswith(case_id, "05")
        return :M_B  # Municipal / Executive Actions
    else
        return :M_C  # External / Conflict Horizons
    end
end

function compile_manifest_stream(json_raw_string::String)::Vector{InstitutionalManifold}
    # Rapid ingestion with JSON3 to avoid heap pollution
    parsed_payload = JSON3.read(json_raw_string)
    compiled_elements = InstitutionalManifold[]

    for item in parsed_payload
        case_id = String(item[:id])
        raw_coords = item[:coordinates]
        score = Float64(item[:ownership_score])

        # Cast raw coordinates directly onto a stack-allocated SVector
        static_coords = SVector{5, Float64}(
            Float64(raw_coords[1]),
            Float64(raw_coords[2]),
            Float64(raw_coords[3]),
            Float64(raw_coords[4]),
            Float64(raw_coords[5])
        )

        # Initialize the checked types
        state_vec = LegalStateVector(static_coords, score)
        target_manifold = assign_manifold_target(case_id)

        push!(compiled_elements, InstitutionalManifold(case_id, target_manifold, state_vec))
    end

    return compiled_elements
end

end
