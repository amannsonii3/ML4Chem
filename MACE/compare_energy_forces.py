from aseMolec import pltProps as pp
from ase.io import read
import matplotlib.pyplot as plt
from aseMolec import extAtoms as ea 
import numpy as np

def plot_RMSEs(file1, file2, labels):
    # Read the atomic configurations
    db1 = read(file1, ':')
    db2 = read(file2, ':')
    
    # Create a figure with two subplots
    plt.figure(figsize=(8,4), dpi=100)
    
    # Plot energies
    plt.subplot(1,2,1)
    pp.plot_prop(
        ea.get_prop(db1, 'info', 'MACE_energy', True).flatten(), ## Ensure that your output.xyz obtained after running eval_configs.py has the label MACE_energy
        ea.get_prop(db2, 'info', 'REF_energies', True).flatten(), ## Ensure that your output.xyz obtained after running eval_configs.py has the label TotEnergy
        title=r'Energy $(\rm eV/atom)$', labs=labels, rel=True
    )
    
    # Plot forces
    plt.subplot(1,2,2)
    pp.plot_prop(
        np.concatenate(ea.get_prop(db1, 'arrays', 'MACE_forces')).flatten(), ## Ensure that your output.xyz obtained after running eval_configs.py has the label MACE_forces
        np.concatenate(ea.get_prop(db2, 'arrays', 'REF_forces')).flatten(), ## Ensure that your output.xyz obtained after running eval_configs.py has the label force
        title=r'Forces $\rm (eV/\AA)$', labs=labels, rel=True
    )
    
    # Adjust layout
    plt.tight_layout()
    plt.show()

# Example usage:
file1 = 'mace_solvent_xtb_output.xyz' ## MACE_eval_output
file2 = 'mace_solvent_xtb_output.xyz' ## test_dataset
labels = ['Solvent_XTB', 'MACE_XTB']

plot_RMSEs(file1, file2, labels)
