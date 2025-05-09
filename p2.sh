#!/bin/bash
versos=("Lá vem o pato..." "Pata aqui, pata acolá..." "Lá vem o pato..." "Para ver o que é que há.")
cores=("\033[31m" "\033[32m" "\033[34m" "\033[35m")

for i in "${!versos[@]}"; do
	echo -e "${cores[$i]}${versos[$i]}\033[0m"
	sleep 2
done
