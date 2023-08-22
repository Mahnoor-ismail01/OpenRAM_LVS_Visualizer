#!/bin/bash

magic -noconsole << EOF
load /home/mahnoor/Downloads/klayout_demo (copy)/inv_demo/sky130_fd_sc_hd__inv_1.mag
select
select scnmos at 120 47
EOF
