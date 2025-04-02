import pandas as pd
from skmob import TrajDataFrame

# Load CSV into a Pandas DataFrame
file_path = "your_data.csv"  # Change this to your actual CSV file
df = pd.read_csv(file_path, parse_dates=['datetime'])

# Convert to TrajDataFrame
tdf = TrajDataFrame(df, datetime=True)

# Extract origin (first record per user)
origins = tdf.groupby("uid").first().reset_index()

# Display relevant columns
print(origins[['uid', 'lat', 'lon', 'datetime']])
