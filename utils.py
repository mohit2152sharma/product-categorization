import nltk
import pandas as pd
from typing import List
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import re
import time
from functools import wraps

def logtime(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Entering function: {func.__name__}')
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        print(f'Exiting function: {func.__name__}')
        print(f'{func.__name__} took {et - st} seconds')

        return result 
    return wrapper

def clean_text(words: str) -> str:
    words = re.sub('[^a-zA-Z]', " ", words)
    text = words.lower().split()
    return " ".join(text)

def remove_stop_words(text: str, stop_words: List) -> str:
    clean_text = [word.lower() for word in text.split() if word.lower() not in stop_words]
    return " ".join(clean_text)

def lemmatize_words(text: str, lemma: WordNetLemmatizer) -> str:
    lem_text = [lemma.lemmatize(word) for word in text.split()]
    return " ".join(lem_text)

def get_stop_words(new_words: List = ["approx", "g", "pc"]) -> List:
    words = stopwords.words('english')
    words.extend(new_words)
    return words 
    
def shop_categories(df_path: str = './data/jio_mart_items_cleaned.parquet', shop_column_name: str = 'shop') -> List[str]:
    """reads the shop categories from cleaned product item dataframe

    Args:
        df_path (str): cleaned dataframe location to read
        shop_column_name (str): name of the column with shop categories

    Returns:
        List[str]: shop categories 
    """
    df = pd.read_parquet(df_path)    
    return df[shop_column_name].unique().tolist()

def download_nltk_dependencies() -> None:
    print('Downloading nltk dependencies, these are downloaded only once')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('stopwords')
    nltk.download('punkt')