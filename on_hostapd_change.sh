#!/bin/bash
#Logs mac and hostname when hostapd connection changes state 
#displays to terminal and writes to connections.log
#
#usage: sudo hostapd_cli -a ./onHostapdChange.sh

ts=$(date "+%Y-%m-%d %T")
sleep 3 #waiting so arp can gather host info
machine=$(arp | grep $3 | awk '{print $1}')

if [[ $2 == "AP-STA-CONNECTED" ]]
then
	echo "$ts: MAC:$3 Action:CONNECT    Host:$machine" | tee -a connections.log
fi

if [[ $2 == "AP-STA-DISCONNECTED" ]]
then
	echo "$ts: MAC:$3 Action:DISCONNECT Host:$machine" | tee -a connections.log
fi
