#!/bin/bash

zmienna=$1
program_running=$(pgrep $zmienna)


echo $program_running

active_window_id=$(xdotool search --name $zmienna  )

echo $active_window_id

#active_window_id=$(xdotool search --name $1 |awk -v line="$2" 'NR==line' )

#echo $active_window_id