import tower
import json

@tower.setup
def hello_world_setup(dir):
    pass

@tower.inference
def hello_world_inference(params):
    person = params["person"]
    return tower.StringResult('Hello, {person}!'.format(person=person))

tower.start()
