#%%
import re
#%%
# Initialize lists to store the values
epochs_mace_192_2 = []
losses_mace_192_2 = []
rmse_e_per_atom_mace_192_2 = []
rmse_f_mace_192_2 = []
#%%

# Define the pattern to extract the necessary information
pattern = re.compile(r"Epoch (\d+): loss=([\d\.]+), RMSE_E_per_atom=([\d\.]+) meV, RMSE_F=([\d\.]+) meV / A")

# Open the log file and process line by line
with open("mace_192_2.out", "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            epochs_mace_192_2.append(int(match.group(1)))
            losses_mace_192_2.append(float(match.group(2)))
            rmse_e_per_atom_mace_192_2.append(float(match.group(3)))
            rmse_f_mace_192_2.append(float(match.group(4)))
#%%
epochs_mace_96_1 = []
losses_mace_96_1 = []
rmse_e_per_atom_mace_96_1 = []
rmse_f_mace_96_1 = []
#%%

# Define the pattern to extract the necessary information
pattern = re.compile(r"Epoch (\d+): loss=([\d\.]+), RMSE_E_per_atom=([\d\.]+) meV, RMSE_F=([\d\.]+) meV / A")

# Open the log file and process line by line
with open("mace_96_1.out", "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            epochs_mace_96_1.append(int(match.group(1)))
            losses_mace_96_1.append(float(match.group(2)))
            rmse_e_per_atom_mace_96_1.append(float(match.group(3)))
            rmse_f_mace_96_1.append(float(match.group(4)))
#%%
epochs_mace_64_0 = []
losses_mace_64_0 = []
rmse_e_per_atom_mace_64_0 = []
rmse_f_mace_64_0 = []
#%%

# Defining the pattern to extract the necessary information
pattern = re.compile(r"Epoch (\d+): loss=([\d\.]+), RMSE_E_per_atom=([\d\.]+) meV, RMSE_F=([\d\.]+) meV / A")

# Open the log file and process line by line
with open("mace_64_0.out", "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            epochs_mace_64_0.append(int(match.group(1)))
            losses_mace_64_0.append(float(match.group(2)))
            rmse_e_per_atom_mace_64_0.append(float(match.group(3)))
            rmse_f_mace_64_0.append(float(match.group(4)))
#%%
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

ax.set_xlabel("Number of Epochs", fontsize=18)
ax.set_ylabel(r"RMSE for Energy per atom $ \rm (meV)$", fontsize=18)

ax.plot(epochs_mace_192_2,rmse_e_per_atom_mace_192_2, 'deepskyblue', linewidth=2.5, label='MACE 192-2')
ax.plot(epochs_mace_96_1,rmse_e_per_atom_mace_96_1, 'limegreen', linewidth=2.5, label='MACE 96-1')
ax.plot(epochs_mace_64_0,rmse_e_per_atom_mace_64_0, 'darkcyan', linewidth=2.5, label='MACE 64-0')

ax.legend()
plt.legend()
plt.title("Energy Training", fontsize=23)
# plt.show()
plt.savefig('energy_training.png', dpi=800)

# %%
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

ax.set_xlabel("Number of Epochs", fontsize=18)
ax.set_ylabel(r"RMSE for Forces per atom per component $ \rm (meV/ \AA)$", fontsize=18)

ax.plot(epochs_mace_192_2,rmse_f_mace_192_2, 'deepskyblue', linewidth=2.5, label='MACE 192-2')
ax.plot(epochs_mace_96_1,rmse_f_mace_96_1, 'limegreen', linewidth=2.5, label='MACE 96-1')
ax.plot(epochs_mace_64_0,rmse_f_mace_64_0, 'darkcyan', linewidth=2.5, label='MACE 64-0')

ax.legend()
plt.legend()
plt.title("Forces Training", fontsize=23)
# plt.show()

plt.savefig('forces_training.png', dpi=800)
# %%
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

ax.set_xlabel("Number of Epochs", fontsize=18)
ax.set_ylabel("Loss", fontsize=18)

ax.plot(epochs_mace_192_2,losses_mace_192_2, 'deepskyblue', linewidth=2.5, label='MACE 192-2')
ax.plot(epochs_mace_96_1,losses_mace_96_1, 'limegreen', linewidth=2.5, label='MACE 96-1')
ax.plot(epochs_mace_64_0,losses_mace_64_0, 'darkcyan', linewidth=2.5, label='MACE 64-0')

ax.legend()
plt.legend()
plt.title("Model Training", fontsize=23)
# plt.show()
plt.savefig('loss_training.png', dpi=800)
# %%
