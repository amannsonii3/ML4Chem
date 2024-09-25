import numpy as np

def write_mace_extxyz(df, filename):
  """
  Writes a DataFrame to a MACE extxyz file format.

  Args:
      df (pandas.DataFrame): The DataFrame containing element symbols, positions, gradients,
                             atomic numbers, number of atoms, and total energy.
      filename (str): The filename to write the data to.
  """
  
  # Get number of atoms
  num_atoms = df['Number of Atoms'].tolist()

  # Extract data
  elements = df['elements'].tolist()
  positions = df['positions'].to_numpy()
  gradients = df['Gradients'].to_numpy() if 'Gradients' in df else None
  atomic_numbers = df['atomicNumbers'].tolist()
  total_energy = df['TotEnergy'].tolist()

  # Open file for writing
  with open(filename, 'w') as f:
    # Write number of atoms (assuming 5 rows in your DataFrame)
    for row in range(df.shape[0]):
      f.write(str(num_atoms[row]) + '\n')

      # Write header line
      f.write(f"REF_Energies={(total_energy[row]*27.211407953):.8f} pbc=\"F F F\" Lattice=\"23.80000000       0.00000000       0.00000000      0.00000000      23.80000000       0.00000000      0.00000000      0.00000000      23.80000000\" Properties=species:S:1:pos:R:3:REF_forces:R:3:Z:I:1\n")

      # Write atom data (one line per atom)
      for i in range(num_atoms[row]):
        element = elements[row][i] # 10s = 10 spacings
        f.write(f"{element:10s}")  # Fixed format string for element symbol 

        # Write positions with proper spacing for negative numbers
        for pos in positions[row][i]:
          f.write(f"{pos:+.8f}")  # Use f-string formatting with '+' sign for spacing
          f.write("      ")

        # Write gradients (if available) with proper spacing for negative numbers
        if gradients is not None:
          for g in gradients[row][i]:
            fau2eVA = 8.2387235038*6.241509
            g = g * fau2eVA
            f.write(f"{g:+.8f}")  # Use f-string formatting with '+' sign for spacing
            f.write("      ")

        f.write(f"{atomic_numbers[row][i]:d}\n")  # Write atomic number

# Improved formatting for element symbol, positions, and gradients
write_mace_extxyz(mace_new_df, "qrnn_hdnnp_mace.xyz")