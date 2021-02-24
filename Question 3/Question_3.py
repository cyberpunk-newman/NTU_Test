#Question 3, the output is on the github

from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import metrics

a = np.loadtxt('C:/Users/RM.Z/Desktop/NTU/train_data.txt',skiprows=1)
y = np.loadtxt('C:/Users/RM.Z/Desktop/NTU/train_truth.txt',skiprows=1)
c = np.loadtxt('C:/Users/RM.Z/Desktop/NTU/test_data.txt',skiprows=1)

x = a[:,0:3]     #get the 1-3 column from a
z = c[:,0:3]    #test_data.txt

# standardize the data
scalex = preprocessing.StandardScaler(with_mean=True,with_std=True)
x = scalex.fit_transform(x)
scalez = preprocessing.StandardScaler(with_mean=True,with_std=True)
z = scalez.fit_transform(z)

# data segmentation 
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)
X_train = X_train.reshape(-1,3)
print(X_train.shape)
X_test = X_test.reshape(-1,3)
print(X_test.shape)
Y_train = Y_train
Y_test = Y_test

# 2 layers, each layer has 4 neurons
model_mlp = MLPRegressor(
    hidden_layer_sizes=(4,4),  activation='relu', solver='adam', alpha=0.0001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=5000, shuffle=True,
    random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False,beta_1=0.9, beta_2=0.999, epsilon=1e-08)

model_mlp.fit(X_train, Y_train)

# visualized loss function
plt.figure()
plt.plot(model_mlp.loss_curve_)
plt.xlabel("iters")
plt.ylabel(model_mlp.loss)
plt.show()

# test model on test set
prediction_Y = model_mlp.predict(X_test)
print("mean absolute error:", metrics.mean_absolute_error(Y_test,prediction_Y))
print("mean squared error:", metrics.mean_squared_error(Y_test,prediction_Y))

# R^2 on train/test set
print("R^2 on train set:",model_mlp.score(X_train,Y_train))
print("R^2 on test set:",model_mlp.score(X_test,Y_test))

# test test_data.txt
prediction_Y = model_mlp.predict(z)
print(prediction_Y)
np.savetxt('C:/Users/RM.Z/Desktop/NTU/test_predicted.txt',prediction_Y)

