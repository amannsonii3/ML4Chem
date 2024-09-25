# %%
from aseMolec import pltProps as pp
from ase.io import read
import matplotlib.pyplot as plt
from aseMolec import extAtoms as ea 
import numpy as np

# %%
file1 = 'mace_solvent_xtb_output.xyz'  # MACE_eval_output
file2 = 'mace_solvent_xtb_output.xyz'  # test_dataset
db1 = read(file1, ':')
db2 = read(file2, ':')

# print(type(db1))
# print(type(db1[10])) # molecule configuration
# print(type(db1[10][0])) # each atom in that molecule configuration

#%%
print(len(db1))
print(len(db1[10])) # no. of atoms in structure 11
total_n_atoms = 0
for i in range(len(db1)):
    total_n_atoms += len(db1[i]) # no. atoms in molecule i
print(total_n_atoms)
print(total_n_atoms*3)

#%%
forces_mace = ea.get_prop(db1, 'arrays', 'MACE_forces')
forces_ref = ea.get_prop(db2, 'arrays', 'REF_forces')
print(type(forces_mace))
print(forces_mace.shape)

#%%
Magnitude_error = []
MACE_Force_Magnitude = []
REF_Force_Magnitude = []
#%%
for i in range(forces_mace.shape[0]): #i iterates over all the structures
    structure_forces_mace = forces_mace[i]
    structure_forces_ref = forces_ref[i]
    for j in range(structure_forces_mace.shape[0]): # j iterates over all the atoms in i^th structure
        mag_j_mace = np.linalg.norm(structure_forces_mace[j]) # magnitude of forces of atom j 
        mag_j_ref = np.linalg.norm(structure_forces_ref[j])
        MACE_Force_Magnitude.append(mag_j_mace)
        REF_Force_Magnitude.append(mag_j_ref)
        rel_error_j = abs(mag_j_mace - mag_j_ref) / mag_j_ref
        Magnitude_error.append(rel_error_j)

#%%
# Magnitude_error
# len(Magnitude_error)


# # %%
# print(type(Magnitude_error[0]))
# print(len(MACE_Force_Magnitude))
# print(type(MACE_Force_Magnitude))
# x = np.arange(1,6)
# x
#%%
import matplotlib.pyplot as plt
plt.style.use('_mpl-gallery')

y = np.array(Magnitude_error, dtype='float64')
x = np.arange(len(y))

fig = plt.figure(figsize=(10,5))

ax = fig.add_subplot(111)
ax.set_ylabel(r'Relative Error of Force Magnitude per atom $\rm (eV / \AA)$')
ax.set_xlabel('Atom Index')

# ax = fig.add_subplot(121) # 1,2 -> 2 subplots(left and right) 1 -> the first left subplot
# ax2 = fig.add_subplot(122) # 1,2 -> 2 subplots(left and right) 2 -> the second right subplot
ax.stem(x,y)
# ax2.stem(x,y)
plt.legend()
plt.show()

# %%
#Correlation Plot between MACE and REF F_magnitude values
y = np.array(MACE_Force_Magnitude, dtype='float64')
x = np.array(REF_Force_Magnitude, dtype='float64')

fig = plt.figure(figsize=(7,7))

ax = fig.add_subplot(111)
ax.set_xlabel(r'REF Force Magnitude per atom $\rm (eV/\AA)$')
ax.set_ylabel(r'MACE Force Magnitude per atom $\rm (eV/\AA)$')

ax.scatter(x,y)
ax.plot([-1,53],[-1,53], color='k', linestyle='dashed')

plt.show()

# %%
# f1 = forces_mace[3][0]
# f2 = forces_ref[3][0]
# m1 = np.linalg.norm(f1)
# m2 = np.linalg.norm(f2)
# f1 = f1/m1
# f2 = f2/m2

# print(1 - np.dot(f1,f2))
#%%
# Scalar Product
Scalar_Product = []
for i in range(forces_mace.shape[0]): #i iterates over all the structures
    structure_forces_mace = forces_mace[i]
    structure_forces_ref = forces_ref[i]
    for j in range(structure_forces_mace.shape[0]): # j iterates over all the atoms in i^th structure
        mag_j_mace = np.linalg.norm(structure_forces_mace[j]) # magnitude of forces of atom j 
        mag_j_ref = np.linalg.norm(structure_forces_ref[j])
        structure_forces_mace[j] = structure_forces_mace[j]/mag_j_mace
        structure_forces_ref[j] = structure_forces_ref[j]/mag_j_ref
        scalar_dot = np.dot(structure_forces_ref[j],structure_forces_mace[j])
        Scalar_Product.append(1-scalar_dot)
#%%
# len(Scalar_Product)

# %%
plt.style.use('_mpl-gallery')

fig = plt.figure(figsize=(10,5))
x = np.arange(len(Scalar_Product))
y = np.array(Scalar_Product, dtype='float64')

ax = fig.add_subplot(111)

ax.set_xlabel('Atom Index')
ax.set_ylabel('[1 - (Scalar Product of Force Unit Vectors)]')
ax.stem(x,y)

plt.show()
# %%
# Plotting all the Forces directionally
MACE_All_Force_Direction = []
REF_All_Force_Direction = []

#%%
for i in range(forces_mace.shape[0]): #i iterates over all the structures
    structure_forces_mace = forces_mace[i]
    structure_forces_ref = forces_ref[i]
    for j in range(structure_forces_mace.shape[0]): # j iterates over all the atoms in i^th structure
        mag_j_mace = np.linalg.norm(structure_forces_mace[j]) # magnitude of forces of atom j 
        mag_j_ref = np.linalg.norm(structure_forces_ref[j])
        structure_forces_mace[j] = structure_forces_mace[j]/mag_j_mace
        structure_forces_ref[j] = structure_forces_ref[j]/mag_j_ref
        for k in range(3):
            MACE_All_Force_Direction.append(structure_forces_mace[j][k])
            REF_All_Force_Direction.append(structure_forces_ref[j][k])
# %%
fig = plt.figure(figsize=(7,7))

x_ref = np.array(REF_All_Force_Direction, dtype = 'float64')
y_mace = np.array(MACE_All_Force_Direction, dtype = 'float64')

ax = fig.add_subplot(111)
ax.set_xlabel('All Force Unit Vector components from REF')
ax.set_ylabel('All Force Unit Vector components by MACE')

ax.scatter(x_ref,y_mace)
ax.plot([-1.05,1.05],[-1.05,1.05], color='black', linestyle='dashed')

plt.show()
# %%
yh = []
yo = []
yc = []
xh = []
xo = []
xc= []

for i in range(len(db1)): #i iterates over all the structures
    structures = db1[i]
    structure_forces_mace = forces_mace[i]
    structure_forces_ref = forces_ref[i]
    for j in range(structure_forces_mace.shape[0]): # j iterates over all the atoms in i^th structure
        atom_j = structures[j].symbol
        mag_j_mace = np.linalg.norm(structure_forces_mace[j]) # magnitude of forces of atom j 
        mag_j_ref = np.linalg.norm(structure_forces_ref[j])
        rel_error_j = abs(mag_j_mace - mag_j_ref) / mag_j_ref # You Cannot divide by zero therefore you will get nan for the first 0 index of H,C,O 
        if atom_j == 'H':
            xh.append((i+j+1))
            yh.append(rel_error_j)
        elif atom_j == 'C':
            xc.append((i+j+1))
            yc.append(rel_error_j)
        elif atom_j == 'O':
            xo.append((i+j+1))
            yo.append(rel_error_j)
#%%
# len(yo) + len(yc) + len(yh)
# #%%
# len(xo) + len(xc) + len(xh)
#%%
#Element Color Coding for Hydrogen, Oxygen, Carbon
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,5))

ax = fig.add_subplot(111)
ax.set_ylabel(r'Relative Error of Force Magnitude per atom $\rm (eV / \AA)$')
ax.set_xlabel('Atom Index')

# ax = fig.add_subplot(121) # 1,2 -> 2 subplots(left and right) 1 -> the first left subplot
# ax2 = fig.add_subplot(122) # 1,2 -> 2 subplots(left and right) 2 -> the second right subplot
ax.plot(xh,yh, 'black', label='hydrogen') # Be carefule with the dimension, dim(x) == dim(y), 
# NOTE:You can either add NaN values in the y_element array where you don't have anything
# Or You can manage the x as x_element
ax.plot(xc,yc, 'grey', label='carbon', alpha=0.7)
ax.plot(xo,yo, 'red',label='oxygen', alpha=0.4)
# ax2.stem(x,y)
ax.legend()
plt.legend()
plt.show()
# %%
# You Cannot divide by zero therefore you will get nan for the first H,C,O index=0
#np.mean() doesn't work with nan values for some reason have to mask it
yh[0] = 0
yc[0] = 0
yo[0] = 0
average_h = np.mean(np.array(yh))
average_c = np.mean(np.array(yc))
average_o = np.mean(np.array(yo))

print(f" Avg_H = {average_h} \n Avg_C = {average_c} \n Avg_O = {average_o} \n")
# %%
# Color Coding for Energy Corel