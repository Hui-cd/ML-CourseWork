import pandas as pd


# load data
train_data = pd.read_csv(
    "assignment-comp3222-comp6246-mediaeval2015-dataset/mediaeval-2015-trainingset.txt", delimiter="\t")
test_data = pd.read_csv(
    "assignment-comp3222-comp6246-mediaeval2015-dataset/mediaeval-2015-testset.txt", delimiter="\t")

# fake data for training data (fake and humor labels)
number_of_fake = train_data.isin(['fake', 'humor']).sum(axis=0)

#  duplicate data for training data (tweet text)
number_of_duplicated = train_data['tweetText'].duplicated().sum()

# change the data type of label to int
train_data['label'] = train_data['label'].map(
    {'fake': 1, 'humor': 1, 'real': 0})
test_data['label'] = test_data['label'].map({'fake': 1, 'humor': 1, 'real': 0})

# add a new column : length of tweet text
train_data['TextLength'] = train_data['tweetText'].str.len()
