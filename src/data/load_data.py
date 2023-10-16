import pandas as pd


def load_data(data_folder_path):
    train_data = pd.read_csv(data_folder_path + "/train.csv")
    test_data = pd.read_csv(data_folder_path + "/test.csv")
    return train_data, test_data
