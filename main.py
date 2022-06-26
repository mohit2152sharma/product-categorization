import sys
import joblib
from nltk.stem.wordnet import WordNetLemmatizer
from utils import (
    clean_text, 
    download_nltk_dependencies, 
    remove_stop_words, 
    lemmatize_words, 
    get_stop_words, 
    shop_categories
)

def load_model(filepath: str):
    return joblib.load(filepath)

def predict(prediction_model, input: str):

    stop_words = get_stop_words()
    text = clean_text(words=input)
    text = remove_stop_words(text=text, stop_words=stop_words)
    text = lemmatize_words(text=text, lemma=WordNetLemmatizer())    

    prediction = prediction_model.predict(text.split(' ')).tolist()[0]

    return prediction

def create_shop_categories_str() -> str:
    shops = shop_categories()
    shop_str = ""
    for i, shop in enumerate(shops):
        shop_str += f'{i+1}. {shop}\n'

    return shop_str


if __name__=="__main__":

    shop_categories_str = create_shop_categories_str()
    download_nltk_dependencies()
    pred_model = load_model(filepath = './models/grid_search_best_model.pkl')

    print(f'\nFollowing are the shop categories:\n{shop_categories_str}')
    cmnd = input('Start by typing product item and program will recommend the shop. Type Cancel/Exit/Quit to cancel the program:\n')
    cmnd = cmnd.lower()
    while True:
        if cmnd in ['exit', 'cancel', 'quit', 'quit()', 'exit()']:
            print('Quiting the program')
            sys.exit()
        else:
            prediction = predict(pred_model, cmnd)
            print(f'The prediction is: {prediction}')
            cmnd = input('Type new product item for recommendation or quit/cancel/exit to quit the program:\n').lower() 

