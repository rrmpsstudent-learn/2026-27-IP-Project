import matplotlib.pyplot as plt
import pandas as pd

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
'Sep','Oct','Nov','Dec']
sales =[30000,35000,40000,45000,50000,55000,60000,65000,
70000,75000,80000,85000]
plt.bar(months,sales)
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()