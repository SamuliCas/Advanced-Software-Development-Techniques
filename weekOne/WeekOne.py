import numpy as np
import matplotlib.pyplot as plt

# -Create a matrix named Jungle with 100 rows and 100 columns, 
# where all values are zeros in the beginning. 
Jungle = np.zeros((100,100))
# print("\n",Jungle)

# -Next, create a dictionary "Ernesti" and another dictionary "Kernesti" and in principle
# try to include their data (location of Ernesti or location of Kernesti in the Jungle) 
# in their dictionaries in the program in some convenient way.

Ernesti = {
    "location" : (0,0)
}

Kernesti = {
    "location" :(99,99)
}

# -In the beginning drop Ernesti and Kernesti to the Jungle, where the result is 
# a matrix that has all other elements zeros but now two ones somewhere there 
# (indicating locations of Ernesti and Kernesti in the Jungle), missing each others. 

Jungle[Ernesti["location"][0], Ernesti["location"][1]] = 1
Jungle[Kernesti["location"][0], Kernesti["location"][1]] = 2

print(Jungle)
print(Ernesti)
print(Kernesti)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()