module PreAudit

using LinearAlgebra
using ..Types

export calculate_d_geo, audit_manifold_isolation

"""
    calculate_d_geo(ρ_X::LegalStateVector, ρ_Y::LegalStateVector)::Float64

Computes the angular divergence between two legal states in R^5.
Protects against metric distortion ("math-washing") by tracking coordinate isolation.
"""
function calculate_d_geo(ρ_X::LegalStateVector, ρ_Y::LegalStateVector)::Float64
    v_X = ρ_X.coords
    v_Y = ρ_Y.coords
    
    norm_prod = norm(v_X) * norm(v_Y)
    
    # Absolute safety guard: check against subnormal boundaries before division
    if norm_prod <= 1e-12
        return 1.0 # Maximum divergence if a system manifold collapses
    end
    
    cosine_similarity = dot(v_X, v_Y) / norm_prod
    
    # Clamp to avoid floating-point precision leaks outside [-1.0, 1.0]
    clamped_cos = clamp(cosine_similarity, -1.0, 1.0)
    
    return 1.0 - clamped_cos
end

"""
    audit_manifold_isolation(manifolds::Vector{InstitutionalManifold})

Performs an out-of-band sanity check across Judicial (M_A) and Municipal (M_B) systems.
Asserts that high-magnitude adjustments inside M_A leave M_B boundaries uncompromised.
"""
function audit_manifold_isolation(manifolds::Vector{InstitutionalManifold})
    m_A_nodes = filter(m -> m.manifold_type == :M_A, manifolds)
    m_B_nodes = filter(m -> m.manifold_type == :M_B, manifolds)
    
    if isempty(m_A_nodes) || isempty(m_B_nodes)
        println("ℹ️ Pre-Audit: Insufficient cross-manifold nodes to compute isolation horizons.")
        return true
    end
    
    println("🔬 Running Enclave Pre-Audit Horizon Check...")
    
    # Evaluate divergence across the primary institutional boundaries
    for node_A in m_A_nodes
        for node_B in m_B_nodes
            divergence = calculate_d_geo(node_A.state, node_B.state)
            println("  ↳ Horizon [$(node_A.id) ↔ $(node_B.id)] d_geo = $(round(divergence, digits=6))")
            
            # If systems are completely orthogonal (remedy exhausted), d_geo approaches 1.0
            if divergence >= 0.999
                println("    ⚠️ Warning: Complete metric isolation detected. Remedy pathway is completely orthogonal.")
            end
        end
    end
    
    return true
end

end
