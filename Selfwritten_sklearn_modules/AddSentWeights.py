"""This class provides a transformer for Sci-kit learn that takes a lexicon with features 
and weights, and a matrix with counted words. It then multiplies all the counts of the 
features with the corresponding weight if the weight is positive or negative, and divides
the count of features whose weight is 0 by 1000"""


from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import scipy.sparse
import pandas as pd

class AddSentWeights(BaseEstimator, TransformerMixin):
    lexicon = []
    def get_lexicon(self):
        return self.lexicon
    def __init__(self, df):
        self.df = df
        weights = np.asarray(self.df.iloc[:,1])
        for i in range (0, len(weights)):
            if weights[i] == 0:
                weights[i] = 0.001
        self.lexicon = scipy.sparse.csr_matrix(weights)


    def fit(self, X, y=0):
        return X

    def transform(self, X):
        return X.multiply(self.lexicon)