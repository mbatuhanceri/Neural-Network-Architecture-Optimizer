import imp
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout

from utility.prepare_data import PrepareData
from utility.model_functions import ModelBase

path_ltc = r'C:\Users\iceri\Desktop\batu\auto_model_optimizer\data\LTC-USD.csv'
column_list = ['Open', 'High', 'Low', 'Close', 'Adj', 'Close', 'Volume']

def Main():
    df_ltc = PrepareData(path_ltc)
    dataset_train, dataset_test = df_ltc.divide_data()
    
    


        


if __name__ == '__main__':
    Main()