#!/bin/bash
PUERTO=8765
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

case "$1" in
    instalar)
        apt update
        apt install -y python3 python3-pip
        pip3 install --upgrade pip
        pip3 install -r requirements.txt
        echo "Instalacion completa. Usa: ./leviatan.sh iniciar"
        ;;
    iniciar)
        python3 servidor.py &
        sleep 2
        echo "LEVIATAN corriendo en http://127.0.0.1:$PUERTO"
        ;;
    detener)
        pkill -f servidor.py
        echo "Detenido"
        ;;
    estado)
        pgrep -f servidor.py >/dev/null && echo "Activo" || echo "No activo"
        ;;
    *)
        echo "Uso: ./leviatan.sh [instalar|iniciar|detener|estado]"
        ;;
esac
