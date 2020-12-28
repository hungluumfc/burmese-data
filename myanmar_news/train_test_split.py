import csv
from sklearn.model_selection import train_test_split

X, y = [], []
with open("topics.csv", encoding="utf-8") as f:
    rdr = csv.reader(f, delimiter="\t")
    next(rdr)
    rownum = 0
    for row in rdr:
        rownum += 1
        X.append(row[0])
        y.append(row[1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)
with open("train.txt", 'w', encoding="utf-8", newline='') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for text, category in zip(X_train, y_train):
        writer.writerow([text, category])

with open("test.txt", 'w', encoding="utf-8", newline='') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for text, category in zip(X_test, y_test):
        writer.writerow([text, category])