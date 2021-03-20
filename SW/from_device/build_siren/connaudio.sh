#!/bin/sh
pulseaudio --start
sleep 5
echo "connect 58:51:00:00:06:FB\nquit" | bluetoothctl
sleep 10
cardindex=$(pacmd list-cards | grep index: | awk '{ print $2 }' | grep -v 0)
pacmd set-card-profile $cardindex a2dp_sink
pacmd set-default-sink bluez_sink.58_51_00_00_06_FB.a2dp_sink
