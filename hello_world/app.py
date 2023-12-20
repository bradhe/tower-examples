import tower
import json

@tower.setup
def hello_world_setup():
    pass

@tower.inference
def hello_world_inference():
    print("Calling inference")
    return tower.StringResult('This is a new version yet again. Here we go again.')

tower.start()
