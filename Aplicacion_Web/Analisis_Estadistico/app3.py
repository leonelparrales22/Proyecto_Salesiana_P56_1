import pandas as pd
import json
data = pd.read_csv('files/pronostico.csv', sep=',')
data = data.values
y = []
for x in data:
    y.append({"dia": int(x[0] + 1), "valor": "{:.2f}".format(x[1])})

y = json.dumps(y)
print(y)
