from Utility import load_data
import numpy as np


trainingSet = load_data("assignment-comp3222-comp6246-mediaeval2015-dataset/mediaeval-2015-trainingset.txt")
testSet = load_data("assignment-comp3222-comp6246-mediaeval2015-dataset/mediaeval-2015-testset.txt")
fake_set = trainingSet[trainingSet["label"] == -1]
real_set = trainingSet[trainingSet["label"] == 1]
humor_set = trainingSet[trainingSet["label"] == 0]
fake_text_set = fake_set['tweetText']
real_text_set = real_set["tweetText"]
humor_text_set = humor_set["tweetText"]
