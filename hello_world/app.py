import tower

@tower.setup
def hello_world_setup():
    print("Calling setup")

@tower.inference
def hello_world_inference():
    print("Calling inference")

tower.start()
