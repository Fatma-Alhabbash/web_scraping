import requests
from bs4 import BeautifulSoup
import pandas as pd
import math

def get_no_jobs_pages(job):
    response = requests.get('https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q='+job.replace(' ','%20'))
    soup = BeautifulSoup(response.content, 'lxml')
    jobs = int(soup.find({'strong'}).text)
    pages = math.ceil(jobs / 15)
    return jobs, pages

def scrap(path):
    all_titles_lst = []
    all_links_lst = []
    all_occupations_lst = []
    all_companies_lst = []
    all_specs_lst = []
    all_locations_lst = []
    jobs, pages = get_no_jobs_pages(path)
    path = path.replace(' ', '%20')
    for page in range(pages):
        req = requests.get('https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=' + path + '&start=' + str(page))
        content = BeautifulSoup(req.content, 'lxml')
        titles = content.find_all('h2', {'class': 'css-m604qf'})
        titles_lst = [title.a.text for title in titles]
        all_titles_lst += titles_lst

        links_lst = ['https://wuzzuf.net' + title.a['href'].replace(' ', '%20') for title in titles]
        all_links_lst += links_lst

        occupations = content.find_all("div", {'class': 'css-1lh32fc'})
        occupations_lst = [occupation.text for occupation in occupations]
        all_occupations_lst += occupations_lst

        companies = content.find_all("a", {'class': 'css-17s97q8'})
        companies_lst = [company.text.replace(' -', '') for company in companies]
        all_companies_lst += companies_lst

        specs = content.find_all("div", {'class': 'css-y4udm8'})
        specs_lst = [spec.text for spec in specs]
        all_specs_lst += specs_lst

        locations = content.find_all('span', {'class': 'css-5wys0k'})
        locations_lst = [location.text for location in locations]
        all_locations_lst += locations_lst

    scraped_data = {}
    scraped_data['Title'] = all_titles_lst
    scraped_data['Link'] = all_links_lst
    scraped_data['Occupation'] = all_occupations_lst
    scraped_data['Company'] = all_companies_lst
    scraped_data['Specs'] = all_specs_lst
    scraped_data['locations'] = all_locations_lst

    df = pd.DataFrame(scraped_data)
    return scraped_data, df

def df_concat(dfs):
    df = pd.concat(dfs, axis = 0)
    df = df.drop_duplicates()
    return df