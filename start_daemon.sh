#!/usr/bin/env bash
set -e
# override env vars
export VAR_1="overridden env var 1";
export VAR_2="overridden env var 2";
export VAR_3="overridden env var 3";
export VAR_4="overridden env var 4"

# initialize pyenv virtual environment
# deactivate it first (in case it was activated), activate it and run.
eval "$(pyenv init -)" \
&& eval "$(pyenv virtualenv-init -)" \
&& pyenv deactivate \
&& pyenv activate daemon_372 \
&& python -u daemon.py
