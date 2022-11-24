import pandas as pd


def load_data(path):
    """
    :param path: path to the data
    :return: data
    """
    data = pd.read_csv(path, delimiter="\t")
    data = data.dropna()
    data.loc[:, "label"] = data["label"].map({"real": 1, "fake": -1, "humor": 0})
    return data
