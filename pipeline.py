import time
from crawler import CrawlJioMart
from utils import logtime

@logtime
def save_jio_mart_items(file_name: str = "jio_mart_items.parquet") -> None:

    crawler = CrawlJioMart()
    df = crawler.crawl_all_items()

    df.to_parquet(f'./data/{file_name}')
    print(f'Jio mart items file saved to disk at: ./data/{file_name}')

    return None

def save_items(site: str = 'jio_mart') -> None:

    if site == 'jio_mart':
        save_jio_mart_items()
    
    return None


if __name__ == '__main__':

    st = time.time()
    save_items()
    et = time.time()

    # takes roughly 1 hour to extract 150k items
    # TODO: explore asyncio to make api calling faster
    print(f'Total time elapsed: {et-st} seconds') 
