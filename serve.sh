#!/bin/bash

export PYTHONPATH=$PYTHONPATH:`pwd`/src

export PREFECT_LOGGING_SETTINGS_PATH=`pwd`/logging.yml

# Start serving all flows in parallel
# Add all your flow here..

pdm run src/example/flow.py &
wait