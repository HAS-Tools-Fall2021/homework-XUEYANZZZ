<center>

### Xueyan Zhang
### Assignment 9
### 10/24/2021

</center>


## Grade:
**3/3:** Nice job!

-- One note I'm fine with collaboraiton but I'm concerrned at the level of similarity between you and Xingyu's written assignments. You both have very similarly worded answers and you have downloaded the same data and gotten the same coefficien of determination on your models. Its fine if you are working together but it needs to be clear that you are doing your own work too. Let me know if you need any help from me to clarify what I mean by this. 
____________
</br>

1. A brief summary of the how you chose to generate your forecast this week.
   
   I built an autoregressive linear model with predictors of flows during one- and two-week ago. The coefficient of determination is 0.33. The forecast for this week is 224.2 cfs.

2. A description of the dataset you added
* What is the dataset? Why did you choose it?
  
  I used daymet precipitation dataset because daymet has a resolution of 4 km and can reflect the average precipitation input condition near the USGS gage. Contrastly, in-situ observed precipitation only reflects water input into this site; however, streamflow is not just that water runs off the land surface but also gather together due to topography.

* What location have you chosen?
  
  I picked a grid cell with latitude of 34.448 and longitude of -111.789 (that is  the river basin where our site is located).

* Where did you get the data from? What was your approach to accessing it?
  
  I used url method to get the data from daymet api.


3. A plot of your additional time series along with your streamflow time series.
   ![picture 1](./two_yaxis_prcp_flow.jpg)
4. A plot that illustrates how you chose your forecast values.
   ![picture 2](./lm.jpg)