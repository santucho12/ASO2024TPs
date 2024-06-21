#!/bin/bash

read -p "Ingrese un nombre: " nombre

nombre_limpio=$(echo "$nombre" | tr '[:upper:]' '[:lower:]' | tr -d ' ')

respuesta=$(curl -s "https://api.genderize.io?name=$nombre_limpio")

genero=$(echo "$respuesta" | grep -oP '(?<="gender":")[^"]*')

if [ -n "$genero" ]; then
echo "El género para el nombre \"$nombre\" es: $genero."
else
echo "No se pudo determinar el género para el nombre \"$nombre\"."
fi
