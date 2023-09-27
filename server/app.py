from flask import render_template
from config import app, jsonify
from routes.routes import *

# Import your other modules here (models, routes, etc.)

# Routes to render the "index.html" template

@app.route('/api/users')
def api_users():
    # Add logic here to handle API requests if needed
    return jsonify({"message": "API endpoint for users"})

@app.route('/')
@app.route('/home')
@app.route('/auth')
@app.route('/useronly')

def index(id=0):
    return render_template("index.html")
if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0', port=8000, debug=False)
    app.run(port=5555, debug=True)