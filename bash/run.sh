#!/bin/bash


# Reading data from input: [app] [monitor] [workspace]

app=$1
monitor=$2
workspace=$3

#cheaking if the program is running 
#if it's not, run it

program_running=$(pgrep $app)

if [ -z "${program_running}" ]; then
    eval "$app" & 
    sleep 3
fi


active_window_id=$(xdotool search --name $app   )



#test
#echo $active_window_id

count=0  # only for spotify

for id in $active_window_id
do 

  # get screen sizes for monitor
  eval $(xdotool getdisplaygeometry --shell)
  screen_width=$WIDTH
  screen_height=$HEIGHT

  # Calculate position x for windor in selectet monitor
  if [ $monitor -eq 0 ]; then
    x=0
  elif [ $monitor -eq 1 ]; then
    x=$screen_width
  else
    echo "Invalid monitor number."
    exit 1
  fi

  #Move the window to the chosen monitor and workspace.
  xdotool windowmove $id $x 0
  xdotool set_desktop_for_window $id $workspace
  
  let count++

  sleep 1
  if [ $app == spotify ] && [ $count -eq 3 ]; then
    xdotool windowactivate --sync $id type " "
    #echo $id
  fi
done


