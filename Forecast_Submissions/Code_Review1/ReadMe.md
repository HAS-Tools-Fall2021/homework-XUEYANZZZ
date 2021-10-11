<center>

### Xueyan Zhang
### 10/10/2021
### Assignment 7

</center>

</br>

### Code instruction
- Just run the script because this is no need to revise streamflow data; however, some code may be not as efficient and effective as we expected. Therefore, please leave your revision or suggestions at the end of this file.
- You will see three plots generated after the run, which will be used in this markdown file.
- Go through the generated plots and have a sense of what the flow will be for next week (hint: we know the October mean and the evolution trend of October flow this year; then guess a value).
- Fill all blanks.
</br>

### Forecast
We generated three plots as follows:
- First plot: observed October flow during 2010-2021. Here we showed only flows after 2010 because climate change greatly affect streamflow


- Second plot: histogram of October flow during all past years with a mean of 130.7 cfs


- Third plot: Weekly mean flow (day 10-16) in October during 1989-2020. We can see increasing variabilities of weekly mean flow during day 10-16, especially after 2010, which supports our choice in the first plot.
  
  
- Therefore, we forecasted weekly mean for next week and two weeks laters should be () and () cfs, respectively. 
</br>

### Code revision or suggestion
- First, Is the script easy to read and understand?
Are variables and functions named descriptively when useful?

Are the comments helpful?

Can you run the script on your own easily?

Are the doc-strings useful?

Yes, all definitions are clear and meaning. The comments well explained why, what, and how to do the flow forecast. The script is well written!

10/10
- Second, Does the code follow PEP8 style consistently?
If not are there specific instances where the script diverges from this style?

Linter does not find any errors through the whole manuscript!

10/10
- Third, Is the code written elegantly without decreasing readability?

No superfluous code was found. The function is essentially the forecast method used in this assignment with good explanation. The author proposed that 1-week and 2-week forecast can be decomposed into mean and mode of corresponding weeks. Moreover, the relaionship of September flow between 2020 and 2021 is the same as Ocotber between these two years.

One suggestion is that moving self-defined functions at the begining of the script (after import).

10/10