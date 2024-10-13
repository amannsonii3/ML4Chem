#%%
import numpy as np
from pyscf import gto, scf
#%%

# Step 1: Define the H2O molecule's geometry (angstroms)
h2o_geometry = '''
O  0.000000  0.000000  0.000000
H  0.000000 -0.757000  0.586000
H  0.000000  0.757000  0.586000
'''

# Step 2: Build the molecule object with STO-3G basis set
# gto - gaussian type orbitals
molecule = gto.M(atom=h2o_geometry, basis='sto-3g', unit='Angstrom')
help(molecule)
#%%
# Step 3: Perform the SCF (Self-Consistent Field) calculation
mf = scf.RHF(molecule)  # Restricted Hartree-Fock calculation for a closed-shell system
mf.kernel()  # Run the SCF iterations
#%%
# Step 4: Access the molecular orbital coefficients and occupation numbers
# Molecular orbital coefficients (C) and occupation numbers
C = mf.mo_coeff       # Coefficients of molecular orbitals (matrix of shape (nbasis, nbasis))
occupation = mf.mo_occ  # Occupation numbers for each molecular orbital (array of length nbasis)
print(C)
print(occupation)
#%%
# Step 5: Construct the density matrix
# The density matrix (P) is constructed as follows:
# P = C * D * C^T, where D is the diagonal matrix of occupation numbers
# P_ij = sum_a (C_ia * C_ja * occupation_a), for each molecular orbital 'a'

# Diagonal matrix of occupation numbers
D = np.diag(occupation)
print(D)
#%%
# Density matrix construction
# P = C * D * C^T
density_matrix = np.dot(C, np.dot(D, C.T))

# Step 6: Print the density matrix
print("Density Matrix (P):")
print(density_matrix)
# %%
from pyscf import dft
molecule2 = gto.M(atom=h2o_geometry, basis='6-31g', unit='Angstrom')
# Perform the DFT calculation with a chosen functional (e.g., B3LYP)

mf2 = dft.RKS(molecule2)  
# Restricted Kohn-Sham DFT for a closed-shell system

mf2.xc = 'b3lyp'         
# Specify the DFT functional (B3LYP in this case)

mf2.kernel()  
#%%
C2 = mf2.mo_coeff     
occupation2 = mf2.mo_occ

print(C2.shape)
print(C2)
print(occupation2.shape)
print(occupation2)
#%%
D2 = np.diag(occupation2)

density_matrix2 = np.dot(C2, np.dot(D2, C2.T))

print("Density Matrix (P2):")
print(density_matrix2)
print(density_matrix2.shape)
# %%