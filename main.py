"""
Created on Fri Sep 15 15:03:11 2023
@author: lillygrella
"""
import pandas as pd
from matplotlib import pyplot as plt, dates
from matplotlib.ticker import FuncFormatter
from pandas.plotting import table


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
    return d_f


def get_summ_stats(d_f):
    """
    Return Summary Stats
    """
    d_f2 = pd.DataFrame({"Summary Stats": d_f["Close"].describe().round(2)})

    axes = plt.subplot(921, frame_on=False)
    axes.xaxis.set_visible(False)
    axes.yaxis.set_visible(False)

    table(axes, d_f2, loc="center")

    plt.savefig("sumstats.png", bbox_inches="tight")
    return d_f["Close"].describe()


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
    _, axes = plt.subplots()
    d_f["Close"].plot()
    axes.set_xticks(d_f.index)
    plt.locator_params(axis="x", nbins=12)
    axes.set_title("SPY Closing Stock Price")
    axes.set_xlabel("Date")
    axes.set_ylabel("Closing Price")
    axes.xaxis.set_major_formatter(dates.DateFormatter("%m/%y"))
    axes.yaxis.set_major_formatter(FuncFormatter(dollars))
    plt.savefig("SPY_Closing.png")


def main():
    """
    Main function to perform actions
    """
    spy = readin("SPY")
    get_summ_stats(spy)
    make_line_graph(spy)


if __name__ == "__main__":
    main()
