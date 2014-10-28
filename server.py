from flask import request
from flask.ext.api import FlaskAPI, status
from pi import Pi

app = FlaskAPI(__name__)
pi = Pi()

@app.route("/", methods=['GET'])
def index():
    """
    Returns a list of actions to the Pebble
    """
    tasks = {
        "light": {
            "name": "Lights",
            "description": "Control the lights"
        },
        "plant": {
            "name": "Plant",
            "description": "Tend to your plant"
        },
        "snack": {
            "name": "Snacks",
            "description": "Dispense candy"
        }
    }

    return tasks, status.HTTP_200_OK

@app.route('/light', methods=['GET'])
def light_actions():
    """
    Return a list of actions that you can do with lights. Put an int after it
    to control a specific light
    """
    actions = {
        "0": {
            "name": "Light Strand 1",
            "description": "Control this light strand"
        },
        "1": {
            "name": "Light Strand 2",
            "description": "Control this light strand"
        }
    }

    return actions, status.HTTP_200_OK


@app.route("/light/<int:light_num>/", methods=['GET', 'POST'])
def light_set_rgba(light_num):
    """
    Defines the color of the lights. The colors are random by default.

    GET: Returns the current colors of the light
    POST: Sets the colors of the lights.
    VARIABLES: 'r', 'g', 'b' ints 0-255, 'a' float 0.0-1.0
    """
    if request.method == "GET":
        response = {
            "message": "The lights colors are",
            "colors": pi.light[light_num].get_color()
        }

        return response, status.HTTP_200_OK

    elif request.method == "POST":
        pi.light[light_num].set_color(r=request.data['r'], g=request.data['g'],
                            b=request.data['b'], a=request.data['a'])

        response = {
            "message": "The lights colors were set",
            "colors": pi.light[light_num].get_color()
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
            "description": "Moist soil checker"
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

@app.route("/plant/water", methods=['GET'])
def plant_water():
    """
    Waters the plant with a GET request
    """
    if pi.plant.water():
        return { 'message': 'The plant was watered' }, status.HTTP_201_CREATED
    else:
        return { 'message': "The plant wasn't watered" }, status.HTTP_500_INTERNAL_SERVER_ERROR

@app.route("/snack", methods=['GET'])
def snackbox():
    pi.snack_box.disperse()
    response = { "message": "Enjoy your candy!" }
    return response,  status.HTTP_200_OK


if __name__ == '__main__':
    app.run(host='0.0.0.0')
