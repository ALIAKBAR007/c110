import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random as rd
import pandas as pd
import csv

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= rd.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean


def show_fig(mean_list):
    df = mean_list
    mean = st.mean(df)
    fig = ff.create_distplot([df], ["average"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 12], mode="lines", name="MEAN"))
    fig.show()



def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = st.mean(mean_list)
    print("Mean of data",mean )

setup()


def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    st_deviation = st.stdev(mean_list)
    print("SD:- ", st_deviation)

standard_deviation()