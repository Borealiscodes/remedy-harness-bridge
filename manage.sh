#!/usr/bin/env bash

# ==============================================================================
# remedy-harness-bridge Toolkit Automation Pipeline
# Unifies data mocking, multi-language testing, core auditing, and visualization.
# ==============================================================================

# Strict execution flags to prevent silent cascade errors
set -euo pipefail

# --- Environment Configurations ---
export STAGE1_REPO_PATH="${STAGE1_REPO_PATH:-../test-mock-stage1-repo}"
export MANIFEST_OUT="data/manifest.json"
export PLOT_OUT="data/manifold_trace.png"

# Colorful Logging Utilities
log_info()  { echo -e "\033[1;34mℹ️  [INFO]\033[0m $1"; }
log_succ()  { echo -e "\033[1;32m✅ [SUCCESS]\033[0m $1"; }
log_warn()  { echo -e "\033[1;33m⚠️  [WARN]\033[0m $1"; }
log_err()   { echo -e "\033[1;31m❌ [ERROR]\033[0m $1"; }

show_help() {
    cat << EOF
Usage: ./manage.sh [command]

Available Commands:
  mock     - Stand up a mock Stage 1 repository environment with 180 case logs.
  test     - Execute Python assertions, Julia invariants, and orchestration prototype.
  run      - Process repo text files through CAUSA filters and compile via Julia.
  clean    - Purge mock datasets, cached manifestations, and visual exports.
  all      - Sequentially execute clean, mock, test, and run pipelines.
EOF
}

# --- Module Actions ---
do_clean() {
    log_info "Purging local runtime caches and staging artifacts..."
    rm -rf "${STAGE1_REPO_PATH}" "data" ".pytest_cache" "__pycache__" "src/*/__pycache__" "test/__pycache__" "tests/__pycache__"
    log_succ "Workspace cleaned."
}

do_mock() {
    log_info "Initializing Stress Test Asset Profiles..."
    python3 utils/mock_generator.py
    log_succ "Mock environments successfully generated."
}

do_test() {
    log_info "Executing Cross-Language Test Suites..."
    
    log_info "Running Python text tokenization assertions via pytest..."
    pytest tests/ -v
    
    log_info "Running Julia static array invariant verifications..."
    julia --project=. test/runtests.jl
    
    log_info "Running Julia Test Orchestration Ingestion Prototype (Allocation Metrics)..."
    julia --project=. test/test_orchestration.jl
    
    log_succ "All validation gates passed successfully."
}

do_run() {
    log_info "Orchestrating Ingestion Handshake Pipeline..."
    python3 run_bridge.py
    log_succ "Execution run completed successfully."
}

# --- Main Entry Execution Router ---
if [ $# -lt 1 ]; then
    show_help
    exit 1
fi

case "$1" in
    mock)  do_mock ;;
    test)  do_test ;;
    run)   do_run ;;
    clean) do_clean ;;
    all)
        do_clean
        do_mock
        do_test
        do_run
        ;;
    *)
        log_err "Unknown pipeline token option: '$1'"
        show_help
        exit 1
        ;;
esac
