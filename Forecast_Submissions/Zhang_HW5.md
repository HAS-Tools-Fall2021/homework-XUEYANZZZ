<center>

### Xueyan Zhang
### 26/09/2021
### Assignment 5
<br />
</center>


Because the average flow dring last week is still over 90 cfs, I forecasted it during next week should be 80 cfs.
<br />

### Questions
1. Provide a summary of the data frames properties.
   
    What are the column names?
    ['00060_Mean', '00060_Mean_cd', 'site_no']
    What is its index?
    datetime
    What data types do each of the columns have?
    [float, obecjt, object]. Here, object has string-like values.

2. Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.
   
<center>

| statistics | value (cfs) |
|------------|-------|
|    count   | 11956 |
|    mean    |  340.9|
|    std     | 1391.2|
|    min     |   19.0|
|    25%     | 93.475|
|    50%     |  157.1|
|    75%     |  214.0|
|    max     |63400.0|

</center>

3. Provide the same information but on a monthly basis.
   
<center>

|datetime |count	|mean	|std	|min	|25%	|50%	|75%	|max	|
|---------|---------|-------|-------|-------|-------|-------|-------|-------|				
|1	|1023.0	|691.002933	|2708.527013	|158.0	|201.000	|218.0	|285.00	|63400.0
|2	|932.0	|903.156652	|3300.470852	|136.0	|200.000	|238.0	|615.75	|61000.0
|3	|1023.0	|919.477028	|1625.606804	|97.0	|178.000	|368.0	|1045.0 |30500.0
|4	|990.0	|295.596970	|540.712365	    |64.9	|111.250	|140.0	|210.00	|4690.0
|5	|1023.0	|104.410850	|50.394386     	|46.0	|77.050	    |92.0	|117.50	|546.0
|6	|990.0	|65.534949	|28.660493   	|22.1	|48.925	    |60.0	|76.55	|481.0
|7	|1023.0	|108.447312	|219.942070  	|19.0	|53.500	    |71.0	|112.50	|5270.0
|8	|1023.0	|171.500782	|295.999467 	|29.6	|77.950	    |116.0	|178.00	|5360.0
|9	|985.0	|170.820203	|282.784408	    |37.5	|88.600	    |118.0	|169.00	|5590.0
|10	|992.0	|144.094556	|110.663378	    |59.8	|104.750	|124.0	|152.25	|1910.0
|11	|960.0	|203.198958	|232.211365	    |117.0	|154.000	|174.0	|198.00	|4600.0
|12	|992.0	|331.986895	|1080.358791    |155.0	|190.000	|203.0	|226.00	|28700.0

</center>

4. Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values in your summary.

<center>

|datetime      |High Flows  |  00060_Mean_cd  |      site_no        |
|--------------|------|-----------------|---------------------|                
|1995-03-06 00:00:00+00:00     |30500.0             |A      |09506000|
|2005-02-12 00:00:00+00:00     |35600.0             |A      |09506000|
|1995-02-15 00:00:00+00:00     |45500.0             |A      |09506000|
|1993-02-20 00:00:00+00:00     |61000.0             |A      |09506000|
|1993-01-08 00:00:00+00:00     |63400.0             |A, e   |09506000|

</center>


<center>

|datetime      |Low Flows (cfs)  |  00060_Mean_cd  |      site_no        |
|--------------|------|-----------------|---------------------|                
|2012-07-01 00:00:00+00:00	|19.0	|A	|09506000|
|2012-07-02 00:00:00+00:00	|20.1	|A	|09506000|
|2012-06-30 00:00:00+00:00	|22.1	|A	|09506000|
|2012-06-29 00:00:00+00:00	|22.5	|A	|09506000|
|2012-07-03 00:00:00+00:00	|23.4	|A	|09506000|

</center>

5. Find the highest and lowest flow values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.

<center>

|Month	|Year	|Maximum monthly flow (cfs)|
|-------|-------|----|
|1	|1993	|63400.0|
|2	|1993	|61000.0|
|3	|1995	|30500.0|
|4	|1991	|4690.0|
|5	|1992	|546.0|
|6	|1992	|481.0|
|7	|2021	|5270.0|
|8	|1992	|5360.0|
|9	|2004	|5590.0|
|10|	2010|	1910.0|
|11|	2004|	4600.0|
|12|	2004|	28700.0|

</center>

<center>

|Month |Year	|Minimum monthly flow (cfs)|
|------|--------|----|	
|1	|2003	|158.0|
|2	|1991	|136.0|
|3	|1989	|97.0|
|4	|2018	|64.9|
|5	|2004	|46.0|
|6	|2012	|22.1|
|7	|2012	|19.0|
|8	|2019	|29.6|
|9	|2020	|37.5|
|10|	2020|	59.8|
|11|	2016|	117.0|
|12|	2012|	155.0|

</center>

6. Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. If there are none than increase the %10 window until you have at least one other value and report the date and the new window you used.
   
    There has a total of 2198 historical dates with flows that are within 10% of my week 1 forecast value (200cfs). See more details in the python script.