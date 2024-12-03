import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

data_dict = pickle.load(open('D:\SignLanguageMediapipe\SignLanguageMediapipe\data.pickle', 'rb'))
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

print(data_dict.keys())
print(data_dict)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)
print('{}% of samples were classified correctly!'.format(score * 100))

print("\nClassification Report:")
print(classification_report(y_test, y_predict))

cm = confusion_matrix(y_test, y_predict)
print("\nConfusion Matrix:")
print(cm)

f = open('data.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
