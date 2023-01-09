from pymatgen.io.vasp import Vasprun
import numpy as np

vrun = Vasprun('vasprun.xml')

dielectric_tensor = vrun.epsilon_static

print("")
print("")
print("p44 component is:", (np.linalg.inv(dielectric_tensor)[1,2] - )/)
