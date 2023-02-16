


def calculate(water_state):
    if water_state > 5:
        return "gas"
    elif water_state < 5:
        return "liquid"
    elif water_state == 5:
        return "solid"



