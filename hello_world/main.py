import tower

@tower.setup
def setup_tower():
    print("Running Tower setup")

@tower.inference
def inference_tower():
    print("Running Tower inference")

tower.start()
