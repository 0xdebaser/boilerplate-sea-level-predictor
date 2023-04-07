import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df.head())

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    bf0 = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    plt.plot(range(1880, 2051), bf0.intercept + bf0.slope * range(1880, 2051), "g")

    # Create second line of best fit
    #later_years = df.loc[(df["Year"] >= 2000), "Year"].tolist()
    bf1 = linregress(x=df.loc[(df["Year"] >= 2000), "Year"], y=df.loc[(df["Year"] >= 2000), "CSIRO Adjusted Sea Level"])
    plt.plot(range(2000, 2051), bf1.intercept + bf1.slope * range(2000, 2051), "r")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()