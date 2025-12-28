#!/bin/sh

select_best_remote() {
    REMOTE1="github.com"
    REMOTE2="gitee.com"
    LATENCY1=$(ping -c 2 "$REMOTE1" 2>/dev/null | tail -1 | awk '{print $4}' | cut -d '/' -f 2 | cut -d '.' -f 1)
    LATENCY2=$(ping -c 2 "$REMOTE2" 2>/dev/null | tail -1 | awk '{print $4}' | cut -d '/' -f 2 | cut -d '.' -f 1)
    if [ -z "$LATENCY1" ]; then LATENCY1=9999; fi
    if [ -z "$LATENCY2" ]; then LATENCY2=9999; fi
    if [ "$LATENCY1" -lt "$LATENCY2" ]; then
        echo "origin"
    else
        echo "gitee"
    fi
}

git_pull_best() {
    best_remote=$(select_best_remote)
    echo "Using remote: $best_remote"
    git pull "$best_remote" master
    cp /auto_dtu/model_config/model-config.toml /auto_dtu/config/.
    cp /auto_dtu/model_config/readme_dtu.txt /auto_dtu/config/.
}

verify_app() {
    echo "ready" > /auto_dtu/state
    while [ "$(cat /auto_dtu/state 2>/dev/null)" != "running" ]; do
        pkill -f "python3 run.py" 2>/dev/null
        python3 run.py &
        sleep 60
    done
}

git_pull_best
if verify_app; then
  while true; do
    if [ -f /auto_dtu/upgrade ]; then
      git_pull_best
      pkill -f "python3 run.py" 2>/dev/null
      python3 run.py &
      rm /auto_dtu/upgrade
    fi
    sleep 300
  done
fi