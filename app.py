from flask import Flask
from datetime import datetime
import os
import subprocess
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        name = "Abhilashitha"  
        username = getpass.getuser()  
        server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
        return f"<h1>Name: {name}</h1><h2>Username: {username}</h2><h3>Server Time: {server_time}</h3><pre>{top_output}</pre>"
    except Exception as e:
        return f"<h1>Internal Server Error</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
