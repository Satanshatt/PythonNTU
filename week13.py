import numpy as np
import keras
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
from keras import optimizers
from keras.callbacks import EarlyStopping
import tensorflow as tf
from tensorflow.keras.optimizers import Adam

# Set the number of epochs
epoch = 40
# Download historical stock data for ^TWII from Yahoo Finance
data_or = yf.download('^TWII',start='2010-01-01',end='2023-11-17')
# Drop missing values
data_or = data_or.dropna()
# Extract the 'Close' prices and convert to numpy array
data_c = np.array(data_or[['Close']])

# Set the length of the test dataset
test_len = 40
# Create training dataset
train_data_c = np.array(data_c[:len(data_c)-test_len])
# Create test dataset and a copy for later reference
test_data_c = np.array(data_c[:])
real_test_data_c = test_data_c
print("Train_close_shape: ",train_data_c.shape)

# Triple Barrier Labeling
# triple_barrier list is used to encode certain events or conditions (1, 2, or 0) based on the movement of values in the train_data_c array relative to dynamically calculated upper and lower barriers.
# 1 is appended when the price movement surpasses the upper barrier, 2 is appended when the price movement falls below the lower barrier, other conditions append 0
triple_barrier = []
for i in range(len(train_data_c)):
        if (i+20)>len(train_data_c):
            ub = train_data_c[i]*1.04
            lb = train_data_c[i]*0.98
            for j in range(i,len(train_data_c)-1):
                if train_data_c[j] > ub:
                    triple_barrier.append(1)
                    break
                elif train_data_c[j] < lb:
                    triple_barrier.append(2)
                    break
                if j == (i+20-1):
                    triple_barrier.append(0)
        else:
            ub = train_data_c[i]*1.04
            lb = train_data_c[i]*0.98
            for j in range(i,i+20):
                if train_data_c[j] > ub:
                    triple_barrier.append(1)
                    break
                elif train_data_c[j] < lb:
                    triple_barrier.append(2)
                    break
                if j == (i+20-1):
                    triple_barrier.append(0)

# Min-Max scaling of features
# Each feature has been scaled, with its minimum value becoming 0 and its maximum value becoming 1. The data is scaled to the range [0,1].
sc = MinMaxScaler(feature_range=(0,1))
train_data_c = sc.fit_transform(train_data_c)

# Prepare input features and target variable for training
x_train_c = []
y_trian_c = []
for a in range(40,len(train_data_c)):
    x_train_c.append(train_data_c[a-40:a])
    y_trian_c.append(train_data_c[a])
x_train_c = np.array(x_train_c)
y_trian_c = np.array(y_trian_c)

# Display the shapes of training features and target variable
print("X_train_shape: ",x_train_c.shape)
print("Y_train_shape: ",y_trian_c.shape)

# Define the LSTM model
model_c = keras.models.Sequential()
model_c = keras.Sequential()
model_c.add(keras.layers.LSTM(units=50,return_sequences=True,input_shape=(40,1)))
model_c.add(keras.layers.Dropout(0.2))
model_c.add(keras.layers.LSTM(units=70,return_sequences=True))
model_c.add(keras.layers.Dropout(0.2))
model_c.add(keras.layers.LSTM(units=90,return_sequences=False))
model_c.add(keras.layers.Dropout(0.2))
model_c.add(keras.layers.LSTM(units=60))
model_c.add(keras.layers.Dropout(0.4))

model_c.add(keras.layers.Dense(1))

# Compile the model
model_c.compile(optimizer='adam',loss='mean_squared_error')
# Display the model summary
model_c.summary()
# Set the condition of early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
# Train the model
model_c.fit(x_train_c, y_trian_c, batch_size=16, epochs=epoch, validation_split=0.2, callbacks=[early_stopping])
# Save the trained model
model_c.save('my_model_c_1.h5')

# Load the best model
best_model = keras.models.load_model('my_model_c_1.h5')
# Min-Max scaling of the test dataset
total_data_c = sc.fit_transform(test_data_c)

# Prepare input features for testing
x_test_c = []
for a in range(40,len(total_data_c)):
    x_test_c.append(total_data_c[a-40:a,0])
x_test_c = np.array(x_test_c)
x_test_c = np.reshape(x_test_c,(x_test_c.shape[0],x_test_c.shape[1],1))

# Make predictions on the test dataset
pred_price_c = best_model.predict(x_test_c)
# Invert the scaling to get the predicted prices in the original scale
pred_price_c = sc.inverse_transform(pred_price_c)

# Display the shapes of the test dataset and predicted prices
print("X_test_shape: ",x_test_c.shape)
print("Y_pred_close: \n",pred_price_c[0:10])

# Fig 1
# Create a new DataFrame for visualization
data_or_new = data_or[40:]
data_or_new['Close Predict'] = pred_price_c

# Plot the predicted prices against the actual prices
plt.figure(figsize=(20,10))
plt.plot(data_or_new['Close Predict'][-500:], label='Predict')
plt.plot(data_or_new['Close'][-500:], label='actual')
plt.legend()
plt.savefig('result.jpg')

# Fig 2
# plot the loss curve
plt.figure(figsize=(20,10))
plt.plot(model_c.history.history['loss'], label='Training Loss')
plt.plot(model_c.history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()