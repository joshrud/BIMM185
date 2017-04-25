"""
+
+	Josh Rudolph
+	BIMM185
+	processing data from ex3 from class
+	takes in data from ex3 CUIs and creates histogram
+	histogramapr18.py
+	
+
+
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

with open(sys.argv[1], 'r') as rfile:

	data = []
	for line in rfile:
		data.append(line.rstrip('\n').split('\t')[1])

# print(data[:10])
# npData = np.array(data)

x = np.random.normal(size = 1000)
plt.hist(x, bins=30)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel('Probability');
plt.show()

