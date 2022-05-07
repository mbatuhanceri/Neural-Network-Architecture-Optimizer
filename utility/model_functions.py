from pyexpat import model
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout

class ModelBase:
    def __init__(self, inp_shape):
        model = Sequential()
        model.add(Dense(units=16, input_shape = inp_shape))
        model.add(Dense(units=1))
        model.summary()
