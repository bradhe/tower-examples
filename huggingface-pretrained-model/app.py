import tower
from transformers import pipeline

CLASSIFIER = None

@tower.setup
def tower_setup(dir):
    global CLASSIFIER
    CLASSIFIER = pipeline("sentiment-analysis")

@tower.inference
def tower_inference(dir):
    global CLASSIFIER
    result = CLASSIFIER("Hello, world!")
    return tower.NumberResult(result["score"])

@tower.start()


