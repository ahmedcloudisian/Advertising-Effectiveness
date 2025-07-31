Advertising effectiveness

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
data = pd.read_csv('advertising_data.csv')

# Step 2: Display the first few rows of the dataset
print("Dataset Overview:")
print(data.head())

# Step 3: Calculate key metrics
data['CTR'] = (data['Clicks'] / data['Impressions']) * 100  # Click-Through Rate
data['Conversion_Rate'] = (data['Conversions'] / data['Clicks']) * 100  # Conversion Rate
data['ROI'] = ((data['Revenue'] - data['Spend']) / data['Spend']) * 100  # Return on Investment

# Step 4: Display the updated dataset with metrics
print("\nDataset with Metrics:")
print(data)

# Step 5: Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Step 6: Platform-wise performance analysis
platform_performance = data.groupby('Platform').agg({
    'Impressions': 'sum',
    'Clicks': 'sum',
    'Conversions': 'sum',
    'Spend': 'sum',
    'Revenue': 'sum',
    'CTR': 'mean',
    'Conversion_Rate': 'mean',
    'ROI': 'mean'
}).reset_index()

print("\nPlatform-wise Performance:")
print(platform_performance)

# Step 7: Visualization
# Set up the figure and subplots
plt.figure(figsize=(15, 10))

# Subplot 1: CTR by Platform
plt.subplot(2, 2, 1)
plt.bar(platform_performance['Platform'], platform_performance['CTR'], color='skyblue')
plt.title('Click-Through Rate (CTR) by Platform')
plt.xlabel('Platform')
plt.ylabel('CTR (%)')

# Subplot 2: Conversion Rate by Platform
plt.subplot(2, 2, 2)
plt.bar(platform_performance['Platform'], platform_performance['Conversion_Rate'], color='orange')
plt.title('Conversion Rate by Platform')
plt.xlabel('Platform')
plt.ylabel('Conversion Rate (%)')

# Subplot 3: ROI by Platform
plt.subplot(2, 2, 3)
plt.bar(platform_performance['Platform'], platform_performance['ROI'], color='lightgreen')
plt.title('Return on Investment (ROI) by Platform')
plt.xlabel('Platform')
plt.ylabel('ROI (%)')

# Subplot 4: Revenue vs Spend by Platform
plt.subplot(2, 2, 4)
plt.bar(platform_performance['Platform'], platform_performance['Revenue'], color='blue', label='Revenue')
plt.bar(platform_performance['Platform'], platform_performance['Spend'], color='red', label='Spend', alpha=0.6)
plt.title('Revenue vs Spend by Platform')
plt.xlabel('Platform')
plt.ylabel('Amount ($)')
plt.legend()

# Adjust layout and display plots
plt.tight_layout()
plt.show()


Data set 
Dataset Overview:
   Campaign_ID    Platform  Impressions  Clicks  Conversions  Spend  Revenue
0            1    Facebook        10000     500           50   1000     5000
1            2  Google Ads        15000     700           70   1500     7000
2            3   Instagram         8000     400           40    800     4000
3            4    Facebook        12000     600           60   1200     6000
4            5  Google Ads        20000    1000          100   2000    10000
