"""
Julia Geometric Layer Assertion Tests
Enforces compile-time invariants and metric alignment.
"""
using Test
using StaticArrays
using LinearAlgebra

# Include the source engine files directly for component isolation
include("../src/julia_engine/Types.jl")
include("../src/julia_engine/PreAudit.jl")
using .Types
using .PreAudit

@testset "Tri-System Bridge Invariant Verifications" begin

    @testset "Vector Magnitude Safety Perimeter" begin
        # 1. Valid vectors above 10^-12 should construct flawlessly
        valid_coords = SVector{5, Float64}(0.5, 0.0, 0.4, 1.0, 0.2)
        valid_vector = LegalStateVector(valid_coords, 0.85)
        @test norm(valid_vector.coords) > 1e-12
        
        # 2. Subnormal vectors must trigger an immediate Axiomatic Collapse Exception
        invalid_coords = SVector{5, Float64}(1e-13, 0.0, 0.0, 0.0, 0.0)
        @test_throws ErrorException LegalStateVector(invalid_coords, 0.5)
    end

    @testset "Angular Divergence Protection" begin
        # Test that orthogonal system states yield maximum divergence (d_geo = 1.0)
        v1 = LegalStateVector(SVector{5, Float64}(1.0, 0.0, 0.0, 0.0, 0.0), 0.5)
        v2 = LegalStateVector(SVector{5, Float64}(0.0, 1.0, 0.0, 0.0, 0.0), 0.5)
        
        d_geo = calculate_d_geo(v1, v2)
        @test d_geo ≈ 1.0 atol=1e-6
        
        # Test that perfectly parallel states yield zero divergence (d_geo = 0.0)
        d_geo_self = calculate_d_geo(v1, v1)
        @test d_geo_self ≈ 0.0 atol=1e-6
    end

end
