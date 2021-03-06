from urllib import request
import pandas as pd 
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import sys

urls = ['http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.hungarian.data',
        'http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data',
        'http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.switzerland.data',
        'http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.va.data']

# urls = ['http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data']


with open('heart.csv', 'w') as file:
    for url in urls:
        with request.urlopen(url) as response:
            for line in response.read().decode('utf-8'):
                file.write(line)
sys.exit()

df = pd.read_csv('heart.csv', header=None)
df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
              'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
df['has_disease'] = df.num.apply(lambda v: v != 0)

# zero_zips = df['Incident Zip'] == '00000'
# requests['Incident Zip'][zero_zips] = np.nan


y = df.has_disease
X = df.drop(['num', 'has_disease', 'ca', 'thal'], axis=1)

# initial run making sure it works
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# model = GradientBoostingClassifier().fit(X_train, y_train)
# print(model.score(X_test, y_test))

# commented out since we already have our predictor
# cv = KFold(n_splits=10)
# accuracy = []
# for estimator in range(100, 1000, 100):
#     for depth in range(1, 4):
#         for sample in (0.1, 0.3, 0.5, 0.7, 0.9):
#             model = GradientBoostingClassifier(n_estimators=estimator, max_depth=depth, subsample=sample)
#             scores = []
#             for train_i, test_i in cv.split(X):
#                 # Xr, yr, Xt, yt = X.loc[train_i], y.loc[train_i], X.loc[test_i], y.loc[test_i]
#                 Xr, yr, Xt, yt = X.loc[train_i], y.loc[train_i], X.loc[test_i], y.loc[test_i]
#                 model.fit(Xr, yr)
#                 scores.append(model.score(Xt, yt))
#                 accuracy = sum(scores) / len(scores)
#             print('sample:', sample, 'depth:', depth, 'estimators:', estimator, 'accuracy:', sum(scores) / len(scores))
# print(accuracy.max)

# best hyperparameters
# sample: 0.5 depth: 1 estimators: 100 accuracy: 0.808817204301
model = GradientBoostingClassifier(
    n_estimators=100, max_depth=1, subsample=0.9).fit(X, y)

joblib.dump(model, 'model.pkl')
