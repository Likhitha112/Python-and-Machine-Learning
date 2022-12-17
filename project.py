import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten
(X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()
X_test.shape
