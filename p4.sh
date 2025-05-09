#!/bin/bash

#a. Saudação
echo "Bom dia, $USER! Bem-vindo."

#b. Dia e hora
echo "Hoje é $(date '+%A'), e agora são $(date '+%H:%M')."

#c. Clima (usando wttr.in)
echo "Clima em João Pessoa:"
curl -s wttr.in/Joao+Pessoa?format=3

#d. Conselho aleatório
conselhos=("beba água!" "Faça uma pausa para respirar." "Acredite no seu potencial!!!" "Organize seu dia")
conselhos=${conselhos[$RANDOM % ${#conselhos[@]}]}
echo "Conselho do dia: $conselho"
