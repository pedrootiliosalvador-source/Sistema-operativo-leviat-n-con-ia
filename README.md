# Sistema-operativo-leviat-n-con-ia

#!/bin/bash
# LEVIATAN — SCRIPT COMPLETO SIN DECORACIONES
# Repositorio: pedrootiliosalvador-source/Sistema-operativo-leviat-n-con-ia

clear

# CREAR CARPETA PRINCIPAL
mkdir -p Sistema-operativo-leviat-n-con-ia
cd Sistema-operativo-leviat-n-con-ia || exit 1

# CREAR .gitignore
cat > .gitignore << 'EOF'
*.key
*.pem
*.secret
id_rsa
id_ed25519
.env
privada.*
__pycache__/
*.pyc
*.pyo
*.log
tmp/
temp/
.DS_Store
Thumbs.db
*.zip
*.tar.gz
*.iso
*.img
EOF

# CREAR README.md
cat > README.md << 'EOF'
# LEVIATAN — Sistema Operativo con IA Integrada
# Autor: Pedro Otilio Salvador Mendez
# Plataforma: Debian 13 Trixie / Linux

## Instalacion
chmod +x leviatan.sh
./leviatan.sh instalar
./leviatan.sh iniciar

## Acceso
http://127.0.0.1:8765
EOF

# CREAR requirements.txt
cat > requirements.txt << 'EOF'
flask>=3.0.0
requests>=2.31.0
python-dotenv>=1.0.0
EOF

# CREAR leviatan.sh
cat > leviatan.sh << 'EOF'
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
EOF
chmod +x leviatan.sh

# CREAR servidor.py
cat > servidor.py << 'EOF'
from flask import Flask, jsonify, request
app = Flask(__name__)
PUERTO = 8765

INDEX = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>LEVIATAN</title>
    <style>
        *{margin:0;padding:0;box-sizing:border-box;font-family:sans-serif}
        body{background:#0f172a;color:#e2e8f0;padding:2rem;max-width:800px;margin:0 auto}
        h1{color:#38bdf8;margin-bottom:1rem}
        .ok{color:#4ade80;margin:1rem 0}
        textarea{width:100%;height:100px;background:#1e293b;border:1px solid #334155;color:#fff;padding:1rem;border-radius:0.5rem;margin:1rem 0}
        button{background:#38bdf8;color:#000;border:none;padding:0.75rem 1.5rem;border-radius:0.5rem;font-weight:bold;cursor:pointer}
        #r{margin-top:1.5rem;padding:1rem;background:#1e293b;border-radius:0.5rem;min-height:50px}
    </style>
</head>
<body>
    <h1>LEVIATAN — IA Local y Privada</h1>
    <div class="ok">SISTEMA ACTIVO — Debian 13</div>
    <textarea id="t" placeholder="Escribe tu consulta..."></textarea>
    <button onclick="go()">Enviar</button>
    <div id="r">Esperando...</div>
    <script>
        async function go(){
            const r=await fetch('/q',{
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify({m:document.getElementById('t').value})
            });
            const d=await r.json();
            document.getElementById('r').textContent=d.r;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def inicio():
    return INDEX

@app.route('/q', methods=['POST'])
def q():
    m = request.json.get('m', '')
    return jsonify({"r": f"[LEVIATAN] Recibi: {m}\nSistema activo — todo local y privado."})

if __name__ == '__main__':
    print(f"LEVIATAN -> http://127.0.0.1:{PUERTO}")
    app.run(host='127.0.0.1', port=PUERTO, debug=False)
EOF

# CREAR CARPETA nucleo
mkdir -p nucleo
cat > nucleo/__init__.py << 'EOF'
# LEVIATAN — Nucleo del sistema
EOF
cat > nucleo/motor.py << 'EOF'
class MotorIA:
    def __init__(self):
        self.nombre = "Leviatan"
        self.activo = True
    def procesar(self, mensaje):
        return f"[{self.nombre}] {mensaje}"
EOF
cat > nucleo/memoria.py << 'EOF'
class Memoria:
    def __init__(self):
        self.historial = []
    def guardar(self, e, s):
        self.historial.append({"e":e,"s":s})
EOF

# CREAR CARPETA interfaz
mkdir -p interfaz
cat > interfaz/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>LEVIATAN</title>
</head>
<body>
    <h1>LEVIATAN — Interfaz</h1>
    <p>Sistema operativo con IA integrada.</p>
</body>
</html>
EOF

# SUBIR A GITHUB
git init
git add .
git commit -m "LEVIATAN v1.0 — Sistema completo"
git branch -M main
git remote add origin git@github.com:pedrootiliosalvador-source/Sistema-operativo-leviat-n-con-ia.git
git push -u origin main

echo "TERMINADO — Repositorio subido a GitHub"
echo "Para usar: cd Sistema-operativo-leviat-n-con-ia && ./leviatan.sh instalar && ./leviatan.sh iniciar"
