"""
Created on Fri Sep 15 15:03:11 2023
@author: lillygrella
"""
# from datetime import datetime
import pandas as pd

# import polars as pl
from matplotlib import pyplot as plt, dates
from matplotlib.ticker import FuncFormatter
from tabulate import tabulate

# read in stock data based on ticker list and dates, restrict to when the market is open based on SPY


def readin(ticker):
    """
    read in CSV
    Create Daily Price Change Variable
    """
    d_f = pd.read_csv(
        f"/workspaces/LG-Week2-Pandas/{ticker}.csv",
        parse_dates=["Date"],
        index_col="Date",
    )
    d_f["PriceChange"] = d_f["Close"] - d_f["Open"]
    return d_f


def get_summ_stats(d_f):
    """
    Return Summary Stats
    """
    stats_summary = d_f["PriceChange"].describe()

    summary_statistics = tabulate(d_f, tablefmt="pipe", showindex=False)

    with open("summary_statistics.md", "w",encoding='UTF-8') as file:
        file.write(summary_statistics)
    return stats_summary


def dollars(value, _):
    """
    Format floats to dollars
    'The two args are the value and tick position'
    """
    return f"${value:.0f}"


def make_line_graph(d_f):
    """
    Create Line Graph of
    """
    # Create a new figure and a subplot
    # fig, ax = plt.subplots()
    # Plot the OHLC data
    # df['Close'].plot()
    # Set the title and labels
    # ax.xaxis.set_major_formatter(dates.DateFormatter('%m-%y'))
    _, axes = plt.subplots()
    d_f["Close"].plot()
    axes.set_xticks(d_f.index)
    plt.locator_params(axis="x", nbins=12)
    axes.set_title("SPY Closing Stock Price")
    axes.set_xlabel("Date")
    axes.set_ylabel("Closing Price")
    # use formatters to specify major and minor ticks
    axes.xaxis.set_major_formatter(dates.DateFormatter("%m/%y"))
    axes.yaxis.set_major_formatter(FuncFormatter(dollars))
    # _ = plt.xticks(rotation=90)
    # Show the plot
    plt.savefig("SPY_Closing.png")

def main():
    """
    Main function to perform actions
    """
    spy = readin("SPY")
    make_line_graph(spy)
    get_summ_stats(spy)


if __name__ == "__main__":
    main()
