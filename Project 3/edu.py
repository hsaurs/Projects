import pandas as pd
import numpy as np
import pickle


filename = 'Employee.csv'
df = pd.read_csv(filename)

from sklearn.model_selection import train_test_split
train, val = train_test_split(df,test_size=.2, random_state=2)

target = 'LeaveOrNot'
features = df.columns.drop([target,'LeaveOrNot'])

X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

pipe = make_pipeline(
    OrdinalEncoder(),
    RandomForestClassifier(
    max_depth=10,
    max_features=0.6175788433594966,
    n_estimators=152,
    random_state=2
    )
)

clf = pipe.fit(X_train,y_train)

pickle.dump(clf, open('edu.pkl','wb'))