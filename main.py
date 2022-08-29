import pandas as pd
from string import ascii_letters
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # load data.csv file and check if it is an n*n matrix
    data = pd.read_csv("data.csv")
    if len(data.index) != len(data.columns):
        raise ValueError("Input must be an n*n matrix.")

    # set index for rows
    data['index'] = list(ascii_letters[:len(data.columns)])
    data = data.set_index('index')

    # create color palette. This is not necessary but its nice if you want to adjust it.
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(data=data, cmap=cmap)
    plt.show()
