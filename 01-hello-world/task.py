import tower
import json

@tower.setup
def hello_world_setup(dir):
    pass

@tower.inference
def hello_world_inference():
    return tower.StringResult('Hello, world!')

tower.start()
