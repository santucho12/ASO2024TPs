#!/bin/bash
echo "Elige piedra, papel o tijera (sin acentos ni mayusculas):"
read opcion_usuario


opcion_usuario=$(echo "$opcion_usuario")
opciones=("piedra" "papel" "tijera")
opcion_terminal=${opciones[$(( RANDOM % 3 ))]}

echo "la terminal eligio: $opcion_terminal"


if [[ "$opcion_usuario" == "piedra" || "$opcion_usuario" == "papel" || "$opcion_usuario" == "tijera" ]]; then

if [ "$opcion_usuario" == "$opcion_terminal" ]; then
echo "empate"
elif [ "$opcion_usuario" == "piedra" ] && [ "$opcion_terminal" == "tijera" ]; then
echo "ganaste"
elif [ "$opcion_usuario" == "papel" ] && [ "$opcion_terminal" == "piedra" ]; then
echo "ganaste"
elif [ "$opcion_usuario" == "tijera" ] && [ "$opcion_terminal" == "papel" ]; then
echo "ganaste"
else
echo "perdiste"
fi
else
echo "opción invalida"
fi
