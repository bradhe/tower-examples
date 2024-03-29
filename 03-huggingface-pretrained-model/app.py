import tower
from transformers import pipeline

CLASSIFIER = None

@tower.setup
def tower_setup(dir):
    print("application: Loading sentiment analysis application")
    model_id = "cardiffnlp/twitter-roberta-base-sentiment-latest"

    global CLASSIFIER
    CLASSIFIER = pipeline("sentiment-analysis", model=model_id)
    
    if CLASSIFIER == None:
        raise ValueError("CLASSIFIER is None")

@tower.inference
def tower_inference():
    print("application: Performing inference")
    global CLASSIFIER
    result = CLASSIFIER("Wow I love AI.")
    return tower.StringResult("The result is \"{dir}\" with score of \"{score}\"".format(dir=result[0]["label"], score=result[0]["score"]))

tower.start()
