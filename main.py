import sys
from nltk.stem.wordnet import WordNetLemmatizer
from utils import (
    clean_text, 
    download_nltk_dependencies, 
    remove_stop_words, 
    lemmatize_words, 
    get_stop_words, 
    shop_categories
)
from gensim.models.doc2vec import Doc2Vec
import pickle
from sklearn.linear_model import LogisticRegression 

def load_model(filepath: str = './models/logistic_regr_model.pkl'):

    with open(filepath, 'rb') as file:
        model = pickle.load(file)
    return model


def load_doc2vec(filepath: str = './models/model.doc2vec'):
    return Doc2Vec.load(filepath)

def predict(prediction_model: LogisticRegression, doc2vec_model: Doc2Vec, input: str):

    stop_words = get_stop_words()
    text = clean_text(words=input)
    text = remove_stop_words(text=text, stop_words=stop_words)
    text = lemmatize_words(text=text, lemma=WordNetLemmatizer())    

    feature = doc2vec_model.infer_vector(text.split(' '))
    prediction = prediction_model.predict(feature.reshape(1, -1)).tolist()[0]

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
    doc2vec = load_doc2vec()
    pred_model = load_model()

    print(f'Following are the shop categories:\n{shop_categories_str}')
    cmnd = input('Start by typing product item and program will recommend the shop. Type Cancel/Exit/Quit to cancel the program:\n')
    cmnd = cmnd.lower()
    while True:
        if cmnd in ['exit', 'cancel', 'quit', 'quit()', 'exit()']:
            print('Quiting the program')
            sys.exit()
        else:
            prediction = predict(pred_model, doc2vec, cmnd)
            print(f'The prediction is: {prediction}')
            cmnd = input('Type new product item for recommendation or quit/cancel/exit to quit the program:\n').lower() 

