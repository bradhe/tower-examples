import tower
import json

@tower.setup
def hello_world_setup():
    pass

@tower.inference
def hello_world_inference():
    print("Calling inference")
    return tower.StringResult('This is yet another attemp!')

tower.start()
