# IPL-Data-Scraping-Live-Scorecard
Web scraping live IPL scorecard from [iplt20.com](https://www.iplt20.com/) to a csv file which can be used further to calculate fantasy points or make datasets

### About
The data in live score card of a running ipl match or complete scorecard of finished ipl match is stored in a csv file which can be used further to calculate fantasy points or make datasets. 

Website scraped is iplt20.com, in particular for a match it is https://www.iplt20.com/match/2021/51?tab=scorecard

Website Scorecard:

<img src="https://user-images.githubusercontent.com/47270916/136180633-90302439-5907-4cbb-a627-e770724bd8ec.png" width="600">

Final CSV file:

<img src="https://user-images.githubusercontent.com/47270916/136181445-6b508fad-8e1f-434a-801c-b24453cb6f5a.png" width="500">

### Idea
- Using beautiful soup python package to select, navigate, filter, delete and get text from html doc
- Manually copy pasted the entire HTML from inspect element tool in the webpage of the match.  (because some web pages fill in the inspect element html data using Javascript, and what appears to be the page content is not actually in the HTML that Beautiful Soup is processing. This is one of those pages). Later I will try to automate this process too using 'requests-html' library as suggested [here](https://stackoverflow.com/a/53754005/12705907).
- Accessed the html file through beautiful soup
- Went through the html code to see where the scorecard tables are present and navigated to it through beautiful soup. 
- Converted each html table in the selected div to list data type and further converted it to csv file through pandas


### Resources
1. Beautiful Soup documentation
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

###### Further improvements will be made soon
