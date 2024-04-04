#!/bin/bash

export PYTHONPATH=$PYTHONPATH:`pwd`/src

export PREFECT_LOGGING_SETTINGS_PATH=`pwd`/logging.yml

source .env

function run_flow() {
    local flow_path="$1"

    pdm run $flow_path &

    pid=$!

    echo $pid >> .background_flows
}

function run_flow_with_tmux() {
    local flow_path="$1"

    # Remove pathname and extension from flow path
    local flow_name="$flow_path"
    flow_name="${flow_name##*/}"
    flow_name="${flow_name%.*}"

    if tmux list-sessions >/dev/null 2>&1 && tmux list-sessions | grep -q "^$flow_name:"; then
        # If a tmux session with the same name already exists.. ask for restarting it 
        local user_input
        echo "A tmux session named '$flow_name' already exists."
        read -p "Do you want to restart this session? (y/n): " user_input

        case $user_input in
            [Yy]* )
                tmux kill-session -t "$flow_name"
                echo "Session restarted."
                ;;
            [Nn]* )
                echo "Session not restared."
                return
                ;;
        esac
    fi
    
    # Start a new tmux session
    tmux new-session -d -s "$flow_name" pdm run $flow_path
}

# Export the function to be used in find
export -f run_flow
export -f run_flow_with_tmux

# Start serving all flows in parallel (the ones under `src/../flows/*.py`)

if [ $SERVE_WITH_TMUX -eq 0 ]; then
    find src/*/flows -type f -name "*.py" -exec bash -c 'run_flow_with_tmux "$0"' {} \;
else
    > .background_flows # reset the pid files 
    find src/*/flows -type f -name "*.py" -exec bash -c 'run_flow "$0"' {} \;
    wait
fi
