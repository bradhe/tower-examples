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
    return tower.StringResult("The total is: {total}".format(total=TOTAL))

tower.start()
