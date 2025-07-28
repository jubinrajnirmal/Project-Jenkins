from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""<pre>
    [◉_◉ ]   ⚙️ Beep boop...
     ( || )   Deploying: POSITIVE VIBES
      /__\\    >> INITIATING: HAVE A GOOD DAY <<

    ⌨️ Uptime: 100%    |   Logs: Clean
    ☕ Coffee: Full    |   Threats: Contained

    Current Date and Time: {current_time}
    </pre>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)