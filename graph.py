import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

df = pd.read_csv("./newdata.csv")
data = df["average"].tolist()
mn = statistics.mean(data)
std = statistics.stdev(data)
print("mean of population is ", mn)
print("stdev of population is ", std)

def exp():
    dataset = []
    for i in range(0,100):
        index = random.randint(0, len(data)-1)
        num = data[index]
        dataset.append(num)

    mean1 = statistics.mean(dataset)
    return mean1

meanlist = []

for i in range(0,1000):
    mean2 = exp()
    meanlist.append(mean2)

finalmean = statistics.mean(meanlist)
print(finalmean)
print(statistics.stdev(meanlist))

figure = ff.create_distplot([meanlist], ["Average"])
figure.show()