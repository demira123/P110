import plotly.figure_factory as pff
import statistics as st
import pandas as pd
import random 

df = pd.read_csv("pro110.csv")

data= df["reading_time"].to_list()

graph=pff.create_distplot([data],["reading_time"] , show_hist=False)

graph.show()

mean = st.mean(data)
stdev = st.stdev(data)

print("-------------------------------------")

print("Mean Of Population : " , mean)

print("stdev Of Population : " , stdev)


# --------------------- code to find mean and std deviation of 100 random data points for 1000 times -----------------------

x=[]

for i in range(0,1000):
    y=[]
    for j in range(0,100):
        y.append(random.choice(data))

    x.append(st.mean(y))

meanOfSample = st.mean(x)

stdevOfSample = st.stdev(x)

print("-------------------------------------")

print("Mean Of Sample : " , meanOfSample)

print("stdev Of Sample : " , stdevOfSample)
