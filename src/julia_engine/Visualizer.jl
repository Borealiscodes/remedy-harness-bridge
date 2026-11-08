module Visualizer

using Plots
using ..Types

export generate_manifold_plot

"""
    generate_manifold_plot(manifolds::Vector{InstitutionalManifold}, output_path::String)

Extracts 5D coordinates directly from the static stack arrays and projects them to a trendline PNG chart.
"""
function generate_manifold_plot(manifolds::Vector{InstitutionalManifold}, output_path::String)
    println("🎨 Generating System Manifold spatial visualization...")
    
    # Initialize a clean plot layout canvas
    p = plot(
        title="Latent Space Trajectory Coordinate Trace",
        xlabel="Dimensions (x1 to x5)",
        ylabel="Scale Factor Weight",
        ylim=(0.0, 1.05),
        grid=true,
        legend=:topright,
        linewidth=2
    )
    
    for item in manifolds
        # Pull the raw static array values straight out of the SVector container
        coords_array = [item.state.coords[1], item.state.coords[2], item.state.coords[3], item.state.coords[4], item.state.coords[5]]
        
        # Color-code line series based on tracking branch mapping targets
        line_color = :grey
        if item.manifold_type == :M_A
            line_color = :red    # Judicial obstructions / immunity targets
        elseif item.manifold_type == :M_B
            line_color = :blue   # Municipal operations
        elseif item.manifold_type == :M_C
            line_color = :green  # External horizons
        end
        
        plot!(p, 1:5, coords_array, label=item.id, color=line_color, marker=:circle)
    end
    
    # Render and save out the visual matrix frame asset cleanly
    savefig(p, output_path)
    println("💾 Manifold cluster visualization successfully exported to: $output_path")
    return true
end

end
