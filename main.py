"""
Created on Fri Sep 15 15:03:11 2023
@author: lillygrella
"""
#from datetime import datetime
import pandas as pd
#import polars as pl
from matplotlib import pyplot as plt, dates
from matplotlib.ticker import FuncFormatter

#read in stock data based on ticker list and dates, restrict to when the market is open based on SPY

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

def dollars(value):
    '''
    Format floats to dollars
    'The two args are the value and tick position'
    '''
    return f'${value:.0f}'


def make_line_graph():
    '''
    Create Line Graph of 
    '''
    d_f = readin('SPY')  
    # Create a new figure and a subplot
    #fig, ax = plt.subplots()
    # Plot the OHLC data
    #df['Close'].plot()
    # Set the title and labels
    #ax.xaxis.set_major_formatter(dates.DateFormatter('%m-%y'))
    figure,a_x = plt.subplots()
    d_f['Close'].plot()
    a_x.set_xticks(d_f.index)
    plt.locator_params(axis='x', nbins=12)
    a_x.set_title('SPY Closing Stock Price')
    a_x.set_xlabel('Date')
    a_x.set_ylabel('Closing Price')   
    # use formatters to specify major and minor ticks
    a_x.xaxis.set_major_formatter(dates.DateFormatter("%m/%y"))
    a_x.yaxis.set_major_formatter(FuncFormatter(dollars))
    #_ = plt.xticks(rotation=90)  
    # Show the plot
    plt.savefig("SPY_Closing.png")
