import pandas as pd


df = pd.read_csv("C:/Users/raghu/FalseAWSKeyDataset.csv")
df.head()

categories = ['Invalid','Valid']

train_x = df.Data
train_y = df.Label
test = df.Data

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
model = make_pipeline(TfidfVectorizer(),MultinomialNB())

model.fit(train_x.astype('U'),train_y.astype('U'))

labels = model.predict(test.astype('U'))

from sklearn.metrics import accuracy_score
print(accuracy_score(train_y.astype('U'),labels.astype('U')))

def predict_category(s,train=df,model=model):
  pred = model.predict([s])
  print(pred)

predict_category("BloombergTickerRatesFromBuilderComponent")

