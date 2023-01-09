from pymatgen.io.vasp import Vasprun
import numpy as np

vrun = Vasprun('vasprun.xml')

dielectric_tensor = vrun.epsilon_static

print("")
print("")
print("Static dielectric tensor:")
print((dielectric_tensor))