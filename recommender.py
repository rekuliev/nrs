import pandas as pd
import numpy as np


class DataSet:
    def __init__(self):
        self.raw_data = pd.read_csv("dataset/netflix_titles.csv")
        self.input_data = None
        self.movie = None
        self.tv_show = None

    def clear_data(self):
        """
        Reorganize dataset to extract main features for calculation
        :return: dataset for further calculation
        """
        pass

    def separate_data(self):
        """
        Separate movies and tv shows in input dataset
        :return: movie dataset, tv show dataset
        """
        pass


class BasicRecommender:  # based on similarity coefficient
    def __init__(self):
        pass

    def define_matrix_of_attributes(self):
        pass

    def calculate_similarity(self):
        pass


# Will be expanded and supplemented
