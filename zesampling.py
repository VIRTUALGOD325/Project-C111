from os import name
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].tolist()

'''
fig = ff.create_distplot([data],["Maths Scores"],show_hist=False)
fig.show()
'''

mean = statistics.mean(data)
sd = statistics.stdev(data)

print("Mean of entire data set is {}".format(mean))
print("Standard deviation of data is {}".format(sd))


#Data 1

df1 = pd.read_csv("data1.csv")

data1 = df1["Math_score"].tolist()

mean_first_intervention = statistics.mean(data1)
sd_first_intervention = statistics.stdev(data1)

print("mean of first intervention {}".format(mean_first_intervention))
print("SD of first intervention {}".format(sd_first_intervention))

'''
sd1_start,sd1_end = mean_first_intervention - sd_first_intervention , mean_first_intervention + sd_first_intervention
sd2_start,sd2_end = mean_first_intervention - sd_first_intervention*2 , mean_first_intervention + sd_first_intervention*2 
sd3_start,sd3_end = mean_first_intervention - sd_first_intervention*3 , mean_first_intervention + sd_first_intervention*3

fig = ff.create_distplot([data1],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="Mean Of data set"))
fig.add_trace(go.Scatter(x=[mean_first_intervention,mean_first_intervention],y=[0,0.2],mode="lines",name="mean of student who had extra class"))
fig.add_trace(go.Scatter(x=[sd1_end,sd1_end],y=[0,0.2],mode="lines",name="SD1 End"))
fig.add_trace(go.Scatter(x=[sd2_end,sd2_end],y=[0,0.2],mode="lines",name="SD2 End"))
fig.add_trace(go.Scatter(x=[sd3_end,sd3_end],y=[0,0.2],mode="lines",name="SD3 End"))
fig.show()
'''


#Data 2
df2 = pd.read_csv("data2.csv")

data2 = df2["Math_score"].tolist()

mean_second_intervention = statistics.mean(data2)
sd_second_intervention = statistics.stdev(data2)

print("mean of first intervention {}".format(mean_second_intervention))
print("SD of first intervention {}".format(sd_second_intervention))

'''
sd1_start,sd1_end = mean_second_intervention - sd_second_intervention , mean_second_intervention + sd_second_intervention
sd2_start,sd2_end = mean_second_intervention - sd_second_intervention*2 , mean_second_intervention + sd_second_intervention*2 
sd3_start,sd3_end = mean_second_intervention - sd_second_intervention*3 , mean_second_intervention + sd_second_intervention*3

fig = ff.create_distplot([data2],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="Mean Of data set"))
fig.add_trace(go.Scatter(x=[mean_second_intervention,mean_second_intervention],y=[0,0.2],mode="lines",name="mean of student who had extra class"))
fig.add_trace(go.Scatter(x=[sd1_end,sd1_end],y=[0,0.2],mode="lines",name="SD1 End"))
fig.add_trace(go.Scatter(x=[sd2_end,sd2_end],y=[0,0.2],mode="lines",name="SD2 End"))
fig.add_trace(go.Scatter(x=[sd3_end,sd3_end],y=[0,0.2],mode="lines",name="SD3 End"))
fig.show()
'''


#Data 3
df3 = pd.read_csv("data3.csv")

data3 = df3["Math_score"].tolist()

mean_third_intervention = statistics.mean(data3)
sd_third_intervention = statistics.stdev(data3)

print("mean of first intervention {}".format(mean_third_intervention))
print("SD of first intervention {}".format(sd_third_intervention))

sd1_start,sd1_end = mean_third_intervention - sd_third_intervention , mean_third_intervention + sd_third_intervention
sd2_start,sd2_end = mean_third_intervention - sd_third_intervention*2 , mean_third_intervention + sd_third_intervention*2 
sd3_start,sd3_end = mean_third_intervention - sd_third_intervention*3 , mean_third_intervention + sd_third_intervention*3

fig = ff.create_distplot([data3],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="Mean Of data set"))
fig.add_trace(go.Scatter(x=[mean_third_intervention,mean_third_intervention],y=[0,0.2],mode="lines",name="mean of student who had extra class"))
fig.add_trace(go.Scatter(x=[sd1_end,sd1_end],y=[0,0.2],mode="lines",name="SD1 End"))
fig.add_trace(go.Scatter(x=[sd2_end,sd2_end],y=[0,0.2],mode="lines",name="SD2 End"))
fig.add_trace(go.Scatter(x=[sd3_end,sd3_end],y=[0,0.2],mode="lines",name="SD3 End"))
fig.show()

zScore = (mean - mean_second_intervention)/sd
print(zScore)