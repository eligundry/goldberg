from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)

tasks = {
    "lights": {
        "name": "Lights",
        "description": "Control the lights"
    },
    "water": {
        "name": "Water",
        "description": "Water your plant"
    },
    "cat": {
        "name": "Cat",
        "description": "Feed your cat"
    }
}

@app.route("/", methods=['GET'])
def index():
    """
    Returns a list of actions to the Pebble
    """
    return tasks

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
