# importing some standard libraries
import numpy as np
from sklearn.metrics import r2_score


# function for metric evaluation
class metrics_for_continuous_target:

    def __init__(self, y_true, y_pred, _filter=None):
        self.y_true = y_true
        self.y_pred = y_pred
        self.Filter = _filter
        
    def MAPE(self): 
        """
        Mean_absolute_percentage_error
        :return:
        """
        y_true, y_pred = np.array(self.y_true), np.array(self.y_pred)
        # todo: y_true should not be equal to zero
        # np.array([i for i in y_true 1 if i==0 else i])

        return np.round(np.mean(np.abs(y_true - y_pred) / (y_true + 0.0001)) * 100, 4)

    def SMAPE(self): 

        """
        Symmetric_mean_absolute_percentage_error
        :return:
        """
        y_true, y_pred = np.array(self.y_true), np.array(self.y_pred)
        return np.round(100/len(y_true) * np.sum(2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred))), 4)
    
    def MAE(self):
        """
        Mean_absolute_error
        :return:
        """
        y_true, y_pred = np.array(self.y_true), np.array(self.y_pred)
        return np.round(np.sum(abs(y_true-y_pred))/len(y_true), 4)
    
    def RMSE(self):
        """
        Root mean squared error
        :return:
        """
        y_true, y_pred = np.array(self.y_true), np.array(self.y_pred)
        return np.round(np.sqrt(np.sum((y_true-y_pred)**2)/len(y_true)),4)
    
    def R2_Score(self):
       """
       R Squared value
       :return:
       """
       return np.round(r2_score(self.y_true, self.y_pred), 4)
        
    def metric_dataframe(self, method):
        import pandas as pd
        metric = [self.R2_Score.__name__, self.MAE.__name__, self.RMSE.__name__, self.SMAPE.__name__]
        value = [self.R2_Score(), self.MAE(), self.RMSE(), self.SMAPE()]
        df = pd.DataFrame({'Metric': metric, method: value})
        return df
