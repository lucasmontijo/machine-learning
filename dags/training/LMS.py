from sklearn.base import BaseEstimator
from sklearn import linear_model


class LMSTrainer(BaseEstimator):
    
    
    def __init__(self, analytic=False):
            self.analytic = analytic
            self._trained = False
            
    def fit(self, X, y=None):
        
        if self.analytic:
          model = linear_model.LinearRegression()
          model.fit(X, y)
          self.model = model

        else:
           
          # TODO: FAZERPELO GRADIENTE DESCENDETE 
          pass
    
        self._trained = True

        return self
        
    def predict(self, X):
        
        if not self._trained:
           raise RuntimeError("You must train classifer before predicting data!")
        
        return self.model.predict(X)  