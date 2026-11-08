module JuliaEngine

include("Types.jl")
include("Compiler.jl")
include("PreAudit.jl")
include("Visualizer.jl") # Inject the new visual tracking layout engine

using .Types
using .Compiler
using .PreAudit
using .Visualizer

export LegalStateVector, InstitutionalManifold, compile_manifest_stream, audit_manifold_isolation, generate_manifold_plot

end
