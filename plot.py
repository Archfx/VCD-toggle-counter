import csv
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style


# Use a style
# plt.style.use('dark_background')

# Set the figure size
plt.rcParams["figure.figsize"] = [14.00, 1.8]
plt.rcParams["figure.autolayout"] = True

# Make a list of columns
columns = ['Power']

df = pd.read_csv("switching.csv", usecols=columns)

# Plot the lines
ax = df.plot(color='#7859A3', label='Normal Execution')
plt.xlabel('Clock Cycles', labelpad=-5, fontsize=14)
plt.axis([937600, 939000, 5, 70])
plt.yticks([])

# Remove plot border from top and right
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

# Define color ranges
start_range = 938160
end_range = 938800


# Plot the second part of the line plot with the modified color
df.loc[start_range:end_range].plot(ax=ax, color='#99004D', label='Context Switch')  # Set the desired color here

custom_legend_labels = ['Normal Execution', 'Context Switch']

# Create a custom legend
handles, labels = ax.get_legend_handles_labels()
custom_legend = plt.legend(handles, custom_legend_labels, loc='upper left')


# # Move legend to bottom left
# leg = plt.legend(loc='lower left', bbox_to_anchor=(0, 0.5))


plt.savefig("power.pdf", format="pdf", bbox_inches="tight")
# plt.show()