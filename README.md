# web_scraping

## A fully functional EXAMPLE project written in Python showing how to create a simple web scraping project

This project is a simple and useful example of how to create a web scraping program to extract needed information from a website.

In this case, I used web scraping to get job information from a website. I followed these steps to complete the program:

1. The first step is to create the main Python file where all the code exists so that it can be used as a user-built module.

    - I used the ``` BeautifulSoup ``` library to search for content.

    - I used the ``` Pandas ``` library to create a data frame containing all information about specified jobs.

    - ```  get_no_jobs_pages ``` function gets the number of pages containing this job field and the number of jobs each page contains.

    - ``` scrap ``` function is used to scrape information from each page.

    - ``` df_concat ``` function used to create a dataframe of all jobs' information.

    

2. In the second Python file (job_scraping), I import the module to extract information about the specific jobs I want.

    - ``` combined_dfs.to_csv('data.csv', index=False) ``` This part of code saves the dataframe in csv. File.
