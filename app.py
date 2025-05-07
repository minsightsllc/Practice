from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    data = {
        "title": "Client Dashboard",
        "metrics": {
            "Referrals": 34,
            "Attendance": "92%",
            "Test Scores": "78%"
        }
    }
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
