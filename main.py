"""
Created on Fri Sep 15 15:03:11 2023
@author: lillygrella
"""

import pandas as pd
#import polars as pl
from matplotlib import pyplot as plt, dates
from matplotlib.ticker import FuncFormatter
from datetime import datetime

#read in stock data based on ticker list and dates, restrict to days when the market is open based on SPY

def readin(ticker):
    '''
    read in CSV
    Create Daily Price Change Variable
    '''
    d_f = pd.read_csv(f"/workspaces/LG-Week2-Pandas/{ticker}.csv", parse_dates=['Date'],index_col='Date')
    d_f['PriceChange'] = d_f['Close'] - d_f['Open']
    return d_f

def get_summ_stats():
    '''
    Return Summary Stats
    '''
    d_f = readin('SPY')
    stats_summary = d_f['PriceChange'].describe()
    return stats_summary

def dollars(x):
    '''
    Format floats to dollars
    'The two args are the value and tick position'
    '''
    return '$%1.0f' % (x)


def make_line_graph():
    '''
    Create Line Graph of 
    '''

    df = readin('SPY')
    
    # Create a new figure and a subplot
    #fig, ax = plt.subplots()
    # Plot the OHLC data
    #df['Close'].plot()
    # Set the title and labels
    #ax.xaxis.set_major_formatter(dates.DateFormatter('%m-%y'))
   
    
    ax = plt.subplots()
    df['Close'].plot()
    ax.set_xticks(df.index)
    plt.locator_params(axis='x', nbins=12)
    ax.set_title('SPY Closing Stock Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    
    # use formatters to specify major and minor ticks
    ax.xaxis.set_major_formatter(dates.DateFormatter("%m/%y"))
    ax.yaxis.set_major_formatter(FuncFormatter(dollars))
    #_ = plt.xticks(rotation=90)    
    # Show the plot
    plt.savefig("SPY_Closing.png")
    