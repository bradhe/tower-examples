import tower

@tower.setup
def hello_world_setup():
    print("Calling setup")
    return "Setup."

@tower.inference
def hello_world_inference():
    print("Calling inference")
    return "Hello, world!"

tower.start()
