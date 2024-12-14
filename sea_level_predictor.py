import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# 1. Import data
def draw_plot():
    # Load the dataset
    df = pd.read_csv('epa-sea-level.csv')

    # Create the scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data', alpha=0.6)

    # Perform linear regression on the full dataset
    regression_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all = regression_all.slope
    intercept_all = regression_all.intercept

    # Generate line of best fit through 2050 for all data
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_all = slope_all * years_extended + intercept_all
    plt.plot(years_extended, sea_levels_all, 'r', label='Best Fit: 1880-2050')

    # Perform linear regression on data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    regression_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    slope_recent = regression_recent.slope
    intercept_recent = regression_recent.intercept

    # Generate line of best fit through 2050 for data from 2000 onwards
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_levels_recent, 'green', label='Best Fit: 2000-2050')

    # Add labels, title, and legend
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.grid()

    # Save plot and return it
    plt.savefig('sea_level_plot.png')
    return plt.gca()
