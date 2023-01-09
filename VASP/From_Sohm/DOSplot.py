"""
Plots DOS as calculated by VASP.
"""
import pyprocar

pyprocar.dosplot(mode='stack_species', savefig='dos.pdf', title='SBN-60 Density of States')
