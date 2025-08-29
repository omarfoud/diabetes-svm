import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm 
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

diabetes = pd.read_csv('diabetes.csv')

diabetes.head()

diabetes.shape
diabetes.isnull().sum()
diabetes.describe()

X = diabetes.drop('Outcome', axis=1)
y = diabetes['Outcome']

scaler = StandardScaler()
scaler.fit(X)

standardized_data = scaler.transform(X)

X = standardized_data
y = diabetes['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y,random_state=2)

svm = svm.SVC(kernel='linear')
svm.fit(X_train, y_train)

y_train_pred = svm.predict(X_train)
y_pred = svm.predict(X_test)

print("\nTraining Set Performance")
print("-" * 50)
print(f"Accuracy: {accuracy_score(y_train, y_train_pred):.4f}")

print("\nTest Set Performance")
print("-" * 50)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")



new_data = np.array([[1, 85, 66, 29, 0, 26.6, 0.351, 31]])
new_data=np.asarray(new_data)
new_data = new_data.reshape(1, -1)
new_data = scaler.transform(new_data)
prediction = svm.predict(new_data)
print("\nPrediction:")
print(prediction)
print("-" * 50)
print("Diabetes" if prediction[0] == 1 else "No Diabetes")

