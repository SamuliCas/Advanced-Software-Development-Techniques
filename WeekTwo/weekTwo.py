import numpy as np

Space = np.zeros((100,100))

ErnestiRocket = {
    "location" : (0,99)
}

KernestiRocket = {
    "location" :(99,0)
}

Space[ErnestiRocket["location"][0], ErnestiRocket["location"][1]] = 1
Space[KernestiRocket["location"][0], KernestiRocket["location"][1]] = 2


print(Space)
print(ErnestiRocket)
print(KernestiRocket)