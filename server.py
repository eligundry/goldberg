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
    return tasks, status.HTTP_200_OK

@app.route("/lights", methods=['GET'])
def lights_actions():
    """
    Return a list of actions that you can do with lights
    """
    actions = {
        "rgb": {
            "name": "Set Color",
            "description": "Make the lights an RGB color"
        },
        "strobe": {
            "name": "Strobe",
            "description": "Strobe the lights with optional frequency"
        }
    }

    return actions, status.HTTP_200_OK

@app.route("/lights/rgb", methods=['GET', 'POST'])
def lights_set_rgb():
    """
    Defines the color of the lights. The colors are random by default.

    GET: Returns the current colors of the light
    POST: Sets the colors of the lights
    """
    if request.method == "GET":
        response = {
            "message": "The lights colors are",
            "colors": pi.lights.get_color()
        }

        return response, status.HTTP_200_OK

    elif request.method == "POST":
        red = request.data['r']
        green = request.data['g']
        blue = request.data['b']

        pi.lights.set_color(red, green, blue)

        response = {
            "message": "The lights colors were set",
            "colors": pi.lights.get_color()
        }

        return response, status.HTTP_201_CREATED


@app.route("/lights/strobe", methods=["GET", "POST", "DELETE"])
def lights_strobe():
    """
    Makes the lights strobe with an optional frequency

    GET: Is light strobbing?
    POST: Starts lights strobing
    DELETE: Stops lights strobing
    """
    if request.method == "GET":
        if pi.lights.is_strobbing:
            return { "strobbing": 1 }, status.HTTP_200_OK
        else:
            return { "strobbing": 0 }, status.HTTP_200_OK

    elif request.method == "POST":
        pi.lights.start_strobe()

        response = {
            "message": "Lights started strobbing"
        }

        return response, status.HTTP_201_CREATED

    elif request.method == "DELETE":
        pi.lights.stop_strobe()

        response = {
            "message": "Successfully stopped the lights from strobing"
        }

        return response, status.HTTP_204_NO_CONTENT

    return

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
