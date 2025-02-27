# -*- coding: utf-8 -*-
"""project Uber Data Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_etLsvAAPohyabSxxpSnsSuilZyX4PVh

#**Uber Data Analysis With Python**

**Uber Technologies, Inc.**, commonly known as **Uber**, is an American technology company. Its services include ride-hailing, food delivery, package delivery, couriers, freight transportation, and, through a partnership with Lime, electric bicycle and motorized scooter rental.

We will mainly use data regarding **Uber ride**


In this tutorial, we will use Python to analyze data from Uber.

By the end of this lesson, you will gain a hands-on experience with Python in analyzing data.

We will use Python to:


*   Check how long do people travel with Uber?
*   What Hour Do Most People Take Uber To Their Destination?
* Check The Purpose Of Trips
* Which Day Has The Highest Number Of Trips
* What Are The Number Of Trips Per Each Day?
* What Are The Trips In The Month
* The starting points of trips. Where Do People Start Boarding Their Trip From Most?

<br>

##**Import The Necessary Libraries**
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

data=pd.read_csv('/content/Uber Drives - .csv')
data.head()

"""##Check for Mising Values

If a data is not available, Python uses **NaN** to represnet it.

Let's check below if there data points missing in our dataset.
"""

data.isnull().any()

data.isnull().sum()

data=data.dropna()

data.isnull().sum()

"""Now we can see that there are not missing values in the dataset."""

data['START_DATE*'] = pd.to_datetime(data['START_DATE*'], format="%m/%d/%Y %H:%M")
data['END_DATE*'] = pd.to_datetime(data['END_DATE*'], format="%m/%d/%Y %H:%M")

hour=[]
day=[]
dayofweek=[]
month=[]
weekday=[]
for x in data['START_DATE*']:
    hour.append(x.hour)
    day.append(x.day)
    dayofweek.append(x.dayofweek)
    month.append(x.month)
    weekday.append(calendar.day_name[dayofweek[-1]])
data['HOUR']=hour
data['DAY']=day
data['DAY_OF_WEEK']=dayofweek
data['MONTH']=month
data['WEEKDAY']=weekday

data.head()

"""##**Categories We Have**"""

data['CATEGORY*'].value_counts()

sns.countplot(x='CATEGORY*',data=data)

"""We have large number of business rides caegory as against very few personal rides.

##**How long do people travel with Uber?**
"""

data['MILES*'].plot.hist()

"""mostly people travel in a short mile with Uber.

##**What Hour Do Most People Take Uber To Their Destination?**
"""

hours = data['START_DATE*'].dt.hour.value_counts()
hours.plot(kind='bar',color='red',figsize=(10,5))
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.title('Number of trips Vs hours')

"""As we can see most people take Uber to their destination around the 13th hour(1pm) and the least hour is 2 am.

#**Check The Purpose Of Trips**
"""

data['PURPOSE*'].value_counts().plot(kind='bar',figsize=(10,5),color='brown')

"""We can notice that mostly the purpose of the trip is meeting and meal/entertain.

##**Which Day Has The Highest Number Of Trips**
"""

data['WEEKDAY'].value_counts().plot(kind='bar',figsize=(10,5),color='blue')

"""So Friday has the highest number of Trips.

##**What Are The Number Of Trips Per Each Day?**
"""

data['DAY'].value_counts().plot(kind='bar',figsize=(10,5),color='green')

"""##**What Are The Trips In The Month**"""

data['MONTH'].value_counts().plot(kind='bar',figsize=(10,5),color='black')

"""We can see that December(12) has the most trips.

##**The starting points of trips. Where Do People Start Boarding Their Trip From Most?**
"""

data['START*'].value_counts().plot(kind='bar',figsize=(25,10),color='blue')

"""Most people in this dataset starts their journey from **Cary** followed by some unknown location and then Morrisville."""