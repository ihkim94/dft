from fileinput import filename
from pymatgen.io.vasp import Poscar

poscar = Poscar.from_file("CONTCAR")
structure = poscar.structure
# primi_structure = structure.get_primitive_structure()
# structure[0] = "Ba", [0.1, 0, 0]

print()
print("The original strucutre before the perturbations to calculate the Raman susceptibility: ")
print()
print(structure)

# Generating the atomic displacements along x-direction for all atoms
for i in range(0, len(structure.sites)):
    poscar = Poscar.from_file("CONTCAR") # Initialize the original structure, otherwise the displacements are gonna accumulate
    structure = poscar.structure
    delta = 0.005 # Amount of perturbation in the unit of Angstrom
    structure.translate_sites(i, [delta, 0, 0], False, False)
    structure.to(filename=f'POSCAR_x_plus_{i+1:02d}')

for i in range(0, len(structure.sites)):
    poscar = Poscar.from_file("CONTCAR") # Initialize the original structure, otherwise the displacements are gonna accumulate
    structure = poscar.structure
    delta = -0.005 # Amount of perturbation in the unit of Angstrom
    structure.translate_sites(i, [delta, 0, 0], False, False)
    structure.to(filename=f'POSCAR_x_minus_{i+1:02d}')

# Generating the atomic displacements along y-direction for all atoms

for i in range(0, len(structure.sites)):
    poscar = Poscar.from_file("CONTCAR") # Initialize the original structure, otherwise the displacements are gonna accumulate
    structure = poscar.structure
    delta = 0.005 # Amount of perturbation in the unit of Angstrom
    structure.translate_sites(i, [0, delta, 0], False, False)
    structure.to(filename=f'POSCAR_y_plus_{i+1:02d}')

for i in range(0, len(structure.sites)):
    poscar = Poscar.from_file("CONTCAR") # Initialize the original structure, otherwise the displacements are gonna accumulate
    structure = poscar.structure
    delta = -0.005 # Amount of perturbation in the unit of Angstrom
    structure.translate_sites(i, [0, delta, 0], False, False)
    structure.to(filename=f'POSCAR_y_minus_{i+1:02d}')

# Generating the atomic displacements along z-direction for all atoms
for i in range(0, len(structure.sites)):
    poscar = Poscar.from_file("CONTCAR") # Initialize the original structure, otherwise the displacements are gonna accumulate
    structure = poscar.structure
    delta = 0.005 # Amount of perturbation in the unit of Angstrom
    structure.translate_sites(i, [0, 0, delta], False, False)
    structure.to(filename=f'POSCAR_z_plus_{i+1:02d}')

for i in range(0, len(structure.sites)):
    poscar = Poscar.from_file("CONTCAR") # Initialize the original structure, otherwise the displacements are gonna accumulate
    structure = poscar.structure
    delta = -0.005 # Amount of perturbation in the unit of Angstrom
    structure.translate_sites(i, [0, 0, delta], False, False)
    structure.to(filename=f'POSCAR_z_minus_{i+1:02d}')
