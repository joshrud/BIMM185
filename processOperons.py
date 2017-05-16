

"""
+
+	Josh Rudolph
+	BIMM185
+
"""

import sys

def main():

	with open(sys.argv[1], 'r') as rfile:

		data = []
		for line in rfile:
			if "ECK" in line:
				data.append(line.split('\t'))

		print(data[1])










if __name__=="__main__":
	main()