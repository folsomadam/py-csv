import pandas as pd

df = pd.read_csv (r'/home/afolsom/invest.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
df.to_json (r'/home/afolsom/invest.json')
print (df.to_json.ticker.[0])

