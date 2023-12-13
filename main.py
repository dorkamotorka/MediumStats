import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
file_path = 'cloudchirp-subscriber-stats.csv'  # Replace 'your_file.csv' with the actual file path
df = pd.read_csv(file_path)

# Convert 'period_end' column to datetime format
df['period_end'] = pd.to_datetime(df['period_end'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['period_end'], df['followers_total'], marker='o', linestyle='-', color='b')
plt.title('Followers Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Followers')
plt.grid(True)
plt.show()
