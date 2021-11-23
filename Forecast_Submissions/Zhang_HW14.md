### Xueyan Zhang
### Assignment 14
### 11/28/2021
</br>

1. What is the paper or project you picked? Include a title, a link the the paper and a 1-2 sentence summary of what its about.
* Title: Global terrestrial water storage and drought severity under climate change
* Paper link: https://www.nature.com/articles/s41558-020-00972-w#data-availability
* This paper assessed future drought severity based on modelled terrestrial water storage. They found a highly agreement on that future drought is dominated by climate change among models, rather than land and water management activities.
2. What codes and/or data are associated with this paper? Provide any link to the codes and datasets and a 1-2 sentence summary of what was included with the paper (i.e. was it a github repo? A python package?A database? Where was it stored and how?)
* Raw data link: https://www.isimip.org/outputdata/; http://www2.csr.utexas.edu/grace/; and https://podaac.jpl.nasa.gov/GRACE
* Processed data link: https://doi.org/10.6084/m9.figshare.13218710 on CUAHSI HydroShare and Figshare 
* Code link:https://doi.org/10.5281/zenodo.4266999 on zenodo.
* Summary: Because of the large amount of raw data, they just provided raw data links. And they also provided the link of processed data used in their plots. The code to process the results and develop the figures is a compressed zip file. 
3. Summarize your experience trying to understand the repo: Was their readme helpful? How was their organization? What about documentation within the code itself?
* Their readme file has no helpful information!
* The code folder includes five python files for each figure in their paper. Overall, the organiztion is simple!
4. Summarize your experience trying to work with their repo: What happened when you tried to run it? Where you successful? Why or why not?
* First, I need to install many python packages; however, that is not the worst part. They used their own packages and imported them. But they did not provide the files of their own packages.
* When I tried to run the code, I ran into the first issue of missing packages. And I tried to install those packages because they may conflict with my current libraies or packages and I did not install it successfully.
* Also, the code almost has no comments so it probably will take more than three hours to understand what the code is doing for and run it!
5. Summarize your experience working with the data associated with this research. Could you access the data? Where was it? Did it have a DOI? What format was it in?
* They provided data with nc and xlsx formats. The data was available on CUAHSI HydroShare with a DOI. 
* The nc file is easily understood because it has explantory information with data; however, their xlxs files did not have any real infomration, which are just a bunch of numbers.
6. Did this experience teach you anything about your own repo or projects? What suggestions would you give to the authors for how they could do better next time?
* Yes, I do learn something about how to make a well-exaplined repo. 
* First, we need to have a infomrational readme, rather a line saying that this is used to generate figures. We could say which environment and system required, like which version of python will be used.
* Second, please comment every important steps!
* Self-defined Functions should have a good help document!
* Third, the author may list all the packages used in the code to a txt or readme file so we can know what to do ahead!