#!/usr/bin/env bash

installation_target=/usr/bin/unison_daemon.py
if [ ! -f ${installation_target} ]; then
  echo ${BASH_SOURCE[0]}
  project_dir=$(cd $(dirname ${BASH_SOURCE[0]}) && pwd)
  ln -s ${project_dir}/unison_daemon.py ${installation_target}
fi
