#!/bin/bash

echo "Hello World"
echo "What is your name?"
read nameResponse
if [[ $nameResponse = monty ]]
	then echo "What is your quest?"
	read questResponse
	if [[ $questResponse = holy grail ]]
		then echo "What is your favorite color?"
		read colorResponse
		echo $colorRespnse
	fi
fi
