import os
import tower

# This holds the state of the model.
TOTAL = 0

@tower.setup
def model_setup(dir):
    with open(os.path.join(dir, "model/model.txt")) as file:
        terms = file.read().split(",")
        total = 0

        for term in terms:
            total += int(term)

        global TOTAL
        TOTAL = total

@tower.inference
def model_inference():
    global TOTAL
    r = requests.get("https://www.google.com")
    return tower.StringResult("The total is: {total} with status {status}".format(total=TOTAL, status=r.status_code))

tower.start()
