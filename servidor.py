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
