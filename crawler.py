from typing import List
from bs4 import BeautifulSoup
import requests
import pandas as pd

class CrawlJioMart:

    def __init__(self, category_page_url: str = "https://www.jiomart.com/all-category"):
        self.category_page_url = category_page_url

    
    def crawl_category_page(self, css_selector: str = 'a[data-category*=""]'):
        page_data = requests.get(self.category_page_url).content
        soup = BeautifulSoup(page_data, 'lxml')

        all_cat = soup.select(css_selector)

        category = []
        sub_category = []
        href = []
        for cat in all_cat:
            category.append(cat['data-category'])
            sub_category.append(cat['data-subcategory'])
            href.append(cat['href'])

        df = pd.DataFrame({'category': category, 'sub_category': sub_category, 'href': href})

        return df 

    
    @staticmethod
    def crawl_all_item_pages(item_page_url: str, attr: str = 'span', class_name: str = 'clsgetname') -> List:

        item_description = []
        while True:
            page_data = requests.get(item_page_url).content
            soup = BeautifulSoup(page_data, 'lxml')
            items = soup.find_all(attr, class_=class_name)
            for item in items:
                item_description.append(item.get_text())
            print(f'Extracted items from url: {item_page_url}')

            # get next page link
            try:
                item_page_url = soup.find_all('li', class_='next')[0].find('a')['href']
            except:
                break
        
        return item_description

    
    def crawl_all_items(self) -> pd.DataFrame:

        category_df = self.crawl_category_page()
        category_df['items'] = category_df['href'].apply(lambda x: self.crawl_all_item_pages(item_page_url=x))
        category_df = category_df.explode('items')

        print(f'Extracted a dataframe of shape: {category_df.shape}')
        return category_df
        