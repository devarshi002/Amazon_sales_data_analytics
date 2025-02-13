import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon.csv")
df.info()
df.describe()
df.columns()