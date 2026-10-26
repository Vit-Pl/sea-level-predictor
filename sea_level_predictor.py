import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)

    # Create first line of best fit
    slope, intercept, *_ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = range(int(df['Year'].min()), 2051)
    line_all = [slope * x + intercept for x in years_all]
    plt.plot(years_all, line_all, color='red', label='All data')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, *_ = linregress(
        df_2000['Year'], df_2000['CSIRO Adjusted Sea Level']
    )
    years_2000 = range(2000, 2051)
    line_2000 = [slope2 *x + intercept2 for x in years_2000]
    plt.plot(years_2000, line_2000, color='green', label='From 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
