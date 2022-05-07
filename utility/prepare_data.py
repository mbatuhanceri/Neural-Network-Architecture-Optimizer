import pandas as pd
import numpy as np

class PrepareData:
    def __init__(self, path):
        self.df = pd.read_csv(path)

    def divide_data(self):
        df = self.df
        df = df['Open'].values
        df = df.reshape(-1,1)
        dataset_train = np.array(df[:int(df.shape[0]*0.8)])
        dataset_test = np.array(df[int(df.shape[0]*0.8)-50:])
        return dataset_train, dataset_test
        
    def create_my_dataset(df):
        x = []
        y = []
        df_open = df
        for i in range(50,df_open.shape[0]):
            x.append(df_open[i-50:i,0])
            y.append(df_open[i,0])
        x = np.array(x)
        y = np.array(y)
        return x,y


    # def create_dataset(self, column_list):
    #     x = []
    #     y = []
    #     for i in range(50, self.df.shape[0]):
    #         for column in column_list:
    #             x_ = []
    #             y_ = []
    #             df_ = self.df[column]
    #             x_.append(df_[i-50 :i , 0])
    #             y_.append(df_[i, 0])
    #         x.append(x_)
    #         y.append(y_)
    #     np.array(x)
    #     np.array(y)
    #     return x, y

