# -*- coding: utf-8 -*-
"""Copy of CFD_A1_Q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Caa2y70vNYEpWe4jN2hnZf-XH9Z4BABi
"""

print("hello")

import pandas as pd

# Read the fixed width file using delim_whitespace
df = pd.read_csv("/content/fdmq1sol (1).txt",delim_whitespace=True)

# Save the DataFrame to a CSV file
df.to_csv("/content/fdmq1sol (1).txt", index=False)

import matplotlib.pyplot as plt
dataframe = pd.read_csv("/content/fdmq1sol (1).txt")

#Plotting x and Y labels
plt.plot(dataframe.iloc[:,0],dataframe.iloc[:,1])

plt.xlabel( "Nodes")
plt.ylabel( "Temperature")
plt.show()

"""# New Section"""