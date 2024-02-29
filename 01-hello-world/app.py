import tower
import json

@tower.setup
def hello_world_setup(dir):
    pass

@tower.inference
def hello_world_inference():
    print("Calling inference")
    return tower.StringResult('Hello, Serhii!')

tower.start()
