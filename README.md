# Product Categorization

`main.py` file contains the recommendation program. Once started it will show the available shop categories. It will then prompt user to input product item and based on that it will recommend the shop. See the following example below:

```
mohitlakshya@mohitLenovo:product-categorization:(develop)$ python3 main.py
Downloading nltk dependencies, these are downloaded only once

Following are the shop categories:
1. vegetable_shop
2. dairy_shop
3. kirana_shop
4. pharamacy_shop
5. other_shop
6. cloth_shop
7. stationary_shop
8. furniture_shop
9. electronics_shop
10. sports_shop
11. hardware_shop
12. mobile_shop
13. beauty_shop
14. jewellery_shop

Start by typing product item and program will recommend the shop. Type Cancel/Exit/Quit to cancel the program:
jeans pant
The prediction is: cloth_shop
Type new product item for recommendation or quit/cancel/exit to quit the program:
quit()
Quiting the program
```

## Data Preparation

Training data was crawled from *jio-mart* website. For multiple product categories, product items name were downloaded from the website. Associated files are `crawler.py` which hits the *jio-mart* website and fetches product information and then `pipeline.py` converts that data into a `parquet` file and stores in `./data`. Product categories are further classified into shops

## Modelling

Machine learning models are trained in `model.ipynb` file. The best machine learning model is selected after doing grid search across different algorithms namely: *random forest classifier*, *support vector classifier*, *logistic regression*, *decision tree classifier*, *knn classifier* and *multinomial naive bayes classifier*. Currently best classifier is selected without any hyper-parameter tuning on different algorithms.

Currently the best algorithm seems to be *Support vector classifier* with `f1-score=0.98`. 

To handle class imbalances *SMOTE* technique is applied. 

The selected best model is stored in `./models` with the name `grid_search_best_model.pkl`.

### Limitation

The class imbalance seems to affect the model adversely and often times for unseen products the model seems to predict most popular class (shop with maximum number of product items). With further hyper parameter tuning and trying different sampling technique (namely: under-sampling), the model can probably be improved.