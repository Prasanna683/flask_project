from flask import Flask, render_template

app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Kakinada',
    'price': 'Starting from Rs.75.00'
  },
  {
    'id': 2,
    'title': 'Vizag',
    'price': 'Starting from Rs.100.00'
  },
  {
    'id': 3,
    'title': 'Rajahmundry',
    'price': 'Starting from Rs.75.00'
  }
]

@app.route("/")
def home():
  return render_template('home.html', branches=jobs)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
