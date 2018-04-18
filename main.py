# Decision Tree Classification
#can't be assed to use argv.
# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from multipleImages import multipleImageLoader

reshapedImagesWithClassInTheEndColumn = multipleImageLoader('human', 'car')

X = reshapedImagesWithClassInTheEndColumn[:,:-1]
y = reshapedImagesWithClassInTheEndColumn[:,reshapedImagesWithClassInTheEndColumn.shape[1]-1]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


df_cm = pd.DataFrame(cm, index = [i for i in ("Car","Human")],
                  columns = [i for i in ("Car","Human")])
plt.figure(figsize = (5,3))
sn.heatmap(df_cm, annot=True)


