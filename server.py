from flask import request
from flask.ext.api import FlaskAPI, status
from pi import Pi

app = FlaskAPI(__name__)
pi = Pi()

tasks = {
    "lights": {
        "name": "Lights",
        "description": "Control the lights"
    },
    "plant": {
        "name": "Plant",
        "description": "Tend to your plant"
    }
}

@app.route("/", methods=['GET'])
def index():
    """
    Returns a list of actions to the Pebble
    """
    return tasks, status.HTTP_200_OK

@app.route("/lights", methods=['GET'])
def lights_actions():
    """
    Return a list of actions that you can do with lights
    """
    actions = {
        "rgba": {
            "name": "Set Color",
            "description": "Make the lights an RGBA color"
        }
    }

    return actions, status.HTTP_200_OK

@app.route("/lights/rgba", methods=['GET', 'POST'])
def lights_set_rgba():
    """
    Defines the color of the lights. The colors are random by default.

    GET: Returns the current colors of the light
    POST: Sets the colors of the lights. Keys are 'r', 'g', 'b', 'a' and must be ints
    """
    if request.method == "GET":
        response = {
            "message": "The lights colors are",
            "colors": pi.lights.get_color()
        }

        return response, status.HTTP_200_OK

    elif request.method == "POST":
        pi.lights.set_color(r=request.data['r'], g=request.data['g'],
                            b=request.data['b'], a=request.data['a'])

        response = {
            "message": "The lights colors were set",
            "colors": pi.lights.get_color()
        }

        return response, status.HTTP_201_CREATED


@app.route("/plant", methods=["GET"])
def plant_actions():
    actions = {
        "water": {
            "name": "Water Plant",
            "description": "Spray water on plant"
        },
        "moisture": {
            "name": "Moisture of Soil",
            "description": "See how much moisture is in the soil"
        },
        "status": {
            "name": "Plant Status",
            "description": "How is planty doing?"
        }
    }

    return actions, status.HTTP_200_OK

@app.route("/plant/status", methods=["GET"])
def plant_status():
    return { "status": pi.plant.status() }, status.HTTP_200_OK

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
