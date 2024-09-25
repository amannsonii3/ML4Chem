# %%
## DONOT FORGET TO ACTIVATE THE RIGHT ENV
import pandas as pd
import re

#%%
def parse_log(file_path):
    ## Define a list to hold the extracted data
    data = []

    ## Define a regular expression pattern to match the relevant lines
    pattern = re.compile(r"Epoch\s+(\d+):\s+loss=([\d.]+),\s+MAE_E_per_atom=([\d.]+)\s+meV,\s+MAE_F=([\d.]+)\s+meV\s+/\s+A")

    ## Open and read the log file line by line
    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                epoch = int(match.group(1))  ## Retrieve the first captured group (\d+), which is the epoch number
                loss = float(match.group(2)) ## Retrieve the second captured group ([\d.]+), which is the loss value
                mae_e_per_atom = float(match.group(3))
                mae_f = float(match.group(4))
                data.append([epoch, loss, mae_e_per_atom, mae_f])

    ## Create a DataFrame from the extracted data
    df = pd.DataFrame(data, columns=['Epoch', 'Loss', 'MAE_E_per_atom', 'MAE_F'])

    # print(df.head())

    return df
#%%
## Use your .log file_path
file_path = 'water_1k_small_run-123.log' 
df = parse_log(file_path)
print(df)

## Plotting the training losses
import matplotlib.pyplot as plt

# %%
plt.figure(figsize=(10, 6))  ## Adjust size if necessary

plt.plot(df['Epoch'], df['Loss'], marker='o', linestyle='-', color='b', label='Loss')

plt.plot(df['Epoch'], df['MAE_E_per_atom'], marker='s', linestyle='--', color='g', label='MAE_E_per_atom')

plt.plot(df['Epoch'], df['MAE_F'], marker='^', linestyle=':', color='r', label='MAE_F')

## Adding labels and title
plt.xlabel('Epoch')
plt.ylabel('Values')
plt.title('Loss, MAE_E_per_atom, MAE_F vs Epoch')
plt.legend()

## Set y-axis range
plt.ylim(-1, 3)
plt.xlim(-5, 350)

## Save the plot
plt.savefig('plot.png')

## Show plot
plt.grid(True)
plt.tight_layout()
plt.show()
