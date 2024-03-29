import tower
from core.readers.github import ReadGithub

CLASSIFIER = None

def github_comment_filter_setup(params):
# TODO: Setup the HuggingFace model
    #global CLASSIFIER
    #CLASSIFIER = pipeline("sentiment-analysis", model=model_id)
    pass

@tower.inference
def github_comment_filter_inference(params):

    # create a reader Task that will read from Github and store in memory (readitems attributes of the class)
    reader = ReadGithub("GitHubReader")

    # read from the source and store all elements in internal property readitems
    # this is equivalent to calling reader.do(source)
    reader("https://api.github.com/repos/dlt-hub/dlt",["issues"])

    # TODO: Add inference with hugging face model
    # global CLASSIFIER
    # result = CLASSIFIER(reader.readitems)
    arr = []
    arr.push(tower.BooleanResult(false, comment_id="123"))
    arr.push(tower.BooleanResult(true, comment_id="abc123"))
    return arr

tower.start()
